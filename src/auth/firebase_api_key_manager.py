"""
Firebase-based API Key Manager for VisionAI Pro Image Classification System
"""

import os
import jwt
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import logging
from dataclasses import dataclass, asdict
import sys
import os

# Add parent directory to path to import firebase_config
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from firebase_config import firebase_config

@dataclass
class APIKey:
    key: str
    user_id: str
    name: str
    permissions: List[str]
    created_at: datetime
    expires_at: Optional[datetime]
    is_active: bool

class FirebaseAPIKeyManager:
    """Firebase Firestore-based API key management and authentication system"""
    
    def __init__(self, secret_key: str = None):
        self.secret_key = secret_key or os.getenv("API_SECRET_KEY", "default-secret-key")
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
    
    def generate_api_key(self, user_id: str, name: str, 
                        permissions: List[str] = None, 
                        expiry_days: int = 365) -> str:
        """Generate new API key"""
        try:
            # Generate 32-character random key
            api_key = secrets.token_urlsafe(32)
            
            # Set default permissions
            if permissions is None:
                permissions = ["read", "classify"]
            
            # Calculate expiry date
            expires_at = datetime.now() + timedelta(days=expiry_days)
            
            # Create document data
            doc_data = {
                "key": api_key,
                "user_id": user_id,
                "name": name,
                "permissions": permissions,
                "created_at": self._convert_datetime_to_timestamp(datetime.now()),
                "expires_at": self._convert_datetime_to_timestamp(expires_at),
                "is_active": True
            }
            
            # Save to Firestore
            self.db.collection("api_keys").document(api_key).set(doc_data)
            
            self.logger.info(f"New API key generated: {name} (User: {user_id})")
            return api_key
            
        except Exception as e:
            self.logger.error(f"API key generation failed: {e}")
            return None
    
    def validate_api_key(self, api_key: str) -> Optional[APIKey]:
        """Validate API key"""
        try:
            # Get document from Firestore
            doc_ref = self.db.collection("api_keys").document(api_key)
            doc = doc_ref.get()
            
            if not doc.exists:
                return None
            
            data = doc.to_dict()
            
            # Check inactive key
            if not data.get("is_active", False):
                return None
            
            # Check expiry date
            expires_at_str = data.get("expires_at")
            if expires_at_str:
                expires_at = self._convert_timestamp_to_datetime(expires_at_str)
                if datetime.now() > expires_at:
                    return None
            
            # Parse creation date
            created_at = self._convert_timestamp_to_datetime(data.get("created_at"))
            expires_at = self._convert_timestamp_to_datetime(expires_at_str) if expires_at_str else None
            
            return APIKey(
                key=data.get("key"),
                user_id=data.get("user_id"),
                name=data.get("name"),
                permissions=data.get("permissions", []),
                created_at=created_at,
                expires_at=expires_at,
                is_active=data.get("is_active", False)
            )
            
        except Exception as e:
            self.logger.error(f"API key validation failed: {e}")
            return None
    
    def revoke_api_key(self, api_key: str) -> bool:
        """Revoke API key"""
        try:
            # Update document in Firestore
            doc_ref = self.db.collection("api_keys").document(api_key)
            doc_ref.update({"is_active": False})
            
            self.logger.info(f"API key revoked: {api_key}")
            return True
            
        except Exception as e:
            self.logger.error(f"API key revocation failed: {e}")
            return False
    
    def get_user_keys(self, user_id: str) -> List[APIKey]:
        """Get all API keys for a user"""
        try:
            # Query Firestore for user's keys
            query = self.db.collection("api_keys").where("user_id", "==", user_id)
            docs = query.stream()
            
            keys = []
            for doc in docs:
                data = doc.to_dict()
                
                created_at = self._convert_timestamp_to_datetime(data.get("created_at"))
                expires_at_str = data.get("expires_at")
                expires_at = self._convert_timestamp_to_datetime(expires_at_str) if expires_at_str else None
                
                keys.append(APIKey(
                    key=data.get("key"),
                    user_id=data.get("user_id"),
                    name=data.get("name"),
                    permissions=data.get("permissions", []),
                    created_at=created_at,
                    expires_at=expires_at,
                    is_active=data.get("is_active", False)
                ))
            
            return keys
            
        except Exception as e:
            self.logger.error(f"Failed to get user API keys: {e}")
            return []
    
    def check_permission(self, api_key: str, required_permission: str) -> bool:
        """Check specific permission"""
        key_info = self.validate_api_key(api_key)
        if not key_info:
            return False
        
        return required_permission in key_info.permissions
    
    def get_key_info(self, api_key: str) -> Optional[Dict]:
        """Get API key info (excluding sensitive information)"""
        key_info = self.validate_api_key(api_key)
        if not key_info:
            return None
        
        return {
            "name": key_info.name,
            "user_id": key_info.user_id,
            "permissions": key_info.permissions,
            "created_at": key_info.created_at.isoformat(),
            "expires_at": key_info.expires_at.isoformat() if key_info.expires_at else None,
            "is_active": key_info.is_active
        }
    
    def delete_api_key(self, api_key: str) -> bool:
        """Permanently delete API key from database"""
        try:
            # Delete document from Firestore
            self.db.collection("api_keys").document(api_key).delete()
            
            self.logger.info(f"API key deleted: {api_key}")
            return True
            
        except Exception as e:
            self.logger.error(f"API key deletion failed: {e}")
            return False
    
    def update_api_key(self, api_key: str, updates: Dict) -> bool:
        """Update API key information"""
        try:
            # Prepare update data
            update_data = {}
            
            if "name" in updates:
                update_data["name"] = updates["name"]
            if "permissions" in updates:
                update_data["permissions"] = updates["permissions"]
            if "expires_at" in updates:
                if updates["expires_at"]:
                    update_data["expires_at"] = self._convert_datetime_to_timestamp(updates["expires_at"])
                else:
                    update_data["expires_at"] = None
            if "is_active" in updates:
                update_data["is_active"] = updates["is_active"]
            
            # Update document in Firestore
            self.db.collection("api_keys").document(api_key).update(update_data)
            
            self.logger.info(f"API key updated: {api_key}")
            return True
            
        except Exception as e:
            self.logger.error(f"API key update failed: {e}")
            return False
