#!/usr/bin/env python3
"""
CustomPosters Pack Generator

Matches images to poster slots based on aspect ratio.
"""

import argparse
from pathlib import Path
import sys

from ratio_matcher import (
    find_matching_images,
    match_images_to_slots,
    display_matching_report,
)
from image_processor import process_all_assignments
from pack_generator import (
    create_pack_structure,
    cleanup_processed_files,
    generate_pack_info,
)


def print_header():
    print("\n" + "=" * 70)
    print("🖼️  CUSTOMPOSTERS PACK GENERATOR")
    print("=" * 70)
    print("Intelligently matches images to poster slots based on aspect ratio")
    print("=" * 70 + "\n")


def validate_directories(input_dir, output_dir):
    if not input_dir.exists():
        print(f"❌ Input directory not found: {input_dir}")
        print(f"   Creating directory...")
        input_dir.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ Created: {input_dir}")
        print(f"\n💡 Add your images to {input_dir} and run again")
        return False

    if not output_dir.exists():
        print(f"📁 Output directory will be created: {output_dir}")

    return True


def main():
    parser = argparse.ArgumentParser(description="Generate CustomPosters pack")
    parser.add_argument("--input", type=str, default="input")
    parser.add_argument("--output", type=str, default="../BepInEx/plugins")
    parser.add_argument("--pack-name", type=str, default="BikininjasPosters")
    parser.add_argument("--no-aspect", action="store_true")
    parser.add_argument("--no-cleanup", action="store_true")

    args = parser.parse_args()

    script_dir = Path(__file__).parent
    input_dir = script_dir / args.input
    output_dir = Path(args.output)
    done_dir = script_dir / "done"
    maintain_aspect = not args.no_aspect

    print_header()

    print("⚙️  Configuration:")
    print(f"   Input:  {input_dir}")
    print(f"   Output: {output_dir}")
    print(f"   Pack:   {args.pack_name}")
    print(f"   Aspect: {'Maintained' if maintain_aspect else 'Stretched'}")
    print()

    if not validate_directories(input_dir, output_dir):
        return 1

    print("🔍 Scanning for images...")
    images_with_ratios = find_matching_images(input_dir)

    if not images_with_ratios:
        print(f"❌ No images found")
        return 1

    print(f"✓ Found {len(images_with_ratios)} image(s)")

    print("\n🎯 Matching images to poster slots...")
    assignments = match_images_to_slots(images_with_ratios)

    if not assignments:
        print("❌ Could not match images")
        return 1

    display_matching_report(assignments, images_with_ratios)

    print(f"\n📦 Creating pack: {args.pack_name}")
    pack_dir = create_pack_structure(args.pack_name, output_dir)
    print(f"✓ Pack directory: {pack_dir}")

    success_count = process_all_assignments(assignments, pack_dir, maintain_aspect)

    if success_count == 0:
        print("\n❌ No images processed")
        return 1

    generate_pack_info(pack_dir, assignments)

    if not args.no_cleanup:
        cleanup_processed_files(assignments, done_dir)

    print("\n" + "=" * 70)
    print("🎉 PACK GENERATION COMPLETE!")
    print("=" * 70)
    print(f"\n✓ Pack: {pack_dir}")
    print(f"✓ Processed: {success_count} image(s)")
    print(f"\n📋 Next steps:")
    print(f"   1. Review: {pack_dir}")
    print(f"   2. Copy '{args.pack_name}' to:")
    print(f"      Lethal Company/BepInEx/plugins/")

    if len(images_with_ratios) > len(assignments):
        print(f"\n💡 {len(images_with_ratios) - len(assignments)} unmatched image(s)")
        print(f"   Run again to create another pack!")

    print("\n" + "=" * 70 + "\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\n⚠️  Cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)
