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

# Add src directory to Python path
src_path = os.path.dirname(os.path.dirname(__file__))
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Direct import with absolute path
import sys
import os

# Get absolute paths
current_dir = os.path.dirname(__file__)
models_path = os.path.abspath(os.path.join(current_dir, '..', 'models'))
auth_path = os.path.abspath(os.path.join(current_dir, '..', 'auth'))

# Add to Python path
if models_path not in sys.path:
    sys.path.insert(0, models_path)
if auth_path not in sys.path:
    sys.path.insert(0, auth_path)

# Debug: print paths
print(f"DEBUG: models_path = {models_path}")
print(f"DEBUG: auth_path = {auth_path}")
print(f"DEBUG: sys.path = {sys.path[:5]}")

# Check if files exist
zero_shot_file = os.path.join(models_path, 'zero_shot_classifier.py')
api_key_file = os.path.join(auth_path, 'api_key_manager.py')
print(f"DEBUG: zero_shot_file = {zero_shot_file}")
print(f"DEBUG: api_key_file = {api_key_file}")
print(f"DEBUG: zero_shot_file exists = {os.path.exists(zero_shot_file)}")
print(f"DEBUG: api_key_file exists = {os.path.exists(api_key_file)}")

# List files in models directory
models_files = os.listdir(models_path) if os.path.exists(models_path) else []
print(f"DEBUG: models directory files = {models_files}")

# Try alternative path construction
alt_zero_shot_file = os.path.join(os.path.dirname(__file__), '..', 'models', 'zero_shot_classifier.py')
alt_zero_shot_file = os.path.abspath(alt_zero_shot_file)
print(f"DEBUG: alt_zero_shot_file = {alt_zero_shot_file}")
print(f"DEBUG: alt_zero_shot_file exists = {os.path.exists(alt_zero_shot_file)}")

try:
    from zero_shot_classifier import ZeroShotCustomClassifier
    print("DEBUG: Successfully imported ZeroShotCustomClassifier")
except ImportError as e:
    print(f"DEBUG: Failed to import ZeroShotCustomClassifier: {e}")
    # Try alternative import
    import importlib.util
    spec = importlib.util.spec_from_file_location("zero_shot_classifier", zero_shot_file)
    zero_shot_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(zero_shot_module)
    ZeroShotCustomClassifier = zero_shot_module.ZeroShotCustomClassifier

try:
    from api_key_manager import APIKeyManager
    print("DEBUG: Successfully imported APIKeyManager")
except ImportError as e:
    print(f"DEBUG: Failed to import APIKeyManager: {e}")
    # Try alternative import
    import importlib.util
    spec = importlib.util.spec_from_file_location("api_key_manager", api_key_file)
    api_key_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(api_key_module)
    APIKeyManager = api_key_module.APIKeyManager
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

# Import security middleware
from middleware.security import setup_security_middleware
from config.config import Config

# CORS 설정 - 보안 강화
if Config.ENABLE_EXTERNAL_ACCESS:
    # 외부 접근 허용 시 제한된 도메인만 허용
    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"],
    )
else:
    # 로컬 접근만 허용
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
        allow_credentials=True,
        allow_methods=["GET", "POST"],
        allow_headers=["*"],
    )

# 보안 미들웨어 설정
app = setup_security_middleware(app)

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
    api_key: str = Form(...),
    request: Request = None
):
    """Zero-shot 이미지 분류"""
    client_ip = request.client.host if request else "unknown"
    
    # API 키 검증
    if not verify_api_key(api_key):
        # 보안 로깅
        api_key_manager.log_api_usage(api_key, client_ip, "/classify", 401)
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # IP 화이트리스트 검증
    if not api_key_manager.validate_ip_access(api_key, client_ip):
        api_key_manager.log_api_usage(api_key, client_ip, "/classify", 403)
        raise HTTPException(status_code=403, detail="IP address not allowed")
    
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
        
        # 성공 로깅
        api_key_manager.log_api_usage(api_key, client_ip, "/classify", 200)
        
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

@app.post("/api/keys/generate-secure")
async def generate_secure_api_key(
    client_name: str = Form(...),
    permissions: str = Form("classify"),
    expires_days: int = Form(365),
    ip_whitelist: str = Form("")
):
    """보안 API 키 생성 (IP 제한 포함)"""
    try:
        permissions_list = [p.strip() for p in permissions.split(",")]
        ip_list = [ip.strip() for ip in ip_whitelist.split(",")] if ip_whitelist else None
        
        api_key = api_key_manager.generate_secure_key(
            user_id=f"user_{int(time.time())}",
            name=client_name,
            permissions=permissions_list,
            expires_days=expires_days,
            ip_whitelist=ip_list
        )
        
        if api_key:
            return {
                "success": True,
                "api_key": api_key,
                "client_name": client_name,
                "permissions": permissions_list,
                "expires_days": expires_days,
                "ip_whitelist": ip_list,
                "message": "보안 API 키가 성공적으로 생성되었습니다.",
                "usage_info": {
                    "rate_limit": f"{Config.RATE_LIMIT_PER_MINUTE} requests/minute",
                    "max_image_size": f"{Config.MAX_REQUEST_SIZE} bytes",
                    "supported_formats": ["JPEG", "PNG", "GIF", "BMP", "TIFF"],
                    "base_url": f"http://{Config.HOST}:{Config.PORT}"
                }
            }
        else:
            raise HTTPException(status_code=500, detail="API 키 생성 실패")
            
    except Exception as e:
        logger.error(f"보안 API 키 생성 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/keys/stats")
async def get_api_key_stats(api_key: str, days: int = 30):
    """API 키 사용량 통계 조회"""
    try:
        # API 키 검증
        if not verify_api_key(api_key):
            raise HTTPException(status_code=401, detail="Invalid API key")
        
        stats = api_key_manager.get_usage_stats(api_key, days)
        
        return {
            "success": True,
            "api_key": api_key[:8] + "..." + api_key[-8:],  # 부분적으로만 표시
            "period_days": days,
            "stats": stats
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API 키 통계 조회 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/keys/revoke")
async def revoke_api_key(api_key: str = Form(...), user_id: str = Form(...)):
    """API 키 취소 (보안상의 이유로)"""
    try:
        # API 키 검증
        if not verify_api_key(api_key):
            raise HTTPException(status_code=401, detail="Invalid API key")
        
        revoked_count = api_key_manager.revoke_compromised_keys(user_id)
        
        return {
            "success": True,
            "message": f"{revoked_count}개의 API 키가 취소되었습니다.",
            "revoked_count": revoked_count,
            "user_id": user_id
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API 키 취소 실패: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
