# CustomPosters Multi-Pack Generator# CustomPosters Multi-Pack Generator# CustomPosters Multi-Pack Generator# CustomPosters Media Resizer



Automatically creates multiple numbered poster packs for the Lethal Company CustomPosters mod with intelligent image/video processing and smart aspect ratio matching.



---Automatically creates multiple numbered poster packs for the Lethal Company CustomPosters mod with intelligent image/video processing and smart aspect ratio matching.



## 📁 Project Structure



```---Automatically creates multiple numbered poster packs for the Lethal Company CustomPosters mod.A Python script to automatically resize images and videos for the [CustomPosters mod](https://github.com/se3ya/CustomPosters) in Lethal Company. This tool resizes media to the exact specifications required by the mod, outputs them with correct filenames and formats, and moves processed files to a `done/` directory.

image_resizer/

├── generate-packs.sh             # Linux/macOS launcher (run this!)

├── generate-packs.ps1            # Windows launcher (run this!)

├── src/                          # Python source code## 📁 Project Structure

│   ├── multi_pack_generator.py  # Main multi-pack generator

│   ├── poster_resizer.py        # Single pack generator (legacy)

│   ├── config.py                # Poster specifications

│   ├── ratio_matcher.py         # Aspect ratio matching engine```## 📁 Project Structure## Features

│   ├── image_processor.py       # Image/video processing

│   ├── pack_generator.py        # Pack structure managementimage_resizer/

│   └── requirements.txt         # Python dependencies

├── input/                        # Place your images/videos here├── bin/                          # Wrapper scripts

├── done/                         # Processed files move here

├── venv/                         # Python virtual environment (auto-created)│   ├── generate-packs.sh        # Linux/macOS launcher

└── README.md                     # This file

```│   └── generate-packs.ps1       # Windows launcher```- ✅ Resizes images and videos to exact CustomPosters specifications



---├── src/                          # Python source code



## ✨ Features│   ├── multi_pack_generator.py  # Main multi-pack generatorimage_resizer/- ✅ **Video support** - converts any video format to MP4 for Poster2



### 🚀 One-Click Setup│   ├── poster_resizer.py        # Single pack generator (legacy)

- ✅ **Auto-detects Python** - Checks if Python 3.7+ is installed

- ✅ **Auto-installs Python** - Linux/macOS auto-install, Windows guided install│   ├── config.py                # Poster specifications├── bin/                          # Executable wrappers- ✅ Maintains aspect ratio with smart cropping/padding

- ✅ **Virtual Environment** - Creates isolated Python environment automatically

- ✅ **Auto-dependencies** - Installs all required packages automatically│   ├── ratio_matcher.py         # Aspect ratio matching engine

- ✅ **Ready to use** - Just run the script!

│   ├── image_processor.py       # Image/video processing│   ├── generate-packs.sh        # Linux/macOS launcher (auto-installs Python)- ✅ Converts to correct output formats (PNG, BMP, JPEG, MP4)

### 🎯 Smart Pack Generation

- 📦 **Auto-numbering** - Creates BikininjasPosters01, 02, 03...│   ├── pack_generator.py        # Pack structure management

- 🎯 **Smart Matching** - Intelligently assigns files to best-fitting slots

- ✂️ **Smart Cropping** - Crops images to match target aspect ratio (no padding!)│   └── requirements.txt         # Python dependencies│   └── generate-packs.ps1       # Windows launcher (auto-installs Python)- ✅ Uses correct filenames (Poster1.png, Poster2.mp4, etc.)

- 🎬 **Video Support** - Converts videos to MP4 (H.264/AAC)

- 🧹 **Auto-Cleanup** - Moves processed files to `done/` directory├── input/                        # Place your images/videos here

- ✅ **Exact 6 Files** - Each pack has exactly 5 posters + 1 tip

- 🔄 **Incremental** - Continues from last pack number├── done/                         # Processed files move here├── src/                          # Python source code- ✅ Places files in the right folders (posters/ and tips/)



---├── venv/                         # Python virtual environment (auto-created)



## 🚀 Quick Start└── README.md                     # This file│   ├── multi_pack_generator.py  # Main multi-pack generator- ✅ **Automatically moves processed files to done/ directory**



### Windows (Copy & Run)```



**Step 1:** Create `generate-packs.ps1` in the `image_resizer` folder:│   ├── poster_resizer.py        # Single pack generator- ✅ Interactive mode for manual assignment



<details>---

<summary>📄 Click to view generate-packs.ps1 (Copy this entire script)</summary>

│   ├── config.py                # Poster specifications- ✅ Auto mode for batch processing

```powershell

################################################################################## ✨ Features

# CustomPosters Multi-Pack Generator - Windows PowerShell Wrapper

################################################################################│   ├── ratio_matcher.py         # Aspect ratio matching- ✅ Handles transparent images properly



$ErrorActionPreference = "Stop"### 🚀 One-Click Setup



# Script paths- ✅ **Auto-detects Python** - Checks if Python 3.7+ is installed│   ├── image_processor.py       # Image/video processing- ✅ Support for multiple input formats

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

$ProjectDir = $ScriptDir- ✅ **Auto-installs Python** - Linux/macOS auto-install, Windows guided install

$SrcDir = Join-Path $ProjectDir "src"

$VenvDir = Join-Path $ProjectDir "venv"- ✅ **Virtual Environment** - Creates isolated Python environment automatically│   ├── pack_generator.py        # Pack structure management- ✅ Extracts video frames for image slots if needed



function Write-Header {- ✅ **Auto-dependencies** - Installs all required packages automatically

    Write-Host ""

    Write-Host "╔════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan- ✅ **Ready to use** - Just run the script!│   └── requirements.txt         # Python dependencies

    Write-Host "║        CustomPosters Multi-Pack Generator - Setup Script          ║" -ForegroundColor Cyan

    Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

    Write-Host ""

}### 🎯 Smart Pack Generation├── input/                        # Place your images/videos here## Poster Specifications



function Write-Success {- 📦 **Auto-numbering** - Creates BikininjasPosters01, 02, 03...

    param([string]$Message)

    Write-Host "✓ $Message" -ForegroundColor Green- 🎯 **Smart Matching** - Intelligently assigns files to best-fitting slots├── done/                         # Processed files move here

}

- ✂️ **Smart Cropping** - Crops images to match target aspect ratio (no padding!)

function Write-Error-Custom {

    param([string]$Message)- 🎬 **Video Support** - Converts videos to MP4 (H.264/AAC)└── venv/                         # Python virtual environment (auto-created)| Poster | Dimensions | Output Format | Output Location |

    Write-Host "✗ $Message" -ForegroundColor Red

}- 🧹 **Auto-Cleanup** - Moves processed files to `done/` directory



function Write-Info {- ✅ **Exact 6 Files** - Each pack has exactly 5 posters + 1 tip```|--------|------------|---------------|-----------------|

    param([string]$Message)

    Write-Host "ℹ $Message" -ForegroundColor Cyan- 🔄 **Incremental** - Continues from last pack number

}

| Poster1 | 639×488 | PNG | posters/Poster1.png |

function Write-Warning-Custom {

    param([string]$Message)---

    Write-Host "⚠ $Message" -ForegroundColor Yellow

}## 🚀 Quick Start| Poster2 | 730×490 | **MP4** 🎬 | posters/Poster2.mp4 |



