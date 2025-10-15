# Image Resizer Update Summary

## Changes Made

### 1. Script Location
✅ **Moved to**: `/home/seb/GITRepos/lc_bikininjaPosters/image_resizer/`
- Auto-detects BikininjasPosters directory (goes up one level from script)
- No hardcoded paths needed

### 2. Video Support Added 🎬
✅ **New Features**:
- Converts any video format to MP4
- Automatic video resizing and re-encoding
- H.264 video codec with AAC audio
- Supports: .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm, .m4v, .mpeg, .mpg

✅ **Poster2 is now VIDEO**:
- Changed from PNG to MP4 format
- Perfect for animated posters in-game
- Maintains aspect ratio during video conversion

✅ **Smart handling**:
- Video → Video slot: Re-encodes to MP4
- Video → Image slot: Extracts a frame
- Image → Video slot: Saves as PNG with warning

### 3. Done Directory Functionality
✅ **Automatic file management**:
- Creates `done/` directory automatically
- Moves successfully processed files from `input/` to `done/`
- Handles duplicate filenames (adds _1, _2, etc.)
- Only moves files that processed successfully
- Failed files stay in `input/` for retry

### 4. Git Ignore Configuration
✅ **Updated `.gitignore` in lc_bikininjaPosters/**:
```gitignore
# Image Resizer - Input and Done directories (media files)
image_resizer/input/*
!image_resizer/input/README.md
!image_resizer/input/.gitkeep
image_resizer/done/*
!image_resizer/done/.gitkeep
image_resizer/temp-*.mp4
image_resizer/temp-audio.m4a
```

✅ **What this does**:
- ✓ Tracks directory structure (input/ and done/)
- ✓ Tracks README and .gitkeep files
- ✗ Ignores all media files (images and videos)
- ✗ Ignores temporary processing files

### 5. Updated Dependencies
✅ **requirements.txt now includes**:
```
Pillow>=10.0.0      # Image processing
moviepy>=1.0.3      # Video processing and conversion
```

### 6. Enhanced File Discovery
✅ **Now finds both images and videos**:
- Image formats: .png, .jpg, .jpeg, .bmp, .gif, .tiff, .webp
- Video formats: .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm, .m4v, .mpeg, .mpg

### 7. Improved User Interface
✅ **Better feedback**:
- Shows file type (🖼️ IMAGE or 🎬 VIDEO)
- Displays processing progress for videos
- Shows which files were moved to done/
- Clear warnings when type mismatches occur

## File Structure

```
lc_bikininjaPosters/
├── .gitignore                      # UPDATED: Ignores media in input/done
├── image_resizer/
│   ├── poster_resizer.py          # UPDATED: Video support, done directory
│   ├── requirements.txt           # UPDATED: Added moviepy
│   ├── README.md                  # UPDATED: Full documentation
│   ├── run_example.sh            # Existing helper script
│   ├── input/                     # Media files go here
│   │   ├── .gitkeep              # NEW: Git tracks directory
│   │   └── README.md             # UPDATED: Added video info
│   └── done/                      # NEW: Processed files moved here
│       └── .gitkeep              # NEW: Git tracks directory
└── BepInEx/plugins/BikininjasPosters/
    ├── posters/
    └── tips/
```

## What You Need to Do

### 1. Create Virtual Environment (Recommended)
```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 2. Install Updated Dependencies
```bash
pip install -r requirements.txt
```

### 3. Usage Examples

#### Process images and videos interactively:
```bash
# Activate venv first
source venv/bin/activate

# Run script
python poster_resizer.py
```

#### Auto-assign files:
```bash
python poster_resizer.py --auto
```

### 4. Workflow
1. Activate virtual environment: `source venv/bin/activate`
2. Add images/videos to `input/` directory
3. Run the script: `python poster_resizer.py`
4. Assign files to poster slots
5. Check output in `BepInEx/plugins/BikininjasPosters/`
6. Original files automatically moved to `done/`
7. Deactivate when done: `deactivate`

## Key Benefits

1. ✅ **Video support** - Poster2 can now be a real animated poster
2. ✅ **Clean workflow** - Processed files moved automatically
3. ✅ **Git-friendly** - Media files won't bloat your repository
4. ✅ **Format flexibility** - Any video format → MP4 automatically
5. ✅ **No manual cleanup** - Script manages file organization
6. ✅ **Portable** - Auto-detects directory structure, no hardcoded paths

## Testing the Script

To test without installing dependencies:
```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
python poster_resizer.py --help
```

To see if moviepy is available (with venv activated):
```bash
source venv/bin/activate
python -c "import moviepy; print('moviepy OK')"
```

If moviepy is not installed:
```bash
source venv/bin/activate
pip install moviepy
```

## Notes

- **Poster2 is special**: It's the only video slot, perfect for animated content
- **Video processing takes time**: Be patient, especially with longer videos
- **Done directory**: Review processed files before deleting
- **Git ignore**: Prevents accidental commits of large media files and virtual environments
- **Type mismatches**: Script handles them gracefully with warnings
- **Virtual environment**: Keeps dependencies isolated from system Python