"""
Firebase Data Manager for VisionAI Pro Image Classification System
"""

import os
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any
import logging
import json

# Add parent directory to path to import firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from config.firebase_config import firebase_config

class FirebaseDataManager:
    """Firebase Firestore-based data management for image classification results"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db = firebase_config.get_db()
        
        if not self.db:
            self.logger.error("Firebase database not available")
            raise RuntimeError("Firebase database not initialized")
    
    def _convert_datetime_to_timestamp(self, dt: datetime) -> str:
        """Convert datetime to ISO format string for Firestore"""
        return dt.isoformat()
    
    def _convert_timestamp_to_datetime(self, timestamp: str) -> datetime:
        """Convert ISO format string from Firestore to datetime"""
        return datetime.fromisoformat(timestamp)
    
    def save_classification_result(self, 
                                 user_id: str,
                                 api_key: str,
                                 image_path: str,
                                 predictions: List[Dict],
                                 confidence_scores: List[float],
                                 processing_time: float,
                                 model_version: str = "prorl_v2") -> str:
        """Save image classification result to Firestore"""
        try:
            # Create document data
            doc_data = {
                "user_id": user_id,
                "api_key": api_key,
                "image_path": image_path,
                "predictions": predictions,
                "confidence_scores": confidence_scores,
                "processing_time": processing_time,
                "model_version": model_version,
                "created_at": self._convert_datetime_to_timestamp(datetime.now()),
                "status": "completed"
            }
            
            # Save to Firestore
            doc_ref = self.db.collection("classification_results").add(doc_data)
            
            self.logger.info(f"Classification result saved: {doc_ref[1].id}")
            return doc_ref[1].id
            
        except Exception as e:
            self.logger.error(f"Failed to save classification result: {e}")
            return None
    
    def get_user_classifications(self, user_id: str, limit: int = 50) -> List[Dict]:
        """Get classification results for a specific user"""
        try:
            # Query Firestore for user's classifications
            query = self.db.collection("classification_results").where("user_id", "==", user_id).order_by("created_at", direction="DESCENDING").limit(limit)
            docs = query.stream()
            
            results = []
            for doc in docs:
                data = doc.to_dict()
                data["id"] = doc.id
                data["created_at"] = self._convert_timestamp_to_datetime(data.get("created_at"))
                results.append(data)
            
            return results
            
        except Exception as e:
            self.logger.error(f"Failed to get user classifications: {e}")
            return []
    
    def get_classification_by_id(self, classification_id: str) -> Optional[Dict]:
        """Get specific classification result by ID"""
        try:
            doc_ref = self.db.collection("classification_results").document(classification_id)
            doc = doc_ref.get()
            
            if not doc.exists:
                return None
            
            data = doc.to_dict()
            data["id"] = doc.id
            data["created_at"] = self._convert_timestamp_to_datetime(data.get("created_at"))
            
            return data
            
        except Exception as e:
            self.logger.error(f"Failed to get classification by ID: {e}")
            return None
    
    def save_user_profile(self, user_id: str, profile_data: Dict) -> bool:
        """Save or update user profile"""
        try:
            # Add timestamp
            profile_data["updated_at"] = self._convert_datetime_to_timestamp(datetime.now())
            
            # Save to Firestore
            self.db.collection("user_profiles").document(user_id).set(profile_data, merge=True)
            
            self.logger.info(f"User profile saved: {user_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to save user profile: {e}")
            return False
    
    def get_user_profile(self, user_id: str) -> Optional[Dict]:
        """Get user profile"""
        try:
            doc_ref = self.db.collection("user_profiles").document(user_id)
            doc = doc_ref.get()
            
            if not doc.exists:
                return None
            
            data = doc.to_dict()
            if "updated_at" in data:
                data["updated_at"] = self._convert_timestamp_to_datetime(data["updated_at"])
            
            return data
            
        except Exception as e:
            self.logger.error(f"Failed to get user profile: {e}")
            return None
    
    def save_usage_statistics(self, user_id: str, api_key: str, 
                             request_type: str, processing_time: float,
                             success: bool = True) -> bool:
        """Save usage statistics for analytics"""
        try:
            # Create document data
            doc_data = {
                "user_id": user_id,
                "api_key": api_key,
                "request_type": request_type,
                "processing_time": processing_time,
                "success": success,
                "timestamp": self._convert_datetime_to_timestamp(datetime.now())
            }
            
            # Save to Firestore
            self.db.collection("usage_statistics").add(doc_data)
            
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to save usage statistics: {e}")
            return False
    
    def get_user_usage_stats(self, user_id: str, days: int = 30) -> Dict:
        """Get usage statistics for a user"""
        try:
            from datetime import timedelta
            
            # Calculate date range
            end_date = datetime.now()
            start_date = end_date - timedelta(days=days)
            
            # Query Firestore for user's usage statistics
            query = self.db.collection("usage_statistics").where("user_id", "==", user_id).where("timestamp", ">=", self._convert_datetime_to_timestamp(start_date))
            docs = query.stream()
            
            stats = {
                "total_requests": 0,
                "successful_requests": 0,
                "failed_requests": 0,
                "average_processing_time": 0,
                "total_processing_time": 0
            }
            
            processing_times = []
            
            for doc in docs:
                data = doc.to_dict()
                stats["total_requests"] += 1
                
                if data.get("success", False):
                    stats["successful_requests"] += 1
                else:
                    stats["failed_requests"] += 1
                
                processing_time = data.get("processing_time", 0)
                stats["total_processing_time"] += processing_time
                processing_times.append(processing_time)
            
            if processing_times:
                stats["average_processing_time"] = stats["total_processing_time"] / len(processing_times)
            
            return stats
            
        except Exception as e:
            self.logger.error(f"Failed to get user usage stats: {e}")
            return {}
    
    def delete_classification_result(self, classification_id: str) -> bool:
        """Delete classification result"""
        try:
            self.db.collection("classification_results").document(classification_id).delete()
            
            self.logger.info(f"Classification result deleted: {classification_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to delete classification result: {e}")
            return False
    
    def search_classifications(self, user_id: str, query: str, limit: int = 20) -> List[Dict]:
        """Search classifications by image path or predictions"""
        try:
            # Get all user classifications and filter locally
            # Note: Firestore doesn't support full-text search, so we filter in Python
            all_results = self.get_user_classifications(user_id, limit=1000)
            
            filtered_results = []
            query_lower = query.lower()
            
            for result in all_results:
                # Search in image path
                if query_lower in result.get("image_path", "").lower():
                    filtered_results.append(result)
                    continue
                
                # Search in predictions
                predictions = result.get("predictions", [])
                for pred in predictions:
                    if query_lower in str(pred).lower():
                        filtered_results.append(result)
                        break
            
            return filtered_results[:limit]
            
        except Exception as e:
            self.logger.error(f"Failed to search classifications: {e}")
            return []
