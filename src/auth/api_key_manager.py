import os
import jwt
import secrets
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import sqlite3
import logging
from dataclasses import dataclass

@dataclass
class APIKey:
    key: str
    user_id: str
    name: str
    permissions: List[str]
    created_at: datetime
    expires_at: Optional[datetime]
    is_active: bool

class APIKeyManager:
    """API key management and authentication system"""
    
    def __init__(self, db_path: str = "api_keys.db", secret_key: str = None):
        self.db_path = db_path
        self.secret_key = secret_key or os.getenv("API_SECRET_KEY", "default-secret-key")
        self.logger = logging.getLogger(__name__)
        
        # Initialize database
        self._init_database()
    
    def _init_database(self):
        """Initialize database tables"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS api_keys (
                    key TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    permissions TEXT NOT NULL,
                    created_at TIMESTAMP NOT NULL,
                    expires_at TIMESTAMP,
                    is_active BOOLEAN NOT NULL DEFAULT 1
                )
            ''')
            
            conn.commit()
            conn.close()
            self.logger.info("API key database initialized")
            
        except Exception as e:
            self.logger.error(f"Database initialization failed: {e}")
            # Fallback to memory database
            if self.db_path != ":memory:":
                self.logger.info("Falling back to memory database")
                self.db_path = ":memory:"
                self._init_database()
            else:
                # If memory database also fails, log warning and continue
                self.logger.warning("Memory database initialization also failed. Continuing with default behavior.")
    
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
            
            # Save to database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO api_keys (key, user_id, name, permissions, created_at, expires_at, is_active)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                api_key, user_id, name, 
                ",".join(permissions), 
                datetime.now(), expires_at, True
            ))
            
            conn.commit()
            conn.close()
            
            self.logger.info(f"New API key generated: {name} (User: {user_id})")
            return api_key
            
        except Exception as e:
            self.logger.error(f"API key generation failed: {e}")
            return None
    
    def validate_api_key(self, api_key: str) -> Optional[APIKey]:
        """Validate API key"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT key, user_id, name, permissions, created_at, expires_at, is_active
                FROM api_keys WHERE key = ?
            ''', (api_key,))
            
            result = cursor.fetchone()
            conn.close()
            
            if not result:
                return None
            
            key, user_id, name, permissions_str, created_at, expires_at, is_active = result
            
            # Check inactive key
            if not is_active:
                return None
            
            # Check expiry date
            if expires_at:
                expires_at = datetime.fromisoformat(expires_at)
                if datetime.now() > expires_at:
                    return None
            
            # Parse permissions
            permissions = permissions_str.split(",") if permissions_str else []
            
            # Parse creation date
            created_at = datetime.fromisoformat(created_at)
            
            return APIKey(
                key=key,
                user_id=user_id,
                name=name,
                permissions=permissions,
                created_at=created_at,
                expires_at=expires_at,
                is_active=is_active
            )
            
        except Exception as e:
            self.logger.error(f"API key validation failed: {e}")
            return None
    
    def revoke_api_key(self, api_key: str) -> bool:
        """Revoke API key"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE api_keys SET is_active = 0 WHERE key = ?
            ''', (api_key,))
            
            conn.commit()
            conn.close()
            
            self.logger.info(f"API key revoked: {api_key}")
            return True
            
        except Exception as e:
            self.logger.error(f"API key revocation failed: {e}")
            return False
    
    def get_user_keys(self, user_id: str) -> List[APIKey]:
        """Get all API keys for a user"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT key, user_id, name, permissions, created_at, expires_at, is_active
                FROM api_keys WHERE user_id = ?
            ''', (user_id,))
            
            results = cursor.fetchall()
            conn.close()
            
            keys = []
            for result in results:
                key, user_id, name, permissions_str, created_at, expires_at, is_active = result
                
                permissions = permissions_str.split(",") if permissions_str else []
                created_at = datetime.fromisoformat(created_at)
                expires_at = datetime.fromisoformat(expires_at) if expires_at else None
                
                keys.append(APIKey(
                    key=key, user_id=user_id, name=name,
                    permissions=permissions, created_at=created_at,
                    expires_at=expires_at, is_active=is_active
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
