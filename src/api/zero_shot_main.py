from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Form, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
import time
import logging
import os
from typing import List, Dict, Optional
import sys
import traceback

# 프로젝트 루트를 Python 경로에 추가
# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.models.zero_shot_classifier import ZeroShotCustomClassifier
from src.auth.api_key_manager import APIKeyManager
from config.config import *

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI 앱 생성
app = FastAPI(
    title="VisionAI Pro Zero-Shot Custom Classification API",
    description="Zero-shot Learning 기반 커스텀 이미지 분류 API - base_words.txt 사용",
    version="3.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 정적 파일 서빙 설정
app.mount("/web_apps", StaticFiles(directory="web_apps"), name="web_apps")

# 전역 변수
classifier: Optional[ZeroShotCustomClassifier] = None
api_key_manager = APIKeyManager()

def get_classifier() -> ZeroShotCustomClassifier:
    """분류기 인스턴스 반환"""
    global classifier
    if classifier is None:
        base_words_path = os.getenv("BASE_WORDS_PATH", "query/base_words.txt")
        classifier = ZeroShotCustomClassifier(base_words_path=base_words_path)
    return classifier

def verify_api_key(api_key: str) -> bool:
    """API 키 검증"""
    try:
        key_info = api_key_manager.validate_api_key(api_key)
        return key_info is not None
    except Exception as e:
        logger.error(f"API 키 검증 실패: {e}")
        return False

@app.on_event("startup")
async def startup_event():
    """서버 시작 시 초기화"""
    logger.info("🚀 VisionAI Pro Zero-Shot Custom Classification API 시작")
    
    # 모델 초기화
    try:
        get_classifier()
        logger.info("✅ Zero-shot 분류기 초기화 완료")
    except Exception as e:
        logger.error(f"❌ 분류기 초기화 실패: {e}")

@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "VisionAI Pro Zero-Shot Custom Classification API",
        "version": "3.0.0",
        "status": "running",
        "model": "CLIP (Zero-shot Learning)",
        "categories": "base_words.txt 기반 커스텀 카테고리",
        "features": [
            "Zero-shot Learning",
            "커스텀 카테고리 추가/제거",
            "카테고리 검색",
            "실시간 학습"
        ]
    }

@app.get("/health")
async def health_check():
    """헬스 체크"""
    try:
        classifier = get_classifier()
        model_info = classifier.get_model_info()
        return {
            "status": "healthy",
            "model_info": model_info,
            "timestamp": time.time()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": time.time()
        }

@app.get("/api/categories")
async def get_categories(
    api_key: str = Query(None),
    search: str = Query(None),
    limit: int = Query(50, ge=1, le=1000)
):
    """사용 가능한 카테고리 목록 반환"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        
        if search:
            # 검색 기능
            categories = classifier.search_categories(search, top_k=limit)
        else:
            # 전체 카테고리
            categories = classifier.get_categories()[:limit]
        
        return {
            "success": True,
            "categories": categories,
            "count": len(categories),
            "total_count": len(classifier.get_categories()),
            "search_query": search if search else None
        }
    except Exception as e:
        logger.error(f"카테고리 목록 조회 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/classify")
async def classify_image(
    file: UploadFile = File(...),
    top_k: int = Form(5),
    api_key: str = Form(...)
):
    """Zero-shot 이미지 분류"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # 파일 검증
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    
    try:
        # 이미지 로드
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # 처리 시간 측정
        start_time = time.time()
        
        # Zero-shot 분류 실행
        classifier = get_classifier()
        predictions = classifier.predict(image, top_k=top_k)
        
        processing_time = time.time() - start_time
        
        # 결과 반환
        return {
            "success": True,
            "image_name": file.filename,
            "processing_time": round(processing_time, 3),
            "predictions": predictions,
            "model_info": classifier.get_model_info()
        }
        
    except Exception as e:
        logger.error(f"이미지 분류 실패: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Classification failed: {str(e)}")

