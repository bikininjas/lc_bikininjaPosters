# Setup Guide - Virtual Environment for Image Resizer

## Why Use a Virtual Environment?

Virtual environments keep Python packages isolated from your system Python installation. This prevents:
- ❌ Package version conflicts
- ❌ System pollution with project-specific packages
- ❌ "Works on my machine" issues

## One-Time Setup

### Linux/Mac

```bash
# Navigate to the image_resizer directory
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show: (venv) user@machine:~$

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import PIL; import moviepy; print('✅ All dependencies installed!')"
```

### Windows

```bash
# Navigate to the image_resizer directory
cd C:\path\to\lc_bikininjaPosters\image_resizer

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Your prompt should now show: (venv) C:\...

# Install dependencies
pip install -r requirements.txt

# Verify installation
python -c "import PIL; import moviepy; print('✅ All dependencies installed!')"
```

## Daily Usage

### Starting Your Work Session

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

You'll know the venv is active when you see `(venv)` at the start of your prompt.

### Using the Script

```bash
# With venv activated:
python poster_resizer.py
```

### Ending Your Work Session

```bash
deactivate
```

## Using the Helper Script (Easiest Method)

The `run_example.sh` script handles everything automatically:

```bash
cd /home/seb/GITRepos/lc_bikininjaPosters/image_resizer
./run_example.sh
```

This script:
1. ✅ Creates venv if it doesn't exist
2. ✅ Activates venv automatically
3. ✅ Installs dependencies if needed
4. ✅ Runs the poster resizer
5. ℹ️ Reminds you to deactivate when done

## Troubleshooting

### "venv: command not found" or "No module named venv"

The venv module should be included with Python 3.3+. If it's missing:

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-venv
```

**Fedora/RHEL:**
```bash
sudo dnf install python3-venv
```

**macOS:**
```bash
# venv should be included with Python 3
# If not, install Python 3 via Homebrew:
brew install python3
```

### "Permission denied: ./run_example.sh"

Make the script executable:
```bash
chmod +x run_example.sh
```

### "Import Error" even with venv activated

Make sure you're using the venv's Python:
```bash
which python  # Should show: .../venv/bin/python
```

If not, try:
```bash
deactivate
source venv/bin/activate
```

### Packages not found after installation

Ensure you're installing in the activated venv:
```bash
# Verify venv is active (should see "(venv)" in prompt)
pip list  # Should show installed packages

# If empty, install again:
pip install -r requirements.txt
```

### "moviepy installation failed"

moviepy has some system dependencies. Try:

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
pip install moviepy
```

**macOS:**
```bash
brew install ffmpeg
pip install moviepy
```

**Windows:**
Download ffmpeg from https://ffmpeg.org/ and add to PATH, then:
```bash
pip install moviepy
```

## Git and Virtual Environments

The `.gitignore` file is configured to ignore:
- `venv/`
- `.venv/`
- `env/`
- `image_resizer/venv/`

This means:
- ✅ Virtual environment won't be committed to git
- ✅ Each user creates their own venv
- ✅ Keeps repository clean and portable

## Requirements.txt

The `requirements.txt` file lists all needed packages:
```
Pillow>=10.0.0      # Image processing
moviepy>=1.0.3      # Video processing
```

To update dependencies:
```bash
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

To add new dependencies:
```bash
pip install package_name
pip freeze > requirements.txt  # Update the file
```

## Quick Reference

| Command | Purpose |
|---------|---------|
| `python3 -m venv venv` | Create virtual environment |
| `source venv/bin/activate` | Activate (Linux/Mac) |
| `venv\Scripts\activate` | Activate (Windows) |
| `deactivate` | Deactivate virtual environment |
| `pip install -r requirements.txt` | Install all dependencies |
| `pip list` | Show installed packages |
| `which python` | Show which Python is being used |
| `./run_example.sh` | Auto setup & run (Linux/Mac) |

## Best Practices

1. ✅ **Always activate venv** before running the script
2. ✅ **Use the helper script** for easiest experience
3. ✅ **Deactivate when done** to return to system Python
4. ✅ **Never commit venv/** to git (already in .gitignore)
5. ✅ **Share requirements.txt** not the venv folder
6. ✅ **Keep venv updated**: `pip install --upgrade -r requirements.txt`