#!/usr/bin/env python3
"""
Multi-Pack Generator for CustomPosters

Automatically creates multiple numbered packs (BikininjasPosters01, 02, etc.)
Each pack contains exactly 5 posters + 1 tip.
"""

import argparse
from pathlib import Path
import sys

from ratio_matcher import find_matching_images, match_images_to_slots
from image_processor import process_all_assignments
from pack_generator import (
    create_pack_structure,
    cleanup_processed_files,
    generate_pack_info,
)


def get_next_pack_number(output_dir: Path, base_name: str) -> int:
    """
    Find the next available pack number.

    Args:
        output_dir: Directory where packs are stored
        base_name: Base name (e.g., 'BikininjasPosters')

    Returns:
        Next pack number (1, 2, 3, etc.)
    """
    if not output_dir.exists():
        return 1

    existing_packs = list(output_dir.glob(f"{base_name}[0-9][0-9]"))
    if not existing_packs:
        return 1

    # Extract numbers from existing packs
    numbers = []
    for pack in existing_packs:
        try:
            num_str = pack.name.replace(base_name, "")
            numbers.append(int(num_str))
        except ValueError:
            continue

    return max(numbers) + 1 if numbers else 1


def process_single_pack(
    input_dir: Path,
    output_dir: Path,
    pack_name: str,
    maintain_aspect: bool,
    cleanup: bool,
) -> int:
    """
    Process a single pack of 6 files (5 posters + 1 tip).

    Args:
        input_dir: Directory with source files
        output_dir: Directory for output packs
        pack_name: Name of the pack (e.g., 'BikininjasPosters01')
        maintain_aspect: Whether to maintain aspect ratio
        cleanup: Whether to move files to done/

    Returns:
        Number of files processed (should be 6 if successful)
    """
    print(f"\n{'=' * 70}")
    print(f"📦 PROCESSING PACK: {pack_name}")
    print(f"{'=' * 70}\n")

    # Find available files
    print("🔍 Scanning for files...")
    available_files = find_matching_images(input_dir)

    if not available_files:
        print("❌ No files found in input directory")
        return 0

    # We need exactly 6 slots (5 posters + 1 tip)
    if len(available_files) < 6:
        print(f"⚠️  Only {len(available_files)} file(s) found")
        print(f"   Need at least 6 files for a complete pack")
        return 0

    print(f"✓ Found {len(available_files)} file(s)")

    # Match files to slots
    print("\n🎯 Matching files to poster slots...")
    assignments = match_images_to_slots(available_files)

    if not assignments:
        print("❌ No valid assignments found")
        return 0

    # Create pack structure
    print(f"\n📦 Creating pack: {pack_name}")
    pack_dir = create_pack_structure(pack_name, output_dir)
    print(f"✓ Pack directory: {pack_dir}")

    # Process all assignments
    success_count = process_all_assignments(assignments, pack_dir, maintain_aspect)

    if success_count == 0:
        print("\n❌ No files processed")
        return 0

    # Generate pack info
    generate_pack_info(pack_dir, assignments)

    # Clean up processed files
    if cleanup:
        done_dir = input_dir.parent / "done"
        cleanup_processed_files(assignments, done_dir)

    return success_count


def main():
    parser = argparse.ArgumentParser(
        description="Generate multiple CustomPosters packs automatically"
    )
    parser.add_argument("--input", type=str, default="input", help="Input directory")
    parser.add_argument(
        "--output",
        type=str,
        default="../BepInEx/plugins",
        help="Output directory for packs",
    )
    parser.add_argument(
        "--base-name",
        type=str,
        default="BikininjasPosters",
        help="Base name for packs (e.g., BikininjasPosters)",
    )
    parser.add_argument(
        "--no-aspect",
        action="store_true",
        help="Disable aspect ratio maintenance (stretch to fit)",
    )
    parser.add_argument(
        "--no-cleanup", action="store_true", help="Keep processed files in input/"
    )
    parser.add_argument(
        "--max-packs",
        type=int,
        default=None,
        help="Maximum number of packs to generate (default: unlimited)",
    )

    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent  # Go up to image_resizer/ from src/
    input_dir = project_dir / args.input
    output_dir = Path(args.output).resolve()

    # Print header
    print("\n" + "=" * 70)
    print("🖼️  CUSTOMPOSTERS MULTI-PACK GENERATOR")
    print("=" * 70)
    print("Automatically creates numbered packs with 5 posters + 1 tip each")
    print("=" * 70 + "\n")

    # Validate input
    if not input_dir.exists():
        print(f"❌ Input directory not found: {input_dir}")
        print(f"   Creating directory...")
        input_dir.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ Created: {input_dir}")
        print(f"\n💡 Add your images/videos to {input_dir} and run again")
        return 1

    # Configuration
    print("⚙️  Configuration:")
    print(f"   Input:  {input_dir}")
    print(f"   Output: {output_dir}")
    print(f"   Base:   {args.base_name}")
    print(f"   Aspect: {'Maintained' if not args.no_aspect else 'Disabled'}")
    print(f"   Max:    {args.max_packs if args.max_packs else 'Unlimited'}\n")

    # Get starting pack number
    pack_number = get_next_pack_number(output_dir, args.base_name)
    print(f"🔢 Starting at: {args.base_name}{pack_number:02d}\n")

    # Process packs until we run out of files
    packs_created = 0
    total_files_processed = 0

    while True:
        # Check if we've hit max packs limit
        if args.max_packs and packs_created >= args.max_packs:
            print(f"\n✓ Reached maximum pack limit: {args.max_packs}")
            break

        # Generate pack name
        pack_name = f"{args.base_name}{pack_number:02d}"

        # Process pack
        files_processed = process_single_pack(
            input_dir,
            output_dir,
            pack_name,
            maintain_aspect=not args.no_aspect,
            cleanup=not args.no_cleanup,
        )

        # Check if we processed a full pack
        if files_processed == 6:
            packs_created += 1
            total_files_processed += files_processed
            pack_number += 1

            print(f"\n{'=' * 70}")
            print(f"✅ PACK COMPLETE: {pack_name}")
            print(f"{'=' * 70}\n")
        else:
            # Not enough files for another pack
            if files_processed > 0:
                print(f"\n⚠️  Only {files_processed} file(s) remaining")
                print("   Need 6 files for a complete pack")
            break

    # Final summary
    print("\n" + "=" * 70)
    print("🎉 MULTI-PACK GENERATION COMPLETE!")
    print("=" * 70 + "\n")

    if packs_created > 0:
        print(f"✓ Packs created: {packs_created}")
        print(f"✓ Files processed: {total_files_processed}")
        print(f"✓ Location: {output_dir}\n")

        # List created packs
        print("📦 Created packs:")
        start_num = pack_number - packs_created
        for i in range(packs_created):
            pack_name = f"{args.base_name}{start_num + i:02d}"
            print(f"   • {pack_name}")

        print(f"\n📋 Next steps:")
        print(f"   1. Review packs in: {output_dir}")
        print(f"   2. Copy pack folders to:")
        print(f"      Lethal Company/BepInEx/plugins/\n")
    else:
        print("❌ No packs created")
        print("   Add more files to input/ directory\n")

    print("=" * 70 + "\n")

    return 0 if packs_created > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
