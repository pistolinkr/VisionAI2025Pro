from fastapi import FastAPI, File, UploadFile, HTTPException, Depends, Form
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

# Add src directory to Python path
src_path = os.path.dirname(os.path.dirname(__file__))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from models.advanced_classifier import AdvancedImageClassifier, MultiModelEnsemble
from auth.api_key_manager import APIKeyManager
from config.config import *

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI 앱 생성
app = FastAPI(
    title="VisionAI Pro Advanced Image Classification API",
    description="고성능 이미지 분류 API - 사전 훈련된 모델 사용",
    version="2.0.0"
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
classifier: Optional[AdvancedImageClassifier] = None
ensemble_classifier: Optional[MultiModelEnsemble] = None
api_key_manager = APIKeyManager()

def get_classifier() -> AdvancedImageClassifier:
    """분류기 인스턴스 반환"""
    global classifier
    if classifier is None:
        model_type = os.getenv("MODEL_TYPE", "resnet50")
        classifier = AdvancedImageClassifier(model_type=model_type)
    return classifier

def get_ensemble_classifier() -> MultiModelEnsemble:
    """앙상블 분류기 인스턴스 반환"""
    global ensemble_classifier
    if ensemble_classifier is None:
        models = os.getenv("ENSEMBLE_MODELS", "resnet50,efficientnet").split(",")
        ensemble_classifier = MultiModelEnsemble(models=models)
    return ensemble_classifier

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
    logger.info("🚀 VisionAI Pro Advanced Image Classification API 시작")
    
    # 모델 초기화
    try:
        get_classifier()
        logger.info("✅ 고성능 분류기 초기화 완료")
    except Exception as e:
        logger.error(f"❌ 분류기 초기화 실패: {e}")

@app.get("/")
async def root():
    """루트 엔드포인트"""
    return {
        "message": "VisionAI Pro Advanced Image Classification API",
        "version": "2.0.0",
        "status": "running",
        "models": ["ResNet50", "EfficientNet", "Vision Transformer"],
        "categories": "1000+ ImageNet categories"
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
async def get_categories(api_key: str = None):
    """사용 가능한 카테고리 목록 반환"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    try:
        classifier = get_classifier()
        categories = classifier.get_categories()
        return {
            "success": True,
            "categories": categories,
            "count": len(categories)
        }
    except Exception as e:
        logger.error(f"카테고리 목록 조회 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/classify")
async def classify_image(
    file: UploadFile = File(...),
    top_k: int = Form(5),
    use_ensemble: bool = Form(False),
    confidence_threshold: float = Form(0.1),
    api_key: str = Form(...)
):
    """이미지 분류"""
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
        
        # 분류 실행
        if use_ensemble:
            ensemble = get_ensemble_classifier()
            predictions = ensemble.predict_ensemble(image, top_k=top_k)
        else:
            classifier = get_classifier()
            if confidence_threshold > 0:
                predictions = classifier.predict_with_confidence_threshold(
                    image, threshold=confidence_threshold
                )
            else:
                predictions = classifier.predict(image, top_k=top_k)
        
        processing_time = time.time() - start_time
        
        # 결과 반환
        return {
            "success": True,
            "image_name": file.filename,
            "processing_time": round(processing_time, 3),
            "predictions": predictions,
            "model_info": classifier.get_model_info() if not use_ensemble else {"type": "ensemble"}
        }
        
    except Exception as e:
        logger.error(f"이미지 분류 실패: {e}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=f"Classification failed: {str(e)}")

@app.post("/api/classify/advanced")
async def advanced_classify(
    file: UploadFile = File(...),
    model_type: str = Form("resnet50"),
    top_k: int = Form(5),
    api_key: str = Form(...)
):
    """고급 이미지 분류 - 모델 타입 선택 가능"""
    # API 키 검증
    if not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # 파일 검증
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Only images are allowed.")
    
    try:
        # 지정된 모델로 분류기 생성
        classifier = AdvancedImageClassifier(model_type=model_type)
        
        # 이미지 로드
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # 처리 시간 측정
        start_time = time.time()
        predictions = classifier.predict(image, top_k=top_k)
        processing_time = time.time() - start_time
        
        # 결과 반환
        return {
            "success": True,
            "image_name": file.filename,
            "model_type": model_type,
            "processing_time": round(processing_time, 3),
            "predictions": predictions,
            "model_info": classifier.get_model_info()
        }
        
    except Exception as e:
        logger.error(f"고급 이미지 분류 실패: {e}")
        raise HTTPException(status_code=500, detail=f"Advanced classification failed: {str(e)}")

@app.get("/api/models")
async def get_available_models(api_key: str = None):
    """사용 가능한 모델 목록"""
    if api_key and not verify_api_key(api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    return {
        "success": True,
        "models": [
            {
                "name": "resnet50",
                "description": "ResNet50 - ImageNet 1000 카테고리",
                "accuracy": "Top-1: 76.1%, Top-5: 92.9%"
            },
            {
                "name": "efficientnet",
                "description": "EfficientNet-B3 - 효율적인 CNN",
                "accuracy": "Top-1: 81.6%, Top-5: 95.7%"
            },
            {
                "name": "huggingface",
                "description": "Vision Transformer - 최신 트랜스포머 모델",
                "accuracy": "Top-1: 81.1%, Top-5: 95.5%"
            }
        ]
    }

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
            "supported_formats": ["JPEG", "PNG", "GIF", "BMP", "TIFF"],
            "max_image_size": "10MB",
            "processing_time_avg": "0.5-2초"
        }
    except Exception as e:
        logger.error(f"통계 조회 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
