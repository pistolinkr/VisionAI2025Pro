import os
import jwt
import secrets
import hashlib
import hmac
from datetime import datetime, timedelta
from typing import Optional, Dict, List
import sqlite3
import logging
from dataclasses import dataclass
import time

@dataclass
class APIKey:
    key: str
    user_id: str
    name: str
    permissions: List[str]
    created_at: datetime
    expires_at: Optional[datetime]
    is_active: bool
    last_used: Optional[datetime] = None
    usage_count: int = 0
    ip_whitelist: Optional[List[str]] = None

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
                    is_active BOOLEAN NOT NULL DEFAULT 1,
                    last_used TIMESTAMP,
                    usage_count INTEGER DEFAULT 0,
                    ip_whitelist TEXT
                )
            ''')
            
            # Create usage tracking table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS api_usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    api_key TEXT NOT NULL,
                    ip_address TEXT NOT NULL,
                    endpoint TEXT NOT NULL,
                    timestamp TIMESTAMP NOT NULL,
                    response_code INTEGER NOT NULL,
                    FOREIGN KEY (api_key) REFERENCES api_keys (key)
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
    
    def log_api_usage(self, api_key: str, ip_address: str, endpoint: str, response_code: int):
        """Log API usage for monitoring and security"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO api_usage (api_key, ip_address, endpoint, timestamp, response_code)
                VALUES (?, ?, ?, ?, ?)
            ''', (api_key, ip_address, endpoint, datetime.now(), response_code))
            
            # Update usage count
            cursor.execute('''
                UPDATE api_keys 
                SET usage_count = usage_count + 1, last_used = ?
                WHERE key = ?
            ''', (datetime.now(), api_key))
            
            conn.commit()
            conn.close()
            
        except Exception as e:
            self.logger.error(f"Failed to log API usage: {e}")
    
    def validate_ip_access(self, api_key: str, ip_address: str) -> bool:
        """Validate if IP address is allowed for this API key"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT ip_whitelist FROM api_keys WHERE key = ? AND is_active = 1
            ''', (api_key,))
            
            result = cursor.fetchone()
            conn.close()
            
            if not result or not result[0]:
                return True  # No IP restrictions
            
            allowed_ips = result[0].split(',')
            return ip_address in allowed_ips
            
        except Exception as e:
            self.logger.error(f"Failed to validate IP access: {e}")
            return False
    
    def generate_secure_key(self, user_id: str, name: str, permissions: List[str], 
                          expires_days: int = 365, ip_whitelist: List[str] = None) -> str:
        """Generate a secure API key with additional security features"""
        try:
            # Generate a cryptographically secure random key
            key = secrets.token_urlsafe(32)
            
            # Create HMAC signature for additional security
            timestamp = str(int(time.time()))
            message = f"{user_id}:{name}:{timestamp}"
            signature = hmac.new(
                self.secret_key.encode(),
                message.encode(),
                hashlib.sha256
            ).hexdigest()
            
            # Combine key with signature
            secure_key = f"vai_{key}_{signature[:8]}"
            
            # Calculate expiry date
            expires_at = datetime.now() + timedelta(days=expires_days)
            
            # Store in database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO api_keys (key, user_id, name, permissions, created_at, expires_at, ip_whitelist)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                secure_key,
                user_id,
                name,
                ','.join(permissions),
                datetime.now(),
                expires_at,
                ','.join(ip_whitelist) if ip_whitelist else None
            ))
            
            conn.commit()
            conn.close()
            
            self.logger.info(f"Generated secure API key for user {user_id}")
            return secure_key
            
        except Exception as e:
            self.logger.error(f"Failed to generate secure key: {e}")
            return None
    
    def get_usage_stats(self, api_key: str, days: int = 30) -> Dict:
        """Get usage statistics for an API key"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get usage count for the period
            since_date = datetime.now() - timedelta(days=days)
            cursor.execute('''
                SELECT COUNT(*) as total_requests,
                       COUNT(CASE WHEN response_code >= 400 THEN 1 END) as error_requests,
                       COUNT(DISTINCT ip_address) as unique_ips
                FROM api_usage 
                WHERE api_key = ? AND timestamp >= ?
            ''', (api_key, since_date))
            
            stats = cursor.fetchone()
            
            # Get recent activity
            cursor.execute('''
                SELECT ip_address, endpoint, timestamp, response_code
                FROM api_usage 
                WHERE api_key = ? 
                ORDER BY timestamp DESC 
                LIMIT 10
            ''', (api_key,))
            
            recent_activity = cursor.fetchall()
            
            conn.close()
            
            return {
                'total_requests': stats[0] or 0,
                'error_requests': stats[1] or 0,
                'unique_ips': stats[2] or 0,
                'recent_activity': [
                    {
                        'ip_address': row[0],
                        'endpoint': row[1],
                        'timestamp': row[2],
                        'response_code': row[3]
                    } for row in recent_activity
                ]
            }
            
        except Exception as e:
            self.logger.error(f"Failed to get usage stats: {e}")
            return {}
    
    def revoke_compromised_keys(self, user_id: str) -> int:
        """Revoke all API keys for a user (in case of compromise)"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE api_keys 
                SET is_active = 0 
                WHERE user_id = ?
            ''', (user_id,))
            
            revoked_count = cursor.rowcount
            conn.commit()
            conn.close()
            
            self.logger.warning(f"Revoked {revoked_count} API keys for user {user_id}")
            return revoked_count
            
        except Exception as e:
            self.logger.error(f"Failed to revoke keys: {e}")
            return 0
    
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
