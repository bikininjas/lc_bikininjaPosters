# Input Directory

Place your **images and videos** here for processing!

## Supported Image Formats
- .jpg, .jpeg
- .png  
- .bmp
- .gif
- .tiff
- .webp

## Supported Video Formats (NEW! 🎬)
- .mp4
- .avi
- .mov
- .mkv
- .flv
- .wmv
- .webm
- .m4v
- .mpeg, .mpg

**All video formats are automatically converted to MP4!**

The script will resize them to the CustomPosters mod specifications and output them with the correct filenames and formats.

## Example Files You Might Add
- landscape_poster.jpg
- cool_animation.mp4 (for Poster2 - it supports video!)
- portrait_artwork.png
- custom_tip_image.jpeg
- intro_video.avi

## After Processing
Successfully processed files will be **automatically moved** to the `done/` directory.

## Usage
After adding your media files, run:
```bash
cd ..
python poster_resizer.py
```

Or use the example script:
```bash
cd ..
./run_example.sh
```

## Git Ignore
Media files in this directory are ignored by git (won't be committed to the repository).
Only the directory structure is tracked.