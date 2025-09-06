#!/usr/bin/env python3
"""
고성능 이미지 분류 모델 테스트 스크립트
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

from src.models.advanced_classifier import AdvancedImageClassifier, MultiModelEnsemble

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

def test_resnet50():
    """ResNet50 모델 테스트"""
    logger.info("=" * 50)
    logger.info("🔍 ResNet50 모델 테스트 시작")
    
    try:
        # 모델 초기화
        classifier = AdvancedImageClassifier(model_type="resnet50")
        
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
        logger.error(f"ResNet50 테스트 실패: {e}")
        return None

def test_efficientnet():
    """EfficientNet 모델 테스트"""
    logger.info("=" * 50)
    logger.info("🔍 EfficientNet 모델 테스트 시작")
    
    try:
        # 모델 초기화
        classifier = AdvancedImageClassifier(model_type="efficientnet")
        
        # 모델 정보 출력
        model_info = classifier.get_model_info()
        logger.info(f"모델 정보: {model_info}")
        
        # 테스트 이미지 로드
        test_image_path = "test_cat.jpg"
        if not os.path.exists(test_image_path):
            logger.error("테스트 이미지가 없습니다.")
            return
        
        image = Image.open(test_image_path)
        
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
        logger.error(f"EfficientNet 테스트 실패: {e}")
        return None

def test_ensemble():
    """앙상블 모델 테스트"""
    logger.info("=" * 50)
    logger.info("🔍 앙상블 모델 테스트 시작")
    
    try:
        # 앙상블 모델 초기화
        ensemble = MultiModelEnsemble(models=["resnet50", "efficientnet"])
        
        # 테스트 이미지 로드
        test_image_path = "test_cat.jpg"
        if not os.path.exists(test_image_path):
            logger.error("테스트 이미지가 없습니다.")
            return
        
        image = Image.open(test_image_path)
        
        # 앙상블 예측 실행
        start_time = time.time()
        predictions = ensemble.predict_ensemble(image, top_k=5)
        processing_time = time.time() - start_time
        
        # 결과 출력
        logger.info(f"처리 시간: {processing_time:.3f}초")
        logger.info("앙상블 예측 결과:")
        for i, pred in enumerate(predictions, 1):
            logger.info(f"  {i}. {pred['category']}: {pred['confidence']:.4f} ({pred['confidence']*100:.1f}%)")
        
        return predictions
        
    except Exception as e:
        logger.error(f"앙상블 테스트 실패: {e}")
        return None

def compare_models():
    """모델 성능 비교"""
    logger.info("=" * 50)
    logger.info("🏆 모델 성능 비교")
    
    results = {}
    
    # ResNet50 테스트
    resnet_results = test_resnet50()
    if resnet_results:
        results["resnet50"] = resnet_results
    
    # EfficientNet 테스트
    efficient_results = test_efficientnet()
    if efficient_results:
        results["efficientnet"] = efficient_results
    
    # 앙상블 테스트
    ensemble_results = test_ensemble()
    if ensemble_results:
        results["ensemble"] = ensemble_results
    
    # 결과 비교
    logger.info("=" * 50)
    logger.info("📊 모델 성능 비교 결과")
    
    for model_name, predictions in results.items():
        logger.info(f"\n{model_name.upper()}:")
        for i, pred in enumerate(predictions[:3], 1):  # 상위 3개만
            logger.info(f"  {i}. {pred['category']}: {pred['confidence']*100:.1f}%")

def test_with_different_images():
    """다양한 이미지로 테스트"""
    logger.info("=" * 50)
    logger.info("🖼️ 다양한 이미지로 테스트")
    
    # 다양한 테스트 이미지 URL들
    test_images = [
        ("고양이", "https://images.unsplash.com/photo-1514888286974-6c03e2a1e311?w=400"),
        ("자동차", "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=400"),
        ("자연 풍경", "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=400"),
        ("음식", "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400"),
        ("건물", "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=400")
    ]
    
    classifier = AdvancedImageClassifier(model_type="resnet50")
    
    for image_name, url in test_images:
        logger.info(f"\n--- {image_name} 테스트 ---")
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

if __name__ == "__main__":
    logger.info("🚀 고성능 이미지 분류 모델 테스트 시작")
    
    try:
        # 개별 모델 테스트
        compare_models()
        
        # 다양한 이미지 테스트
        test_with_different_images()
        
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
