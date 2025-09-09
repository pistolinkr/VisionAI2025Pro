import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import numpy as np
from typing import List, Dict, Tuple
import logging

class ProRLV2Classifier:
    """VisionAI Pro image category classifier (ProRL V2 foundation)"""
    
    def __init__(self, model_path: str = None, device: str = "cpu"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.model = None
        self.transform = None
        self.categories = []
        self.logger = logging.getLogger(__name__)
        
        # 이미지 전처리 변환
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], 
                               std=[0.229, 0.224, 0.225])
        ])
        
        if model_path:
            self.load_model(model_path)
        else:
            self._initialize_default_model()
    
    def _initialize_default_model(self):
        """기본 ProRL V2 모델 초기화 (실제 모델이 없는 경우)"""
        self.logger.info("기본 ProRL V2 모델을 초기화합니다...")
        
        # 간단한 CNN 기반 분류기 (실제 ProRL V2 모델 대체)
        self.model = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(64, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, 20)  # 20개 카테고리
        ).to(self.device)
        
        # Default category definitions
        self.categories = [
            "Nature", "City", "People", "Animals", "Food", "Architecture", "Transport", "Sports",
            "Art", "Technology", "Fashion", "Travel", "Music", "Movies", "Books", "Furniture",
            "Garden", "Ocean", "Mountains", "Other"
        ]
        
        self.logger.info(f"Default model loaded on {self.device}")
    
    def load_model(self, model_path: str):
        """Load saved model"""
        try:
            self.model = torch.load(model_path, map_location=self.device)
            self.model.eval()
            self.logger.info(f"Model loaded from {model_path}")
        except Exception as e:
            self.logger.warning(f"Model loading failed: {e}. Using default model.")
            self._initialize_default_model()
    
    def preprocess_image(self, image: Image.Image) -> torch.Tensor:
        """Preprocess image"""
        if image.mode != 'RGB':
            image = image.convert('RGB')
        return self.transform(image).unsqueeze(0).to(self.device)
    
    def predict(self, image: Image.Image, top_k: int = 5) -> List[Dict[str, float]]:
        """Predict image categories"""
        try:
            # Image preprocessing
            input_tensor = self.preprocess_image(image)
            
            # Prediction
            with torch.no_grad():
                outputs = self.model(input_tensor)
                probabilities = torch.softmax(outputs, dim=1)
            
            # Return top k results
            top_probs, top_indices = torch.topk(probabilities, top_k)
            
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
            self.logger.error(f"Error during prediction: {e}")
            return [{"category": "Error", "confidence": 0.0}]
    
    def get_categories(self) -> List[str]:
        """Return available categories list"""
        return self.categories
    
    def add_category(self, category: str):
        """Add new category"""
        if category not in self.categories:
            self.categories.append(category)
            # Model output layer size adjustment needed
            self.logger.info(f"New category '{category}' added")
    
    def save_model(self, path: str):
        """Save model"""
        try:
            torch.save(self.model, path)
            self.logger.info(f"Model saved to {path}")
        except Exception as e:
            self.logger.error(f"Model saving failed: {e}")
