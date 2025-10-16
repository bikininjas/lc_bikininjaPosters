"""
Generate complete poster pack structures.
"""

from pathlib import Path
from typing import Dict, List
import shutil


def create_pack_structure(pack_name: str, base_dir: Path) -> Path:
    """
    Create a complete pack directory structure.
    Cleans existing pack directory to avoid duplicates.

    Args:
        pack_name: Name of the pack (e.g., 'BikininjasPosters')
        base_dir: Base directory where pack will be created

    Returns:
        Path to the created pack directory
    """
    pack_dir = base_dir / pack_name
    posters_dir = pack_dir / "posters"
    tips_dir = pack_dir / "tips"

    # Clean existing pack directory to avoid duplicates
    if pack_dir.exists():
        print(f"   Cleaning existing pack directory...")
        for file in posters_dir.glob("*"):
            if file.is_file() and file.name != ".placeholder":
                file.unlink()
        for file in tips_dir.glob("*"):
            if file.is_file() and file.name != ".placeholder":
                file.unlink()

    posters_dir.mkdir(parents=True, exist_ok=True)
    tips_dir.mkdir(parents=True, exist_ok=True)

    return pack_dir


def move_to_done(source_path: Path, done_dir: Path) -> bool:
    """
    Move a processed file to the done directory.

    Args:
        source_path: Path to source file
        done_dir: Path to done directory

    Returns:
        True if successful, False otherwise
    """
    try:
        done_dir.mkdir(parents=True, exist_ok=True)
        destination = done_dir / source_path.name

        # Handle duplicates
        counter = 1
        while destination.exists():
            stem = source_path.stem
            suffix = source_path.suffix
            destination = done_dir / f"{stem}_{counter}{suffix}"
            counter += 1

        shutil.move(str(source_path), str(destination))
        return True

    except Exception as e:
        print(f"⚠️  Could not move {source_path.name} to done: {e}")
        return False


def cleanup_processed_files(assignments: Dict[str, Path], done_dir: Path):
    """
    Move all processed files to done directory.

    Args:
        assignments: Dictionary mapping slot names to image paths
        done_dir: Path to done directory
    """
    if not assignments:
        return

    print("\n" + "=" * 70)
    print("🧹 CLEANING UP")
    print("=" * 70 + "\n")

    moved_count = 0
    for slot_name, image_path in assignments.items():
        if image_path.exists():
            if move_to_done(image_path, done_dir):
                print(f"✓ Moved to done: {image_path.name}")
                moved_count += 1

    print(f"\n✓ Moved {moved_count} files to done directory")
    print("=" * 70)


def generate_pack_info(pack_dir: Path, assignments: Dict[str, Path]):
    """
    Generate a text file with pack information.

    Args:
        pack_dir: Path to pack directory
        assignments: Dictionary mapping slot names to image paths
    """
    info_file = pack_dir / "pack_info.txt"

    with open(info_file, "w") as f:
        f.write(f"Poster Pack: {pack_dir.name}\n")
        f.write("=" * 50 + "\n\n")
        f.write("Contents:\n")
        for slot_name in [
            "Poster1",
            "Poster2",
            "Poster3",
            "Poster4",
            "Poster5",
            "CustomTips",
        ]:
            if slot_name in assignments:
                f.write(f"  {slot_name}: {assignments[slot_name].name}\n")
            else:
                f.write(f"  {slot_name}: (empty)\n")
        f.write("\n")
        f.write("Installation:\n")
        f.write(f"  Copy the '{pack_dir.name}' folder to:\n")
        f.write("  Lethal Company/BepInEx/plugins/\n")

    print(f"\n📄 Pack info saved: {info_file}")
