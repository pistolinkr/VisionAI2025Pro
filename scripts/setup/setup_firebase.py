#!/usr/bin/env python3
"""
Firebase Setup Helper Script
"""

import os
import sys
import json
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_firebase_dependencies():
    """Check if Firebase dependencies are installed"""
    try:
        import firebase_admin
        import google.cloud.firestore
        logger.info("✅ Firebase dependencies are installed")
        return True
    except ImportError as e:
        logger.error(f"❌ Firebase dependencies missing: {e}")
        logger.info("💡 Install with: pip install firebase-admin google-cloud-firestore")
        return False

def check_service_account_file():
    """Check if Firebase service account file exists"""
    service_account_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "./firebase-service-account.json")
    
    if os.path.exists(service_account_path):
        try:
            with open(service_account_path, 'r') as f:
                data = json.load(f)
            
            # Check required fields
            required_fields = ["type", "project_id", "private_key_id", "private_key", "client_email"]
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                logger.error(f"❌ Service account file missing fields: {missing_fields}")
                return False
            
            logger.info(f"✅ Service account file found: {service_account_path}")
            logger.info(f"📁 Project ID: {data.get('project_id', 'Unknown')}")
            return True
            
        except json.JSONDecodeError:
            logger.error("❌ Service account file is not valid JSON")
            return False
        except Exception as e:
            logger.error(f"❌ Error reading service account file: {e}")
            return False
    else:
        logger.warning(f"⚠️ Service account file not found: {service_account_path}")
        return False

def create_env_file():
    """Create .env file with Firebase configuration"""
    env_file = Path(".env")
    
    if env_file.exists():
        logger.info("📄 .env file already exists")
        return True
    
    try:
        env_content = """# API Configuration
API_SECRET_KEY=your-secret-key-change-this

API_KEY_EXPIRY_DAYS=365

# Firebase Configuration
FIREBASE_SERVICE_ACCOUNT_PATH=./firebase-service-account.json

# Model Configuration
MODEL_PATH=./models/prorl_v2_model
DEVICE=cpu

# Image Storage Configuration
UPLOAD_DIR=./uploads
MAX_FILE_SIZE=10485760

# Logging Configuration
LOG_LEVEL=INFO

# Environment
ENVIRONMENT=development
"""
        
        with open(env_file, 'w') as f:
            f.write(env_content)
        
        logger.info("✅ Created .env file with Firebase configuration")
        return True
        
    except Exception as e:
        logger.error(f"❌ Failed to create .env file: {e}")
        return False

def check_firebase_project():
    """Check Firebase project configuration"""
    firebaserc_file = Path(".firebaserc")
    
    if firebaserc_file.exists():
        try:
            with open(firebaserc_file, 'r') as f:
                data = json.load(f)
            
            project_id = data.get("projects", {}).get("default")
            if project_id:
                logger.info(f"✅ Firebase project configured: {project_id}")
                return True
            else:
                logger.error("❌ No default project configured in .firebaserc")
                return False
                
        except Exception as e:
            logger.error(f"❌ Error reading .firebaserc: {e}")
            return False
    else:
        logger.warning("⚠️ .firebaserc file not found")
        return False

def setup_firebase():
    """Main Firebase setup function"""
    logger.info("🚀 Starting Firebase Setup")
    
    checks = [
        ("Firebase Dependencies", check_firebase_dependencies),
        ("Service Account File", check_service_account_file),
        ("Environment File", create_env_file),
        ("Firebase Project", check_firebase_project)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        logger.info(f"\n📋 Checking {check_name}...")
        if check_func():
            passed += 1
        else:
            logger.warning(f"⚠️ {check_name} check failed")
    
    logger.info(f"\n📊 Setup Results: {passed}/{total} checks passed")
    
    if passed >= 3:  # At least dependencies, env file, and project config
        logger.info("\n🎉 Firebase setup is ready!")
        logger.info("\n📝 Next steps:")
        logger.info("1. Download service account JSON from Firebase Console")
        logger.info("2. Save as 'firebase-service-account.json' in project root")
        logger.info("3. Run: python test_firebase.py")
        logger.info("4. Start Firebase API: python run_firebase.py")
        return True
    else:
        logger.error("\n⚠️ Firebase setup incomplete. Please fix the issues above.")
        return False

def main():
    """Main function"""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("""
Firebase Setup Helper

Usage:
  python setup_firebase.py          # Run setup checks
  python setup_firebase.py --help   # Show this help

This script will:
1. Check if Firebase dependencies are installed
2. Verify service account file configuration
3. Create .env file with Firebase settings
4. Check Firebase project configuration

Prerequisites:
1. Firebase project created in Firebase Console
2. Firestore Database enabled
3. Service account key downloaded
""")
        return
    
    success = setup_firebase()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
