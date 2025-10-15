# Quick Start Guide - Image Resizer for CustomPosters

## 🚀 Installation (One-Time Setup)

### Option 1: With Virtual Environment (Recommended)

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

### Option 2: System-Wide Installation

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
pip install -r requirements.txt
```

This installs:
- **Pillow** - for image processing
- **moviepy** - for video conversion

### Activating Virtual Environment Later

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
source venv/bin/activate  # On Linux/Mac
```

When done, deactivate with:
```bash
deactivate
```

## 📁 Basic Workflow

### Quick Start with Helper Script

The easiest way to get started:

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
# Add your media to input/
./run_example.sh
```

This helper script will:
- ✅ Create a virtual environment if it doesn't exist
- ✅ Activate the virtual environment
- ✅ Install dependencies automatically
- ✅ Run the poster resizer in interactive mode

### Manual Workflow

### Step 1: Add Your Media
Place your images and videos in the `input/` folder:
```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
# Copy your files to input/
cp ~/Downloads/my_video.mp4 input/
cp ~/Pictures/cool_poster.jpg input/
```

### Step 2: Run the Script
```bash
# If using virtual environment, activate it first
source venv/bin/activate  # (if not already activated)

# Run the script
python poster_resizer.py
```

### Step 3: Assign Files
The script will ask you which poster slot each file should fill:
- **poster1** - 639×488 (image, landscape)
- **poster2** - 730×490 (**VIDEO** 🎬, landscape) 
- **poster3** - 749×1054 (image, portrait)
- **poster4** - 729×999 (image, portrait)
- **poster5** - 552×769 (image, portrait)
- **customtips** - 860×1219 (image, portrait)

### Step 4: Check Results
- Output files: `../BepInEx/plugins/BikininjasPosters/posters/` and `/tips/`
- Original files: Automatically moved to `done/`

## 🎬 Video Support

### Supported Video Formats
All these formats work and are automatically converted to MP4:
- .mp4, .avi, .mov, .mkv
- .flv, .wmv, .webm, .m4v
- .mpeg, .mpg

### Tips for Videos
- **Poster2 is the video slot** - it supports animated playback in-game
- Keep videos short (30 seconds or less recommended)
- Any video format → automatically converted to MP4
- Video quality and audio are preserved

## 📋 Quick Commands

```bash
# Interactive mode (recommended)
python poster_resizer.py

# Auto-assign mode (uses files in order)
python poster_resizer.py --auto

# Custom input directory
python poster_resizer.py --input ~/my_media

# Show help
python poster_resizer.py --help
```

## 🔍 What Gets Ignored by Git

The `.gitignore` is configured to:
- ✅ Track the script, READMEs, and directory structure
- ❌ Ignore all media files in `input/` and `done/`
- ❌ Ignore temporary video processing files

This keeps your repository clean and prevents large files from being committed.

## 📦 What to Commit

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters

# Add the script and configuration
git add image_resizer/
git add .gitignore

# Commit
git commit -m "Add image/video resizer tool for CustomPosters mod

- Supports all image formats (.png, .jpg, .bmp, etc.)
- Video conversion support (.mp4, .avi, .mov, etc.)
- Auto-moves processed files to done/ directory
- Git ignores media files to keep repo clean
- Poster2 now supports video (.mp4) format"
```

## 🎯 Example Session

```bash
$ cd image_resizer
$ ls input/
cool_animation.mp4  landscape.jpg  portrait.png

$ python poster_resizer.py

🖼️  CustomPosters Media Resizer
========================================
Found 3 file(s) in input:
  - 2 image(s)
  - 1 video(s)
  🎬 cool_animation.mp4
  🖼️ landscape.jpg
  🖼️ portrait.png

============================================================
Processing: cool_animation.mp4 (VIDEO)
============================================================
Which poster slot should this file fill?
Your choice: poster2
Processing video to 730x490...
✓ Saved: ../BepInEx/plugins/BikininjasPosters/posters/Poster2.mp4
  ↳ Moved to done: cool_animation.mp4

... (continues with other files)

🎉 Processing complete! Processed 3 file(s).
```

## 🆘 Troubleshooting

### "moviepy library not found"
```bash
pip install moviepy
```

### "No supported media files found"
Check that your files are in the `input/` directory and have supported extensions.

### Video processing is slow
Video encoding takes time. Be patient or use shorter clips.

### Permission denied
Make sure you have write permissions:
```bash
chmod -R u+w /home/seb/GITRepos/lc_bikininjaPosters/BepInEx
```

## 📚 More Information

See `README.md` for complete documentation including:
- Detailed poster specifications
- Advanced usage options
- Image/video processing details
- Complete troubleshooting guide