# Bikininjas Custom Posters

A content pack and intelligent pack generator for the [CustomPosters mod](https://github.com/se3ya/CustomPosters) in Lethal Company.

## 🎯 What's Included

- **Custom Poster Pack**: Pre-configured posters ready for the game
- **Intelligent Pack Generator**: Python script that automatically matches images to poster slots based on aspect ratio similarity

---

## 📦 Quick Start - Using the Poster Pack

1. Download this repository
2. Copy the `BepInEx` folder to your Lethal Company directory
3. Launch the game and enjoy custom posters!

---

## 🛠️ Pack Generator Tool

### ✨ How It Works

The pack generator uses **intelligent aspect ratio matching** to automatically assign your images and videos to the best-fitting poster slots:

1. **Scans** all images and videos in the `input/` folder
2. **Calculates** the aspect ratio of each file (width/height)
3. **Matches** each file to the poster slot with the closest aspect ratio
4. **Generates** a complete poster pack ready for the game
5. **Videos** are automatically converted to MP4 format

### 📐 Poster Specifications

The mod supports **exactly 6 slots** per pack:

| Slot | Dimensions | Aspect Ratio | Orientation | Output Format |
|------|-----------|--------------|-------------|---------------|
| **Poster1** | 639 × 488 | 1.31:1 | Landscape | PNG or MP4 |
| **Poster2** | 730 × 490 | 1.49:1 | Landscape | PNG or MP4 |
| **Poster3** | 749 × 1054 | 0.71:1 | Portrait | PNG or MP4 |
| **Poster4** | 729 × 999 | 0.73:1 | Portrait | PNG or MP4 |
| **Poster5** | 552 × 769 | 0.72:1 | Portrait | PNG or MP4 |
| **CustomTips** | 860 × 1219 | 0.71:1 | Portrait | PNG or MP4 |

**Note**: 
- Images are saved as `.png` files
- Videos are converted to `.mp4` files (H.264 video, AAC audio)
- All files are saved to `posters/` or `tips/` folders

### � Intelligent Matching Example

If you have these images:
- `landscape1.jpg` (1920×1080, ratio 1.78:1)
- `landscape2.jpg` (1280×720, ratio 1.78:1)
- `portrait1.jpg` (1080×1920, ratio 0.56:1)
- `portrait2.jpg` (800×1200, ratio 0.67:1)
- `portrait3.jpg` (900×1400, ratio 0.64:1)
- `portrait4.jpg` (1000×1500, ratio 0.67:1)

The script will automatically match:
- `landscape1.jpg` → **Poster2** (closest to 1.49:1)
- `landscape2.jpg` → **Poster1** (closest to 1.31:1)
- `portrait1.jpg` → **CustomTips** (closest to 0.71:1)
- `portrait2.jpg` → **Poster4** (closest to 0.73:1)
- `portrait3.jpg` → **Poster5** (closest to 0.72:1)
- `portrait4.jpg` → **Poster3** (closest to 0.71:1)

### 📋 Supported Formats

`.jpg` `.jpeg` `.png` `.bmp` `.gif` `.tiff` `.webp` `.avif`

---

## 🚀 Installation & Setup

### 1. Install Python (3.7+)

### 2. Navigate to Image Resizer Directory
```bash
cd /path/to/lc_bikininjaPosters/image_resizer
```

### 3. Create Virtual Environment (Recommended)
```bash
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- **Pillow** - Image processing
- **pillow-avif-plugin** - AVIF format support
- **moviepy** - Video conversion and processing

---

## 💻 Usage

### Basic Workflow

```bash
# 1. Activate virtual environment
cd /path/to/lc_bikininjaPosters/image_resizer
source venv/bin/activate  # Linux/Mac

# 2. Add your images and videos to input/
cp ~/Pictures/*.jpg input/
cp ~/Videos/*.mp4 input/

# 3. Run the generator
python poster_resizer.py

# 4. The script will:
#    - Analyze all images and videos
#    - Match them to best-fitting slots
#    - Convert videos to MP4 format
#    - Create a complete poster pack
#    - Move processed files to done/
```

### Example Session

```bash
$ python poster_resizer.py

======================================================================
🖼️  CUSTOMPOSTERS PACK GENERATOR
======================================================================
Intelligently matches images to poster slots based on aspect ratio
======================================================================

⚙️  Configuration:
   Input:  input
   Output: ../BepInEx/plugins
   Pack:   BikininjasPosters
   Aspect: Maintained

🔍 Scanning for images...
✓ Found 6 file(s)

🎯 Matching images to poster slots...

======================================================================
📊 IMAGE-TO-SLOT MATCHING REPORT
======================================================================

✓ Matched 6 of 6 possible slots

✓ Poster1      (639×488) → landscape1.jpg
   Target ratio: 1.309 | Image ratio: 1.333 | Fit: Excellent

✓ Poster2      (730×490) → action_video.mp4 🎬
   Target ratio: 1.490 | Image ratio: 1.500 | Fit: Perfect

✓ Poster3      (749×1054) → portrait1.jpg
   Target ratio: 0.710 | Image ratio: 0.700 | Fit: Perfect

✓ Poster4      (729×999) → portrait2.jpg
   Target ratio: 0.730 | Image ratio: 0.720 | Fit: Perfect

✓ Poster5      (552×769) → animation.mp4 🎬
   Target ratio: 0.718 | Image ratio: 0.714 | Fit: Perfect

✓ CustomTips   (860×1219) → portrait4.jpg
   Target ratio: 0.705 | Image ratio: 0.707 | Fit: Perfect

======================================================================

📦 Creating pack: BikininjasPosters
✓ Pack directory: ../BepInEx/plugins/BikininjasPosters

======================================================================
🖼️  PROCESSING IMAGES & VIDEOS
======================================================================

📌 Poster1:
   Processing IMAGE: landscape1.jpg → Poster1.png
   ✓ Saved: ../BepInEx/plugins/BikininjasPosters/posters/Poster1.png

📌 Poster2:
   Processing VIDEO: action_video.mp4 → Poster2.mp4
   Loading video: action_video.mp4
   Encoding video to MP4...
   ✓ Saved: ../BepInEx/plugins/BikininjasPosters/posters/Poster2.mp4

[... continues for all slots ...]

✓ Successfully processed 6 of 6 files
======================================================================

📄 Pack info saved: ../BepInEx/plugins/BikininjasPosters/pack_info.txt

======================================================================
🧹 CLEANING UP
======================================================================

✓ Moved to done: landscape1.jpg
✓ Moved to done: action_video.mp4
[... continues ...]

✓ Moved 6 files to done directory
======================================================================

======================================================================
🎉 PACK GENERATION COMPLETE!
======================================================================

✓ Pack: ../BepInEx/plugins/BikininjasPosters
✓ Processed: 6 file(s) (4 images, 2 videos)

📋 Next steps:
   1. Review: ../BepInEx/plugins/BikininjasPosters
   2. Copy 'BikininjasPosters' to:
      Lethal Company/BepInEx/plugins/

======================================================================
```

---

## 🔧 Advanced Options

### Custom Pack Name
```bash
python poster_resizer.py --pack-name MyAwesomePosters
```

### Custom Directories
```bash
python poster_resizer.py --input ~/my_images --output ~/game_mods
```

### Stretch Images (No Aspect Ratio Preservation)
```bash
python poster_resizer.py --no-aspect
```

### Keep Original Files in Input
```bash
python poster_resizer.py --no-cleanup
```

### Show Help
```bash
python poster_resizer.py --help
```

---

## 📂 Directory Structure

```
lc_bikininjaPosters/
├── BepInEx/plugins/
│   └── BikininjasPosters/          # Generated pack (ready for game)
│       ├── posters/
│       │   ├── Poster1.png
│       │   ├── Poster2.png
│       │   ├── Poster3.png
│       │   ├── Poster4.png
│       │   └── Poster5.png
│       ├── tips/
│       │   └── CustomTips.png
│       └── pack_info.txt          # Pack information
└── image_resizer/
    ├── poster_resizer.py          # Main script
    ├── config.py                  # Poster specifications
    ├── ratio_matcher.py           # Aspect ratio matching logic
    ├── image_processor.py         # Image resizing and saving
    ├── pack_generator.py          # Pack structure creation
    ├── requirements.txt           # Python dependencies
    ├── input/                     # Add your images here
    ├── done/                      # Processed files moved here
    └── venv/                      # Virtual environment
```

---

## 💡 Multiple Packs

If you have more than 6 images, the script will match the best 6 and leave the rest in `input/`:

```bash
$ python poster_resizer.py

✓ Found 15 image(s)
✓ Matched 6 of 6 possible slots

📦 Unmatched images (9):
   • image7.jpg (ratio: 1.500)
   • image8.jpg (ratio: 0.720)
   [... etc ...]

💡 Tip: These images can be used for additional packs
```

To create another pack:

```bash
# The matched images are now in done/
# Unmatched images are still in input/

# Create a second pack
python poster_resizer.py --pack-name BikininjasPosters2

# Create a third pack
python poster_resizer.py --pack-name BikininjasPosters3
```

---

## 🎯 Tips for Best Results

1. **Media Quality** - Use high-resolution images and videos (script downscales)
2. **Aspect Ratios** - Pre-sort files by orientation:
   - Landscape files (~1.3:1 to 1.5:1) → Poster1, Poster2
   - Portrait files (~0.7:1 to 0.75:1) → Poster3, Poster4, Poster5, CustomTips
3. **Video Tips**:
   - Keep videos short (30 seconds or less recommended)
   - Any format works - automatically converted to MP4 (H.264)
   - Video encoding may take time - be patient
4. **File Names** - Use descriptive names to track which file goes where
5. **Review First** - Check the matching report before deploying
6. **Test In-Game** - Review posters in game before creating more packs

---

## 🆘 Troubleshooting

### No images found
```bash
# Check input directory
ls input/
# Ensure files have valid extensions
```

### moviepy library not found
```bash
# Activate venv
source venv/bin/activate

# Install moviepy
pip install moviepy
```

### Video processing is slow
- Video encoding takes time - be patient
- Consider shorter clips or lower resolution sources
- The script shows encoding progress

### Import errors
```bash
# Activate venv
source venv/bin/activate

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Poor aspect ratio matches
The script always assigns all 6 slots. If your images don't match well:
- Add more images with different aspect ratios
- Use `--no-aspect` to stretch images (may distort)
- Manually crop images before processing

### Permission denied
```bash
chmod -R u+w BepInEx/
```

### Virtual environment issues
```bash
# Ubuntu/Debian
sudo apt-get install python3-venv

# Recreate venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧹 File Management

### Automatic Cleanup
- Successfully processed images → moved to `done/`
- Unmatched images → stay in `input/` for next pack
- Duplicate filenames → automatically numbered (_1, _2, etc.)

### Git Ignore
The following are automatically ignored by git:
- All media files in `input/`, `done/`
- Virtual environment (`venv/`)
- Generated pack folders

---

## 📊 Technical Details

### Aspect Ratio Matching Algorithm

1. Calculate aspect ratio for each input image
2. Calculate target ratios for all 6 slots
3. Use **greedy assignment**:
   - Prioritize slots with most unique ratios first
   - For each slot, find the closest-matching available image
   - Remove matched image from available pool
4. Report match quality (Perfect/Excellent/Good/Fair)

### Image Processing
- **Resizing**: Pillow/LANCZOS for high quality
- **Aspect ratio**: **Smart cropping** - crops images to match target ratio, then resizes
- **No padding**: Images fill entire space (no white/black bars)
- **Centering**: Crops are centered to preserve focal point
- **Format**: Images saved as PNG
- **Quality**: Lossless compression

### Video Processing
- **Codec**: H.264 video, AAC audio
- **Output**: Always MP4 format
- **Aspect ratio**: Maintained with black bars (centered)
- **Quality**: Preserves original quality where possible
- **Framerate**: Maintains original framerate
- **Dimensions**: Adjusted to even numbers (required for H.264)

### Pack Management
- **Auto-cleanup**: Existing pack directory is cleaned before generating new pack
- **No duplicates**: Each source file used exactly once per pack
- **Processed tracking**: Files moved to `done/` after successful processing

---

## 📄 License

This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images you process.

---

## 🔗 Links

- [CustomPosters Mod](https://github.com/se3ya/CustomPosters)
- [Lethal Company on Steam](https://store.steampowered.com/app/1966720/Lethal_Company/)

---

**Smart matching • Perfect packs • Infinite creativity** 🎨

## 🛠️ Image Resizer Tool

A Python script that batch-processes images and videos for the CustomPosters mod with **triple output** functionality.

### ✨ Key Features

- ✅ **Unlimited files** - Process as many images/videos as you want
- ✅ **Triple output** - Each file saved to 3 locations automatically:
  - `posters/` - for in-game wall decorations
  - `tips/` - for in-game loading screens
  - `output/` - for additional processing with 3rd party tools
- ✅ **Same naming** - All locations use identical filenames (Poster1, Poster2, etc.)
- ✅ **Dimension cycling** - Automatically cycles through 5 different poster sizes
- ✅ **Video support** - Converts any video format to MP4
- ✅ **Zero interaction** - Fully automatic, no prompts
- ✅ **Auto cleanup** - Moves processed files to `done/` directory
- ✅ **Git-friendly** - Media files automatically ignored

### 📐 Dimension Cycling

Files automatically cycle through 5 standard dimensions:

| File # | Dimensions | Format | Extension |
|--------|-----------|---------|-----------|
| 1, 6, 11... | 639×488 | PNG | .png |
| 2, 7, 12... | 730×490 | JPEG | .jpg |
| 3, 8, 13... | 749×1054 | BMP | .bmp |
| 4, 9, 14... | 729×999 | BMP | .bmp |
| 5, 10, 15... | 552×769 | JPEG | .jpg |

**Videos**: Always `.mp4` regardless of cycle

### 📋 Supported Formats

**Images**: `.jpg` `.jpeg` `.png` `.bmp` `.gif` `.tiff` `.webp` `.avif`  
**Videos**: `.mp4` `.avi` `.mov` `.mkv` `.flv` `.wmv` `.webm` `.m4v`

---

## 🚀 Installation & Setup

### 1. Install Python (3.7+)

### 2. Navigate to the Image Resizer Directory
```bash
cd /path/to/lc_bikininjaPosters/image_resizer
```

### 3. Create Virtual Environment (Recommended)
```bash
# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Your prompt should show: (venv)
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- **Pillow** - Image processing
- **pillow-avif-plugin** - AVIF format support
- **moviepy** - Video conversion

---

## 💻 Usage

### Basic Workflow (3 Commands)

```bash
# 1. Activate virtual environment
cd /path/to/lc_bikininjaPosters/image_resizer
source venv/bin/activate  # Linux/Mac

# 2. Add your images/videos to input/
cp ~/Pictures/*.jpg input/

# 3. Run the script (fully automatic)
python poster_resizer.py
```

### What Happens

Each file in `input/` is:
1. Resized to the appropriate dimensions (cycling through 5 sizes)
2. Saved to **THREE locations** with the same name:
   - `../BepInEx/plugins/BikininjasPosters/posters/`
   - `../BepInEx/plugins/BikininjasPosters/tips/`
   - `output/` (for additional processing)
3. Original file moved to `done/`

### Example Session

```bash
$ ls input/
cat.jpg  dog.png  video.mp4

$ python poster_resizer.py

Found 3 file(s) in input/:
  - 2 image(s)
  - 1 video(s)

Processing #1: cat.jpg → Poster1.png (639x488)
  ✓ Saved to posters: Poster1.png
  ✓ Saved to tips: Poster1.png
  ✓ Saved to output: Poster1.png
  ↳ Moved to done: cat.jpg

Processing #2: dog.png → Poster2.jpg (730x490)
  ✓ Saved to posters: Poster2.jpg
  ✓ Saved to tips: Poster2.jpg
  ✓ Saved to output: Poster2.jpg
  ↳ Moved to done: dog.png

Processing #3: video.mp4 → Poster3.mp4 (749x1054)
  ✓ Saved to posters: Poster3.mp4
  ✓ Saved to tips: Poster3.mp4
  ✓ Saved to output: Poster3.mp4
  ↳ Moved to done: video.mp4

🎉 Processing complete! Processed 3 files

Output summary:
  📂 3 files in each location:
     - BepInEx/plugins/BikininjasPosters/posters
     - BepInEx/plugins/BikininjasPosters/tips
     - output
```

---

## 📂 Directory Structure

```
lc_bikininjaPosters/
├── BepInEx/plugins/BikininjasPosters/
│   ├── posters/              # Game-ready posters (output from script)
│   │   ├── Poster1.png
│   │   ├── Poster2.jpg
│   │   └── ...
│   └── tips/                 # Game-ready tips (output from script)
│       ├── Poster1.png
│       ├── Poster2.jpg
│       └── ...
└── image_resizer/
    ├── poster_resizer.py     # Main script
    ├── requirements.txt      # Python dependencies
    ├── input/                # Put your media files here
    ├── done/                 # Processed files moved here
    ├── output/               # Additional processing workspace
    └── venv/                 # Virtual environment (created by you)
```

---

## 💡 Use Cases

### Use Case 1: Simple Mod Creation
```bash
# 1. Add images to input/
cp ~/Pictures/*.jpg input/

# 2. Run script
python poster_resizer.py

# 3. Copy to game
cp -r BepInEx ~/Games/LethalCompany/
```

### Use Case 2: With Additional Processing
```bash
# 1. Run script
python poster_resizer.py

# 2. Process files in output/ with 3rd party tools
cd output/
# ... run optimization, filters, etc ...

# 3. Copy optimized files back to posters/tips if needed
cp optimized_*.png ../BepInEx/plugins/BikininjasPosters/posters/
```

### Use Case 3: Quality Check Before Deploy
```bash
# 1. Run script
python poster_resizer.py

# 2. Review files in output/
ls -lh output/

# 3. If issues found, reprocess
mv done/bad_image.jpg input/
python poster_resizer.py
```

---

## 🔧 Advanced Options

### Custom Commands

```bash
# Use custom input directory
python poster_resizer.py --input ~/my_media

# Use custom target directory
python poster_resizer.py --target /path/to/mod

# Show help
python poster_resizer.py --help
```

### Aspect Ratio

By default, the script **maintains aspect ratio** with white/black padding.

To stretch/distort images instead:
```bash
python poster_resizer.py --no-aspect
```

---

## 🎯 Tips for Best Results

1. **Use high-quality source media** - Script downscales but won't enhance quality
2. **Consider aspect ratios**:
   - Files 1, 6, 11... (639×488) - Landscape ~1.31:1
   - Files 2, 7, 12... (730×490) - Landscape ~1.49:1
   - Files 3, 8, 13... (749×1054) - Portrait ~0.71:1
   - Files 4, 9, 14... (729×999) - Portrait ~0.73:1
   - Files 5, 10, 15... (552×769) - Portrait ~0.72:1
3. **For videos**:
   - Keep short (30 seconds or less recommended)
   - Any format works - auto-converted to MP4
   - Consider file size for mod distribution
4. **Review output/** before deploying to game

---

## 🆘 Troubleshooting

### "No supported media files found"
```bash
# Check input directory
ls input/
# Make sure files have valid extensions
```

### "moviepy library not found"
```bash
# Activate venv first
source venv/bin/activate
# Reinstall dependencies
pip install -r requirements.txt
```

### Video processing is slow
- Video encoding takes time - be patient
- Consider shorter clips or lower resolution sources

### Permission denied
```bash
# Fix permissions
chmod -R u+w BepInEx/
```

### Import errors
```bash
# Ensure venv is activated
source venv/bin/activate
which python  # Should show: .../venv/bin/python

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Virtual environment issues
```bash
# Ubuntu/Debian: Install venv module
sudo apt-get install python3-venv

# Recreate venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🧹 File Management

### What Gets Processed
- All supported image and video files in `input/`
- Files are processed in alphabetical order
- Sequential numbering: Poster1, Poster2, Poster3...

### What Happens to Files
- **Successful**: Moved from `input/` to `done/`
- **Failed**: Stays in `input/` for retry
- **Duplicates**: Number suffix added (_1, _2, etc.)

### Git Ignore Configuration
Automatically ignored by git:
- ❌ All media files in `input/`, `done/`, `output/`
- ❌ Virtual environment (`venv/`, `.venv/`, `env/`)
- ❌ Temporary video files
- ✅ Directory structure and scripts tracked

---

## 📊 Technical Details

### Image Processing
- **Aspect ratio**: Maintained by default (white padding added)
- **Transparency**: Converted to RGB with white background
- **Quality**: JPEG 95%, PNG lossless, BMP standard

### Video Processing
- **Codec**: H.264 video, AAC audio
- **Output**: Always MP4 format
- **Quality**: Preserves original quality where possible
- **Framerate**: Maintains original framerate

### Triple Output Logic
```
For each file in input/:
1. Determine dimensions (cycle index)
2. Resize/convert media
3. Save to posters/PosterN.ext
4. Copy to tips/PosterN.ext
5. Copy to output/PosterN.ext
6. Move original to done/
```

---

## 🎉 Benefits

| Feature | Benefit |
|---------|---------|
| **Unlimited files** | Process entire collections at once |
| **Triple output** | Maximum flexibility for any workflow |
| **Zero interaction** | Just run and go |
| **Dimension cycling** | Automatic variety across poster sizes |
| **Video support** | Animated posters made easy |
| **Auto cleanup** | Organized workflow, no manual file management |
| **Git-friendly** | Clean repository, no large media commits |
| **Virtual environment** | Isolated dependencies, no conflicts |

---

## 📦 File Count Examples

| Input Files | Output Files | Total Created |
|-------------|--------------|---------------|
| 1 file | 3 files | 3× multiplication |
| 5 files | 15 files | 3× multiplication |
| 13 files | 39 files | 3× multiplication |
| 100 files | 300 files | 3× multiplication |

**Disk usage**: 3× the processed file sizes (by design)

---

## 📚 Quick Reference

### First Time Setup
```bash
cd image_resizer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Every Time After
```bash
source venv/bin/activate
python poster_resizer.py
deactivate
```

### Essential Commands
| Command | Purpose |
|---------|---------|
| `source venv/bin/activate` | Activate virtual environment |
| `python poster_resizer.py` | Run the script |
| `deactivate` | Exit virtual environment |
| `ls input/` | Check input files |
| `ls output/` | Check processed files |
| `ls done/` | Check archived originals |

---

## 📄 License

This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images you process.

---

## 🔗 Links

- [CustomPosters Mod](https://github.com/se3ya/CustomPosters)
- [Lethal Company on Steam](https://store.steampowered.com/app/1966720/Lethal_Company/)

---

**Remember**: Each file → 3 locations → Same name → Automatic! 🎉