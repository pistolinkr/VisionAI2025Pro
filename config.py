"""
VisionAI Pro Image Classification System Configuration
"""

import os
from pathlib import Path

# Base directory configuration
BASE_DIR = Path(__file__).parent
MODELS_DIR = BASE_DIR / "models"
UPLOADS_DIR = BASE_DIR / "uploads"
LOGS_DIR = BASE_DIR / "logs"
STATIC_DIR = BASE_DIR / "static"
TEMPLATES_DIR = BASE_DIR / "templates"

# Create directories
for dir_path in [MODELS_DIR, UPLOADS_DIR, LOGS_DIR, STATIC_DIR, TEMPLATES_DIR]:
    dir_path.mkdir(exist_ok=True)

# Load configuration from environment variables (with defaults)
class Config:
    # API configuration
    API_SECRET_KEY = os.getenv("API_SECRET_KEY", "your-secret-key-change-this")
    API_KEY_EXPIRY_DAYS = int(os.getenv("API_KEY_EXPIRY_DAYS", "365"))
    
    # Server configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Model configuration
    MODEL_PATH = os.getenv("MODEL_PATH", str(MODELS_DIR / "prorl_v2_model"))
    # 젯슨 환경에서는 GPU 사용 가능 여부 확인
    DEVICE = os.getenv("DEVICE", "cuda" if os.path.exists("/dev/nvidia0") else "cpu")
    
    # Image configuration
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", str(UPLOADS_DIR))
    MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", "10485760"))  # 10MB
    ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'}
    
    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/image_categories.db")
    
    # Logging configuration
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = LOGS_DIR / "app.log"
    
    # CORS configuration
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
    
    # Security configuration
    RATE_LIMIT_PER_MINUTE = int(os.getenv("RATE_LIMIT_PER_MINUTE", "60"))
    
    # Cache configuration
    CACHE_TTL = int(os.getenv("CACHE_TTL", "3600"))  # 1 hour

# Development environment configuration
class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = "DEBUG"

# Production environment configuration
class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = "WARNING"
    CORS_ORIGINS = ["https://yourdomain.com"]  # Change to actual domain

# Testing environment configuration
class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = "sqlite:///:memory:"

# Environment-specific configuration mapping
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig
}

def get_config(env_name: str = None) -> Config:
    """Return environment-specific configuration"""
    if env_name is None:
        env_name = os.getenv("ENVIRONMENT", "development")
    
    return config_by_name.get(env_name, DevelopmentConfig)

# Current configuration
current_config = get_config()
