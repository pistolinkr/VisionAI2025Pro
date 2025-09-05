#!/usr/bin/env python3
"""
Zero-shot Learning 기반 커스텀 이미지 분류 API 서버 실행 스크립트
"""

import os
import sys
import logging
import uvicorn

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    """Zero-shot API 서버 실행"""
    logger.info("🚀 VisionAI Pro Zero-Shot Custom Classification API 서버 시작")
    
    # 환경 변수 설정
    os.environ.setdefault("BASE_WORDS_PATH", "query/base_words.txt")
    os.environ.setdefault("BUILDING_TERMS_PATH", "query/building_terms_clean_final.csv")
    
    # 서버 설정
    host = "0.0.0.0"
    port = 8002  # 다른 서버와 다른 포트 사용
    
    logger.info(f"서버 주소: http://{host}:{port}")
    logger.info(f"API 문서: http://{host}:{port}/docs")
    logger.info(f"Base Words 파일: {os.environ.get('BASE_WORDS_PATH')}")
    logger.info(f"Building Terms 파일: {os.environ.get('BUILDING_TERMS_PATH')}")
    logger.info("=" * 50)
    
    # 서버 실행
    uvicorn.run(
        "src.api.zero_shot_main:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    main()
