#!/usr/bin/env python3
"""
빠른 서버 시작 테스트 스크립트
"""

import os
import sys
import time
import logging

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(__file__))

from src.models.zero_shot_classifier import ZeroShotCustomClassifier

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def test_quick_start():
    """빠른 시작 테스트"""
    logger.info("🚀 빠른 시작 테스트")
    
    start_time = time.time()
    
    try:
        # 분류기 생성 (lazy loading)
        logger.info("분류기 생성 중...")
        classifier = ZeroShotCustomClassifier()
        
        creation_time = time.time() - start_time
        logger.info(f"✅ 분류기 생성 완료: {creation_time:.2f}초")
        
        # 모델 정보 확인 (CLIP 모델 초기화 없이)
        model_info = classifier.get_model_info()
        logger.info(f"모델 정보: {model_info}")
        
        # 카테고리 수 확인
        base_categories = len(classifier.categories)
        building_categories = len(classifier.building_categories)
        total_categories = base_categories + building_categories
        
        logger.info(f"기본 카테고리: {base_categories}개")
        logger.info(f"건물 카테고리: {building_categories}개")
        logger.info(f"총 카테고리: {total_categories}개")
        
        total_time = time.time() - start_time
        logger.info(f"🎉 전체 초기화 완료: {total_time:.2f}초")
        
        return True
        
    except Exception as e:
        logger.error(f"빠른 시작 테스트 실패: {e}")
        return False

if __name__ == "__main__":
    logger.info("🚀 빠른 시작 테스트 시작")
    
    try:
        success = test_quick_start()
        
        if success:
            logger.info("✅ 빠른 시작 테스트 성공!")
        else:
            logger.error("❌ 빠른 시작 테스트 실패!")
            
    except Exception as e:
        logger.error(f"테스트 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()
