# Input Directory

Place your **images and videos** here for processing!

## Supported Formats

**Images**: `.jpg` `.jpeg` `.png` `.bmp` `.gif` `.tiff` `.webp` `.avif`  
**Videos**: `.mp4` `.avi` `.mov` `.mkv` `.flv` `.wmv` `.webm` `.m4v`

All video formats are automatically converted to MP4!

## How It Works

Each file you add will be:
1. **Resized** to appropriate dimensions (cycling through 5 standard sizes)
2. **Saved to 3 locations** with the same name:
   - `posters/` - for in-game wall decorations
   - `tips/` - for in-game loading screens  
   - `output/` - for additional processing
3. **Moved to done/** after successful processing

## Example

```
Input:
  input/cat.jpg
  input/dog.png
  input/video.mp4

Output (9 files total):
  posters/Poster1.png, Poster2.jpg, Poster3.mp4
  tips/Poster1.png, Poster2.jpg, Poster3.mp4
  output/Poster1.png, Poster2.jpg, Poster3.mp4
  
Cleanup:
  done/cat.jpg, done/dog.png, done/video.mp4
```

## Usage

```bash
# Activate virtual environment
cd ..
source venv/bin/activate

# Run the script (fully automatic)
python poster_resizer.py

# Deactivate when done
deactivate
```

## Git Note
Media files in this directory are ignored by git. Only the directory structure is tracked.