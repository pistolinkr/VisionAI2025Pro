#!/usr/bin/env python3
"""
ProRL V2 Image Classification CLI Tool
"""

import argparse
import os
import sys
import logging
from pathlib import Path
from PIL import Image

# 로컬 모듈 import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.prorl_classifier import ProRLV2Classifier
from auth.api_key_manager import APIKeyManager

def setup_logging(verbose: bool = False):
    """Setup logging"""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def classify_image(classifier: ProRLV2Classifier, image_path: str, top_k: int = 5):
    """Perform image classification"""
    try:
        # Load image
        image = Image.open(image_path)
        
        # Perform classification
        results = classifier.predict(image, top_k=top_k)
        
        print(f"\n📸 Image: {image_path}")
        print(f"🔍 Classification Results (Top {top_k}):")
        print("-" * 50)
        
        for i, result in enumerate(results, 1):
            confidence = result['confidence'] * 100
            print(f"{i}. {result['category']:<15} {confidence:>6.1f}%")
        
        return results
        
    except Exception as e:
        print(f"❌ Image classification failed: {e}")
        return None

def manage_api_keys(manager: APIKeyManager, action: str, **kwargs):
    """API key management"""
    try:
        if action == "generate":
            user_id = kwargs.get('user_id', 'default_user')
            name = kwargs.get('name', 'CLI Generated Key')
            permissions = kwargs.get('permissions', ['read', 'classify'])
            expiry_days = kwargs.get('expiry_days', 365)
            
            api_key = manager.generate_api_key(
                user_id=user_id,
                name=name,
                permissions=permissions,
                expiry_days=expiry_days
            )
            
            if api_key:
                print(f"✅ New API key generated:")
                print(f"   Key: {api_key}")
                print(f"   Name: {name}")
                print(f"   Permissions: {', '.join(permissions)}")
                print(f"   Expires in: {expiry_days} days")
            else:
                print("❌ Failed to generate API key")
                
        elif action == "list":
            user_id = kwargs.get('user_id', 'default_user')
            keys = manager.get_user_keys(user_id)
            
            if keys:
                print(f"🔑 API Keys for user '{user_id}':")
                print("-" * 60)
                for key in keys:
                    status = "🟢 Active" if key.is_active else "🔴 Inactive"
                    print(f"   Name: {key.name}")
                    print(f"   Key: {key.key[:20]}...")
                    print(f"   Permissions: {', '.join(key.permissions)}")
                    print(f"   Status: {status}")
                    print(f"   Created: {key.created_at}")
                    if key.expires_at:
                        print(f"   Expires: {key.expires_at}")
                    print("-" * 60)
            else:
                print(f"No API keys found for user '{user_id}'")
                
        elif action == "revoke":
            target_key = kwargs.get('target_key')
            if manager.revoke_api_key(target_key):
                print(f"✅ API key has been revoked")
            else:
                print("❌ Failed to revoke API key")
                
    except Exception as e:
        print(f"❌ API key management failed: {e}")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="ProRL V2 Image Classification CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Usage Examples:
  # Image classification
  python main.py classify image.jpg
  
  # Generate API key
  python main.py keys generate --name "Test Key"
  
  # List API keys
  python main.py keys list
  
  # Revoke API key
  python main.py keys revoke --key "your-api-key"
        """
    )
    
    # Common options
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose log output')
    parser.add_argument('--model-path', help='ProRL V2 model path')
    parser.add_argument('--device', default='cpu', choices=['cpu', 'cuda'], help='Device to use')
    
    # Subcommands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Image classification command
    classify_parser = subparsers.add_parser('classify', help='Image classification')
    classify_parser.add_argument('image_path', help='Path to image to classify')
    classify_parser.add_argument('--top-k', type=int, default=5, help='Return top k results')
    
    # API key management commands
    keys_parser = subparsers.add_parser('keys', help='API key management')
    keys_subparsers = keys_parser.add_subparsers(dest='keys_action', help='API key operations')
    
    # Generate API key
    generate_parser = keys_subparsers.add_parser('generate', help='Generate new API key')
    generate_parser.add_argument('--name', required=True, help='Key name')
    generate_parser.add_argument('--user-id', default='default_user', help='User ID')
    generate_parser.add_argument('--permissions', default='read,classify', help='Permissions (comma separated)')
    generate_parser.add_argument('--expiry-days', type=int, default=365, help='Expiry days')
    
    # List API keys
    list_parser = keys_subparsers.add_parser('list', help='List API keys')
    list_parser.add_argument('--user-id', default='default_user', help='User ID')
    
    # Revoke API key
    revoke_parser = keys_subparsers.add_parser('revoke', help='Revoke API key')
    revoke_parser.add_argument('--key', required=True, help='API key to revoke')
    
    # Parse arguments
    args = parser.parse_args()
    
    # If no command, show help
    if not args.command:
        parser.print_help()
        return
    
    # Setup logging
    setup_logging(args.verbose)
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize classifier
        classifier = ProRLV2Classifier(
            model_path=args.model_path,
            device=args.device
        )
        
        # Initialize API key manager
        api_key_manager = APIKeyManager()
        
        # Execute commands
        if args.command == 'classify':
            # Validate image path
            if not os.path.exists(args.image_path):
                print(f"❌ Image file not found: {args.image_path}")
                return
            
            # Perform image classification
            classify_image(classifier, args.image_path, args.top_k)
            
        elif args.command == 'keys':
            if args.keys_action == 'generate':
                permissions = [p.strip() for p in args.permissions.split(',')]
                manage_api_keys(api_key_manager, 'generate',
                              user_id=args.user_id,
                              name=args.name,
                              permissions=permissions,
                              expiry_days=args.expiry_days)
                                
            elif args.keys_action == 'list':
                manage_api_keys(api_key_manager, 'list', user_id=args.user_id)
                
            elif args.keys_action == 'revoke':
                manage_api_keys(api_key_manager, 'revoke', target_key=args.key)
                
    except KeyboardInterrupt:
        print("\n\n⏹️  Operation interrupted")
    except Exception as e:
        logger.error(f"Error occurred: {e}")
        print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main()
