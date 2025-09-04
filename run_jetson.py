#!/usr/bin/env python3
"""
VisionAI Pro Image Classification System - Jetson Optimized Execution Script
"""

import os
import sys
import uvicorn
import logging
import subprocess
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config import current_config

def check_jetson_environment():
    """Check if running on Jetson and set appropriate environment"""
    print("🔍 Checking Jetson environment...")
    
    # Check if running on Jetson
    try:
        with open("/proc/device-tree/model", "r") as f:
            model = f.read().strip()
            if "jetson" in model.lower():
                print(f"✅ Running on Jetson: {model}")
                return True
    except:
        pass
    
    # Check for NVIDIA GPU
    try:
        result = subprocess.run(["nvidia-smi"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ NVIDIA GPU detected")
            return True
    except:
        pass
    
    print("⚠️  Not running on Jetson or NVIDIA GPU not detected")
    return False

def setup_jetson_environment():
    """Setup Jetson-specific environment variables"""
    print("⚙️  Setting up Jetson environment...")
    
    # Set environment variables for Jetson
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"
    
    # Set PyTorch to use CUDA if available
    if os.path.exists("/dev/nvidia0"):
        os.environ["DEVICE"] = "cuda"
        print("✅ CUDA device enabled")
    else:
        os.environ["DEVICE"] = "cpu"
        print("⚠️  Using CPU (CUDA not available)")

def setup_logging():
    """Setup logging"""
    logging.basicConfig(
        level=getattr(logging, current_config.LOG_LEVEL),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(current_config.LOG_FILE),
            logging.StreamHandler(sys.stdout)
        ]
    )

def main():
    """Main execution function for Jetson"""
    print("🚀 Starting VisionAI Pro Image Classification System on Jetson...")
    
    # Check Jetson environment
    is_jetson = check_jetson_environment()
    
    # Setup Jetson-specific environment
    if is_jetson:
        setup_jetson_environment()
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Output environment information
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    logger.info(f"Device: {current_config.DEVICE}")
    logger.info(f"Model path: {current_config.MODEL_PATH}")
    logger.info(f"Port: {current_config.PORT}")
    logger.info(f"Host: {current_config.HOST}")
    
    try:
        # Start uvicorn server with Jetson optimizations
        uvicorn.run(
            "src.api.main:app",
            host=current_config.HOST,
            port=current_config.PORT,
            reload=current_config.DEBUG,
            log_level=current_config.LOG_LEVEL.lower(),
            access_log=True,
            workers=1  # Jetson에서는 단일 워커 권장
        )
    except KeyboardInterrupt:
        logger.info("Server interrupted")
    except Exception as e:
        logger.error(f"Server startup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
