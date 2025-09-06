#!/bin/bash

# VisionAI Pro Sample Setup Script
# Downloads, organizes, and manages image samples for testing

echo "📦 VisionAI Pro Sample Setup"
echo "============================"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 first."
    exit 1
fi

# Check if required packages are installed
echo "📦 Checking required packages..."
python3 -c "import requests, PIL" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📥 Installing required packages..."
    pip3 install requests pillow
fi

echo ""
echo "🚀 Starting complete sample setup..."
echo "This will:"
echo "  1. Download 1000+ images from free sources"
echo "  2. Organize them by category and quality"
echo "  3. Create test sets and sample packages"
echo "  4. Generate metadata and reports"
echo ""
echo "Press Ctrl+C to cancel"
echo ""

# Step 1: Download images
echo "📥 Step 1: Downloading images..."
python3 download_images.py
if [ $? -ne 0 ]; then
    echo "❌ Image download failed"
    exit 1
fi

echo ""
echo "🚀 Step 2: Downloading advanced images..."
python3 advanced_image_scraper.py
if [ $? -ne 0 ]; then
    echo "❌ Advanced image download failed"
    exit 1
fi

# Step 3: Organize samples
echo ""
echo "📦 Step 3: Organizing samples..."
python3 sample_manager.py << EOF
6
EOF

if [ $? -ne 0 ]; then
    echo "❌ Sample organization failed"
    exit 1
fi

# Step 4: Show summary
echo ""
echo "📊 Step 4: Sample summary..."
python3 sample_manager.py << EOF
7
EOF

echo ""
echo "✅ Sample setup completed!"
echo ""
echo "📁 Sample locations:"
echo "  - Raw images: image_samples/raw/"
echo "  - Organized packages: image_samples/organized/"
echo "  - By category: image_samples/by_category/"
echo "  - By quality: image_samples/by_quality/"
echo "  - Test sets: image_samples/test_sets/"
echo ""
echo "🧪 To test with samples:"
echo "  python3 test_with_downloaded_images.py"
echo ""
echo "📖 For more info:"
echo "  cat image_samples/README.md"
