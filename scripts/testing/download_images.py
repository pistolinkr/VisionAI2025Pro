#!/usr/bin/env python3
"""
Free Image Downloader for VisionAI Pro Testing
Downloads 1000+ free images from various sources for testing classification accuracy
"""

import os
import requests
import time
import random
from PIL import Image
import io
from urllib.parse import urlparse
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageDownloader:
    def __init__(self, output_dir="test_images"):
        self.output_dir = output_dir
        self.downloaded_count = 0
        self.failed_count = 0
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Create category subdirectories
        self.categories = [
            "people", "animals", "vehicles", "buildings", "nature", 
            "food", "objects", "technology", "art", "sports"
        ]
        
        for category in self.categories:
            os.makedirs(os.path.join(output_dir, category), exist_ok=True)
    
    def download_from_unsplash(self, category, count=50):
        """Download images from Unsplash (free stock photos)"""
        logger.info(f"Downloading {count} {category} images from Unsplash...")
        
        # Unsplash API endpoints for different categories
        unsplash_urls = {
            "people": [
                "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
                "https://images.unsplash.com/photo-1494790108755-2616b612b786",
                "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e",
                "https://images.unsplash.com/photo-1438761681033-6461ffad8d80",
                "https://images.unsplash.com/photo-1500648767791-00dcc994a43e"
            ],
            "animals": [
                "https://images.unsplash.com/photo-1551963831-b3b1ca40c98e",
                "https://images.unsplash.com/photo-1517849845537-4d257902454a",
                "https://images.unsplash.com/photo-1552053831-71594a27632d",
                "https://images.unsplash.com/photo-1583337130417-b6a64a1d304e",
                "https://images.unsplash.com/photo-1574158622682-e40e69881006"
            ],
            "vehicles": [
                "https://images.unsplash.com/photo-1552519507-da3b142c6e3d",
                "https://images.unsplash.com/photo-1549317336-206569e8475c",
                "https://images.unsplash.com/photo-1562140177-5ed3a9b1c67f",
                "https://images.unsplash.com/photo-1558618666-fcd25c85cd64",
                "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b"
            ],
            "buildings": [
                "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab",
                "https://images.unsplash.com/photo-1511818966892-d7d671e672a2",
                "https://images.unsplash.com/photo-1512453979798-5ea266f8880c",
                "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
                "https://images.unsplash.com/photo-1494522358652-f30e61a2b5b5"
            ],
            "nature": [
                "https://images.unsplash.com/photo-1506905925346-21bda4d32df4",
                "https://images.unsplash.com/photo-1441974231531-c6227db76b6e",
                "https://images.unsplash.com/photo-1464822759844-d150baec1b1b",
                "https://images.unsplash.com/photo-1506905925346-21bda4d32df4",
                "https://images.unsplash.com/photo-1441974231531-c6227db76b6e"
            ],
            "food": [
                "https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b",
                "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445",
                "https://images.unsplash.com/photo-1565958011703-44f9829ba187",
                "https://images.unsplash.com/photo-1571091718767-18b5b1457add",
                "https://images.unsplash.com/photo-1565299507177-b0ac66763828"
            ]
        }
        
        if category not in unsplash_urls:
            logger.warning(f"No Unsplash URLs defined for category: {category}")
            return
        
        base_urls = unsplash_urls[category]
        
        for i in range(count):
            try:
                # Generate random image URL with different parameters
                base_url = random.choice(base_urls)
                url = f"{base_url}?w=400&h=400&fit=crop&auto=format&q=80"
                
                # Download image
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                # Save image
                filename = f"{category}_{i+1:03d}.jpg"
                filepath = os.path.join(self.output_dir, category, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                self.downloaded_count += 1
                logger.info(f"Downloaded: {filename}")
                
                # Rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                self.failed_count += 1
                logger.error(f"Failed to download {category} image {i+1}: {e}")
    
    def download_from_picsum(self, category, count=50):
        """Download random images from Picsum (Lorem Picsum)"""
        logger.info(f"Downloading {count} random images from Picsum...")
        
        for i in range(count):
            try:
                # Picsum provides random images
                url = f"https://picsum.photos/400/400?random={random.randint(1, 10000)}"
                
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                filename = f"{category}_picsum_{i+1:03d}.jpg"
                filepath = os.path.join(self.output_dir, category, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                self.downloaded_count += 1
                logger.info(f"Downloaded: {filename}")
                
                time.sleep(0.3)
                
            except Exception as e:
                self.failed_count += 1
                logger.error(f"Failed to download Picsum image {i+1}: {e}")
    
    def download_from_placeholder(self, category, count=30):
        """Download placeholder images"""
        logger.info(f"Downloading {count} placeholder images...")
        
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "gray"]
        
        for i in range(count):
            try:
                color = random.choice(colors)
                url = f"https://via.placeholder.com/400x400/{color}/ffffff?text={category.title()}"
                
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                
                filename = f"{category}_placeholder_{i+1:03d}.jpg"
                filepath = os.path.join(self.output_dir, category, filename)
                
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                
                self.downloaded_count += 1
                logger.info(f"Downloaded: {filename}")
                
                time.sleep(0.2)
                
            except Exception as e:
                self.failed_count += 1
                logger.error(f"Failed to download placeholder image {i+1}: {e}")
    
    def download_all_categories(self, images_per_category=100):
        """Download images for all categories"""
        logger.info(f"Starting download of {len(self.categories)} categories with {images_per_category} images each...")
        
        for category in self.categories:
            logger.info(f"\n=== Downloading {category.upper()} images ===")
            
            # Download from multiple sources
            self.download_from_unsplash(category, images_per_category // 2)
            self.download_from_picsum(category, images_per_category // 3)
            self.download_from_placeholder(category, images_per_category // 6)
            
            logger.info(f"Completed {category} category")
            time.sleep(1)  # Brief pause between categories
    
    def create_sample_dataset(self, total_images=1000):
        """Create a balanced sample dataset"""
        images_per_category = total_images // len(self.categories)
        
        logger.info(f"Creating sample dataset with {total_images} images...")
        logger.info(f"Images per category: {images_per_category}")
        
        self.download_all_categories(images_per_category)
        
        logger.info(f"\n=== Download Summary ===")
        logger.info(f"Total downloaded: {self.downloaded_count}")
        logger.info(f"Failed downloads: {self.failed_count}")
        logger.info(f"Success rate: {(self.downloaded_count / (self.downloaded_count + self.failed_count) * 100):.1f}%")
        
        # Create a summary file
        summary_file = os.path.join(self.output_dir, "download_summary.txt")
        with open(summary_file, 'w') as f:
            f.write(f"Image Download Summary\n")
            f.write(f"=====================\n")
            f.write(f"Total images: {self.downloaded_count}\n")
            f.write(f"Failed downloads: {self.failed_count}\n")
            f.write(f"Categories: {', '.join(self.categories)}\n")
            f.write(f"Images per category: ~{images_per_category}\n")
            f.write(f"Download date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        logger.info(f"Summary saved to: {summary_file}")

def main():
    """Main function to download images"""
    print("🖼️  VisionAI Pro Image Downloader")
    print("=" * 50)
    
    downloader = ImageDownloader()
    
    try:
        # Download 1000+ images
        downloader.create_sample_dataset(1000)
        
        print(f"\n✅ Download completed!")
        print(f"📁 Images saved to: {downloader.output_dir}")
        print(f"📊 Total images: {downloader.downloaded_count}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Download interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Download failed: {e}")

if __name__ == "__main__":
    main()
