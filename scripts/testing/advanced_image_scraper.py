#!/usr/bin/env python3
"""
Advanced Image Scraper for VisionAI Pro
Downloads high-quality images from multiple free sources
"""

import os
import requests
import time
import random
import json
from PIL import Image
import io
from urllib.parse import urlparse, urljoin
import logging
import hashlib

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AdvancedImageScraper:
    def __init__(self, output_dir="advanced_test_images"):
        self.output_dir = output_dir
        self.downloaded_count = 0
        self.failed_count = 0
        self.downloaded_urls = set()  # Prevent duplicates
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Enhanced categories with subcategories
        self.categories = {
            "people": ["portrait", "group", "child", "elderly", "professional"],
            "animals": ["dog", "cat", "bird", "wildlife", "farm"],
            "vehicles": ["car", "truck", "motorcycle", "airplane", "boat"],
            "buildings": ["house", "office", "church", "bridge", "skyscraper"],
            "nature": ["landscape", "forest", "mountain", "ocean", "desert"],
            "food": ["fruit", "vegetable", "meal", "dessert", "beverage"],
            "objects": ["furniture", "electronics", "tools", "books", "clothing"],
            "technology": ["computer", "phone", "camera", "gadget", "robot"],
            "art": ["painting", "sculpture", "drawing", "photography", "design"],
            "sports": ["football", "basketball", "tennis", "swimming", "running"]
        }
        
        # Create category directories
        for category, subcategories in self.categories.items():
            os.makedirs(os.path.join(output_dir, category), exist_ok())
            for subcategory in subcategories:
                os.makedirs(os.path.join(output_dir, category, subcategory), exist_ok())
    
    def get_image_hash(self, image_data):
        """Generate hash for image to prevent duplicates"""
        return hashlib.md5(image_data).hexdigest()
    
    def download_image(self, url, filename, category, subcategory=""):
        """Download a single image with error handling"""
        try:
            # Check if URL already downloaded
            if url in self.downloaded_urls:
                return False
            
            # Download image
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            
            # Check if it's actually an image
            if not response.headers.get('content-type', '').startswith('image/'):
                return False
            
            # Generate file path
            if subcategory:
                filepath = os.path.join(self.output_dir, category, subcategory, filename)
            else:
                filepath = os.path.join(self.output_dir, category, filename)
            
            # Save image
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            # Verify image is valid
            try:
                with Image.open(filepath) as img:
                    img.verify()
            except Exception:
                os.remove(filepath)
                return False
            
            self.downloaded_urls.add(url)
            self.downloaded_count += 1
            logger.info(f"Downloaded: {filename}")
            return True
            
        except Exception as e:
            self.failed_count += 1
            logger.error(f"Failed to download {filename}: {e}")
            return False
    
    def download_from_unsplash_collections(self, category, count=50):
        """Download from Unsplash collections"""
        logger.info(f"Downloading {count} {category} images from Unsplash collections...")
        
        # Unsplash collection IDs for different categories
        collections = {
            "people": ["317099", "935777", "139386"],
            "animals": ["1423578", "1065976", "139386"],
            "vehicles": ["1423578", "1065976", "139386"],
            "buildings": ["1423578", "1065976", "139386"],
            "nature": ["1423578", "1065976", "139386"],
            "food": ["1423578", "1065976", "139386"]
        }
        
        if category not in collections:
            return
        
        collection_ids = collections[category]
        
        for i in range(count):
            try:
                collection_id = random.choice(collection_ids)
                url = f"https://source.unsplash.com/collection/{collection_id}/400x400"
                
                filename = f"{category}_unsplash_{i+1:03d}.jpg"
                if self.download_image(url, filename, category):
                    time.sleep(0.5)  # Rate limiting
                
            except Exception as e:
                logger.error(f"Unsplash download error: {e}")
    
    def download_from_picsum_with_categories(self, category, count=50):
        """Download from Picsum with category-specific seeds"""
        logger.info(f"Downloading {count} {category} images from Picsum...")
        
        # Use category-specific seeds for more relevant images
        seeds = {
            "people": [1, 2, 3, 4, 5],
            "animals": [10, 11, 12, 13, 14],
            "vehicles": [20, 21, 22, 23, 24],
            "buildings": [30, 31, 32, 33, 34],
            "nature": [40, 41, 42, 43, 44],
            "food": [50, 51, 52, 53, 54]
        }
        
        category_seeds = seeds.get(category, [1, 2, 3, 4, 5])
        
        for i in range(count):
            try:
                seed = random.choice(category_seeds) + i
                url = f"https://picsum.photos/seed/{seed}/400/400"
                
                filename = f"{category}_picsum_{i+1:03d}.jpg"
                if self.download_image(url, filename, category):
                    time.sleep(0.3)
                
            except Exception as e:
                logger.error(f"Picsum download error: {e}")
    
    def download_from_placeholder_with_text(self, category, count=30):
        """Download placeholder images with category-specific text"""
        logger.info(f"Downloading {count} placeholder images for {category}...")
        
        colors = ["FF6B6B", "4ECDC4", "45B7D1", "96CEB4", "FFEAA7", "DDA0DD", "98D8C8", "F7DC6F"]
        subcategories = self.categories.get(category, [])
        
        for i in range(count):
            try:
                color = random.choice(colors)
                text = random.choice(subcategories) if subcategories else category.title()
                url = f"https://via.placeholder.com/400x400/{color}/ffffff?text={text}"
                
                filename = f"{category}_placeholder_{i+1:03d}.jpg"
                if self.download_image(url, filename, category):
                    time.sleep(0.2)
                
            except Exception as e:
                logger.error(f"Placeholder download error: {e}")
    
    def download_from_fakeimg(self, category, count=20):
        """Download from fakeimg.pl (another placeholder service)"""
        logger.info(f"Downloading {count} images from fakeimg.pl for {category}...")
        
        for i in range(count):
            try:
                url = f"https://fakeimg.pl/400x400/282828/EAEAEA/?text={category.title()}&font=bebas"
                
                filename = f"{category}_fakeimg_{i+1:03d}.jpg"
                if self.download_image(url, filename, category):
                    time.sleep(0.2)
                
            except Exception as e:
                logger.error(f"Fakeimg download error: {e}")
    
    def download_category_images(self, category, total_count=100):
        """Download images for a specific category from multiple sources"""
        logger.info(f"\n=== Downloading {category.upper()} images ===")
        
        # Distribute downloads across sources
        unsplash_count = total_count // 2
        picsum_count = total_count // 3
        placeholder_count = total_count // 6
        fakeimg_count = total_count // 12
        
        self.download_from_unsplash_collections(category, unsplash_count)
        self.download_from_picsum_with_categories(category, picsum_count)
        self.download_from_placeholder_with_text(category, placeholder_count)
        self.download_from_fakeimg(category, fakeimg_count)
        
        logger.info(f"Completed {category} category")
    
    def create_advanced_dataset(self, total_images=1000):
        """Create an advanced balanced dataset"""
        images_per_category = total_images // len(self.categories)
        
        logger.info(f"Creating advanced dataset with {total_images} images...")
        logger.info(f"Images per category: {images_per_category}")
        
        for category in self.categories.keys():
            self.download_category_images(category, images_per_category)
            time.sleep(1)  # Brief pause between categories
        
        self.print_summary()
    
    def print_summary(self):
        """Print download summary"""
        logger.info(f"\n=== Download Summary ===")
        logger.info(f"Total downloaded: {self.downloaded_count}")
        logger.info(f"Failed downloads: {self.failed_count}")
        logger.info(f"Success rate: {(self.downloaded_count / (self.downloaded_count + self.failed_count) * 100):.1f}%")
        
        # Create detailed summary
        summary_file = os.path.join(self.output_dir, "advanced_download_summary.txt")
        with open(summary_file, 'w') as f:
            f.write(f"Advanced Image Download Summary\n")
            f.write(f"==============================\n")
            f.write(f"Total images: {self.downloaded_count}\n")
            f.write(f"Failed downloads: {self.failed_count}\n")
            f.write(f"Success rate: {(self.downloaded_count / (self.downloaded_count + self.failed_count) * 100):.1f}%\n")
            f.write(f"Categories: {', '.join(self.categories.keys())}\n")
            f.write(f"Download date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("Category breakdown:\n")
            for category in self.categories.keys():
                category_dir = os.path.join(self.output_dir, category)
                if os.path.exists(category_dir):
                    count = len([f for f in os.listdir(category_dir) if f.endswith(('.jpg', '.jpeg', '.png'))])
                    f.write(f"  {category}: {count} images\n")
        
        logger.info(f"Detailed summary saved to: {summary_file}")

def main():
    """Main function"""
    print("🚀 Advanced Image Scraper for VisionAI Pro")
    print("=" * 50)
    
    scraper = AdvancedImageScraper()
    
    try:
        # Download 1000+ images
        scraper.create_advanced_dataset(1000)
        
        print(f"\n✅ Advanced download completed!")
        print(f"📁 Images saved to: {scraper.output_dir}")
        print(f"📊 Total images: {scraper.downloaded_count}")
        
    except KeyboardInterrupt:
        print("\n⏹️  Download interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Advanced download failed: {e}")

if __name__ == "__main__":
    main()
