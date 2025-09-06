#!/bin/bash

# VisionAI Pro Image Download Script
# Downloads 1000+ free images for testing classification accuracy

echo "🖼️  VisionAI Pro Image Downloader"
echo "=================================="

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
echo "🚀 Starting image download..."
echo "This will download 1000+ images from free sources"
echo "Press Ctrl+C to cancel"
echo ""

# Run the basic downloader
echo "📥 Running basic image downloader..."
python3 download_images.py

echo ""
echo "🚀 Running advanced image downloader..."
python3 advanced_image_scraper.py

echo ""
echo "✅ Image download completed!"
echo "📁 Check the 'test_images' and 'advanced_test_images' directories"
echo "🎯 You can now test the VisionAI Pro classification with these images!"
