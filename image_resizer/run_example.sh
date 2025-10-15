#!/bin/bash

# Example script demonstrating poster_resizer.py usage
# Run this after placing your images in the input/ folder

echo "🖼️  CustomPosters Media Resizer - Example Usage"
echo "================================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if input directory exists and has images
if [ ! -d "input" ]; then
    echo "📁 Creating input directory..."
    mkdir input
    echo "   Please add your images/videos to the input/ folder and run this script again."
    exit 1
fi

# Count media files in input directory
media_count=$(find input -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.bmp" -o -iname "*.gif" -o -iname "*.tiff" -o -iname "*.webp" -o -iname "*.mp4" -o -iname "*.avi" -o -iname "*.mov" -o -iname "*.mkv" -o -iname "*.flv" -o -iname "*.wmv" -o -iname "*.webm" -o -iname "*.m4v" \) | wc -l)

if [ "$media_count" -eq 0 ]; then
    echo "📁 No media files found in input/ directory."
    echo "   Please add some images or videos and run this script again."
    exit 1
fi

echo "📁 Found $media_count media file(s) in input/ directory"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🔧 Virtual environment not found. Creating one..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if Pillow and moviepy are installed
if ! python3 -c "import PIL" &> /dev/null || ! python3 -c "import moviepy" &> /dev/null; then
    echo "📦 Installing required dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "🚀 Starting poster resizer in interactive mode..."
echo "   You'll be asked to assign each file to a poster slot."
echo ""

# Run the poster resizer
python3 poster_resizer.py

echo ""
echo "✅ Done! Check the BikininjasPosters folder for your processed media."
echo "💡 To deactivate the virtual environment, type: deactivate"