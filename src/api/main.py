from fastapi import FastAPI, HTTPException, Depends, File, UploadFile, Form, Header
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
import logging
from typing import Optional, List
from PIL import Image
import io
import json
from datetime import datetime

# 로컬 모듈 import
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.prorl_classifier import ProRLV2Classifier
from auth.api_key_manager import APIKeyManager

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI 앱 초기화
app = FastAPI(
    title="ProRL V2 Image Classification API",
    description="ProRL V2 based image category auto-recommendation system",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files and templates setup
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Global objects initialization
classifier = None
api_key_manager = None

@app.on_event("startup")
async def startup_event():
    """App initialization on startup"""
    global classifier, api_key_manager
    
    # Load environment variables
    model_path = os.getenv("MODEL_PATH")
    device = os.getenv("DEVICE", "cpu")
    secret_key = os.getenv("API_SECRET_KEY", "default-secret-key")
    
    # Initialize classifier
    classifier = ProRLV2Classifier(model_path=model_path, device=device)
    
    # Initialize API key manager
    api_key_manager = APIKeyManager(secret_key=secret_key)
    
    logger.info("VisionAI Pro Image Classification API started")

def verify_api_key(api_key: str = Header(..., alias="X-API-Key")) -> dict:
    """API key validation dependency"""
    if not api_key_manager:
        raise HTTPException(status_code=500, detail="API key manager not initialized")
    
    key_info = api_key_manager.validate_api_key(api_key)
    if not key_info:
        raise HTTPException(status_code=401, detail="Invalid API key")
    
    # Return a dict with the key info and the original API key
    return {
        "key": api_key,
        "user_id": key_info.user_id,
        "name": key_info.name,
        "permissions": key_info.permissions,
        "created_at": key_info.created_at,
        "expires_at": key_info.expires_at,
        "is_active": key_info.is_active
    }

@app.get("/", response_class=HTMLResponse)
async def root():
    """Main page"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>VisionAI Pro Image Classification API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            .endpoint { background: #f5f5f5; padding: 15px; margin: 10px 0; border-radius: 5px; }
            code { background: #e0e0e0; padding: 2px 5px; border-radius: 3px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 VisionAI Pro Image Classification API</h1>
            <p>ProRL V2 based image category auto-recommendation system</p>
            
            <h2>📚 API Endpoints</h2>
            
            <div class="endpoint">
                <h3>POST /api/classify</h3>
                <p>Image Classification</p>
                <code>X-API-Key: your-api-key</code>
            </div>
            
            <div class="endpoint">
                <h3>GET /api/categories</h3>
                <p>Available Categories List</p>
                <code>X-API-Key: your-api-key</code>
            </div>
            
            <div class="endpoint">
                <h3>POST /api/keys/generate</h3>
                <p>Generate New API Key</p>
                <code>X-API-Key: your-api-key</code>
            </div>
            
            <h2>🔑 API Key Management</h2>
            <p>Valid API key is required to use the API.</p>
            
            <h2>📖 Documentation</h2>
            <p><a href="/docs">Swagger UI Docs</a> | <a href="/redoc">ReDoc Docs</a></p>
        </div>
    </body>
    </html>
    """

@app.post("/api/classify")
async def classify_image(
    file: UploadFile = File(...),
    top_k: int = Form(5),
    api_key_info: dict = Depends(verify_api_key)
):
    """Image Classification API"""
    try:
        # File type validation
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Only image files can be uploaded")
        
        # Read image
        image_data = await file.read()
        image = Image.open(io.BytesIO(image_data))
        
        # Perform classification
        results = classifier.predict(image, top_k=top_k)
        
        return {
            "success": True,
            "image_name": file.filename,
            "predictions": results,
            "user_id": api_key_info["user_id"],
            "timestamp": str(api_key_info["created_at"])
        }
        
    except Exception as e:
        logger.error(f"Image classification failed: {e}")
        raise HTTPException(status_code=500, detail=f"Error occurred during classification: {str(e)}")

@app.get("/api/categories")
async def get_categories(api_key_info: dict = Depends(verify_api_key)):
    """Get available categories list"""
    try:
        categories = classifier.get_categories()
        return {
            "success": True,
            "categories": categories,
            "total_count": len(categories)
        }
    except Exception as e:
        logger.error(f"Category retrieval failed: {e}")
        raise HTTPException(status_code=500, detail="Error occurred while retrieving categories")

@app.post("/api/keys/generate")
async def generate_api_key(
    name: str = Form(...),
    permissions: str = Form("read,classify"),
    expiry_days: int = Form(365),
    api_key_info: dict = Depends(verify_api_key)
):
    """Generate new API key"""
    try:
        # Permission check (admin permission required)
        if "admin" not in api_key_info["permissions"]:
            raise HTTPException(status_code=403, detail="No permission to generate API key")
        
        # Parse permissions
        permission_list = [p.strip() for p in permissions.split(",")]
        
        # Generate new API key
        new_key = api_key_manager.generate_api_key(
            user_id=api_key_info["user_id"],
            name=name,
            permissions=permission_list,
            expiry_days=expiry_days
        )
        
        if not new_key:
            raise HTTPException(status_code=500, detail="Failed to generate API key")
        
        return {
            "success": True,
            "api_key": new_key,
            "name": name,
            "permissions": permission_list,
            "expires_in_days": expiry_days
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API key generation failed: {e}")
        raise HTTPException(status_code=500, detail="Error occurred while generating API key")

@app.get("/api/keys/info")
async def get_key_info(api_key_info: dict = Depends(verify_api_key)):
    """Get current API key information"""
    try:
        key_info = api_key_manager.get_key_info(api_key_info["key"])
        return {
            "success": True,
            "key_info": key_info
        }
    except Exception as e:
        logger.error(f"Failed to get API key info: {e}")
        raise HTTPException(status_code=500, detail="Error occurred while retrieving API key info")

@app.delete("/api/keys/revoke")
async def revoke_api_key(
    target_key: str = Form(...),
    api_key_info: dict = Depends(verify_api_key)
):
    """Revoke API key"""
    try:
        # Permission check (admin permission required)
        if "admin" not in api_key_info.permissions:
            raise HTTPException(status_code=403, detail="No permission to revoke API key")
        
        # Revoke key
        success = api_key_manager.revoke_api_key(target_key)
        
        if not success:
            raise HTTPException(status_code=500, detail="Failed to revoke API key")
        
        return {
            "success": True,
            "message": "API key has been revoked"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"API key revocation failed: {e}")
        raise HTTPException(status_code=500, detail="Error occurred while revoking API key")

@app.get("/health")
async def health_check():
    """Health check"""
    return {
        "status": "healthy",
        "classifier_loaded": classifier is not None,
        "api_key_manager_loaded": api_key_manager is not None,
        "timestamp": str(datetime.now()),
        "version": "1.0.0"
    }

@app.get("/debug")
async def debug_info():
    """Debug information (no authentication required)"""
    return {
        "server_time": str(datetime.now()),
        "classifier_loaded": classifier is not None,
        "api_key_manager_loaded": api_key_manager is not None,
        "available_endpoints": [
            "/",
            "/health",
            "/debug",
            "/docs",
            "/redoc",
            "/api/classify",
            "/api/categories",
            "/api/keys/generate",
            "/api/keys/info",
            "/api/keys/revoke"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
