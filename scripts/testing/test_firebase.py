#!/usr/bin/env python3
"""
Firebase Integration Test Script
"""

import os
import sys
import logging
from datetime import datetime

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_firebase_connection():
    """Test Firebase connection"""
    try:
        from firebase_config import firebase_config
        
        if firebase_config.is_connected():
            logger.info("✅ Firebase connection successful")
            return True
        else:
            logger.error("❌ Firebase connection failed")
            return False
            
    except Exception as e:
        logger.error(f"❌ Firebase connection error: {e}")
        return False

def test_api_key_manager():
    """Test Firebase API key manager"""
    try:
        from src.auth.firebase_api_key_manager import FirebaseAPIKeyManager
        
        manager = FirebaseAPIKeyManager()
        
        # Test API key generation
        test_key = manager.generate_api_key(
            user_id="test_user",
            name="Test Key",
            permissions=["read", "classify"],
            expiry_days=1
        )
        
        if test_key:
            logger.info(f"✅ API key generated: {test_key[:10]}...")
            
            # Test API key validation
            key_info = manager.validate_api_key(test_key)
            if key_info:
                logger.info("✅ API key validation successful")
                
                # Test key info retrieval
                info = manager.get_key_info(test_key)
                if info:
                    logger.info("✅ API key info retrieval successful")
                
                # Clean up - delete test key
                manager.delete_api_key(test_key)
                logger.info("✅ Test API key deleted")
                
                return True
            else:
                logger.error("❌ API key validation failed")
                return False
        else:
            logger.error("❌ API key generation failed")
            return False
            
    except Exception as e:
        logger.error(f"❌ API key manager test error: {e}")
        return False

def test_data_manager():
    """Test Firebase data manager"""
    try:
        from src.models.firebase_data_manager import FirebaseDataManager
        
        manager = FirebaseDataManager()
        
        # Test user profile operations
        profile_data = {
            "name": "Test User",
            "email": "test@example.com",
            "created_at": datetime.now().isoformat()
        }
        
        success = manager.save_user_profile("test_user", profile_data)
        if success:
            logger.info("✅ User profile saved")
            
            # Test profile retrieval
            profile = manager.get_user_profile("test_user")
            if profile:
                logger.info("✅ User profile retrieved")
                
                # Test usage statistics
                stats_success = manager.save_usage_statistics(
                    user_id="test_user",
                    api_key="test_key",
                    request_type="test",
                    processing_time=1.5,
                    success=True
                )
                
                if stats_success:
                    logger.info("✅ Usage statistics saved")
                    
                    # Test statistics retrieval
                    stats = manager.get_user_usage_stats("test_user", days=1)
                    if stats:
                        logger.info("✅ Usage statistics retrieved")
                        return True
                    else:
                        logger.error("❌ Usage statistics retrieval failed")
                        return False
                else:
                    logger.error("❌ Usage statistics save failed")
                    return False
            else:
                logger.error("❌ User profile retrieval failed")
                return False
        else:
            logger.error("❌ User profile save failed")
            return False
            
    except Exception as e:
        logger.error(f"❌ Data manager test error: {e}")
        return False

def main():
    """Main test function"""
    logger.info("🚀 Starting Firebase Integration Tests")
    
    tests = [
        ("Firebase Connection", test_firebase_connection),
        ("API Key Manager", test_api_key_manager),
        ("Data Manager", test_data_manager)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        logger.info(f"\n📋 Running {test_name} test...")
        if test_func():
            passed += 1
            logger.info(f"✅ {test_name} test passed")
        else:
            logger.error(f"❌ {test_name} test failed")
    
    logger.info(f"\n📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        logger.info("🎉 All Firebase integration tests passed!")
        return True
    else:
        logger.error("⚠️ Some tests failed. Please check Firebase configuration.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