function Test-PythonInstalled {## 🚀 Quick Start

    Write-Info "Checking Python installation..."

    | Poster3 | 749×1054 | BMP | posters/Poster3.bmp |

    $pythonCmd = $null

    ### Windows (Copy & Run)

    if (Get-Command python3 -ErrorAction SilentlyContinue) {

        $pythonCmd = "python3"### Windows| Poster4 | 729×999 | JPEG | posters/Poster4.jpeg |

    }

    elseif (Get-Command python -ErrorAction SilentlyContinue) {**Step 1:** Create `generate-packs.ps1` in the `image_resizer/bin` folder:

        $pythonCmd = "python"

    }| Poster5 | 552×769 | PNG | posters/Poster5.png |

    

    if ($pythonCmd) {<details>

        try {

            $version = & $pythonCmd --version 2>&1 | Out-String<summary>📄 Click to view generate-packs.ps1 (Copy this entire script)</summary>1. **Double-click** `bin\generate-packs.ps1`| CustomTips | 860×1219 | JPEG | tips/CustomTips.jpg |

            if ($version -match "Python (\d+)\.(\d+)\.(\d+)") {

                $major = [int]$Matches[1]

                $minor = [int]$Matches[2]

                ```powershell2. If Python is not installed, it will open the download page

                if ($major -eq 3 -and $minor -ge 7) {

                    Write-Success "Found Python $($Matches[1]).$($Matches[2]).$($Matches[3])"################################################################################

                    return $pythonCmd

                }# CustomPosters Multi-Pack Generator - Windows PowerShell Wrapper3. After Python installation, run the script again**🎬 Poster2 is special!** It supports video playback in-game, making it perfect for animated posters.

                else {

                    Write-Warning-Custom "Found Python $($Matches[1]).$($Matches[2]), but need Python 3.7+"################################################################################

                }

            }4. Done! Packs will be created in `BepInEx/plugins/`

        }

        catch {$ErrorActionPreference = "Stop"

            Write-Warning-Custom "Error checking Python version: $_"

        }## Installation

    }

    # Script paths

    return $null

}$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path**Command Line:**



function Install-Python {$ProjectDir = Split-Path -Parent $ScriptDir

    Write-Warning-Custom "Python 3.7+ not found. Installation required."

    Write-Info "Opening Python download page in browser..."$SrcDir = Join-Path $ProjectDir "src"```powershell1. **Install Python** (3.7 or higher)

    

    Start-Process "https://www.python.org/downloads/"$VenvDir = Join-Path $ProjectDir "venv"

    

    Write-Host ""cd image_resizer\bin

    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow

    Write-Host "  MANUAL INSTALLATION REQUIRED" -ForegroundColor Yellowfunction Write-Header {

    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow

    Write-Host ""    Write-Host "".\generate-packs.ps12. **Create a virtual environment** (recommended):

    Write-Host "Please download and install Python 3.7 or higher from the browser window." -ForegroundColor Yellow

    Write-Host ""    Write-Host "╔════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan

    Write-Host "IMPORTANT: During installation, make sure to:" -ForegroundColor Yellow

    Write-Host "  ☑ Check 'Add Python to PATH'" -ForegroundColor Yellow    Write-Host "║        CustomPosters Multi-Pack Generator - Setup Script          ║" -ForegroundColor Cyan```   ```bash

    Write-Host "  ☑ Check 'Install pip'" -ForegroundColor Yellow

    Write-Host ""    Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan

    Write-Host "After installation, close this window and run the script again." -ForegroundColor Yellow

    Write-Host ""    Write-Host ""   cd /path/to/lc_bikininjaPosters/image_resizer

    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow

    Write-Host ""}

    

    Read-Host "Press Enter to exit"### Linux / macOS   python3 -m venv venv

    exit 1

}function Write-Success {



function Setup-VirtualEnvironment {    param([string]$Message)   ```

    param([string]$PythonCmd)

        Write-Host "✓ $Message" -ForegroundColor Green

    Write-Info "Setting up virtual environment..."

    }1. **Open terminal** in the `image_resizer/bin` directory

    if (Test-Path $VenvDir) {

        Write-Success "Virtual environment already exists"

    }

    else {function Write-Error-Custom {2. Run: `./generate-packs.sh`3. **Activate the virtual environment:**

        Write-Info "Creating virtual environment..."

        & $PythonCmd -m venv $VenvDir    param([string]$Message)

        if ($LASTEXITCODE -ne 0) {

            Write-Error-Custom "Failed to create virtual environment"    Write-Host "✗ $Message" -ForegroundColor Red3. Script will auto-install Python if needed (may ask for sudo password)   ```bash

            exit 1

        }}

        Write-Success "Virtual environment created"

    }4. Done! Packs will be created in `BepInEx/plugins/`   # Linux/Mac:

}

function Write-Info {

function Install-Dependencies {

    Write-Info "Installing Python dependencies..."    param([string]$Message)   source venv/bin/activate

    

    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"    Write-Host "ℹ $Message" -ForegroundColor Cyan

    

    if (Test-Path $activateScript) {}**Command:**   

        & $activateScript

    }

    else {

        Write-Error-Custom "Virtual environment activation script not found"function Write-Warning-Custom {```bash   # Windows:

        exit 1

    }    param([string]$Message)

    

    python -m pip install --upgrade pip --quiet    Write-Host "⚠ $Message" -ForegroundColor Yellowcd image_resizer/bin   venv\Scripts\activate

    

    $requirementsFile = Join-Path $SrcDir "requirements.txt"}

    if (Test-Path $requirementsFile) {

        pip install -r $requirementsFile./generate-packs.sh   ```

        if ($LASTEXITCODE -ne 0) {

            Write-Error-Custom "Failed to install dependencies"function Test-PythonInstalled {

            exit 1

        }    Write-Info "Checking Python installation..."```   

        Write-Success "Dependencies installed successfully"

    }    

    else {

        Write-Error-Custom "requirements.txt not found at $requirementsFile"    $pythonCmd = $null   Your prompt should now show `(venv)` at the beginning.

        exit 1

    }    

}

    if (Get-Command python3 -ErrorAction SilentlyContinue) {## ✨ Features

function Run-Generator {

    param([string[]]$Arguments)        $pythonCmd = "python3"

    

    Write-Info "Starting Multi-Pack Generator..."    }4. **Install required dependencies:**

    Write-Host ""

        elseif (Get-Command python -ErrorAction SilentlyContinue) {

    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"

    & $activateScript        $pythonCmd = "python"### Auto-Installation   ```bash

    

    Set-Location $ProjectDir    }

    

    $generatorScript = Join-Path $SrcDir "multi_pack_generator.py"    - ✅ **Detects Python** - Checks if Python 3.7+ is installed   pip install -r requirements.txt

    

    if ($Arguments.Count -gt 0) {    if ($pythonCmd) {

        & python $generatorScript $Arguments

    }        try {- ✅ **Auto-installs** - Installs Python automatically on Linux/macOS   ```

    else {

        & python $generatorScript            $version = & $pythonCmd --version 2>&1 | Out-String

    }

                if ($version -match "Python (\d+)\.(\d+)\.(\d+)") {- ✅ **Windows Helper** - Opens download page on Windows   This installs:

    $exitCode = $LASTEXITCODE

                    $major = [int]$Matches[1]

    Write-Host ""

    if ($exitCode -eq 0) {                $minor = [int]$Matches[2]- ✅ **Virtual Environment** - Creates isolated Python environment   - **Pillow** - for image processing

        Write-Success "Pack generation completed successfully!"

    }                

    else {

        Write-Error-Custom "Pack generation failed with exit code $exitCode"                if ($major -eq 3 -and $minor -ge 7) {- ✅ **Dependencies** - Installs all required packages automatically   - **moviepy** - for video processing and conversion

    }

                        Write-Success "Found Python $($Matches[1]).$($Matches[2]).$($Matches[3])"

    return $exitCode

}                    return $pythonCmd



function Main {                }

    param([string[]]$ScriptArgs)

                    else {### Pack Generation5. **Add your media files** to the `input/` folder

    Write-Header

                        Write-Warning-Custom "Found Python $($Matches[1]).$($Matches[2]), but need Python 3.7+"

    $pythonCmd = Test-PythonInstalled

                    }- 🎯 **Smart Matching** - Intelligently assigns files to best-fitting slots

    if (-not $pythonCmd) {

        Install-Python            }

    }

            }- ✂️ **Smart Cropping** - Crops images to match target aspect ratio**Note**: You'll need to activate the virtual environment each time you use the script:

    Setup-VirtualEnvironment -PythonCmd $pythonCmd

    Install-Dependencies        catch {

    

    $exitCode = Run-Generator -Arguments $ScriptArgs            Write-Warning-Custom "Error checking Python version: $_"- 🎬 **Video Support** - Converts videos to MP4 (H.264/AAC)```bash

    

    Write-Host ""        }

    Write-Host "Press any key to exit..." -ForegroundColor Gray

    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")    }- 📦 **Auto-Numbering** - Creates BikininjasPosters01, 02, 03...source venv/bin/activate  # Linux/Mac

    

    exit $exitCode    

}

    return $null- 🧹 **Auto-Cleanup** - Moves processed files to `done/` directory```

Main -ScriptArgs $args

```}



</details>- ✅ **Exact 6 Files** - Each pack has exactly 5 posters + 1 tip



**Step 2:** Right-click `generate-packs.ps1` and select **"Run with PowerShell"**function Install-Python {



Or from Command Line:    Write-Warning-Custom "Python 3.7+ not found. Installation required."## Usage

```powershell

cd image_resizer    Write-Info "Opening Python download page in browser..."

.\generate-packs.ps1

```    ## 📋 Requirements



---    Start-Process "https://www.python.org/downloads/"



### Linux / macOS (Copy & Run)    **First, activate your virtual environment** (if you created one):



**Step 1:** Create `generate-packs.sh` in the `image_resizer` folder:    Write-Host ""



<details>    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow### Automatic (handled by wrappers)```bash

<summary>📄 Click to view generate-packs.sh (Copy this entire script)</summary>

    Write-Host "  MANUAL INSTALLATION REQUIRED" -ForegroundColor Yellow

```bash

#!/usr/bin/env bash    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow- Python 3.7+source venv/bin/activate  # Linux/Mac

################################################################################

# CustomPosters Multi-Pack Generator - Linux/macOS Wrapper    Write-Host ""

################################################################################

    Write-Host "Please download and install Python 3.7 or higher from the browser window." -ForegroundColor Yellow- Pillow (image processing)```

set -e

    Write-Host ""

RED='\033[0;31m'

GREEN='\033[0;32m'    Write-Host "IMPORTANT: During installation, make sure to:" -ForegroundColor Yellow- pillow-avif-plugin (AVIF support)

YELLOW='\033[1;33m'

BLUE='\033[0;34m'    Write-Host "  ☑ Check 'Add Python to PATH'" -ForegroundColor Yellow

NC='\033[0m'

    Write-Host "  ☑ Check 'Install pip'" -ForegroundColor Yellow- moviepy (video conversion)### Interactive Mode (Recommended)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

PROJECT_DIR="$SCRIPT_DIR"    Write-Host ""

SRC_DIR="$PROJECT_DIR/src"

VENV_DIR="$PROJECT_DIR/venv"    Write-Host "After installation, close this window and run the script again." -ForegroundColor Yellow```bash



print_header() {    Write-Host ""

    echo -e "${BLUE}"

    echo "╔════════════════════════════════════════════════════════════════════╗"    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow### Manual (if needed)python poster_resizer.py

    echo "║        CustomPosters Multi-Pack Generator - Setup Script          ║"

    echo "╚════════════════════════════════════════════════════════════════════╝"    Write-Host ""

    echo -e "${NC}"

}    - **Linux**: Package manager (apt, dnf, yum, pacman, or brew)```



print_success() {    Read-Host "Press Enter to exit"

    echo -e "${GREEN}✓ $1${NC}"

}    exit 1- **Windows**: Administrator rights (for Python installation)



print_error() {}

    echo -e "${RED}✗ $1${NC}"

}This mode will:



print_info() {function Setup-VirtualEnvironment {

    echo -e "${BLUE}ℹ $1${NC}"

}    param([string]$PythonCmd)## 🎮 Usage- Show you each image/video found in the `input/` folder



print_warning() {    

    echo -e "${YELLOW}⚠ $1${NC}"

}    Write-Info "Setting up virtual environment..."- Ask which poster slot each file should fill



check_python() {    

    print_info "Checking Python installation..."

        if (Test-Path $VenvDir) {### Basic Usage- Allow you to skip files or quit at any time

    if command -v python3 &> /dev/null; then

        PYTHON_CMD="python3"        Write-Success "Virtual environment already exists"

        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')

        print_success "Found Python $PYTHON_VERSION"    }- Move processed files to `done/` automatically

        return 0

    elif command -v python &> /dev/null; then    else {

        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')

        PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)        Write-Info "Creating virtual environment..."**Windows:**

        if [ "$PYTHON_MAJOR" = "3" ]; then

            PYTHON_CMD="python"        & $PythonCmd -m venv $VenvDir

            print_success "Found Python $PYTHON_VERSION"

            return 0        if ($LASTEXITCODE -ne 0) {```powershell### Auto Mode

        fi

    fi            Write-Error-Custom "Failed to create virtual environment"

    

    return 1            exit 1.\generate-packs.ps1```bash

}

        }

install_python() {

    print_warning "Python 3 not found. Attempting to install..."        Write-Success "Virtual environment created"```python poster_resizer.py --auto

    

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then    }

        if command -v apt-get &> /dev/null; then

            print_info "Detected Debian/Ubuntu. Installing Python..."}```

            sudo apt-get update

            sudo apt-get install -y python3 python3-pip python3-venv

            print_success "Python installed successfully"

        elif command -v dnf &> /dev/null; thenfunction Install-Dependencies {**Linux/macOS:**

            print_info "Detected Fedora. Installing Python..."

            sudo dnf install -y python3 python3-pip    Write-Info "Installing Python dependencies..."

            print_success "Python installed successfully"

        elif command -v yum &> /dev/null; then    ```bashThis mode automatically assigns files to poster slots in order (Poster1, Poster2, etc.).

            print_info "Detected CentOS/RHEL. Installing Python..."

            sudo yum install -y python3 python3-pip    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"

            print_success "Python installed successfully"

        elif command -v pacman &> /dev/null; then    ./generate-packs.sh

            print_info "Detected Arch Linux. Installing Python..."

            sudo pacman -S --noconfirm python python-pip    if (Test-Path $activateScript) {

            print_success "Python installed successfully"

        else        & $activateScript```### Custom Directories

            print_error "Unable to detect package manager"

            print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"    }

            exit 1

        fi    else {```bash

    elif [[ "$OSTYPE" == "darwin"* ]]; then

        if command -v brew &> /dev/null; then        Write-Error-Custom "Virtual environment activation script not found"

            print_info "Installing Python via Homebrew..."

            brew install python3        exit 1### With Options# Use a different input directory

            print_success "Python installed successfully"

        else    }

            print_error "Homebrew not found"

            print_info "Install Homebrew from: https://brew.sh/"    python poster_resizer.py --input my_media

            print_info "Or install Python from: https://www.python.org/downloads/"

            exit 1    python -m pip install --upgrade pip --quiet

        fi

    else    **Limit to 3 packs:**

        print_error "Unsupported operating system: $OSTYPE"

        print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"    $requirementsFile = Join-Path $SrcDir "requirements.txt"

        exit 1

    fi    if (Test-Path $requirementsFile) {```bash# Use a different target directory

}

        pip install -r $requirementsFile

setup_venv() {

    print_info "Setting up virtual environment..."        if ($LASTEXITCODE -ne 0) {./generate-packs.sh --max-packs 3python poster_resizer.py --target /path/to/your/mod/BikininjasPosters

    

    if [ -d "$VENV_DIR" ]; then            Write-Error-Custom "Failed to install dependencies"

        print_success "Virtual environment already exists"

    else            exit 1``````

        print_info "Creating virtual environment..."

        $PYTHON_CMD -m venv "$VENV_DIR"        }

        print_success "Virtual environment created"

    fi        Write-Success "Dependencies installed successfully"

}

    }

install_dependencies() {

    print_info "Installing Python dependencies..."    else {**Custom base name:**### Other Options

    

    source "$VENV_DIR/bin/activate"        Write-Error-Custom "requirements.txt not found at $requirementsFile"

    pip install --upgrade pip > /dev/null 2>&1

            exit 1```bash```bash

    if [ -f "$SRC_DIR/requirements.txt" ]; then

        pip install -r "$SRC_DIR/requirements.txt"    }

        print_success "Dependencies installed successfully"

    else}./generate-packs.sh --base-name "MyPosters"# Don't maintain aspect ratio (may distort images)

        print_error "requirements.txt not found at $SRC_DIR/requirements.txt"

        exit 1

    fi

}function Run-Generator {```python poster_resizer.py --no-aspect



run_generator() {    param([string[]]$Arguments)

    print_info "Starting Multi-Pack Generator..."

    echo ""    

    

    source "$VENV_DIR/bin/activate"    Write-Info "Starting Multi-Pack Generator..."

    cd "$PROJECT_DIR"

        Write-Host ""**Keep files in input/ (don't move to done/):**# Show help

    python "$SRC_DIR/multi_pack_generator.py" "$@"

        

    exit_code=$?

    echo ""    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"```bashpython poster_resizer.py --help

    if [ $exit_code -eq 0 ]; then

        print_success "Pack generation completed successfully!"    & $activateScript

    else

        print_error "Pack generation failed with exit code $exit_code"    ./generate-packs.sh --no-cleanup```

    fi

        Set-Location $ProjectDir

    return $exit_code

}    ```



main() {    $generatorScript = Join-Path $SrcDir "multi_pack_generator.py"

    print_header

        ## Directory Structure

    if ! check_python; then

        install_python    if ($Arguments.Count -gt 0) {

        if ! check_python; then

            print_error "Python installation failed"        & python $generatorScript $Arguments**Disable smart cropping:**

            exit 1

        fi    }

    fi

        else {```bash### Before (Your Setup)

    setup_venv

    install_dependencies        & python $generatorScript

    run_generator "$@"

}    }./generate-packs.sh --no-aspect```



main "$@"    

```

    $exitCode = $LASTEXITCODE```lc_bikininjaPosters/

</details>

    

**Step 2:** Make it executable and run:

```bash    Write-Host ""├── image_resizer/

cd image_resizer

chmod +x generate-packs.sh    if ($exitCode -eq 0) {

./generate-packs.sh

```        Write-Success "Pack generation completed successfully!"**Show all options:**│   ├── poster_resizer.py



---    }



## 📋 Requirements    else {```bash│   ├── requirements.txt



### Automatic (handled by wrapper scripts)        Write-Error-Custom "Pack generation failed with exit code $exitCode"

- Python 3.7+

- Pillow (image processing)    }./generate-packs.sh --help│   ├── README.md

- pillow-avif-plugin (AVIF support)

- moviepy (video conversion)    



### Manual (if needed)    return $exitCode```│   ├── input/                # Put your images/videos here

- **Linux**: Package manager (apt, dnf, yum, pacman, or brew)

- **Windows**: Administrator rights (for Python installation)}



---│   │   ├── cool_video.mp4



## 🎮 Usagefunction Main {



### Basic Usage    param([string[]]$ScriptArgs)## 📝 Step-by-Step Guide│   │   ├── awesome_image.png



**Windows:**    

```powershell

.\generate-packs.ps1    Write-Header│   │   └── my_tip.jpg

```

    

**Linux/macOS:**

```bash    $pythonCmd = Test-PythonInstalled### 1. Add Your Media│   └── done/                 # Processed files moved here automatically

./generate-packs.sh

```    



### With Options    if (-not $pythonCmd) {└── BepInEx/plugins/BikininjasPosters/



```bash        Install-Python

# Limit to 3 packs

./generate-packs.sh --max-packs 3    }Place images and/or videos in the `input/` directory:    ├── posters/



# Custom base name    

./generate-packs.sh --base-name "MyPosters"

    Setup-VirtualEnvironment -PythonCmd $pythonCmd    └── tips/

# Keep files in input/ (don't move to done/)

./generate-packs.sh --no-cleanup    Install-Dependencies



# Disable smart cropping    ```bash```

./generate-packs.sh --no-aspect

    $exitCode = Run-Generator -Arguments $ScriptArgs

# Show all options

./generate-packs.sh --help    image_resizer/input/

```

    Write-Host ""

---

    Write-Host "Press any key to exit..." -ForegroundColor Gray├── landscape1.jpg### After (Generated Output)

## 📝 Step-by-Step Guide

    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

### 1. Add Your Media

    ├── portrait1.png```

Place images and/or videos in the `input/` directory:

    exit $exitCode

```

input/}├── video1.mp4lc_bikininjaPosters/

├── landscape1.jpg

├── portrait1.png

├── video1.mp4

├── landscape2.webpMain -ScriptArgs $args├── landscape2.webp├── image_resizer/

└── portrait2.avif

``````



**Supported Formats:**└── portrait2.avif│   ├── input/                # Empty (files moved to done/)

- **Images**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`, `.webp`, `.avif`

- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.m4v`, `.mpeg`, `.mpg`</details>



### 2. Run the Generator```│   └── done/                 # Your original files



**Windows:** Double-click `generate-packs.ps1` or run from PowerShell  **Step 2:** Right-click `generate-packs.ps1` and select **"Run with PowerShell"**

**Linux/macOS:** Run `./generate-packs.sh` from terminal

│       ├── cool_video.mp4

### 3. First Run Setup (One-Time Only)

Or from Command Line:

The script will automatically:

1. ✅ Check for Python installation```powershell**Supported Formats:**│       ├── awesome_image.png

2. ✅ Install Python if needed (Linux/macOS auto, Windows guided)

3. ✅ Create virtual environmentcd image_resizer\bin

4. ✅ Install all dependencies

5. ✅ Run the pack generator.\generate-packs.ps1- **Images**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`, `.webp`, `.avif`│       └── my_tip.jpg



**This only happens once!** Subsequent runs start instantly.```



### 4. Review Output- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.m4v`, `.mpeg`, `.mpg`└── BepInEx/plugins/BikininjasPosters/



Packs are created in `../BepInEx/plugins/`:---



```    ├── posters/

BepInEx/plugins/

├── BikininjasPosters01/### Linux / macOS (Copy & Run)

│   ├── posters/

│   │   ├── Poster1.png### 2. Run the Generator    │   ├── Poster1.png       # 639×488

│   │   ├── Poster2.mp4  ← Video!

│   │   ├── Poster3.png**Step 1:** Create `generate-packs.sh` in the `image_resizer/bin` folder:

│   │   ├── Poster4.png

│   │   └── Poster5.png    │   ├── Poster2.mp4       # 730×490 (video!)

│   ├── tips/

│   │   └── CustomTips.png<details>

│   └── pack_info.txt

└── BikininjasPosters02/<summary>📄 Click to view generate-packs.sh (Copy this entire script)</summary>**Windows:**    │   ├── Poster3.bmp       # 749×1054

    └── ...

```



### 5. Install in Game```bash```powershell    │   ├── Poster4.jpeg      # 729×999



Copy pack folders to Lethal Company:#!/usr/bin/env bash



```################################################################################cd image_resizer\bin    │   └── Poster5.png       # 552×769

Lethal Company/BepInEx/plugins/

├── BikininjasPosters01/# CustomPosters Multi-Pack Generator - Linux/macOS Wrapper

└── BikininjasPosters02/

```################################################################################.\generate-packs.ps1    └── tips/



---



## 🎯 How It Worksset -e```        └── CustomTips.jpg    # 860×1219



### Intelligent Aspect Ratio Matching



Each file is matched to the poster slot with the closest aspect ratio:RED='\033[0;31m'```



| Slot | Dimensions | Aspect Ratio | Orientation | Best For |GREEN='\033[0;32m'

|------|-----------|--------------|-------------|----------|

| **Poster1** | 639×488 | 1.31:1 | Landscape | Wide images/videos |YELLOW='\033[1;33m'**Linux/macOS:**

| **Poster2** | 730×490 | 1.49:1 | Landscape | Wide images/videos |

| **Poster3** | 749×1054 | 0.71:1 | Portrait | Tall images/videos |BLUE='\033[0;34m'

| **Poster4** | 729×999 | 0.73:1 | Portrait | Tall images/videos |

| **Poster5** | 552×769 | 0.72:1 | Portrait | Tall images/videos |NC='\033[0m'```bash## Supported Input Formats

| **CustomTips** | 860×1219 | 0.71:1 | Portrait | Tall images/videos |



### Smart Cropping vs. Padding

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"cd image_resizer/bin

**Old method (padding - ❌):**

```PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

┌─────────────────┐

│                 │SRC_DIR="$PROJECT_DIR/src"./generate-packs.sh### Images

│   ┌─────────┐   │

│   │  Image  │   │ ← White barsVENV_DIR="$PROJECT_DIR/venv"

│   └─────────┘   │

│                 │```- `.jpg`, `.jpeg`

└─────────────────┘

```print_header() {



**New method (smart crop - ✅):**    echo -e "${BLUE}"- `.png`

```

┌─────────────────┐    echo "╔════════════════════════════════════════════════════════════════════╗"

│                 │

│     Image       │ ← Fills entire space    echo "║        CustomPosters Multi-Pack Generator - Setup Script          ║"### 3. First Run Setup- `.bmp`

│    (cropped)    │ ← Centered crop

│                 │    echo "╚════════════════════════════════════════════════════════════════════╝"

└─────────────────┘

```    echo -e "${NC}"- `.gif`



### Video Processing}



Videos are automatically converted to MP4:The script will automatically:- `.tiff`

- **Codec**: H.264 video, AAC audio

- **Aspect Ratio**: Maintained with black barsprint_success() {

- **Quality**: Preserves original quality

- **Framerate**: Maintains original framerate    echo -e "${GREEN}✓ $1${NC}"1. ✅ Check for Python installation- `.webp`



---}



## 🔧 Troubleshooting2. ✅ Install Python if needed (Linux/macOS) or guide you (Windows)



### Windows Issuesprint_error() {



**"Running scripts is disabled on this system"**    echo -e "${RED}✗ $1${NC}"3. ✅ Create virtual environment### Videos (NEW! 🎬)



Open PowerShell as Administrator:}

```powershell

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser4. ✅ Install all dependencies- `.mp4`

```

print_info() {

**Python not added to PATH**

    echo -e "${BLUE}ℹ $1${NC}"5. ✅ Run the pack generator- `.avi`

Reboot after Python installation, or manually add Python to PATH.

}

### Linux/macOS Issues

- `.mov`

**"Permission denied"**

```bashprint_warning() {

chmod +x generate-packs.sh

```    echo -e "${YELLOW}⚠ $1${NC}"**This only happens once!** Subsequent runs are instant.- `.mkv`



**"sudo: command not found"**}



Log in as root or use your system's privilege escalation method.- `.flv`



**Homebrew not found (macOS)**check_python() {

```bash

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"    print_info "Checking Python installation..."### 4. Review Output- `.wmv`

```

    

### General Issues

    if command -v python3 &> /dev/null; then- `.webm`

**"No files found"**

- Add images/videos to `input/` directory        PYTHON_CMD="python3"

- Check file extensions are supported

- Files must be directly in `input/`, not subdirectories        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')Packs are created in `BepInEx/plugins/`:- `.m4v`



**"Only X file(s) found, need at least 6"**        print_success "Found Python $PYTHON_VERSION"

- Need minimum 6 files per pack

- Add more files to `input/`        return 0- `.mpeg`, `.mpg`

- Remaining files processed in next run

    elif command -v python &> /dev/null; then

**"Video processing is slow"**

- Normal for video encoding        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')```

- Use shorter clips (≤30 seconds recommended)

- Consider lower resolution sources        PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)

- Progress shown during encoding

        if [ "$PYTHON_MAJOR" = "3" ]; thenBepInEx/plugins/**All video formats are automatically converted to MP4!**

---

            PYTHON_CMD="python"

## 💡 Tips for Best Results

            print_success "Found Python $PYTHON_VERSION"├── BikininjasPosters01/

1. **Sort by Orientation**

   - Landscape (~1.3:1 to 1.5:1) → Poster1, Poster2            return 0

   - Portrait (~0.7:1 to 0.75:1) → Poster3, Poster4, Poster5, Tips

        fi│   ├── posters/## Image Processing Details

2. **Use High Resolution**

   - Minimum: 1920×1080 (landscape), 1080×1920 (portrait)    fi

   - Script downscales, so start high-res

    │   │   ├── Poster1.png

3. **Mix Images and Videos**

   - Videos great for animated posters    return 1

   - Keep videos short (≤30 seconds)

   - Any format auto-converts to MP4}│   │   ├── Poster2.mp4  ← Video!### Aspect Ratio Handling



4. **Batch Processing**

   - Process large collections in batches

   - Use `--max-packs` to limit outputinstall_python() {│   │   ├── Poster3.pngBy default, the script maintains the original aspect ratio of your media:

   - Run multiple times as needed

    print_warning "Python 3 not found. Attempting to install..."

---

    │   │   ├── Poster4.png- Media is resized to fit within the target dimensions

## 🛠️ Advanced Usage

    if [[ "$OSTYPE" == "linux-gnu"* ]]; then

### Manual Python Environment

        if command -v apt-get &> /dev/null; then│   │   └── Poster5.png- If needed, white padding (images) or black bars (videos) are added to reach exact dimensions

If you prefer manual setup:

            print_info "Detected Debian/Ubuntu. Installing Python..."

```bash

# Create virtual environment            sudo apt-get update│   ├── tips/- This prevents distortion of your content

python3 -m venv venv

            sudo apt-get install -y python3 python3-pip python3-venv

# Activate

source venv/bin/activate  # Linux/macOS            print_success "Python installed successfully"│   │   └── CustomTips.png

venv\Scripts\activate     # Windows

        elif command -v dnf &> /dev/null; then

# Install dependencies

pip install -r src/requirements.txt            print_info "Detected Fedora. Installing Python..."│   └── pack_info.txt### Transparency Handling



# Run generator            sudo dnf install -y python3 python3-pip

python src/multi_pack_generator.py

```            print_success "Python installed successfully"└── BikininjasPosters02/- Transparent PNG images are converted to RGB with white backgrounds



### All Command-Line Options        elif command -v yum &> /dev/null; then



```            print_info "Detected CentOS/RHEL. Installing Python..."    └── ...- This ensures compatibility with all output formats

--input DIR           Input directory (default: input)

--output DIR          Output directory (default: ../BepInEx/plugins)            sudo yum install -y python3 python3-pip

--base-name NAME      Base pack name (default: BikininjasPosters)

--max-packs N         Maximum packs to generate            print_success "Python installed successfully"```

--no-aspect           Disable aspect ratio maintenance (stretch)

--no-cleanup          Keep files in input/ directory        elif command -v pacman &> /dev/null; then

--help                Show all options

```            print_info "Detected Arch Linux. Installing Python..."### Video Processing



### Example Workflows            sudo pacman -S --noconfirm python python-pip



**Process large batch in chunks:**            print_success "Python installed successfully"### 5. Install in Game- Videos are resized and re-encoded to MP4 format

```bash

# Process 3 packs at a time        else

./generate-packs.sh --max-packs 3

            print_error "Unable to detect package manager"- Audio is preserved (AAC codec)

# Review the output

ls -l ../BepInEx/plugins/            print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"



# Process next 3 packs            exit 1Copy the pack folders to your Lethal Company mods directory:- Video codec: H.264 for maximum compatibility

./generate-packs.sh --max-packs 3

```        fi



**Custom pack names:**    elif [[ "$OSTYPE" == "darwin"* ]]; then- Maintains original framerate and quality where possible

```bash

./generate-packs.sh --base-name "HorrorPosters"        if command -v brew &> /dev/null; then

# Creates: HorrorPosters01, HorrorPosters02...

```            print_info "Installing Python via Homebrew..."```



**Keep originals for reference:**            brew install python3

```bash

./generate-packs.sh --no-cleanup            print_success "Python installed successfully"Lethal Company/BepInEx/plugins/### Quality Settings

# Files stay in input/ (not moved to done/)

```        else



---            print_error "Homebrew not found"├── BikininjasPosters01/- JPEG files are saved with 95% quality and optimization



## 📦 Sharing with Others            print_info "Install Homebrew from: https://brew.sh/"



1. Zip the entire `image_resizer` directory            print_info "Or install Python from: https://www.python.org/downloads/"└── BikininjasPosters02/- PNG files use lossless compression

2. Share with friends

3. They just run the wrapper script!            exit 1



No manual setup required - wrappers handle everything automatically.        fi```- BMP files are saved in standard format



---    else



## 📄 License        print_error "Unsupported operating system: $OSTYPE"- MP4 videos use H.264 with AAC audio



This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images/videos you process.        print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"



---        exit 1## 🎯 How It Works



## 🎉 Credits    fi



- **CustomPosters Mod**: [se3ya's CustomPosters](https://github.com/se3ya/CustomPosters)}## File Management

- **Lethal Company**: Zeekerss

- **Python**: Python Software Foundation

- **Libraries**: Pillow, moviepy, pillow-avif-plugin

setup_venv() {### Intelligent Matching

---

    print_info "Setting up virtual environment..."

**🚀 Ready to generate packs!**

    ### Automatic Move to Done Directory

For technical details, see the source code in `src/` directory.

    if [ -d "$VENV_DIR" ]; then

        print_success "Virtual environment already exists"Each file is matched to the poster slot with the closest aspect ratio:After successful processing:

    else

        print_info "Creating virtual environment..."- Source files are **automatically moved** from `input/` to `done/`

        $PYTHON_CMD -m venv "$VENV_DIR"

        print_success "Virtual environment created"| Slot | Dimensions | Aspect Ratio | Orientation | Best For |- If a file with the same name exists in `done/`, a number suffix is added

    fi

}|------|-----------|--------------|-------------|----------|- Only successfully processed files are moved



install_dependencies() {| **Poster1** | 639×488 | 1.31:1 | Landscape | Wide images/videos |- Failed/skipped files remain in `input/` for retry

    print_info "Installing Python dependencies..."

    | **Poster2** | 730×490 | 1.49:1 | Landscape | Wide images/videos |

    source "$VENV_DIR/bin/activate"

    pip install --upgrade pip > /dev/null 2>&1| **Poster3** | 749×1054 | 0.71:1 | Portrait | Tall images/videos |### Git Ignore

    

    if [ -f "$SRC_DIR/requirements.txt" ]; then| **Poster4** | 729×999 | 0.73:1 | Portrait | Tall images/videos |The `.gitignore` file is configured to:

        pip install -r "$SRC_DIR/requirements.txt"

        print_success "Dependencies installed successfully"| **Poster5** | 552×769 | 0.72:1 | Portrait | Tall images/videos |- ✅ Track the `input/` and `done/` directories

    else

        print_error "requirements.txt not found at $SRC_DIR/requirements.txt"| **CustomTips** | 860×1219 | 0.71:1 | Portrait | Tall images/videos |- ❌ Ignore all media files in those directories

        exit 1

    fi- ✅ Keep directory structure in git

}

### Smart Cropping- ❌ Prevent large media files from being committed

run_generator() {

    print_info "Starting Multi-Pack Generator..."- ❌ Ignore virtual environments (`venv/`, `.venv/`, `env/`)

    echo ""

    Images are intelligently cropped to match the target aspect ratio:

    source "$VENV_DIR/bin/activate"

    cd "$PROJECT_DIR"## Tips for Best Results

    

    python "$SRC_DIR/multi_pack_generator.py" "$@"**Before (with padding):**

    

    exit_code=$?```1. **Use high-quality source media** - The script will downscale but won't enhance quality

    echo ""

    if [ $exit_code -eq 0 ]; then┌─────────────────┐2. **Consider target aspect ratios** when selecting media:

        print_success "Pack generation completed successfully!"

    else│                 │   - Poster1: ~1.31:1 (landscape)

        print_error "Pack generation failed with exit code $exit_code"

    fi│   ┌─────────┐   │   - Poster2: ~1.49:1 (landscape) - **Perfect for videos!** 🎬

    

    return $exit_code│   │  Image  │   │ ← White bars   - Poster3: ~0.71:1 (portrait)

}

│   └─────────┘   │   - Poster4: ~0.73:1 (portrait)

main() {

    print_header│                 │   - Poster5: ~0.72:1 (portrait)

    

    if ! check_python; then└─────────────────┘   - CustomTips: ~0.71:1 (portrait)

        install_python

        if ! check_python; then```

            print_error "Python installation failed"

            exit 13. **For Poster2 (video slot)**: 

        fi

    fi**After (smart crop):**   - Use any video format - it will be converted to MP4

    

    setup_venv```   - Keep videos short (30 seconds or less recommended)

    install_dependencies

    run_generator "$@"┌─────────────────┐   - Consider file size for mod distribution

}

│                 │

main "$@"

```│     Image       │ ← Fills entire space4. **Video to image slots**: If you assign a video to an image slot, the script will extract a frame



</details>│    (cropped)    │ ← Centered crop5. **Image to Poster2**: You can assign images to Poster2, but videos work better for this slot



**Step 2:** Make it executable and run:│                 │

```bash

cd image_resizer/bin└─────────────────┘## Troubleshooting

chmod +x generate-packs.sh

./generate-packs.sh```

```

### "No supported media files found"

---

### Video Processing- Make sure you have images or videos in the `input/` directory

## 📋 Requirements

- Check that your files have supported extensions

### Automatic (handled by wrapper scripts)

- Python 3.7+Videos are automatically converted to MP4 format:

- Pillow (image processing)

- pillow-avif-plugin (AVIF support)- **Codec**: H.264 video, AAC audio### "Input directory not found"

- moviepy (video conversion)

- **Aspect Ratio**: Maintained with black bars- The `input/` directory should be created automatically

### Manual (if needed)

- **Linux**: Package manager (apt, dnf, yum, pacman, or brew)- **Quality**: Preserves original quality- Or specify a different directory with `--input`

- **Windows**: Administrator rights (for Python installation)

- **Framerate**: Maintains original framerate

---

### "moviepy library not found"

## 🎮 Usage

## 🔧 Troubleshooting- Make sure your virtual environment is activated: `source venv/bin/activate`

### Basic Usage

- Install dependencies: `pip install -r requirements.txt`

**Windows:**

```powershell### Windows Issues- Or manually: `pip install moviepy`

cd bin

.\generate-packs.ps1

```

**"Running scripts is disabled on this system"**### Video processing is slow

**Linux/macOS:**

```bash- Video encoding takes time, especially for longer videos

cd bin

./generate-packs.shOpen PowerShell as Administrator and run:- Consider using shorter clips or lower resolution source videos

```

```powershell- The script will show encoding progress

### With Options

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

```bash

# Limit to 3 packs```### Permission errors

./generate-packs.sh --max-packs 3

- Make sure you have write permissions to the target directory

# Custom base name

./generate-packs.sh --base-name "MyPosters"**Python installation doesn't add to PATH**- Try running with elevated permissions if needed



# Keep files in input/ (don't move to done/)

./generate-packs.sh --no-cleanup

After installing Python, reboot your computer or manually add Python to PATH.### File already exists in done/

# Disable smart cropping

./generate-packs.sh --no-aspect- The script automatically adds number suffixes (_1, _2, etc.)



# Show all options### Linux/macOS Issues- No data will be overwritten

./generate-packs.sh --help

```



---**"Permission denied"**### Image processing errors



## 📝 Step-by-Step Guide- Check that your image files aren't corrupted



### 1. Add Your MediaMake the script executable:- Try converting problematic images to PNG first



Place images and/or videos in the `input/` directory:```bash



```chmod +x bin/generate-packs.sh## Examples

input/

├── landscape1.jpg```

├── portrait1.png

├── video1.mp4### Example 1: Basic Interactive Usage

├── landscape2.webp

└── portrait2.avif**"sudo: command not found"**```bash

```

$ python poster_resizer.py

**Supported Formats:**

- **Images**: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`, `.tiff`, `.webp`, `.avif`You need administrator privileges. Log in as root or use your system's equivalent.

- **Videos**: `.mp4`, `.avi`, `.mov`, `.mkv`, `.flv`, `.wmv`, `.webm`, `.m4v`, `.mpeg`, `.mpg`

🖼️  CustomPosters Media Resizer

### 2. Run the Generator

**Homebrew not found (macOS)**========================================

**Windows:** Double-click `bin/generate-packs.ps1` or run from PowerShell  

**Linux/macOS:** Run `bin/generate-packs.sh` from terminalInput directory: /path/to/image_resizer/input



### 3. First Run Setup (One-Time Only)Install Homebrew first:Done directory: /path/to/image_resizer/done



The script will automatically:```bashOutput base: /path/to/BikininjasPosters

1. ✅ Check for Python installation

2. ✅ Install Python if needed (Linux/macOS auto, Windows guided)/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"Mode: Interactive

3. ✅ Create virtual environment

4. ✅ Install all dependencies```Aspect ratio: Maintained

5. ✅ Run the pack generator



**This only happens once!** Subsequent runs start instantly.

### General Issues✓ Created/verified directories:

### 4. Review Output

  - /path/to/BikininjasPosters/posters

Packs are created in `../BepInEx/plugins/`:

**"No files found in input directory"**  - /path/to/BikininjasPosters/tips

```

BepInEx/plugins/  - /path/to/image_resizer/done

├── BikininjasPosters01/

│   ├── posters/- Add images or videos to the `input/` directory

│   │   ├── Poster1.png

│   │   ├── Poster2.mp4  ← Video!- Check that files have supported extensionsFound 4 file(s) in input:

│   │   ├── Poster3.png

│   │   ├── Poster4.png- Make sure files aren't in subdirectories  - 2 image(s)

│   │   └── Poster5.png

│   ├── tips/  - 2 video(s)

│   │   └── CustomTips.png

│   └── pack_info.txt**"Only X file(s) found, need at least 6"**  🖼️ landscape.jpg

└── BikininjasPosters02/

    └── ...  🎬 cool_animation.mp4

```

- Need minimum 6 files per pack  🖼️ portrait.png

### 5. Install in Game

- Add more files to `input/` directory  🎬 intro_video.avi

Copy pack folders to Lethal Company:

- Remaining files will be processed in next run

```

Lethal Company/BepInEx/plugins/Available poster slots:

├── BikininjasPosters01/

└── BikininjasPosters02/**"Video processing is slow"**  poster1 (IMAGE): 639x488 -> posters/Poster1.png

```

  poster2 (VIDEO): 730x490 -> posters/Poster2.mp4

---

- Normal for video encoding  poster3 (IMAGE): 749x1054 -> posters/Poster3.bmp

## 🎯 How It Works

- Use shorter clips (≤30 seconds recommended)  poster4 (IMAGE): 729x999 -> posters/Poster4.jpeg

### Intelligent Aspect Ratio Matching

- Consider lower resolution sources  poster5 (IMAGE): 552x769 -> posters/Poster5.png

Each file is matched to the poster slot with the closest aspect ratio:

- Progress is shown during encoding  customtips (IMAGE): 860x1219 -> tips/CustomTips.jpg

| Slot | Dimensions | Aspect Ratio | Orientation | Best For |

|------|-----------|--------------|-------------|----------|

| **Poster1** | 639×488 | 1.31:1 | Landscape | Wide images/videos |

| **Poster2** | 730×490 | 1.49:1 | Landscape | Wide images/videos |## 🛠️ Advanced Usage============================================================

| **Poster3** | 749×1054 | 0.71:1 | Portrait | Tall images/videos |

| **Poster4** | 729×999 | 0.73:1 | Portrait | Tall images/videos |Processing: cool_animation.mp4 (VIDEO)

| **Poster5** | 552×769 | 0.72:1 | Portrait | Tall images/videos |

| **CustomTips** | 860×1219 | 0.71:1 | Portrait | Tall images/videos |### Manual Python Environment============================================================



### Smart Cropping vs. PaddingWhich poster slot should this file fill?



**Old method (padding - ❌):**If you prefer to set up Python manually:Options: poster1, poster2, poster3, poster4, poster5, customtips

```

┌─────────────────┐Enter 'skip' to skip this file, 'quit' to exit

│                 │

│   ┌─────────┐   │```bashYour choice: poster2

│   │  Image  │   │ ← White bars

│   └─────────┘   │# Create virtual environmentProcessing video to 730x490...

│                 │

└─────────────────┘python3 -m venv venv  Loading video (this may take a moment)...

```

  Encoding video to MP4...

**New method (smart crop - ✅):**

```# Activate (Linux/macOS)✓ Saved: /path/to/BikininjasPosters/posters/Poster2.mp4

┌─────────────────┐

│                 │source venv/bin/activate  ↳ Moved to done: cool_animation.mp4

│     Image       │ ← Fills entire space

│    (cropped)    │ ← Centered crop```

│                 │

└─────────────────┘# Activate (Windows)

```

venv\Scripts\activate### Example 2: Auto Mode

### Video Processing

```bash

Videos are automatically converted to MP4:

- **Codec**: H.264 video, AAC audio# Install dependencies$ python poster_resizer.py --auto

- **Aspect Ratio**: Maintained with black bars

- **Quality**: Preserves original qualitypip install -r src/requirements.txt

- **Framerate**: Maintains original framerate

============================================================

---

# Run generator directly🎉 Processing complete! Processed 4 file(s).

## 🔧 Troubleshooting

python src/multi_pack_generator.py============================================================

### Windows Issues

```

**"Running scripts is disabled on this system"**

Processed files (moved to done/):

Open PowerShell as Administrator:

```powershell### Custom Options  ✓ cool_animation.mp4

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

```  ✓ landscape.jpg



**Python not added to PATH**All options can be passed to the wrappers:  ✓ portrait.png



Reboot after Python installation, or manually add Python to PATH.  ✓ intro_video.avi



### Linux/macOS Issues**Windows:**



**"Permission denied"**```powershellNext steps:

```bash

chmod +x bin/generate-packs.sh.\generate-packs.ps1 --max-packs 5 --base-name "CustomPack"1. Check the output files in:

```

```   - /path/to/BikininjasPosters/posters

**"sudo: command not found"**

   - /path/to/BikininjasPosters/tips

Log in as root or use your system's privilege escalation method.

**Linux/macOS:**2. Copy the entire BikininjasPosters folder to your Lethal Company mod directory

**Homebrew not found (macOS)**

```bash```bash3. Processed source files are in: /path/to/image_resizer/done

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```./generate-packs.sh --max-packs 5 --base-name "CustomPack"```



### General Issues```



**"No files found"**## License

- Add images/videos to `input/` directory

- Check file extensions are supported**Available Options:**

- Files must be directly in `input/`, not subdirectories

```This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images you process.

**"Only X file(s) found, need at least 6"**--input DIR           Input directory (default: input)

- Need minimum 6 files per pack--output DIR          Output directory (default: ../BepInEx/plugins)

- Add more files to `input/`--base-name NAME      Base pack name (default: BikininjasPosters)

- Remaining files processed in next run--max-packs N         Maximum packs to generate

--no-aspect           Disable aspect ratio maintenance

**"Video processing is slow"**--no-cleanup          Keep files in input/ directory

- Normal for video encoding--help                Show all options

- Use shorter clips (≤30 seconds recommended)```

- Consider lower resolution sources

- Progress shown during encoding## 📦 Distribution



---### Sharing with Others



## 💡 Tips for Best Results1. **Zip the entire `image_resizer` directory**

2. **Share with friends**

1. **Sort by Orientation**3. **They just run the wrapper scripts!**

   - Landscape (~1.3:1 to 1.5:1) → Poster1, Poster2

   - Portrait (~0.7:1 to 0.75:1) → Poster3, Poster4, Poster5, TipsNo manual setup required - the wrappers handle everything.



2. **Use High Resolution**### CI/CD Integration

   - Minimum: 1920×1080 (landscape), 1080×1920 (portrait)

   - Script downscales, so start high-resThe wrappers can be used in automated workflows:



3. **Mix Images and Videos**```bash

   - Videos great for animated posters# Exit code 0 = success, non-zero = failure

   - Keep videos short (≤30 seconds)./generate-packs.sh --max-packs 10 --no-cleanup

   - Any format auto-converts to MP4if [ $? -eq 0 ]; then

    echo "Success!"

4. **Batch Processing**fi

   - Process large collections in batches```

   - Use `--max-packs` to limit output

   - Run multiple times as needed## 🎉 Credits



---- **CustomPosters Mod**: [Thunderstore Link]

- **Lethal Company**: Zeekerss

## 🛠️ Advanced Usage- **Python**: Python Software Foundation

- **Libraries**: Pillow, moviepy, pillow-avif-plugin

### Manual Python Environment

## 📄 License

If you prefer manual setup:

This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images/videos you process.

```bash

# Create virtual environment---

python3 -m venv venv

**Ready to generate packs!** 🚀

# Activate

source venv/bin/activate  # Linux/macOSFor more information, see `MULTI_PACK_README.md` in the project directory.

venv\Scripts\activate     # Windows

# Install dependencies
pip install -r src/requirements.txt

# Run generator
python src/multi_pack_generator.py
```

### All Command-Line Options

```
--input DIR           Input directory (default: input)
--output DIR          Output directory (default: ../BepInEx/plugins)
--base-name NAME      Base pack name (default: BikininjasPosters)
--max-packs N         Maximum packs to generate
--no-aspect           Disable aspect ratio maintenance (stretch)
--no-cleanup          Keep files in input/ directory
--help                Show all options
```

### Example Workflows

**Process large batch in chunks:**
```bash
# Process 3 packs at a time
./generate-packs.sh --max-packs 3

# Review the output
ls -l ../BepInEx/plugins/

# Process next 3 packs
./generate-packs.sh --max-packs 3
```

**Custom pack names:**
```bash
./generate-packs.sh --base-name "HorrorPosters"
# Creates: HorrorPosters01, HorrorPosters02...
```

**Keep originals for reference:**
```bash
./generate-packs.sh --no-cleanup
# Files stay in input/ (not moved to done/)
```

---

## 📦 Sharing with Others

1. Zip the entire `image_resizer` directory
2. Share with friends
3. They just run the wrapper script!

No manual setup required - wrappers handle everything automatically.

---

## 📄 License

This tool is provided as-is for use with the CustomPosters mod. Please respect the original mod's license and the copyrights of any images/videos you process.

---

## 🎉 Credits

- **CustomPosters Mod**: [se3ya's CustomPosters](https://github.com/se3ya/CustomPosters)
- **Lethal Company**: Zeekerss
- **Python**: Python Software Foundation
- **Libraries**: Pillow, moviepy, pillow-avif-plugin

---

**🚀 Ready to generate packs!**

For technical details, see the source code in `src/` directory.
