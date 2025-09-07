#!/usr/bin/env python3
"""
Firebase-based VisionAI Pro Image Classification System Runner
"""

import os
import sys
import uvicorn
import logging
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).parent / "src"))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv("LOG_LEVEL", "INFO")),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

def main():
    """Main function to run the Firebase-based API"""
    try:
        # Check Firebase configuration
        firebase_config_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")
        
        if firebase_config_path and not os.path.exists(firebase_config_path):
            logger.warning(f"Firebase service account file not found: {firebase_config_path}")
            logger.info("Make sure to set up Firebase credentials properly")
            logger.info("You can download the service account JSON from Firebase Console")
        
        # Import and run the Firebase API
        from src.api.firebase_main import app
        
        # Get configuration
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", "8000"))
        debug = os.getenv("DEBUG", "False").lower() == "true"
        
        logger.info(f"Starting VisionAI Pro Image Classification API (Firebase)")
        logger.info(f"Host: {host}")
        logger.info(f"Port: {port}")
        logger.info(f"Debug: {debug}")
        
        # Run the application
        uvicorn.run(
            "src.api.firebase_main:app",
            host=host,
            port=port,
            reload=debug,
            log_level=os.getenv("LOG_LEVEL", "info").lower()
        )
        
    except ImportError as e:
        logger.error(f"Failed to import required modules: {e}")
        logger.error("Make sure all dependencies are installed: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Failed to start the application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
