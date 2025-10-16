"""
Configuration for CustomPosters mod specifications.
"""

# Poster slot specifications
POSTER_SPECS = {
    "Poster1": {
        "width": 639,
        "height": 488,
        "extension": ".png",
        "location": "posters",
    },
    "Poster2": {
        "width": 730,
        "height": 490,
        "extension": ".png",
        "location": "posters",
    },
    "Poster3": {
        "width": 749,
        "height": 1054,
        "extension": ".png",
        "location": "posters",
    },
    "Poster4": {
        "width": 729,
        "height": 999,
        "extension": ".png",
        "location": "posters",
    },
    "Poster5": {
        "width": 552,
        "height": 769,
        "extension": ".png",
        "location": "posters",
    },
    "CustomTips": {
        "width": 860,
        "height": 1219,
        "extension": ".png",
        "location": "tips",
    },
}

# Supported image formats
SUPPORTED_IMAGE_FORMATS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".gif",
    ".tiff",
    ".webp",
    ".avif",
}

# Supported video formats
SUPPORTED_VIDEO_FORMATS = {
    ".mp4",
    ".avi",
    ".mov",
    ".mkv",
    ".flv",
    ".wmv",
    ".webm",
    ".m4v",
    ".mpeg",
    ".mpg",
}

# All supported formats
SUPPORTED_FORMATS = SUPPORTED_IMAGE_FORMATS | SUPPORTED_VIDEO_FORMATS

# Target aspect ratios for each slot (calculated)
TARGET_RATIOS = {
    slot: specs["width"] / specs["height"] for slot, specs in POSTER_SPECS.items()
}
