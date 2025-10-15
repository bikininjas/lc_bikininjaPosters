#!/usr/bin/env python3
"""
Poster Resizer for CustomPosters Mod (Lethal Company)

This script resizes images/videos from an 'input' folder to match the CustomPosters mod requirements
and saves them with the correct filenames and formats in the appropriate output folders.
Processed files are moved to a 'done' directory.

Requirements:
- Pillow library for image processing
- moviepy library for video processing (pip install moviepy)
- Input images/videos in 'input' subfolder
- Target folder structure matching BikininjasPosters mod

Poster Specifications:
- Poster1: 639x488 pixels -> Poster1.png
- Poster2: 730x490 pixels -> Poster2.mp4 (video support!)
- Poster3: 749x1054 pixels -> Poster3.bmp
- Poster4: 729x999 pixels -> Poster4.jpeg
- Poster5: 552x769 pixels -> Poster5.png
- CustomTips: 860x1219 pixels -> CustomTips.jpg

Usage:
    python poster_resizer.py
"""

import os
import sys
import shutil
from pathlib import Path
from PIL import Image, ImageOps
import argparse


class PosterResizer:
    """Handles resizing and formatting of poster images/videos for CustomPosters mod."""
    
    # Poster specifications: (width, height, output_format, output_filename, is_video)
    POSTER_SPECS = {
        'poster1': (639, 488, 'PNG', 'Poster1.png', False),
        'poster2': (730, 490, 'MP4', 'Poster2.mp4', True),  # Video support!
        'poster3': (749, 1054, 'BMP', 'Poster3.bmp', False),
        'poster4': (729, 999, 'JPEG', 'Poster4.jpeg', False),
        'poster5': (552, 769, 'PNG', 'Poster5.png', False),
        'customtips': (860, 1219, 'JPEG', 'CustomTips.jpg', False),
    }
    
    def __init__(self, input_dir="input", target_base_dir=None):
        """
        Initialize the poster resizer.
        
        Args:
            input_dir (str): Directory containing source images/videos
            target_base_dir (str): Base directory for BikininjasPosters (optional)
        """
        self.script_dir = Path(__file__).parent
        self.input_dir = self.script_dir / input_dir
        self.done_dir = self.script_dir / "done"
        
        if target_base_dir:
            self.target_base_dir = Path(target_base_dir)
        else:
            # Auto-detect: go up one level from script dir to find BepInEx
            parent_dir = self.script_dir.parent
            self.target_base_dir = parent_dir / "BepInEx" / "plugins" / "BikininjasPosters"
        
        self.posters_dir = self.target_base_dir / "posters"
        self.tips_dir = self.target_base_dir / "tips"
        self.processed_files = []  # Track successfully processed files
        
    def create_output_dirs(self):
        """Create output directories if they don't exist."""
        self.posters_dir.mkdir(parents=True, exist_ok=True)
        self.tips_dir.mkdir(parents=True, exist_ok=True)
        self.done_dir.mkdir(parents=True, exist_ok=True)
        print(f"✓ Created/verified directories:")
        print(f"  - {self.posters_dir}")
        print(f"  - {self.tips_dir}")
        print(f"  - {self.done_dir}")
        
    def resize_image(self, input_path, target_width, target_height, maintain_aspect=True):
        """
        Resize an image to target dimensions.
        
        Args:
            input_path (Path): Path to input image
            target_width (int): Target width in pixels
            target_height (int): Target height in pixels
            maintain_aspect (bool): Whether to maintain aspect ratio
            
        Returns:
            PIL.Image: Resized image
        """
        try:
            with Image.open(input_path) as img:
                # Convert to RGB if necessary (handles RGBA, P mode, etc.)
                if img.mode in ('RGBA', 'LA'):
                    # Create white background for transparent images
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'RGBA':
                        background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                    else:
                        background.paste(img, mask=img.split()[-1])
                    img = background
                elif img.mode != 'RGB':
                    img = img.convert('RGB')
                
                if maintain_aspect:
                    # Resize maintaining aspect ratio, then crop/pad to exact dimensions
                    img.thumbnail((target_width, target_height), Image.Resampling.LANCZOS)
                    
                    # Create new image with target dimensions and paste resized image centered
                    new_img = Image.new('RGB', (target_width, target_height), (255, 255, 255))
                    paste_x = (target_width - img.width) // 2
                    paste_y = (target_height - img.height) // 2
                    new_img.paste(img, (paste_x, paste_y))
                    return new_img
                else:
                    # Direct resize (may distort aspect ratio)
                    return img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    
        except Exception as e:
            print(f"✗ Error processing {input_path}: {e}")
            return None
    
    def resize_video(self, input_path, target_width, target_height, maintain_aspect=True):
        """
        Resize a video to target dimensions and convert to MP4.
        
        Args:
            input_path (Path): Path to input video
            target_width (int): Target width in pixels
            target_height (int): Target height in pixels
            maintain_aspect (bool): Whether to maintain aspect ratio
            
        Returns:
            str: Path to temporary processed video file, or None on error
        """
        try:
            from moviepy.editor import VideoFileClip
            
            print(f"  Loading video (this may take a moment)...")
            with VideoFileClip(str(input_path)) as video:
                # Get original dimensions
                orig_width, orig_height = video.size
                
                if maintain_aspect:
                    # Calculate scaling to fit within target dimensions
                    scale_w = target_width / orig_width
                    scale_h = target_height / orig_height
                    scale = min(scale_w, scale_h)
                    
                    new_width = int(orig_width * scale)
                    new_height = int(orig_height * scale)
                    
                    # Resize video
                    resized = video.resize((new_width, new_height))
                    
                    # If dimensions don't match exactly, we'll pad with black bars
                    # Note: moviepy's margin() could be used but resize is simpler for now
                    if new_width != target_width or new_height != target_height:
                        print(f"  ⚠️  Video will be {new_width}x{new_height} (aspect ratio preserved)")
                        print(f"      Target was {target_width}x{target_height}")
                else:
                    # Direct resize (may distort)
                    resized = video.resize((target_width, target_height))
                
                # Create temporary output file
                temp_output = self.script_dir / f"temp_{input_path.stem}.mp4"
                
                print(f"  Encoding video to MP4...")
                resized.write_videofile(
                    str(temp_output),
                    codec='libx264',
                    audio_codec='aac',
                    temp_audiofile=str(self.script_dir / 'temp-audio.m4a'),
                    remove_temp=True,
                    logger=None  # Suppress moviepy progress bars
                )
                
                return str(temp_output)
                
        except ImportError:
            print(f"✗ moviepy library not found. Install with: pip install moviepy")
            print(f"  Video processing is required for Poster2.mp4")
            return None
        except Exception as e:
            print(f"✗ Error processing video {input_path}: {e}")
            return None
    
    def find_input_files(self):
        """
        Find all supported media files in the input directory.
        
        Returns:
            tuple: (image_files, video_files) as lists of Path objects
        """
        if not self.input_dir.exists():
            print(f"✗ Input directory not found: {self.input_dir}")
            print(f"  Please create the directory and add your media files.")
            return [], []
        
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp'}
        video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', '.mpeg', '.mpg'}
        
        images = []
        videos = []
        
        for file_path in self.input_dir.iterdir():
            if file_path.is_file():
                ext = file_path.suffix.lower()
                if ext in image_extensions:
                    images.append(file_path)
                elif ext in video_extensions:
                    videos.append(file_path)
        
        return sorted(images), sorted(videos)
    
    def move_to_done(self, file_path):
        """
        Move a successfully processed file to the done directory.
        
        Args:
            file_path (Path): Path to the file to move
        """
        try:
            dest_path = self.done_dir / file_path.name
            # If file already exists in done, add a number suffix
            if dest_path.exists():
                counter = 1
                while dest_path.exists():
                    dest_path = self.done_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
                    counter += 1
            
            shutil.move(str(file_path), str(dest_path))
            print(f"  ↳ Moved to done: {dest_path.name}")
            return True
        except Exception as e:
            print(f"  ⚠️  Could not move to done: {e}")
            return False
    
    def process_images(self, maintain_aspect=True, interactive=True):
        """
        Process all media files in the input directory.
        
        Args:
            maintain_aspect (bool): Whether to maintain aspect ratio
            interactive (bool): Whether to ask for user confirmation for each file
        """
        input_images, input_videos = self.find_input_files()
        all_files = input_images + input_videos
        
        if not all_files:
            print(f"✗ No supported media files found in {self.input_dir}")
            print(f"  Image formats: .jpg, .jpeg, .png, .bmp, .gif, .tiff, .webp")
            print(f"  Video formats: .mp4, .avi, .mov, .mkv, .flv, .wmv, .webm, .m4v")
            return
        
        print(f"\nFound {len(all_files)} file(s) in {self.input_dir}:")
        print(f"  - {len(input_images)} image(s)")
        print(f"  - {len(input_videos)} video(s)")
        for f in all_files:
            file_type = "🎬" if f in input_videos else "🖼️"
            print(f"  {file_type} {f.name}")
        
        print(f"\nAvailable poster slots:")
        for key, (width, height, fmt, filename, is_video) in self.POSTER_SPECS.items():
            output_dir = self.tips_dir if key == 'customtips' else self.posters_dir
            media_type = "VIDEO" if is_video else "IMAGE"
            print(f"  {key} ({media_type}): {width}x{height} -> {output_dir}/{filename}")
        
        processed_count = 0
        
        for file_path in all_files:
            is_video_file = file_path in input_videos
            print(f"\n{'='*60}")
            print(f"Processing: {file_path.name} ({'VIDEO' if is_video_file else 'IMAGE'})")
            print(f"{'='*60}")
            
            if interactive:
                print("Which poster slot should this file fill?")
                print("Options:", ", ".join(self.POSTER_SPECS.keys()))
                print("Enter 'skip' to skip this file, 'quit' to exit")
                
                choice = input("Your choice: ").strip().lower()
                
                if choice == 'quit':
                    break
                elif choice == 'skip':
                    continue
                elif choice not in self.POSTER_SPECS:
                    print(f"✗ Invalid choice: {choice}")
                    continue
            else:
                # Auto-assign based on order
                poster_keys = list(self.POSTER_SPECS.keys())
                if processed_count >= len(poster_keys):
                    print(f"✗ More files than poster slots available. Skipping {file_path.name}")
                    continue
                choice = poster_keys[processed_count]
                print(f"Auto-assigning to: {choice}")
            
            # Get poster specifications
            width, height, output_format, output_filename, is_video_slot = self.POSTER_SPECS[choice]
            output_dir = self.tips_dir if choice == 'customtips' else self.posters_dir
            output_path = output_dir / output_filename
            
            # Warn if type mismatch
            if is_video_file and not is_video_slot:
                print(f"⚠️  Warning: Assigning video to image slot. Will extract first frame.")
            elif not is_video_file and is_video_slot:
                print(f"⚠️  Warning: Assigning image to video slot (Poster2).")
            
            success = False
            
            # Process based on file type and target slot
            if is_video_slot and is_video_file:
                # Video to video slot
                print(f"Processing video to {width}x{height}...")
                temp_video = self.resize_video(file_path, width, height, maintain_aspect)
                
                if temp_video:
                    try:
                        shutil.copy(temp_video, output_path)
                        os.remove(temp_video)  # Clean up temp file
                        print(f"✓ Saved: {output_path}")
                        success = True
                    except Exception as e:
                        print(f"✗ Error saving {output_path}: {e}")
                        if os.path.exists(temp_video):
                            os.remove(temp_video)
            
            elif is_video_file and not is_video_slot:
                # Video to image slot - extract first frame
                print(f"Extracting first frame from video...")
                try:
                    from moviepy.editor import VideoFileClip
                    with VideoFileClip(str(file_path)) as video:
                        # Get frame at 1 second (or 0 if video is shorter)
                        frame_time = min(1.0, video.duration / 2)
                        frame = video.get_frame(frame_time)
                        
                        # Convert to PIL Image
                        from PIL import Image as PILImage
                        img = PILImage.fromarray(frame)
                        
                        # Now resize as normal image
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        
                        if maintain_aspect:
                            img.thumbnail((width, height), PILImage.Resampling.LANCZOS)
                            new_img = PILImage.new('RGB', (width, height), (255, 255, 255))
                            paste_x = (width - img.width) // 2
                            paste_y = (height - img.height) // 2
                            new_img.paste(img, (paste_x, paste_y))
                            img = new_img
                        else:
                            img = img.resize((width, height), PILImage.Resampling.LANCZOS)
                        
                        # Save
                        save_kwargs = {}
                        if output_format == 'JPEG':
                            save_kwargs['quality'] = 95
                            save_kwargs['optimize'] = True
                        
                        img.save(output_path, format=output_format, **save_kwargs)
                        print(f"✓ Saved: {output_path}")
                        success = True
                        
                except ImportError:
                    print(f"✗ moviepy library required for video frame extraction")
                except Exception as e:
                    print(f"✗ Error extracting frame: {e}")
            
            else:
                # Image processing (either to image slot or video slot)
                print(f"Resizing to {width}x{height}...")
                resized_img = self.resize_image(file_path, width, height, maintain_aspect)
                
                if resized_img:
                    try:
                        # For video slot (Poster2), save as PNG then note conversion needed
                        if is_video_slot:
                            # Save as PNG temporarily
                            temp_png = output_dir / f"{Path(output_filename).stem}.png"
                            resized_img.save(temp_png, format='PNG')
                            print(f"✓ Saved as PNG: {temp_png}")
                            print(f"  ⚠️  Note: You assigned an image to Poster2 (video slot).")
                            print(f"      The mod works best with .mp4 videos for Poster2.")
                            print(f"      Consider converting this to video or using a video file.")
                            success = True
                        else:
                            # Normal image save
                            save_kwargs = {}
                            if output_format == 'JPEG':
                                save_kwargs['quality'] = 95
                                save_kwargs['optimize'] = True
                            
                            resized_img.save(output_path, format=output_format, **save_kwargs)
                            print(f"✓ Saved: {output_path}")
                            success = True
                            
                    except Exception as e:
                        print(f"✗ Error saving {output_path}: {e}")
            
            # Move to done if successful
            if success:
                if self.move_to_done(file_path):
                    processed_count += 1
                    self.processed_files.append(file_path.name)
        
        print(f"\n{'='*60}")
        print(f"🎉 Processing complete! Processed {processed_count} file(s).")
        print(f"{'='*60}")
        
        if processed_count > 0:
            print(f"\nProcessed files (moved to done/):")
            for filename in self.processed_files:
                print(f"  ✓ {filename}")
            
            print(f"\nNext steps:")
            print(f"1. Check the output files in:")
            print(f"   - {self.posters_dir}")
            print(f"   - {self.tips_dir}")
            print(f"2. Copy the entire BikininjasPosters folder to your Lethal Company mod directory")
            print(f"3. Processed source files are in: {self.done_dir}")



