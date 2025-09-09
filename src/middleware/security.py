"""
Security middleware for VisionAI Pro API
"""

import time
import logging
from typing import Dict, List
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
import redis
from config.config import Config

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Redis connection for rate limiting (fallback to in-memory if Redis not available)
try:
    redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
    redis_client.ping()
    logger.info("Redis connected successfully for rate limiting")
except:
    redis_client = None
    logger.warning("Redis not available, using in-memory rate limiting")

# Rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379" if redis_client else "memory://",
    default_limits=[f"{Config.RATE_LIMIT_PER_MINUTE}/minute"]
)

# In-memory rate limiting fallback
rate_limit_storage: Dict[str, List[float]] = {}

def check_rate_limit(client_ip: str, limit: int = 60, window: int = 60) -> bool:
    """Check if client has exceeded rate limit"""
    if redis_client:
        return True  # Redis handles this
    
    current_time = time.time()
    if client_ip not in rate_limit_storage:
        rate_limit_storage[client_ip] = []
    
    # Remove old requests outside the window
    rate_limit_storage[client_ip] = [
        req_time for req_time in rate_limit_storage[client_ip]
        if current_time - req_time < window
    ]
    
    # Check if limit exceeded
    if len(rate_limit_storage[client_ip]) >= limit:
        return False
    
    # Add current request
    rate_limit_storage[client_ip].append(current_time)
    return True

def validate_origin(request: Request, allowed_origins: List[str]) -> bool:
    """Validate request origin"""
    origin = request.headers.get("origin")
    if not origin:
        return True  # Allow requests without origin (e.g., direct API calls)
    
    return origin in allowed_origins

def validate_host(request: Request, allowed_hosts: List[str]) -> bool:
    """Validate request host"""
    host = request.headers.get("host", "").split(":")[0]
    return host in allowed_hosts

def validate_request_size(request: Request, max_size: int) -> bool:
    """Validate request size"""
    content_length = request.headers.get("content-length")
    if content_length and int(content_length) > max_size:
        return False
    return True

async def security_middleware(request: Request, call_next):
    """Main security middleware"""
    try:
        # Get client IP
        client_ip = get_remote_address(request)
        
        # Check rate limit
        if not check_rate_limit(client_ip, Config.RATE_LIMIT_PER_MINUTE):
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return JSONResponse(
                status_code=429,
                content={"error": "Rate limit exceeded", "detail": "Too many requests"}
            )
        
        # Validate origin if external access is enabled
        if Config.ENABLE_EXTERNAL_ACCESS:
            if not validate_origin(request, Config.ALLOWED_ORIGINS):
                logger.warning(f"Invalid origin: {request.headers.get('origin')} from IP: {client_ip}")
                return JSONResponse(
                    status_code=403,
                    content={"error": "Forbidden", "detail": "Origin not allowed"}
                )
            
            if not validate_host(request, Config.ALLOWED_HOSTS):
                logger.warning(f"Invalid host: {request.headers.get('host')} from IP: {client_ip}")
                return JSONResponse(
                    status_code=403,
                    content={"error": "Forbidden", "detail": "Host not allowed"}
                )
        
        # Validate request size
        if not validate_request_size(request, Config.MAX_REQUEST_SIZE):
            logger.warning(f"Request too large from IP: {client_ip}")
            return JSONResponse(
                status_code=413,
                content={"error": "Request too large", "detail": f"Maximum size: {Config.MAX_REQUEST_SIZE} bytes"}
            )
        
        # Log request
        logger.info(f"Request: {request.method} {request.url} from {client_ip}")
        
        # Process request
        response = await call_next(request)
        
        # Add security headers
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        
        return response
        
    except Exception as e:
        logger.error(f"Security middleware error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"error": "Internal server error", "detail": "Security check failed"}
        )

def setup_security_middleware(app):
    """Setup security middleware for FastAPI app"""
    # Add rate limiting
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
    
    # Add custom security middleware
    app.middleware("http")(security_middleware)
    
    return app
