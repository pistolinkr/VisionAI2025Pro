#!/usr/bin/env python3
"""
VisionAI Pro Image Classification System - Main Entry Point
"""

import os
import sys
import argparse
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from config.config import current_config

def run_zero_shot_server():
    """Run Zero-shot classification server"""
    import uvicorn
    from src.api.zero_shot_main import app
    
    print("🚀 Starting Zero-shot Classification Server...")
    print(f"📡 Server will run on http://{current_config.HOST}:8002")
    print(f"📱 Web interface: http://{current_config.HOST}:8002/web_apps/zero_shot/zero_shot_web_app.html")
    
    uvicorn.run(
        app,
        host=current_config.HOST,
        port=8002,
        log_level=current_config.LOG_LEVEL.lower()
    )

def run_advanced_server():
    """Run Advanced classification server"""
    import uvicorn
    from src.api.advanced_main import app
    
    print("🚀 Starting Advanced Classification Server...")
    print(f"📡 Server will run on http://{current_config.HOST}:8001")
    print(f"📱 Web interface: http://{current_config.HOST}:8001/web_apps/advanced/advanced_web_app.html")
    
    uvicorn.run(
        app,
        host=current_config.HOST,
        port=8001,
        log_level=current_config.LOG_LEVEL.lower()
    )

def run_firebase_server():
    """Run Firebase-based server"""
    import uvicorn
    from src.api.firebase_main import app
    
    print("🚀 Starting Firebase Server...")
    print(f"📡 Server will run on http://{current_config.HOST}:8003")
    
    uvicorn.run(
        app,
        host=current_config.HOST,
        port=8003,
        log_level=current_config.LOG_LEVEL.lower()
    )

def run_main_server():
    """Run main classification server"""
    import uvicorn
    from src.api.main import app
    
    print("🚀 Starting Main Classification Server...")
    print(f"📡 Server will run on http://{current_config.HOST}:{current_config.PORT}")
    print(f"📱 Web interface: http://{current_config.HOST}:{current_config.PORT}")
    
    uvicorn.run(
        app,
        host=current_config.HOST,
        port=current_config.PORT,
        log_level=current_config.LOG_LEVEL.lower()
    )

def main():
    parser = argparse.ArgumentParser(description="VisionAI Pro Image Classification System")
    parser.add_argument(
        "server",
        choices=["zero-shot", "advanced", "firebase", "main"],
        help="Which server to run"
    )
    
    args = parser.parse_args()
    
    print("🧠 VisionAI Pro Image Classification System")
    print("=" * 50)
    
    if args.server == "zero-shot":
        run_zero_shot_server()
    elif args.server == "advanced":
        run_advanced_server()
    elif args.server == "firebase":
        run_firebase_server()
    elif args.server == "main":
        run_main_server()

if __name__ == "__main__":
    main()
