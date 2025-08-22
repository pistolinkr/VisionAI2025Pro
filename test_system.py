#!/usr/bin/env python3
"""
ProRL V2 Image Classification System Test Script
"""

import os
import sys
import tempfile
from PIL import Image
import numpy as np

# Add project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def create_test_image():
    """Create test image"""
    # Generate 224x224 random image
    img_array = np.random.randint(0, 255, (224, 224, 3), dtype=np.uint8)
    img = Image.fromarray(img_array)
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
    img.save(temp_file.name, 'JPEG')
    temp_file.close()
    
    return temp_file.name

def test_classifier():
    """VisionAI Pro classifier test"""
    print("🧪 Starting classifier test...")
    
    try:
        from src.models.prorl_classifier import ProRLV2Classifier
        
        # Initialize classifier
        classifier = ProRLV2Classifier(device="cpu")
        print("✅ Classifier initialization successful")
        
        # Check category list
        categories = classifier.get_categories()
        print(f"✅ Category list loaded: {len(categories)} items")
        print(f"   Sample: {categories[:5]}")
        
        # Create test image
        test_image_path = create_test_image()
        print(f"✅ Test image created: {test_image_path}")
        
        # Test image classification
        test_image = Image.open(test_image_path)
        results = classifier.predict(test_image, top_k=3)
        print("✅ Image classification successful")
        print("   Results:")
        for i, result in enumerate(results, 1):
            print(f"     {i}. {result['category']}: {result['confidence']:.4f}")
        
        # Clean up temporary file
        os.unlink(test_image_path)
        print("✅ Test image cleanup completed")
        
        return True
        
    except Exception as e:
        print(f"❌ Classifier test failed: {e}")
        return False

def test_api_key_manager():
    """API key manager test"""
    print("\n🔑 Starting API key manager test...")
    
    try:
        from src.auth.api_key_manager import APIKeyManager
        
        # Initialize API key manager (use memory database)
        manager = APIKeyManager(db_path=":memory:")
        print("✅ API key manager initialization successful")
        
        # Test API key generation
        api_key = manager.generate_api_key(
            user_id="test_user",
            name="Test Key",
            permissions=["read", "classify"],
            expiry_days=30
        )
        print(f"✅ API key generation successful: {api_key[:20]}...")
        
        # Test API key validation
        key_info = manager.validate_api_key(api_key)
        if key_info:
            print("✅ API key validation successful")
            print(f"   User: {key_info.user_id}")
            print(f"   Name: {key_info.name}")
            print(f"   Permissions: {key_info.permissions}")
        else:
            print("❌ API key validation failed")
            return False
        
        # Test permission check
        has_read = manager.check_permission(api_key, "read")
        has_admin = manager.check_permission(api_key, "admin")
        print(f"✅ Permission check: read={has_read}, admin={has_admin}")
        
        # Test API key info retrieval
        key_details = manager.get_key_info(api_key)
        if key_details:
            print("✅ API key info retrieval successful")
        else:
            print("❌ API key info retrieval failed")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ API key manager test failed: {e}")
        return False

def test_web_interface():
    """Web interface test"""
    print("\n🌐 Starting web interface test...")
    
    try:
        # Check HTML file existence
        html_path = os.path.join(project_root, "templates", "index.html")
        if os.path.exists(html_path):
            print("✅ HTML template file exists")
            
            # Check file content partially
            with open(html_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "ProRL V2 Image Finder" in content:
                    print("✅ HTML content validation successful")
                else:
                    print("❌ HTML content validation failed")
                    return False
        else:
            print("❌ HTML template file not found")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Web interface test failed: {e}")
        return False

def test_config():
    """Configuration file test"""
    print("\n⚙️ Starting configuration file test...")
    
    try:
        from config import current_config
        
        print("✅ Configuration file loaded successfully")
        print(f"   API Secret Key: {current_config.API_SECRET_KEY[:20]}...")
        print(f"   Device: {current_config.DEVICE}")
        print(f"   Port: {current_config.PORT}")
        print(f"   Max File Size: {current_config.MAX_FILE_SIZE / 1024 / 1024:.1f}MB")
        
        return True
        
    except Exception as e:
        print(f"❌ Configuration file test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Starting ProRL V2 Image Classification System Test\n")
    
    tests = [
        ("Configuration", test_config),
        ("Classifier", test_classifier),
        ("API Key Manager", test_api_key_manager),
        ("Web Interface", test_web_interface),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ Exception occurred during {test_name} test: {e}")
            results.append((test_name, False))
    
    # Results summary
    print("\n" + "="*50)
    print("📊 Test Results Summary")
    print("="*50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ Passed" if result else "❌ Failed"
        print(f"{test_name:<15}: {status}")
        if result:
            passed += 1
    
    print("-" * 50)
    print(f"Total: {total}, Passed: {passed}, Failed: {total - passed}")
    
    if passed == total:
        print("\n🎉 All tests passed!")
        print("System is working correctly.")
        return 0
    else:
        print(f"\n⚠️  {total - passed} tests failed.")
        print("Please check and fix the issues.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
