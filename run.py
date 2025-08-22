#!/usr/bin/env python3
"""
VisionAI Pro Image Classification System Execution Script
"""

import os
import sys
import uvicorn
import logging
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config import current_config

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
    """Main execution function"""
    print("🚀 Starting VisionAI Pro Image Classification System...")
    
    # Setup logging
    setup_logging()
    logger = logging.getLogger(__name__)
    
    # Output environment information
    logger.info(f"Environment: {os.getenv('ENVIRONMENT', 'development')}")
    logger.info(f"Device: {current_config.DEVICE}")
    logger.info(f"Model path: {current_config.MODEL_PATH}")
    logger.info(f"Port: {current_config.PORT}")
    
    try:
        # Start uvicorn server
        uvicorn.run(
            "src.api.main:app",
            host=current_config.HOST,
            port=current_config.PORT,
            reload=current_config.DEBUG,
            log_level=current_config.LOG_LEVEL.lower(),
            access_log=True
        )
    except KeyboardInterrupt:
        logger.info("Server interrupted")
    except Exception as e:
        logger.error(f"Server startup failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
