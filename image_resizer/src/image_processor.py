"""
Image and video processing and resizing functionality.
"""

from pathlib import Path
from PIL import Image
from typing import Dict, Optional
import os
import tempfile
from config import POSTER_SPECS, SUPPORTED_VIDEO_FORMATS


def resize_image(
    image_path: Path,
    target_width: int,
    target_height: int,
    maintain_aspect: bool = True,
) -> Image.Image:
    """
    Resize an image to target dimensions.

    Args:
        image_path: Path to source image
        target_width: Target width in pixels
        target_height: Target height in pixels
        maintain_aspect: Whether to maintain aspect ratio (crops to fit)

    Returns:
        Resized PIL Image object
    """
    with Image.open(image_path) as img:
        # Convert to RGB if needed (handles transparency, CMYK, etc.)
        if img.mode not in ("RGB", "L"):
            img = img.convert("RGB")

        if maintain_aspect:
            # Calculate target aspect ratio
            target_ratio = target_width / target_height
            img_ratio = img.width / img.height

            # Crop to match target aspect ratio, then resize
            if abs(img_ratio - target_ratio) > 0.01:  # If ratios don't match
                if img_ratio > target_ratio:
                    # Image is wider - crop width
                    new_width = int(img.height * target_ratio)
                    left = (img.width - new_width) // 2
                    img = img.crop((left, 0, left + new_width, img.height))
                else:
                    # Image is taller - crop height
                    new_height = int(img.width / target_ratio)
                    top = (img.height - new_height) // 2
                    img = img.crop((0, top, img.width, top + new_height))

            # Now resize to exact dimensions
            new_img = img.resize(
                (target_width, target_height), Image.Resampling.LANCZOS
            )

            return new_img
        else:
            # Stretch to exact dimensions
            return img.resize((target_width, target_height), Image.Resampling.LANCZOS)


def resize_video(
    video_path: Path,
    target_width: int,
    target_height: int,
    maintain_aspect: bool = True,
) -> Optional[str]:
    """
    Resize a video to target dimensions and convert to MP4.

    Args:
        video_path: Path to source video
        target_width: Target width in pixels
        target_height: Target height in pixels
        maintain_aspect: Whether to maintain aspect ratio

    Returns:
        Path to temporary output MP4 file, or None if error
    """
    try:
        from moviepy import VideoFileClip

        print(f"   Loading video: {video_path.name}")

        with VideoFileClip(str(video_path)) as video:
            # Calculate dimensions
            if maintain_aspect:
                # Calculate scale to fit within target dimensions
                scale = min(target_width / video.w, target_height / video.h)
                new_width = int(video.w * scale)
                new_height = int(video.h * scale)

                # Ensure even dimensions (required for H.264)
                new_width = new_width - (new_width % 2)
                new_height = new_height - (new_height % 2)

                # Resize video
                resized_video = video.resized((new_width, new_height))

                # Add padding if needed (black bars)
                if new_width != target_width or new_height != target_height:
                    from moviepy import ColorClip, CompositeVideoClip

                    # Create black background
                    background = ColorClip(
                        size=(target_width, target_height),
                        color=(0, 0, 0),
                        duration=resized_video.duration,
                    )

                    # Center the video
                    x_pos = (target_width - new_width) // 2
                    y_pos = (target_height - new_height) // 2

                    positioned_video = resized_video.with_position((x_pos, y_pos))
                    resized_video = CompositeVideoClip(
                        [background, positioned_video],
                        size=(target_width, target_height),
                    )
            else:
                # Ensure even dimensions
                target_width = target_width - (target_width % 2)
                target_height = target_height - (target_height % 2)
                resized_video = video.resized((target_width, target_height))

            # Create temporary output file
            temp_output = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False).name

            print(f"   Encoding video to MP4...")
            # Write video with H.264 codec
            resized_video.write_videofile(
                temp_output,
                codec="libx264",
                audio_codec="aac",
                fps=video.fps,
                logger=None,  # Suppress moviepy output
            )

            return temp_output

    except ImportError:
        print(f"   ✗ moviepy library not found. Install with: pip install moviepy")
        return None
    except Exception as e:
        print(f"   ✗ Error processing video: {e}")
        return None


def is_video_file(file_path: Path) -> bool:
    """Check if file is a video."""
    return file_path.suffix.lower() in SUPPORTED_VIDEO_FORMATS


def process_and_save_image(
    media_path: Path, slot_name: str, output_base: Path, maintain_aspect: bool = True
) -> bool:
    """
    Process an image or video and save it to the appropriate location.

    Args:
        media_path: Path to source image or video
        slot_name: Name of the poster slot (e.g., 'Poster1', 'CustomTips')
        output_base: Base output directory
        maintain_aspect: Whether to maintain aspect ratio

    Returns:
        True if successful, False otherwise
    """
    try:
        specs = POSTER_SPECS[slot_name]

        # Determine output path
        output_dir = output_base / specs["location"]
        output_dir.mkdir(parents=True, exist_ok=True)

        is_video = is_video_file(media_path)

        if is_video:
            # Videos always output as .mp4
            output_path = output_dir / f"{slot_name}.mp4"
            print(f"   Processing VIDEO: {media_path.name} → {slot_name}.mp4")

            temp_video = resize_video(
                media_path, specs["width"], specs["height"], maintain_aspect
            )

            if temp_video:
                # Move temp file to final location
                import shutil

                shutil.move(temp_video, str(output_path))
                print(f"   ✓ Saved: {output_path}")
                return True
            else:
                return False
        else:
            # Images output as PNG
            output_path = output_dir / f"{slot_name}{specs['extension']}"
            print(
                f"   Processing IMAGE: {media_path.name} → {slot_name}{specs['extension']}"
            )

            resized_img = resize_image(
                media_path, specs["width"], specs["height"], maintain_aspect
            )

            # Save with high quality
            save_kwargs = {"optimize": True}
            if specs["extension"] in [".jpg", ".jpeg"]:
                save_kwargs["quality"] = 95

            resized_img.save(output_path, **save_kwargs)
            print(f"   ✓ Saved: {output_path}")
            return True

    except Exception as e:
        print(f"   ✗ Error processing {slot_name}: {e}")
        return False


def process_all_assignments(
    assignments: Dict[str, Path], output_base: Path, maintain_aspect: bool = True
) -> int:
    """
    Process all image assignments and save to output directory.

    Args:
        assignments: Dictionary mapping slot names to image paths
        output_base: Base output directory
        maintain_aspect: Whether to maintain aspect ratio

    Returns:
        Number of successfully processed images
    """
    if not assignments:
        print("\n❌ No media to process")
        return 0

    print("\n" + "=" * 70)
    print("🖼️  PROCESSING IMAGES & VIDEOS")
    print("=" * 70 + "\n")

    success_count = 0

    for slot_name in [
        "Poster1",
        "Poster2",
        "Poster3",
        "Poster4",
        "Poster5",
        "CustomTips",
    ]:
        if slot_name in assignments:
            print(f"\n📌 {slot_name}:")
            if process_and_save_image(
                assignments[slot_name], slot_name, output_base, maintain_aspect
            ):
                success_count += 1

    print("\n" + "=" * 70)
    print(f"✓ Successfully processed {success_count} of {len(assignments)} files")
    print("=" * 70)

    return success_count
