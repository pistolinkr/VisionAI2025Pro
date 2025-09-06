#!/usr/bin/env python3
"""
VisionAI Pro Sample Manager
Organizes and manages image samples for testing and validation
"""

import os
import shutil
import json
import time
from PIL import Image
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SampleManager:
    def __init__(self, base_dir="image_samples"):
        self.base_dir = Path(base_dir)
        self.raw_dir = self.base_dir / "raw"
        self.organized_dir = self.base_dir / "organized"
        self.test_sets_dir = self.base_dir / "test_sets"
        self.validation_dir = self.base_dir / "validation"
        self.by_category_dir = self.base_dir / "by_category"
        self.by_quality_dir = self.base_dir / "by_quality"
        
        # Create directories
        self._create_directories()
        
        # Sample metadata
        self.metadata = {
            "total_samples": 0,
            "categories": {},
            "quality_distribution": {},
            "last_updated": None,
            "sources": []
        }
    
    def _create_directories(self):
        """Create all necessary directories"""
        directories = [
            self.raw_dir,
            self.organized_dir,
            self.test_sets_dir,
            self.validation_dir,
            self.by_category_dir,
            self.by_quality_dir
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
        
        # Create category subdirectories
        categories = ["people", "animals", "vehicles", "buildings", "nature", 
                     "food", "objects", "technology", "art", "sports"]
        
        for category in categories:
            (self.by_category_dir / category).mkdir(exist_ok=True)
        
        # Create quality subdirectories
        quality_levels = ["high_quality", "medium_quality", "low_quality", "placeholder"]
        for quality in quality_levels:
            (self.by_quality_dir / quality).mkdir(exist_ok=True)
    
    def import_from_download(self, source_dir="test_images"):
        """Import images from download directory"""
        logger.info(f"Importing images from {source_dir}...")
        
        source_path = Path(source_dir)
        if not source_path.exists():
            logger.error(f"Source directory {source_dir} does not exist")
            return False
        
        imported_count = 0
        
        # Copy all images to raw directory
        for root, dirs, files in os.walk(source_path):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                    source_file = Path(root) / file
                    dest_file = self.raw_dir / file
                    
                    # Avoid duplicates
                    counter = 1
                    while dest_file.exists():
                        name_parts = file.rsplit('.', 1)
                        if len(name_parts) == 2:
                            dest_file = self.raw_dir / f"{name_parts[0]}_{counter}.{name_parts[1]}"
                        else:
                            dest_file = self.raw_dir / f"{file}_{counter}"
                        counter += 1
                    
                    shutil.copy2(source_file, dest_file)
                    imported_count += 1
        
        logger.info(f"Imported {imported_count} images to raw directory")
        return True
    
    def organize_by_category(self):
        """Organize images by category based on filename patterns"""
        logger.info("Organizing images by category...")
        
        category_patterns = {
            "people": ["person", "human", "man", "woman", "child", "face", "portrait"],
            "animals": ["animal", "dog", "cat", "bird", "fish", "horse", "cow"],
            "vehicles": ["vehicle", "car", "truck", "bus", "motorcycle", "airplane"],
            "buildings": ["building", "house", "home", "office", "church", "bridge"],
            "nature": ["nature", "tree", "forest", "mountain", "ocean", "landscape"],
            "food": ["food", "meal", "fruit", "vegetable", "bread", "drink"],
            "objects": ["object", "furniture", "tool", "book", "clothing", "bag"],
            "technology": ["technology", "computer", "phone", "camera", "gadget"],
            "art": ["art", "painting", "drawing", "photo", "picture", "design"],
            "sports": ["sport", "game", "football", "basketball", "tennis", "swimming"]
        }
        
        organized_count = 0
        
        for image_file in self.raw_dir.glob("*"):
            if image_file.is_file() and image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                filename_lower = image_file.name.lower()
                
                # Find matching category
                matched_category = None
                for category, patterns in category_patterns.items():
                    if any(pattern in filename_lower for pattern in patterns):
                        matched_category = category
                        break
                
                if matched_category:
                    dest_dir = self.by_category_dir / matched_category
                    dest_file = dest_dir / image_file.name
                    
                    # Avoid duplicates
                    counter = 1
                    while dest_file.exists():
                        name_parts = image_file.stem, image_file.suffix
                        dest_file = dest_dir / f"{name_parts[0]}_{counter}{name_parts[1]}"
                        counter += 1
                    
                    shutil.copy2(image_file, dest_file)
                    organized_count += 1
                    
                    # Update metadata
                    if matched_category not in self.metadata["categories"]:
                        self.metadata["categories"][matched_category] = 0
                    self.metadata["categories"][matched_category] += 1
        
        logger.info(f"Organized {organized_count} images by category")
        return organized_count
    
    def organize_by_quality(self):
        """Organize images by quality based on source and characteristics"""
        logger.info("Organizing images by quality...")
        
        quality_count = 0
        
        for image_file in self.raw_dir.glob("*"):
            if image_file.is_file() and image_file.suffix.lower() in ['.jpg', '.jpeg', '.png']:
                filename_lower = image_file.name.lower()
                
                # Determine quality based on source
                if "unsplash" in filename_lower:
                    quality = "high_quality"
                elif "picsum" in filename_lower:
                    quality = "medium_quality"
                elif "placeholder" in filename_lower or "fakeimg" in filename_lower:
                    quality = "placeholder"
                else:
                    # Try to analyze image quality
                    try:
                        with Image.open(image_file) as img:
                            width, height = img.size
                            if width >= 400 and height >= 400:
                                quality = "high_quality"
                            elif width >= 200 and height >= 200:
                                quality = "medium_quality"
                            else:
                                quality = "low_quality"
                    except Exception:
                        quality = "low_quality"
                
                dest_dir = self.by_quality_dir / quality
                dest_file = dest_dir / image_file.name
                
                # Avoid duplicates
                counter = 1
                while dest_file.exists():
                    name_parts = image_file.stem, image_file.suffix
                    dest_file = dest_dir / f"{name_parts[0]}_{counter}{name_parts[1]}"
                    counter += 1
                
                shutil.copy2(image_file, dest_file)
                quality_count += 1
                
                # Update metadata
                if quality not in self.metadata["quality_distribution"]:
                    self.metadata["quality_distribution"][quality] = 0
                self.metadata["quality_distribution"][quality] += 1
        
        logger.info(f"Organized {quality_count} images by quality")
        return quality_count
    
    def create_test_sets(self, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
        """Create train/validation/test sets"""
        logger.info("Creating train/validation/test sets...")
        
        # Get all organized images
        all_images = []
        for category_dir in self.by_category_dir.iterdir():
            if category_dir.is_dir():
                for image_file in category_dir.glob("*"):
                    if image_file.is_file():
                        all_images.append((image_file, category_dir.name))
        
        # Shuffle and split
        import random
        random.shuffle(all_images)
        
        total_images = len(all_images)
        train_count = int(total_images * train_ratio)
        val_count = int(total_images * val_ratio)
        
        train_images = all_images[:train_count]
        val_images = all_images[train_count:train_count + val_count]
        test_images = all_images[train_count + val_count:]
        
        # Create sets
        self._create_set(train_images, "train", self.test_sets_dir)
        self._create_set(val_images, "validation", self.test_sets_dir)
        self._create_set(test_images, "test", self.test_sets_dir)
        
        logger.info(f"Created test sets: Train({len(train_images)}), Val({len(val_images)}), Test({len(test_images)})")
        return len(train_images), len(val_images), len(test_images)
    
    def _create_set(self, images, set_name, base_dir):
        """Create a specific set (train/val/test)"""
        set_dir = base_dir / set_name
        set_dir.mkdir(exist_ok=True)
        
        for image_file, category in images:
            dest_file = set_dir / f"{category}_{image_file.name}"
            shutil.copy2(image_file, dest_file)
    
    def create_sample_packages(self):
        """Create organized sample packages"""
        logger.info("Creating sample packages...")
        
        packages = {
            "quick_test": 50,      # Quick test package
            "standard_test": 200,  # Standard test package
            "comprehensive_test": 500,  # Comprehensive test package
            "full_dataset": 1000   # Full dataset package
        }
        
        for package_name, count in packages.items():
            package_dir = self.organized_dir / package_name
            package_dir.mkdir(exist_ok=True)
            
            # Select diverse images
            selected_images = self._select_diverse_images(count)
            
            for i, (image_file, category) in enumerate(selected_images):
                dest_file = package_dir / f"{i+1:03d}_{category}_{image_file.name}"
                shutil.copy2(image_file, dest_file)
            
            logger.info(f"Created {package_name} package with {len(selected_images)} images")
    
    def _select_diverse_images(self, count):
        """Select diverse images from all categories"""
        all_images = []
        for category_dir in self.by_category_dir.iterdir():
            if category_dir.is_dir():
                category_images = list(category_dir.glob("*"))
                for img in category_images:
                    all_images.append((img, category_dir.name))
        
        # Distribute evenly across categories
        import random
        random.shuffle(all_images)
        
        # Group by category
        by_category = {}
        for img, cat in all_images:
            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append((img, cat))
        
        # Select evenly from each category
        selected = []
        categories = list(by_category.keys())
        images_per_category = count // len(categories)
        
        for category in categories:
            category_images = by_category[category]
            random.shuffle(category_images)
            selected.extend(category_images[:images_per_category])
        
        # Fill remaining slots randomly
        remaining = count - len(selected)
        if remaining > 0:
            all_remaining = [(img, cat) for img, cat in all_images if (img, cat) not in selected]
            random.shuffle(all_remaining)
            selected.extend(all_remaining[:remaining])
        
        return selected[:count]
    
    def generate_metadata(self):
        """Generate comprehensive metadata"""
        logger.info("Generating metadata...")
        
        self.metadata["total_samples"] = len(list(self.raw_dir.glob("*")))
        self.metadata["last_updated"] = time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Count by category
        for category_dir in self.by_category_dir.iterdir():
            if category_dir.is_dir():
                count = len(list(category_dir.glob("*")))
                self.metadata["categories"][category_dir.name] = count
        
        # Count by quality
        for quality_dir in self.by_quality_dir.iterdir():
            if quality_dir.is_dir():
                count = len(list(quality_dir.glob("*")))
                self.metadata["quality_distribution"][quality_dir.name] = count
        
        # Save metadata
        metadata_file = self.base_dir / "metadata.json"
        with open(metadata_file, 'w') as f:
            json.dump(self.metadata, f, indent=2)
        
        logger.info(f"Metadata saved to {metadata_file}")
        return self.metadata
    
    def print_summary(self):
        """Print sample summary"""
        metadata = self.generate_metadata()
        
        print("\n📊 Sample Manager Summary")
        print("=" * 50)
        print(f"Total samples: {metadata['total_samples']}")
        print(f"Last updated: {metadata['last_updated']}")
        
        print(f"\n📂 By Category:")
        for category, count in metadata['categories'].items():
            print(f"  {category}: {count} images")
        
        print(f"\n🎨 By Quality:")
        for quality, count in metadata['quality_distribution'].items():
            print(f"  {quality}: {count} images")
        
        print(f"\n📁 Directory Structure:")
        print(f"  Raw: {len(list(self.raw_dir.glob('*')))} images")
        print(f"  Organized: {len(list(self.organized_dir.glob('*')))} packages")
        print(f"  Test Sets: {len(list(self.test_sets_dir.glob('*')))} sets")
    
    def cleanup(self):
        """Clean up temporary files"""
        logger.info("Cleaning up...")
        # Add cleanup logic if needed
        pass

def main():
    """Main function"""
    print("📦 VisionAI Pro Sample Manager")
    print("=" * 40)
    
    manager = SampleManager()
    
    print("\nChoose action:")
    print("1. Import from download directory")
    print("2. Organize by category")
    print("3. Organize by quality")
    print("4. Create test sets")
    print("5. Create sample packages")
    print("6. Full organization (all steps)")
    print("7. Show summary")
    
    try:
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == "1":
            source = input("Enter source directory (default: test_images): ").strip() or "test_images"
            manager.import_from_download(source)
        elif choice == "2":
            manager.organize_by_category()
        elif choice == "3":
            manager.organize_by_quality()
        elif choice == "4":
            manager.create_test_sets()
        elif choice == "5":
            manager.create_sample_packages()
        elif choice == "6":
            print("Running full organization...")
            manager.import_from_download()
            manager.organize_by_category()
            manager.organize_by_quality()
            manager.create_test_sets()
            manager.create_sample_packages()
            print("✅ Full organization completed!")
        elif choice == "7":
            manager.print_summary()
        else:
            print("Invalid choice")
            
    except KeyboardInterrupt:
        print("\n⏹️  Operation interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Operation failed: {e}")

if __name__ == "__main__":
    main()
