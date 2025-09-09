import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.models import resnet50, ResNet50_Weights, efficientnet_b3, EfficientNet_B3_Weights
from transformers import AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import numpy as np
from typing import List, Dict, Tuple, Optional
import logging
import requests
from io import BytesIO

class AdvancedImageClassifier:
    """고성능 이미지 분류기 - 사전 훈련된 모델 사용"""
    
    def __init__(self, model_type: str = "resnet50", device: str = "cpu"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.model_type = model_type
        self.model = None
        self.processor = None
        self.transform = None
        self.categories = []
        self.logger = logging.getLogger(__name__)
        
        self._initialize_model()
    
    def _initialize_model(self):
        """모델 초기화"""
        self.logger.info(f"고성능 {self.model_type} 모델을 초기화합니다...")
        
        if self.model_type == "resnet50":
            self._setup_resnet50()
        elif self.model_type == "efficientnet":
            self._setup_efficientnet()
        elif self.model_type == "huggingface":
            self._setup_huggingface_model()
        else:
            self._setup_resnet50()  # 기본값
    
    def _setup_resnet50(self):
        """ResNet50 모델 설정"""
        # 사전 훈련된 ResNet50 로드
        self.model = resnet50(weights=ResNet50_Weights.IMAGENET1K_V2)
        self.model.eval()
        self.model.to(self.device)
        
        # ImageNet 카테고리 (1000개)
        self.categories = self._load_imagenet_categories()
        
        # 전처리 변환
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
        self.logger.info("ResNet50 모델 로드 완료 (ImageNet 1000 카테고리)")
    
    def _setup_efficientnet(self):
        """EfficientNet 모델 설정"""
        # 사전 훈련된 EfficientNet 로드
        self.model = efficientnet_b3(weights=EfficientNet_B3_Weights.IMAGENET1K_V1)
        self.model.eval()
        self.model.to(self.device)
        
        # ImageNet 카테고리
        self.categories = self._load_imagenet_categories()
        
        # 전처리 변환
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
        self.logger.info("EfficientNet 모델 로드 완료")
    
    def _setup_huggingface_model(self):
        """Hugging Face 모델 설정"""
        try:
            # Google의 Vision Transformer 모델 사용
            model_name = "google/vit-base-patch16-224"
            self.processor = AutoImageProcessor.from_pretrained(model_name)
            self.model = AutoModelForImageClassification.from_pretrained(model_name)
            self.model.eval()
            self.model.to(self.device)
            
            # 모델의 카테고리 정보 가져오기
            self.categories = list(self.model.config.id2label.values())
            
            self.logger.info(f"Hugging Face {model_name} 모델 로드 완료")
            
        except Exception as e:
            self.logger.error(f"Hugging Face 모델 로드 실패: {e}")
            self._setup_resnet50()  # 폴백
    
    def _load_imagenet_categories(self) -> List[str]:
        """ImageNet 카테고리 로드"""
        try:
            # ImageNet 1000 카테고리 URL
            url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
            response = requests.get(url)
            categories = response.text.strip().split('\n')
            return categories
        except Exception as e:
            self.logger.warning(f"ImageNet 카테고리 로드 실패: {e}")
            # 기본 카테고리 반환
            return [
                "person", "bicycle", "car", "motorcycle", "airplane", "bus", "train", "truck", "boat",
                "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack",
                "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball",
                "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
                "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
                "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
                "chair", "couch", "potted plant", "bed", "dining table", "toilet", "tv", "laptop",
                "mouse", "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink",
                "refrigerator", "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"
            ]
    
    def preprocess_image(self, image: Image.Image) -> torch.Tensor:
        """이미지 전처리"""
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        if self.model_type == "huggingface":
            # Hugging Face 모델용 전처리
            inputs = self.processor(images=image, return_tensors="pt")
            return inputs.to(self.device)
        else:
            # PyTorch 모델용 전처리
            return self.transform(image).unsqueeze(0).to(self.device)
    
    def predict(self, image: Image.Image, top_k: int = 5) -> List[Dict[str, float]]:
        """이미지 분류 예측"""
        try:
            # 이미지 전처리
            if self.model_type == "huggingface":
                inputs = self.preprocess_image(image)
                
                # 예측
                with torch.no_grad():
                    outputs = self.model(**inputs)
                    probabilities = torch.softmax(outputs.logits, dim=1)
            else:
                input_tensor = self.preprocess_image(image)
                
                # 예측
                with torch.no_grad():
                    outputs = self.model(input_tensor)
                    probabilities = torch.softmax(outputs, dim=1)
            
            # 상위 k개 결과 반환
            top_probs, top_indices = torch.topk(probabilities, min(top_k, len(self.categories)))
            
            results = []
            for prob, idx in zip(top_probs[0], top_indices[0]):
                category = self.categories[idx.item()]
                confidence = prob.item()
                results.append({
                    "category": category,
                    "confidence": round(confidence, 4)
                })
            
            return results
            
        except Exception as e:
            self.logger.error(f"예측 중 오류 발생: {e}")
            return [{"category": "Error", "confidence": 0.0}]
    
    def predict_with_confidence_threshold(self, image: Image.Image, threshold: float = 0.1) -> List[Dict[str, float]]:
        """신뢰도 임계값을 적용한 예측"""
        predictions = self.predict(image, top_k=20)
        return [pred for pred in predictions if pred["confidence"] >= threshold]
    
    def get_categories(self) -> List[str]:
        """사용 가능한 카테고리 목록 반환"""
        return self.categories
    
    def get_model_info(self) -> Dict[str, str]:
        """모델 정보 반환"""
        return {
            "model_type": self.model_type,
            "device": str(self.device),
            "categories_count": len(self.categories),
            "model_name": self.model.__class__.__name__
        }

class MultiModelEnsemble:
    """여러 모델을 조합한 앙상블 분류기"""
    
    def __init__(self, models: List[str] = None):
        self.models = []
        self.logger = logging.getLogger(__name__)
        
        if models is None:
            models = ["resnet50", "efficientnet"]
        
        for model_type in models:
            try:
                classifier = AdvancedImageClassifier(model_type)
                self.models.append(classifier)
                self.logger.info(f"{model_type} 모델 추가됨")
            except Exception as e:
                self.logger.error(f"{model_type} 모델 로드 실패: {e}")
    
    def predict_ensemble(self, image: Image.Image, top_k: int = 5) -> List[Dict[str, float]]:
        """앙상블 예측"""
        all_predictions = []
        
        # 각 모델에서 예측
        for model in self.models:
            try:
                predictions = model.predict(image, top_k=top_k)
                all_predictions.extend(predictions)
            except Exception as e:
                self.logger.error(f"모델 예측 실패: {e}")
        
        # 카테고리별 평균 신뢰도 계산
        category_scores = {}
        for pred in all_predictions:
            category = pred["category"]
            confidence = pred["confidence"]
            
            if category in category_scores:
                category_scores[category].append(confidence)
            else:
                category_scores[category] = [confidence]
        
        # 평균 신뢰도로 정렬
        ensemble_results = []
        for category, confidences in category_scores.items():
            avg_confidence = sum(confidences) / len(confidences)
            ensemble_results.append({
                "category": category,
                "confidence": round(avg_confidence, 4)
            })
        
        # 상위 k개 반환
        ensemble_results.sort(key=lambda x: x["confidence"], reverse=True)
        return ensemble_results[:top_k]
