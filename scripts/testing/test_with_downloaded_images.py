#!/usr/bin/env python3
"""
Test VisionAI Pro with downloaded images
Automatically tests classification accuracy on downloaded image dataset
"""

import os
import sys
import time
import random
from PIL import Image
import logging

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.models.zero_shot_classifier import ZeroShotCustomClassifier

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageTester:
    def __init__(self, image_dir="test_images"):
        self.image_dir = image_dir
        self.classifier = None
        self.results = []
        
    def initialize_classifier(self):
        """Initialize the zero-shot classifier"""
        logger.info("Initializing Zero-shot Classifier...")
        try:
            self.classifier = ZeroShotCustomClassifier(
                base_words_path="query/base_words.txt",
                building_terms_path="query/building_terms_clean_final.csv"
            )
            logger.info("✅ Classifier initialized successfully")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to initialize classifier: {e}")
            return False
    
    def get_image_files(self, category=None, max_images=50):
        """Get list of image files to test"""
        image_files = []
        
        if category:
            category_dir = os.path.join(self.image_dir, category)
            if os.path.exists(category_dir):
                files = [f for f in os.listdir(category_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                image_files = [os.path.join(category_dir, f) for f in files[:max_images]]
        else:
            # Get images from all categories
            for root, dirs, files in os.walk(self.image_dir):
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                        image_files.append(os.path.join(root, file))
                        if len(image_files) >= max_images:
                            break
                if len(image_files) >= max_images:
                    break
        
        return image_files
    
    def test_image(self, image_path, expected_category=None):
        """Test classification on a single image"""
        try:
            # Load image
            image = Image.open(image_path)
            
            # Get prediction
            start_time = time.time()
            predictions = self.classifier.predict(image, top_k=5, use_fast_mode=True)
            processing_time = time.time() - start_time
            
            # Extract top prediction
            top_prediction = predictions[0] if predictions else {"category": "Unknown", "confidence": 0.0}
            
            result = {
                "image_path": image_path,
                "expected_category": expected_category,
                "predicted_category": top_prediction["category"],
                "confidence": top_prediction["confidence"],
                "processing_time": processing_time,
                "all_predictions": predictions
            }
            
            return result
            
        except Exception as e:
            logger.error(f"Error testing image {image_path}: {e}")
            return None
    
    def test_category(self, category, max_images=20):
        """Test images from a specific category"""
        logger.info(f"\n🧪 Testing {category} images...")
        
        image_files = self.get_image_files(category, max_images)
        
        if not image_files:
            logger.warning(f"No images found for category: {category}")
            return []
        
        logger.info(f"Found {len(image_files)} images for {category}")
        
        category_results = []
        for i, image_path in enumerate(image_files):
            logger.info(f"Testing {i+1}/{len(image_files)}: {os.path.basename(image_path)}")
            
            result = self.test_image(image_path, category)
            if result:
                category_results.append(result)
                logger.info(f"  → Predicted: {result['predicted_category']} (confidence: {result['confidence']:.3f})")
            
            # Small delay to avoid overwhelming the system
            time.sleep(0.1)
        
        return category_results
    
    def test_all_categories(self, max_images_per_category=20):
        """Test images from all categories"""
        logger.info("🚀 Starting comprehensive image testing...")
        
        if not self.classifier:
            logger.error("Classifier not initialized")
            return
        
        # Get all categories
        categories = []
        if os.path.exists(self.image_dir):
            categories = [d for d in os.listdir(self.image_dir) 
                         if os.path.isdir(os.path.join(self.image_dir, d))]
        
        if not categories:
            logger.error(f"No categories found in {self.image_dir}")
            return
        
        logger.info(f"Found categories: {', '.join(categories)}")
        
        all_results = []
        for category in categories:
            category_results = self.test_category(category, max_images_per_category)
            all_results.extend(category_results)
        
        self.results = all_results
        self.print_summary()
    
    def test_random_sample(self, total_images=100):
        """Test a random sample of images"""
        logger.info(f"🎲 Testing random sample of {total_images} images...")
        
        if not self.classifier:
            logger.error("Classifier not initialized")
            return
        
        image_files = self.get_image_files(max_images=total_images)
        
        if not image_files:
            logger.error(f"No images found in {self.image_dir}")
            return
        
        # Randomly sample images
        random.shuffle(image_files)
        sample_files = image_files[:total_images]
        
        logger.info(f"Testing {len(sample_files)} random images...")
        
        all_results = []
        for i, image_path in enumerate(sample_files):
            logger.info(f"Testing {i+1}/{len(sample_files)}: {os.path.basename(image_path)}")
            
            result = self.test_image(image_path)
            if result:
                all_results.append(result)
                logger.info(f"  → Predicted: {result['predicted_category']} (confidence: {result['confidence']:.3f})")
            
            time.sleep(0.1)
        
        self.results = all_results
        self.print_summary()
    
    def print_summary(self):
        """Print test results summary"""
        if not self.results:
            logger.warning("No results to summarize")
            return
        
        logger.info(f"\n📊 Test Results Summary")
        logger.info(f"=" * 50)
        logger.info(f"Total images tested: {len(self.results)}")
        
        # Calculate average confidence
        avg_confidence = sum(r['confidence'] for r in self.results) / len(self.results)
        logger.info(f"Average confidence: {avg_confidence:.3f}")
        
        # Calculate average processing time
        avg_time = sum(r['processing_time'] for r in self.results) / len(self.results)
        logger.info(f"Average processing time: {avg_time:.3f} seconds")
        
        # Count predictions by category
        category_counts = {}
        for result in self.results:
            category = result['predicted_category']
            category_counts[category] = category_counts.get(category, 0) + 1
        
        logger.info(f"\n📈 Top predicted categories:")
        sorted_categories = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)
        for category, count in sorted_categories[:10]:
            percentage = (count / len(self.results)) * 100
            logger.info(f"  {category}: {count} images ({percentage:.1f}%)")
        
        # Save detailed results
        self.save_results()
    
    def save_results(self):
        """Save detailed results to file"""
        if not self.results:
            return
        
        results_file = "image_test_results.txt"
        with open(results_file, 'w') as f:
            f.write("VisionAI Pro Image Test Results\n")
            f.write("=" * 40 + "\n")
            f.write(f"Test date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total images: {len(self.results)}\n\n")
            
            for i, result in enumerate(self.results):
                f.write(f"Image {i+1}: {os.path.basename(result['image_path'])}\n")
                f.write(f"  Predicted: {result['predicted_category']}\n")
                f.write(f"  Confidence: {result['confidence']:.4f}\n")
                f.write(f"  Processing time: {result['processing_time']:.3f}s\n")
                f.write(f"  All predictions: {result['all_predictions']}\n\n")
        
        logger.info(f"Detailed results saved to: {results_file}")

def main():
    """Main function"""
    print("🧪 VisionAI Pro Image Tester")
    print("=" * 40)
    
    tester = ImageTester()
    
    # Initialize classifier
    if not tester.initialize_classifier():
        print("❌ Failed to initialize classifier")
        return
    
    print("\nChoose test mode:")
    print("1. Test all categories (20 images each)")
    print("2. Test random sample (100 images)")
    print("3. Test specific category")
    
    try:
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            tester.test_all_categories()
        elif choice == "2":
            tester.test_random_sample()
        elif choice == "3":
            category = input("Enter category name: ").strip()
            tester.test_category(category)
        else:
            print("Invalid choice, running random sample test...")
            tester.test_random_sample()
            
    except KeyboardInterrupt:
        print("\n⏹️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        logger.error(f"Test failed: {e}")

if __name__ == "__main__":
    main()
