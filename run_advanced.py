#!/usr/bin/env python3
"""
고성능 이미지 분류 API 서버 실행 스크립트
"""

import os
import sys
import logging
import uvicorn

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """고성능 API 서버 실행"""
    logger.info("🚀 VisionAI Pro Advanced Image Classification API 서버 시작")
    
    # 환경 변수 설정
    os.environ.setdefault("MODEL_TYPE", "resnet50")
    os.environ.setdefault("ENSEMBLE_MODELS", "resnet50,efficientnet")
    
    # 서버 설정
    host = "0.0.0.0"
    port = 8001  # 기존 서버와 다른 포트 사용
    
    logger.info(f"서버 주소: http://{host}:{port}")
    logger.info(f"API 문서: http://{host}:{port}/docs")
    logger.info(f"모델 타입: {os.environ.get('MODEL_TYPE')}")
    logger.info("=" * 50)
    
    # 서버 실행
    uvicorn.run(
        "src.api.advanced_main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
