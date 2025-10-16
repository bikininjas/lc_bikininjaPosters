"""
Matches input images and videos to poster slots based on aspect ratio similarity.
"""

from pathlib import Path
from PIL import Image
from typing import Dict, List, Tuple, Optional
from config import (
    POSTER_SPECS,
    SUPPORTED_FORMATS,
    TARGET_RATIOS,
    SUPPORTED_VIDEO_FORMATS,
)


def get_media_ratio(media_path: Path) -> Optional[float]:
    """
    Calculate the aspect ratio of an image or video.

    Args:
        media_path: Path to the media file

    Returns:
        Aspect ratio (width/height) or None if error
    """
    # Check if it's a video
    if media_path.suffix.lower() in SUPPORTED_VIDEO_FORMATS:
        try:
            from moviepy import VideoFileClip

            with VideoFileClip(str(media_path)) as video:
                width, height = video.size
                return width / height if height > 0 else None
        except ImportError:
            print(f"⚠️  moviepy required for video: {media_path.name}")
            return None
        except Exception as e:
            print(f"⚠️  Error reading video {media_path.name}: {e}")
            return None
    else:
        # It's an image
        try:
            with Image.open(media_path) as img:
                width, height = img.size
                return width / height if height > 0 else None
        except Exception as e:
            print(f"⚠️  Error reading {media_path.name}: {e}")
            return None


def find_matching_images(input_dir: Path) -> List[Tuple[Path, float]]:
    """
    Find all valid images and videos in input directory and calculate their ratios.

    Args:
        input_dir: Path to input directory

    Returns:
        List of (media_path, aspect_ratio) tuples
    """
    media_with_ratios = []

    for file_path in sorted(input_dir.iterdir()):
        if file_path.suffix.lower() in SUPPORTED_FORMATS:
            ratio = get_media_ratio(file_path)
            if ratio is not None:
                media_with_ratios.append((file_path, ratio))

    return media_with_ratios


def calculate_ratio_difference(image_ratio: float, target_ratio: float) -> float:
    """
    Calculate how different two aspect ratios are.

    Args:
        image_ratio: The image's aspect ratio
        target_ratio: The target poster slot's aspect ratio

    Returns:
        Difference score (lower is better)
    """
    return abs(image_ratio - target_ratio)


def match_images_to_slots(images: List[Tuple[Path, float]]) -> Dict[str, Path]:
    """
    Match images to poster slots using optimal assignment.
    Each slot gets the best-fitting image based on aspect ratio.

    Args:
        images: List of (image_path, aspect_ratio) tuples

    Returns:
        Dictionary mapping slot names to image paths
    """
    if not images:
        return {}

    # Create a copy of available images
    available_images = images.copy()
    slot_assignments = {}

    # Sort slots by specificity (most specific ratio first)
    # Portrait ratios (< 1.0) are more specific, so prioritize them
    slots_by_priority = sorted(
        TARGET_RATIOS.items(),
        key=lambda x: (abs(x[1] - 1.0), x[1]),  # Prioritize ratios furthest from 1:1
    )

    # Greedy assignment: for each slot, find the best available image
    for slot_name, target_ratio in slots_by_priority:
        if not available_images:
            break

        # Find the image with the closest aspect ratio
        best_match = min(
            available_images,
            key=lambda img: calculate_ratio_difference(img[1], target_ratio),
        )

        slot_assignments[slot_name] = best_match[0]
        available_images.remove(best_match)

    return slot_assignments


def display_matching_report(
    assignments: Dict[str, Path], images: List[Tuple[Path, float]]
):
    """
    Display a report of how images were matched to slots.

    Args:
        assignments: Dictionary mapping slot names to image paths
        images: Original list of images with ratios
    """
    print("\n" + "=" * 70)
    print("📊 IMAGE-TO-SLOT MATCHING REPORT")
    print("=" * 70)

    if not assignments:
        print("❌ No images could be matched to slots")
        return

    # Create a map of image paths to ratios
    image_ratios = {path: ratio for path, ratio in images}

    print(f"\n✓ Matched {len(assignments)} of 6 possible slots\n")

    for slot_name in [
        "Poster1",
        "Poster2",
        "Poster3",
        "Poster4",
        "Poster5",
        "CustomTips",
    ]:
        specs = POSTER_SPECS[slot_name]
        target_ratio = TARGET_RATIOS[slot_name]

        if slot_name in assignments:
            image_path = assignments[slot_name]
            image_ratio = image_ratios[image_path]
            difference = calculate_ratio_difference(image_ratio, target_ratio)
            fit_quality = (
                "Perfect"
                if difference < 0.01
                else (
                    "Excellent"
                    if difference < 0.05
                    else "Good" if difference < 0.1 else "Fair"
                )
            )

            print(
                f"✓ {slot_name:12} ({specs['width']}×{specs['height']}) → {image_path.name}"
            )
            print(
                f"   Target ratio: {target_ratio:.3f} | Image ratio: {image_ratio:.3f} | Fit: {fit_quality}"
            )
        else:
            print(
                f"✗ {slot_name:12} ({specs['width']}×{specs['height']}) → No match found"
            )
        print()

    # Show unmatched images
    matched_paths = set(assignments.values())
    unmatched = [path for path, _ in images if path not in matched_paths]

    if unmatched:
        print(f"📦 Unmatched images ({len(unmatched)}):")
        for path in unmatched:
            ratio = image_ratios[path]
            print(f"   • {path.name} (ratio: {ratio:.3f})")
        print("\n💡 Tip: These images can be used for additional packs")

    print("=" * 70)
