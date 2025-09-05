#!/usr/bin/env python3
"""
Zero-shot Learning 모델 테스트 스크립트
"""

import os
import sys
import time
import logging
from PIL import Image
import requests
from io import BytesIO

# 프로젝트 루트를 Python 경로에 추가
sys.path.append(os.path.dirname(__file__))

from src.models.zero_shot_classifier import ZeroShotCustomClassifier

# 로깅 설정
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def download_test_image():
    """테스트용 이미지 다운로드"""
    try:
        # 고양이 이미지 다운로드
        url = "https://images.unsplash.com/photo-1514888286974-6c03e2a1e311?w=400"
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        
        # 테스트용으로 저장
        test_path = "test_cat.jpg"
        image.save(test_path)
        logger.info(f"테스트 이미지 다운로드 완료: {test_path}")
        return test_path
    except Exception as e:
        logger.error(f"테스트 이미지 다운로드 실패: {e}")
        return None

def test_zero_shot_classifier():
    """Zero-shot 분류기 테스트"""
    logger.info("=" * 50)
    logger.info("🔍 Zero-shot 분류기 테스트 시작")
    
    try:
        # 모델 초기화
        classifier = ZeroShotCustomClassifier()
        
        # 모델 정보 출력
        model_info = classifier.get_model_info()
        logger.info(f"모델 정보: {model_info}")
        
        # 테스트 이미지 로드
        test_image_path = download_test_image()
        if not test_image_path:
            logger.error("테스트 이미지를 로드할 수 없습니다.")
            return
        
        image = Image.open(test_image_path)
        logger.info(f"테스트 이미지 크기: {image.size}")
        
        # 예측 실행
        start_time = time.time()
        predictions = classifier.predict(image, top_k=5)
        processing_time = time.time() - start_time
        
        # 결과 출력
        logger.info(f"처리 시간: {processing_time:.3f}초")
        logger.info("예측 결과:")
        for i, pred in enumerate(predictions, 1):
            logger.info(f"  {i}. {pred['category']}: {pred['confidence']:.4f} ({pred['confidence']*100:.1f}%)")
        
        return predictions
        
    except Exception as e:
        logger.error(f"Zero-shot 테스트 실패: {e}")
        return None

def test_category_management():
    """카테고리 관리 기능 테스트"""
    logger.info("=" * 50)
    logger.info("🔧 카테고리 관리 기능 테스트")
    
    try:
        classifier = ZeroShotCustomClassifier()
        
        # 카테고리 추가 테스트
        logger.info("새로운 카테고리 추가 테스트:")
        success = classifier.add_custom_category("my_custom_category", "테스트용 커스텀 카테고리")
        logger.info(f"카테고리 추가 결과: {success}")
        
        # 카테고리 검색 테스트
        logger.info("카테고리 검색 테스트:")
        search_results = classifier.search_categories("animal", top_k=5)
        logger.info(f"검색 결과: {search_results}")
        
        # 카테고리 제거 테스트
        logger.info("카테고리 제거 테스트:")
        success = classifier.remove_category("my_custom_category")
        logger.info(f"카테고리 제거 결과: {success}")
        
        return True
        
    except Exception as e:
        logger.error(f"카테고리 관리 테스트 실패: {e}")
        return False

def test_with_different_images():
    """다양한 이미지로 테스트"""
    logger.info("=" * 50)
    logger.info("🖼️ 다양한 이미지로 Zero-shot 테스트")
    
    # 다양한 테스트 이미지 URL들
    test_images = [
        ("고양이", "https://images.unsplash.com/photo-1514888286974-6c03e2a1e311?w=400"),
        ("자동차", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=400"),
        ("자연 풍경", "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400"),
        ("음식", "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400"),
        ("건물", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400")
    ]
    
    classifier = ZeroShotCustomClassifier()
    
    for image_name, url in test_images:
        logger.info(f"\n--- {image_name} Zero-shot 테스트 ---")
        try:
            # 이미지 다운로드
            response = requests.get(url)
            image = Image.open(BytesIO(response.content))
            
            # 예측
            predictions = classifier.predict(image, top_k=3)
            
            # 결과 출력
            logger.info(f"예측 결과:")
            for i, pred in enumerate(predictions, 1):
                logger.info(f"  {i}. {pred['category']}: {pred['confidence']*100:.1f}%")
                
        except Exception as e:
            logger.error(f"{image_name} 테스트 실패: {e}")

def test_building_terms_integration():
    """건물 용어 통합 테스트"""
    logger.info("=" * 50)
    logger.info("🏢 건물 용어 통합 테스트")
    
    try:
        classifier = ZeroShotCustomClassifier()
        
        # 모델 정보 확인
        model_info = classifier.get_model_info()
        logger.info(f"모델 정보: {model_info}")
        
        # 건물 관련 카테고리 확인
        building_categories = classifier.get_building_categories()
        logger.info(f"건물 관련 카테고리 수: {len(building_categories)}")
        logger.info(f"건물 카테고리 샘플: {building_categories[:10]}")
        
        # 건물 관련 검색 테스트
        building_search_queries = [
            "building",
            "office",
            "hospital",
            "museum",
            "church",
            "tower",
            "apartment",
            "hotel",
            "restaurant",
            "school"
        ]
        
        for query in building_search_queries:
            logger.info(f"\n건물 검색어: '{query}'")
            results = classifier.search_categories(query, top_k=5)
            logger.info(f"검색 결과: {results}")
        
        return True
        
    except Exception as e:
        logger.error(f"건물 용어 통합 테스트 실패: {e}")
        return False

def test_building_images():
    """건물 이미지로 테스트"""
    logger.info("=" * 50)
    logger.info("🏢 건물 이미지로 Zero-shot 테스트")
    
    # 건물 관련 테스트 이미지 URL들
    building_images = [
        ("고층 건물", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400"),
        ("교회", "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=400"),
        ("병원", "https://images.unsplash.com/photo-1519494026892-80bbd28d69a9?w=400"),
        ("학교", "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?w=400"),
        ("박물관", "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400"),
        ("호텔", "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400"),
        ("레스토랑", "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400"),
        ("아파트", "https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=400")
    ]
    
    classifier = ZeroShotCustomClassifier()
    
    for image_name, url in building_images:
        logger.info(f"\n--- {image_name} Zero-shot 테스트 ---")
        try:
            # 이미지 다운로드
            response = requests.get(url)
            image = Image.open(BytesIO(response.content))
            
            # 예측
            predictions = classifier.predict(image, top_k=5)
            
            # 결과 출력
            logger.info(f"예측 결과:")
            for i, pred in enumerate(predictions, 1):
                logger.info(f"  {i}. {pred['category']}: {pred['confidence']*100:.1f}%")
                
        except Exception as e:
            logger.error(f"{image_name} 테스트 실패: {e}")

if __name__ == "__main__":
    logger.info("🚀 Zero-shot Learning 모델 테스트 시작")
    
    try:
        # 기본 분류 테스트
        test_zero_shot_classifier()
        
        # 카테고리 관리 테스트
        test_category_management()
        
        # 다양한 이미지 테스트
        test_with_different_images()
        
        # 건물 용어 통합 테스트
        test_building_terms_integration()
        
        # 건물 이미지 테스트
        test_building_images()
        
        logger.info("✅ 모든 테스트 완료!")
        
    except Exception as e:
        logger.error(f"테스트 중 오류 발생: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 테스트 파일 정리
        if os.path.exists("test_cat.jpg"):
            os.remove("test_cat.jpg")
            logger.info("테스트 파일 정리 완료")
