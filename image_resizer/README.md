# CustomPosters Media Resizer

A Python script to automatically resize images and videos for the [CustomPosters mod](https://github.com/se3ya/CustomPosters) in Lethal Company. This tool resizes media to the exact specifications required by the mod, outputs them with correct filenames and formats, and moves processed files to a `done/` directory.

## Features

- ✅ Resizes images and videos to exact CustomPosters specifications
- ✅ **Video support** - converts any video format to MP4 for Poster2
- ✅ Maintains aspect ratio with smart cropping/padding
- ✅ Converts to correct output formats (PNG, BMP, JPEG, MP4)
- ✅ Uses correct filenames (Poster1.png, Poster2.mp4, etc.)
- ✅ Places files in the right folders (posters/ and tips/)
- ✅ **Automatically moves processed files to done/ directory**
- ✅ Interactive mode for manual assignment
- ✅ Auto mode for batch processing
- ✅ Handles transparent images properly
- ✅ Support for multiple input formats
- ✅ Extracts video frames for image slots if needed

## Poster Specifications

| Poster | Dimensions | Output Format | Output Location |
|--------|------------|---------------|-----------------|
| Poster1 | 639×488 | PNG | posters/Poster1.png |
| Poster2 | 730×490 | **MP4** 🎬 | posters/Poster2.mp4 |
| Poster3 | 749×1054 | BMP | posters/Poster3.bmp |
| Poster4 | 729×999 | JPEG | posters/Poster4.jpeg |
| Poster5 | 552×769 | PNG | posters/Poster5.png |
| CustomTips | 860×1219 | JPEG | tips/CustomTips.jpg |

**🎬 Poster2 is special!** It supports video playback in-game, making it perfect for animated posters.

## Installation

1. **Install Python** (3.7 or higher)

2. **Create a virtual environment** (recommended):
   ```bash
   cd /path/to/lc_bikininjaPosters/image_resizer
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Linux/Mac:
   source venv/bin/activate
   
   # Windows:
   venv\Scripts\activate
   ```
   
   Your prompt should now show `(venv)` at the beginning.

4. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   This installs:
   - **Pillow** - for image processing
   - **moviepy** - for video processing and conversion

5. **Add your media files** to the `input/` folder

**Note**: You'll need to activate the virtual environment each time you use the script:
```bash
source venv/bin/activate  # Linux/Mac
```

## Usage

**First, activate your virtual environment** (if you created one):
```bash
source venv/bin/activate  # Linux/Mac
```

### Interactive Mode (Recommended)
```bash
python poster_resizer.py
```

This mode will:
- Show you each image/video found in the `input/` folder
- Ask which poster slot each file should fill
- Allow you to skip files or quit at any time
- Move processed files to `done/` automatically

### Auto Mode
```bash
python poster_resizer.py --auto
```

This mode automatically assigns files to poster slots in order (Poster1, Poster2, etc.).

### Custom Directories
```bash
# Use a different input directory
python poster_resizer.py --input my_media

# Use a different target directory
python poster_resizer.py --target /path/to/your/mod/BikininjasPosters
```

### Other Options
```bash
# Don't maintain aspect ratio (may distort images)
python poster_resizer.py --no-aspect

# Show help
python poster_resizer.py --help
```

## Directory Structure

### Before (Your Setup)
```
lc_bikininjaPosters/
├── image_resizer/
│   ├── poster_resizer.py
│   ├── requirements.txt
│   ├── README.md
│   ├── input/                # Put your images/videos here
│   │   ├── cool_video.mp4
│   │   ├── awesome_image.png
│   │   └── my_tip.jpg
│   └── done/                 # Processed files moved here automatically
└── BepInEx/plugins/BikininjasPosters/
    ├── posters/
    └── tips/
```

### After (Generated Output)
```
lc_bikininjaPosters/
├── image_resizer/
│   ├── input/                # Empty (files moved to done/)
│   └── done/                 # Your original files
│       ├── cool_video.mp4
│       ├── awesome_image.png
│       └── my_tip.jpg
└── BepInEx/plugins/BikininjasPosters/
    ├── posters/
    │   ├── Poster1.png       # 639×488
    │   ├── Poster2.mp4       # 730×490 (video!)
    │   ├── Poster3.bmp       # 749×1054
    │   ├── Poster4.jpeg      # 729×999
    │   └── Poster5.png       # 552×769
    └── tips/
        └── CustomTips.jpg    # 860×1219
```

## Supported Input Formats

### Images
- `.jpg`, `.jpeg`
- `.png`
- `.bmp`
- `.gif`
- `.tiff`
- `.webp`

### Videos (NEW! 🎬)
- `.mp4`
- `.avi`
- `.mov`
- `.mkv`
- `.flv`
- `.wmv`
- `.webm`
- `.m4v`
- `.mpeg`, `.mpg`

**All video formats are automatically converted to MP4!**

## Image Processing Details

### Aspect Ratio Handling
By default, the script maintains the original aspect ratio of your media:
- Media is resized to fit within the target dimensions
- If needed, white padding (images) or black bars (videos) are added to reach exact dimensions
- This prevents distortion of your content

### Transparency Handling
- Transparent PNG images are converted to RGB with white backgrounds
- This ensures compatibility with all output formats

### Video Processing
- Videos are resized and re-encoded to MP4 format
- Audio is preserved (AAC codec)
- Video codec: H.264 for maximum compatibility
- Maintains original framerate and quality where possible

### Quality Settings
- JPEG files are saved with 95% quality and optimization
- PNG files use lossless compression
- BMP files are saved in standard format
- MP4 videos use H.264 with AAC audio

## File Management

### Automatic Move to Done Directory
After successful processing:
- Source files are **automatically moved** from `input/` to `done/`
- If a file with the same name exists in `done/`, a number suffix is added
- Only successfully processed files are moved
- Failed/skipped files remain in `input/` for retry

### Git Ignore
The `.gitignore` file is configured to:
- ✅ Track the `input/` and `done/` directories
- ❌ Ignore all media files in those directories
- ✅ Keep directory structure in git
- ❌ Prevent large media files from being committed
- ❌ Ignore virtual environments (`venv/`, `.venv/`, `env/`)

## Tips for Best Results

1. **Use high-quality source media** - The script will downscale but won't enhance quality
2. **Consider target aspect ratios** when selecting media:
   - Poster1: ~1.31:1 (landscape)
   - Poster2: ~1.49:1 (landscape) - **Perfect for videos!** 🎬
   - Poster3: ~0.71:1 (portrait)
   - Poster4: ~0.73:1 (portrait)
   - Poster5: ~0.72:1 (portrait)
   - CustomTips: ~0.71:1 (portrait)

3. **For Poster2 (video slot)**: 
   - Use any video format - it will be converted to MP4
   - Keep videos short (30 seconds or less recommended)
   - Consider file size for mod distribution

4. **Video to image slots**: If you assign a video to an image slot, the script will extract a frame
5. **Image to Poster2**: You can assign images to Poster2, but videos work better for this slot

## Troubleshooting

### "No supported media files found"
- Make sure you have images or videos in the `input/` directory
- Check that your files have supported extensions

### "Input directory not found"
- The `input/` directory should be created automatically
- Or specify a different directory with `--input`

### "moviepy library not found"
- Make sure your virtual environment is activated: `source venv/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Or manually: `pip install moviepy`

### Video processing is slow
- Video encoding takes time, especially for longer videos
- Consider using shorter clips or lower resolution source videos
- The script will show encoding progress

### Permission errors
- Make sure you have write permissions to the target directory
- Try running with elevated permissions if needed

### File already exists in done/
- The script automatically adds number suffixes (_1, _2, etc.)
- No data will be overwritten

### Image processing errors
- Check that your image files aren't corrupted
- Try converting problematic images to PNG first

## Examples

### Example 1: Basic Interactive Usage
```bash
$ python poster_resizer.py

🖼️  CustomPosters Media Resizer
========================================
Input directory: /path/to/image_resizer/input
Done directory: /path/to/image_resizer/done
Output base: /path/to/BikininjasPosters
Mode: Interactive
Aspect ratio: Maintained

✓ Created/verified directories:
  - /path/to/BikininjasPosters/posters
  - /path/to/BikininjasPosters/tips
  - /path/to/image_resizer/done

Found 4 file(s) in input:
  - 2 image(s)
  - 2 video(s)
  🖼️ landscape.jpg
  🎬 cool_animation.mp4
  🖼️ portrait.png
  🎬 intro_video.avi

Available poster slots:
  poster1 (IMAGE): 639x488 -> posters/Poster1.png
  poster2 (VIDEO): 730x490 -> posters/Poster2.mp4
  poster3 (IMAGE): 749x1054 -> posters/Poster3.bmp
  poster4 (IMAGE): 729x999 -> posters/Poster4.jpeg
  poster5 (IMAGE): 552x769 -> posters/Poster5.png
  customtips (IMAGE): 860x1219 -> tips/CustomTips.jpg

============================================================
Processing: cool_animation.mp4 (VIDEO)
============================================================
Which poster slot should this file fill?
Options: poster1, poster2, poster3, poster4, poster5, customtips
Enter 'skip' to skip this file, 'quit' to exit
Your choice: poster2
Processing video to 730x490...
  Loading video (this may take a moment)...
  Encoding video to MP4...
✓ Saved: /path/to/BikininjasPosters/posters/Poster2.mp4
  ↳ Moved to done: cool_animation.mp4
```

### Example 2: Auto Mode
```bash
$ python poster_resizer.py --auto

============================================================
🎉 Processing complete! Processed 4 file(s).
============================================================

Processed files (moved to done/):
  ✓ cool_animation.mp4
  ✓ landscape.jpg
  ✓ portrait.png
  ✓ intro_video.avi

Next steps:
1. Check the output files in:
   - /path/to/BikininjasPosters/posters
   - /path/to/BikininjasPosters/tips
2. Copy the entire BikininjasPosters folder to your Lethal Company mod directory
3. Processed source files are in: /path/to/image_resizer/done
```

## License

This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images you process.