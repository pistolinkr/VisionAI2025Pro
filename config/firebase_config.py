"""
Firebase Configuration for VisionAI Pro Image Classification System
"""

import os
import firebase_admin
from firebase_admin import credentials, firestore
from typing import Optional
import logging

class FirebaseConfig:
    """Firebase configuration and initialization"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.db: Optional[firestore.Client] = None
        self._initialize_firebase()
    
    def _initialize_firebase(self):
        """Initialize Firebase Admin SDK"""
        try:
            # Check if Firebase is already initialized
            if not firebase_admin._apps:
                # Try to load service account key from environment variable
                service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
                
                if service_account_path and os.path.exists(service_account_path):
                    # Load from service account file
                    cred = credentials.Certificate(service_account_path)
                    firebase_admin.initialize_app(cred)
                    self.logger.info("Firebase initialized with service account file")
                else:
                    # Try to use default credentials (for Google Cloud deployment)
                    firebase_admin.initialize_app()
                    self.logger.info("Firebase initialized with default credentials")
            else:
                self.logger.info("Firebase already initialized")
            
            # Initialize Firestore client
            self.db = firestore.client()
            self.logger.info("Firestore client initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Firebase initialization failed: {e}")
            # Try to initialize without credentials (for testing)
            try:
                firebase_admin.initialize_app()
                self.db = firestore.client()
                self.logger.info("Firebase initialized without credentials (test mode)")
            except Exception as test_error:
                self.logger.error(f"Test initialization also failed: {test_error}")
                self.db = None
    
    def get_db(self) -> Optional[firestore.Client]:
        """Get Firestore database client"""
        return self.db
    
    def is_connected(self) -> bool:
        """Check if Firebase is properly connected"""
        return self.db is not None

# Global Firebase configuration instance
firebase_config = FirebaseConfig()