def main():
    """Main function with command line argument parsing."""
    parser = argparse.ArgumentParser(
        description="Resize images for CustomPosters mod in Lethal Company",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python poster_resizer.py                          # Interactive mode with default paths
  python poster_resizer.py --auto                   # Auto-assign images to poster slots
  python poster_resizer.py --input my_images        # Use custom input directory
  python poster_resizer.py --target /path/to/mod    # Use custom target directory
  python poster_resizer.py --no-aspect              # Don't maintain aspect ratio
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        default='input',
        help='Input directory containing images (default: input)'
    )
    
    parser.add_argument(
        '--target', '-t',
        help='Target base directory for BikininjasPosters mod (default: auto-detect from workspace)'
    )
    
    parser.add_argument(
        '--auto', '-a',
        action='store_true',
        help='Auto-assign images to poster slots instead of interactive mode'
    )
    
    parser.add_argument(
        '--no-aspect',
        action='store_true',
        help='Don\'t maintain aspect ratio (may distort images)'
    )
    
    args = parser.parse_args()
    
    # Initialize resizer
    resizer = PosterResizer(
        input_dir=args.input,
        target_base_dir=args.target
    )
    
    print("🖼️  CustomPosters Media Resizer")
    print("=" * 40)
    print(f"Input directory: {resizer.input_dir}")
    print(f"Done directory: {resizer.done_dir}")
    print(f"Output base: {resizer.target_base_dir}")
    print(f"Mode: {'Auto-assign' if args.auto else 'Interactive'}")
    print(f"Aspect ratio: {'Maintained' if not args.no_aspect else 'Ignored'}")
    
    # Create output directories
    resizer.create_output_dirs()
    
    # Process images
    resizer.process_images(
        maintain_aspect=not args.no_aspect,
        interactive=not args.auto
    )


if __name__ == "__main__":
    main()