@app.post("/api/categories/add")
async def add_category(
    category: str = Form(...),
    description: str = Form(""),
    api_key: str = Form(...)
):
    """새로운 커스텀 카테고리 추가"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        success = classifier.add_custom_category(category, description)
        
        if success:
            return {
                "success": True,
                "message": f"카테고리 '{category}' 추가 완료",
                "category": category,
                "description": description,
                "total_categories": len(classifier.get_categories())
            }
        else:
            raise HTTPException(status_code=400, detail=f"카테고리 '{category}' 추가 실패")
            
    except Exception as e:
        logger.error(f"카테고리 추가 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/categories/remove")
async def remove_category(
    category: str = Query(...),
    api_key: str = Query(...)
):
    """카테고리 제거"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        success = classifier.remove_category(category)
        
        if success:
            return {
                "success": True,
                "message": f"카테고리 '{category}' 제거 완료",
                "total_categories": len(classifier.get_categories())
            }
        else:
            raise HTTPException(status_code=400, detail=f"카테고리 '{category}' 제거 실패")
            
    except Exception as e:
        logger.error(f"카테고리 제거 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/categories/search")
async def search_categories(
    query: str = Query(...),
    limit: int = Query(10, ge=1, le=100),
    api_key: str = Query(None)
):
    """카테고리 검색"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        results = classifier.search_categories(query, top_k=limit)
        
        return {
            "success": True,
            "query": query,
            "results": results,
            "count": len(results)
        }
        
    except Exception as e:
        logger.error(f"카테고리 검색 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/categories/save")
async def save_categories(
    filepath: str = Form("custom_categories.json"),
    api_key: str = Form(...)
):
    """카테고리를 파일로 저장"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        classifier.save_categories(filepath)
        
        return {
            "success": True,
            "message": f"카테고리를 저장했습니다: {filepath}",
            "filepath": filepath,
            "categories_count": len(classifier.get_categories())
        }
        
    except Exception as e:
        logger.error(f"카테고리 저장 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/categories/load")
async def load_categories(
    filepath: str = Form(...),
    api_key: str = Form(...)
):
    """파일에서 카테고리 로드"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        classifier.load_categories(filepath)
        
        return {
            "success": True,
            "message": f"카테고리를 로드했습니다: {filepath}",
            "filepath": filepath,
            "categories_count": len(classifier.get_categories())
        }
        
    except Exception as e:
        logger.error(f"카테고리 로드 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/stats")
async def get_classification_stats(api_key: str = None):
    """분류 통계"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        model_info = classifier.get_model_info()
        
        return {
            "success": True,
            "model_info": model_info,
            "total_categories": len(classifier.get_categories()),
            "base_words_file": classifier.base_words_path,
            "supported_formats": ["JPEG", "PNG", "GIF", "BMP", "TIFF"],
            "max_image_size": "10MB",
            "processing_time_avg": "1-3초",
            "learning_method": "Zero-shot Learning",
            "model_type": "CLIP (Vision-Language Model)"
        }
    except Exception as e:
        logger.error(f"통계 조회 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/models")
async def get_available_models(api_key: str = None):
    """사용 가능한 모델 목록"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {
        "success": True,
        "models": [
            {
                "name": "zero_shot_clip",
                "description": "CLIP Zero-shot Learning - 커스텀 카테고리 지원",
                "accuracy": "Zero-shot 성능 우수",
                "features": ["실시간 학습", "커스텀 카테고리", "언어 이해"]
            }
        ]
    }

@app.post("/api/keys/generate")
async def generate_api_key(
    client_name: str = Form(...),
    email: str = Form(None),
    description: str = Form(None)
):
    """API 키 생성 (외부 사용자용)"""
    try:
        # API 키 생성
        api_key = api_key_manager.generate_api_key(
            client_name=client_name,
            email=email,
            description=description or f"외부 사용자: {client_name}"
        )
        
        return {
            "success": True,
            "api_key": api_key,
            "client_name": client_name,
            "message": "API 키가 성공적으로 생성되었습니다.",
            "usage_info": {
                "rate_limit": "1000 requests/hour",
                "max_image_size": "10MB",
                "supported_formats": ["JPEG", "PNG", "GIF", "BMP", "TIFF"],
                "base_url": "http://your-server:8002"
            }
        }
        
    except Exception as e:
        logger.error(f"API 키 생성 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/keys/validate")
async def validate_api_key(api_key: str):
    """API 키 유효성 검증"""
    try:
        key_info = api_key_manager.validate_api_key(api_key)
        if key_info:
            return {
                "valid": True,
                "key_info": {
                    "client_name": key_info.get("client_name"),
                    "created_at": key_info.get("created_at"),
                    "last_used": key_info.get("last_used"),
                    "usage_count": key_info.get("usage_count", 0)
                }
            }
        else:
            return {"valid": False, "message": "Invalid API key"}
            
    except Exception as e:
        logger.error(f"API 키 검증 실패: {e}")
        return {"valid": False, "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
