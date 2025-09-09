import torch
import torch.nn as nn
import torchvision.transforms as transforms
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
import numpy as np
from typing import List, Dict, Tuple, Optional
import logging
import os
import json
from pathlib import Path

class ZeroShotCustomClassifier:
    """Zero-shot Learning 기반 커스텀 이미지 분류기"""
    
    def __init__(self, base_words_path: str = "query/base_words.txt", device: str = "cpu"):
        self.device = torch.device(device if torch.cuda.is_available() else "cpu")
        self.base_words_path = base_words_path
        self.model = None
        self.processor = None
        self.categories = []
        self.category_embeddings = None
        self.logger = logging.getLogger(__name__)
        
        self._load_base_words()
        self._initialize_clip_model()
    
    def _load_base_words(self):
        """base_words.txt에서 카테고리 로드"""
        try:
            with open(self.base_words_path, 'r', encoding='utf-8') as f:
                words = [line.strip() for line in f.readlines() if line.strip()]
            
            # 단어 정제 및 필터링
            self.categories = self._filter_and_clean_words(words)
            self.logger.info(f"로드된 카테고리 수: {len(self.categories)}")
            
        except Exception as e:
            self.logger.error(f"base_words.txt 로드 실패: {e}")
            # 기본 카테고리로 폴백
            self.categories = [
                "person", "animal", "vehicle", "building", "nature", "food", "object",
                "technology", "art", "sport", "music", "book", "furniture", "clothing"
            ]
    
    def _filter_and_clean_words(self, words: List[str]) -> List[str]:
        """단어 필터링 및 정제"""
        filtered_words = []
        
        for word in words:
            # 기본 필터링
            if len(word) < 2 or len(word) > 50:  # 너무 짧거나 긴 단어 제외
                continue
            
            # 특수문자만 있는 단어 제외
            if not any(c.isalpha() for c in word):
                continue
            
            # 숫자로만 된 단어 제외
            if word.isdigit():
                continue
            
            # 알파벳과 숫자만 포함된 단어만 허용
            if word.replace('-', '').replace('_', '').isalnum():
                filtered_words.append(word.lower())
        
        # 중복 제거
        unique_words = list(set(filtered_words))
        
        # 의미있는 카테고리 우선순위
        priority_categories = [
            "person", "people", "human", "man", "woman", "child", "baby",
            "animal", "dog", "cat", "bird", "fish", "horse", "cow", "sheep", "pig",
            "vehicle", "car", "truck", "bus", "train", "airplane", "boat", "bicycle",
            "building", "house", "office", "school", "hospital", "church", "tower",
            "nature", "tree", "flower", "mountain", "ocean", "river", "forest",
            "food", "fruit", "vegetable", "meat", "bread", "cake", "pizza",
            "object", "table", "chair", "bed", "lamp", "phone", "computer",
            "technology", "computer", "phone", "camera", "television", "radio",
            "art", "painting", "sculpture", "music", "instrument", "book",
            "sport", "football", "basketball", "tennis", "swimming",
            "clothing", "shirt", "pants", "dress", "shoes", "hat"
        ]
        
        # 우선순위 카테고리를 앞에 배치
        final_categories = []
        for priority in priority_categories:
            if priority in unique_words:
                final_categories.append(priority)
                unique_words.remove(priority)
        
        # 나머지 카테고리 추가 (모든 단어 사용)
        final_categories.extend(unique_words)
        
        return final_categories
    
    def _initialize_clip_model(self):
        """CLIP 모델 초기화"""
        try:
            self.logger.info("CLIP 모델을 초기화합니다...")
            
            # CLIP 모델 로드
            model_name = "openai/clip-vit-base-patch32"
            self.model = CLIPModel.from_pretrained(model_name)
            self.processor = CLIPProcessor.from_pretrained(model_name)
            
            self.model.to(self.device)
            self.model.eval()
            
            # 카테고리 임베딩 미리 계산
            self._precompute_category_embeddings()
            
            self.logger.info(f"CLIP 모델 로드 완료 ({len(self.categories)} 카테고리)")
            
        except Exception as e:
            self.logger.error(f"CLIP 모델 로드 실패: {e}")
            raise e
    
    def _precompute_category_embeddings(self):
        """카테고리 텍스트 임베딩 미리 계산"""
        try:
            self.logger.info("카테고리 임베딩을 계산합니다...")
            
            # 텍스트 전처리
            text_inputs = self.processor(
                text=self.categories,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=77
            ).to(self.device)
            
            # 텍스트 임베딩 계산
            with torch.no_grad():
                text_features = self.model.get_text_features(**text_inputs)
                text_features = text_features / text_features.norm(dim=-1, keepdim=True)
            
            self.category_embeddings = text_features
            self.logger.info("카테고리 임베딩 계산 완료")
            
        except Exception as e:
            self.logger.error(f"카테고리 임베딩 계산 실패: {e}")
            self.category_embeddings = None
    
    def predict(self, image: Image.Image, top_k: int = 5) -> List[Dict[str, float]]:
        """Zero-shot 이미지 분류 예측"""
        try:
            if self.category_embeddings is None:
                raise ValueError("카테고리 임베딩이 초기화되지 않았습니다")
            
            # 이미지 전처리
            image_inputs = self.processor(
                images=image,
                return_tensors="pt"
            ).to(self.device)
            
            # 이미지 임베딩 계산
            with torch.no_grad():
                image_features = self.model.get_image_features(**image_inputs)
                image_features = image_features / image_features.norm(dim=-1, keepdim=True)
            
            # 유사도 계산
            similarity = torch.matmul(image_features, self.category_embeddings.T)
            similarity = similarity.squeeze(0)
            
            # 상위 k개 결과 반환
            top_indices = torch.topk(similarity, min(top_k, len(self.categories))).indices
            top_scores = torch.topk(similarity, min(top_k, len(self.categories))).values
            
            results = []
            for score, idx in zip(top_scores, top_indices):
                category = self.categories[idx.item()]
                confidence = torch.sigmoid(score).item()  # 0-1 범위로 정규화
                results.append({
                    "category": category,
                    "confidence": round(confidence, 4)
                })
            
            return results
            
        except Exception as e:
            self.logger.error(f"예측 중 오류 발생: {e}")
            return [{"category": "Error", "confidence": 0.0}]
    
    def add_custom_category(self, category: str, description: str = ""):
        """새로운 커스텀 카테고리 추가"""
        try:
            if category not in self.categories:
                self.categories.append(category)
                
                # 새로운 카테고리 임베딩 계산
                text_inputs = self.processor(
                    text=[category],
                    return_tensors="pt",
                    padding=True,
                    truncation=True,
                    max_length=77
                ).to(self.device)
                
                with torch.no_grad():
                    text_features = self.model.get_text_features(**text_inputs)
                    text_features = text_features / text_features.norm(dim=-1, keepdim=True)
                
                # 임베딩 업데이트
                if self.category_embeddings is not None:
                    self.category_embeddings = torch.cat([self.category_embeddings, text_features], dim=0)
                else:
                    self.category_embeddings = text_features
                
                self.logger.info(f"새로운 카테고리 추가: {category}")
                return True
            else:
                self.logger.warning(f"카테고리가 이미 존재합니다: {category}")
                return False
                
        except Exception as e:
            self.logger.error(f"카테고리 추가 실패: {e}")
            return False
    
    def remove_category(self, category: str):
        """카테고리 제거"""
        try:
            if category in self.categories:
                idx = self.categories.index(category)
                self.categories.pop(idx)
                
                # 임베딩에서도 제거
                if self.category_embeddings is not None:
                    self.category_embeddings = torch.cat([
                        self.category_embeddings[:idx],
                        self.category_embeddings[idx+1:]
                    ])
                
                self.logger.info(f"카테고리 제거: {category}")
                return True
            else:
                self.logger.warning(f"카테고리가 존재하지 않습니다: {category}")
                return False
                
        except Exception as e:
            self.logger.error(f"카테고리 제거 실패: {e}")
            return False
    
    def search_categories(self, query: str, top_k: int = 10) -> List[str]:
        """카테고리 검색"""
        try:
            if not query.strip():
                return self.categories[:top_k]
            
            # 검색어 임베딩 계산
            text_inputs = self.processor(
                text=[query],
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=77
            ).to(self.device)
            
            with torch.no_grad():
                query_features = self.model.get_text_features(**text_inputs)
                query_features = query_features / query_features.norm(dim=-1, keepdim=True)
            
            # 유사도 계산
            similarity = torch.matmul(query_features, self.category_embeddings.T)
            similarity = similarity.squeeze(0)
            
            # 상위 결과 반환
            top_indices = torch.topk(similarity, min(top_k, len(self.categories))).indices
            
            return [self.categories[idx.item()] for idx in top_indices]
            
        except Exception as e:
            self.logger.error(f"카테고리 검색 실패: {e}")
            return []
    
    def get_categories(self) -> List[str]:
        """사용 가능한 카테고리 목록 반환"""
        return self.categories
    
    def get_model_info(self) -> Dict[str, str]:
        """모델 정보 반환"""
        return {
            "model_type": "zero_shot_clip",
            "device": str(self.device),
            "categories_count": len(self.categories),
            "model_name": "CLIP (Zero-shot Learning)",
            "base_words_file": self.base_words_path
        }
    
    def save_categories(self, filepath: str):
        """카테고리를 파일로 저장"""
        try:
            data = {
                "categories": self.categories,
                "model_info": self.get_model_info()
            }
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            self.logger.info(f"카테고리를 저장했습니다: {filepath}")
            
        except Exception as e:
            self.logger.error(f"카테고리 저장 실패: {e}")
    
    def load_categories(self, filepath: str):
        """파일에서 카테고리 로드"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.categories = data.get("categories", [])
            self._precompute_category_embeddings()
            
            self.logger.info(f"카테고리를 로드했습니다: {filepath}")
            
        except Exception as e:
            self.logger.error(f"카테고리 로드 실패: {e}")
