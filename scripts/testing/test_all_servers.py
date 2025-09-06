#!/usr/bin/env python3
"""
VisionAI Pro - All Servers Test Script
"""

import sys
import os
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

def test_imports():
    """Test all server imports"""
    print("🧪 Testing server imports...")
    
    try:
        from config.config import current_config
        print("✅ Config loaded successfully")
    except Exception as e:
        print(f"❌ Config failed: {e}")
        return False
    
    try:
        from src.api.zero_shot_main import app as zero_shot_app
        print("✅ Zero-shot server imports successfully")
    except Exception as e:
        print(f"❌ Zero-shot server failed: {e}")
        return False
    
    try:
        from src.api.advanced_main import app as advanced_app
        print("✅ Advanced server imports successfully")
    except Exception as e:
        print(f"❌ Advanced server failed: {e}")
        return False
    
    try:
        from src.api.firebase_main import app as firebase_app
        print("✅ Firebase server imports successfully")
    except Exception as e:
        print(f"❌ Firebase server failed: {e}")
        return False
    
    try:
        from src.api.main import app as main_app
        print("✅ Main server imports successfully")
    except Exception as e:
        print(f"❌ Main server failed: {e}")
        return False
    
    return True

def test_config():
    """Test configuration"""
    print("\n🔧 Testing configuration...")
    
    try:
        from config.config import current_config
        
        print(f"✅ Host: {current_config.HOST}")
        print(f"✅ Port: {current_config.PORT}")
        print(f"✅ Debug: {current_config.DEBUG}")
        print(f"✅ Log Level: {current_config.LOG_LEVEL}")
        print(f"✅ Models Dir: {current_config.MODELS_DIR}")
        print(f"✅ Uploads Dir: {current_config.UPLOADS_DIR}")
        
        return True
    except Exception as e:
        print(f"❌ Configuration test failed: {e}")
        return False

def test_directories():
    """Test directory structure"""
    print("\n📁 Testing directory structure...")
    
    required_dirs = [
        "web_apps/zero_shot",
        "web_apps/advanced", 
        "web_apps/firebase",
        "scripts/deployment",
        "scripts/setup",
        "scripts/testing",
        "data/models",
        "data/cache",
        "data/uploads",
        "config",
        "docs/setup",
        "docs/api",
        "src/api",
        "src/auth",
        "src/models",
        "src/cli"
    ]
    
    all_exist = True
    for dir_path in required_dirs:
        full_path = project_root / dir_path
        if full_path.exists():
            print(f"✅ {dir_path}")
        else:
            print(f"❌ {dir_path} - Missing!")
            all_exist = False
    
    return all_exist

def main():
    print("🧠 VisionAI Pro - Server Test Suite")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    # Test configuration
    config_ok = test_config()
    
    # Test directories
    dirs_ok = test_directories()
    
    print("\n📊 Test Results:")
    print("=" * 20)
    print(f"Imports: {'✅ PASS' if imports_ok else '❌ FAIL'}")
    print(f"Config:  {'✅ PASS' if config_ok else '❌ FAIL'}")
    print(f"Dirs:    {'✅ PASS' if dirs_ok else '❌ FAIL'}")
    
    if imports_ok and config_ok and dirs_ok:
        print("\n🎉 All tests passed! System is ready to run.")
        print("\n🚀 To start servers:")
        print("   python3 main.py zero-shot   # Zero-shot server (port 8002)")
        print("   python3 main.py advanced    # Advanced server (port 8001)")
        print("   python3 main.py firebase    # Firebase server (port 8003)")
        print("   python3 main.py main        # Main server (port 8000)")
        return 0
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
