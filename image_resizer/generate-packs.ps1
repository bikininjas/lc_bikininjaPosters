################################################################################
# CustomPosters Multi-Pack Generator - Windows PowerShell Wrapper
################################################################################
# 
# This script automatically sets up Python environment and runs the 
# multi-pack generator for CustomPosters mod on Windows.
#
# Usage:
#   .\generate-packs.ps1 [options]
#   
# Examples:
#   .\generate-packs.ps1
#   .\generate-packs.ps1 --max-packs 5
#   .\generate-packs.ps1 --base-name "MyPosters"
#
################################################################################

# Ensure script stops on errors
$ErrorActionPreference = "Stop"

# Script paths
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectDir = Split-Path -Parent $ScriptDir
$SrcDir = Join-Path $ProjectDir "src"
$VenvDir = Join-Path $ProjectDir "venv"

################################################################################
# Helper Functions
################################################################################

function Write-Header {
    Write-Host ""
    Write-Host "╔════════════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
    Write-Host "║        CustomPosters Multi-Pack Generator - Setup Script          ║" -ForegroundColor Cyan
    Write-Host "╚════════════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
    Write-Host ""
}

function Write-Success {
    param([string]$Message)
    Write-Host "✓ $Message" -ForegroundColor Green
}

function Write-Error-Custom {
    param([string]$Message)
    Write-Host "✗ $Message" -ForegroundColor Red
}

function Write-Info {
    param([string]$Message)
    Write-Host "ℹ $Message" -ForegroundColor Cyan
}

function Write-Warning-Custom {
    param([string]$Message)
    Write-Host "⚠ $Message" -ForegroundColor Yellow
}

################################################################################
# Check Python Installation
################################################################################

function Test-PythonInstalled {
    Write-Info "Checking Python installation..."
    
    # Try to find Python in PATH
    $pythonCmd = $null
    
    # Check python3 first
    if (Get-Command python3 -ErrorAction SilentlyContinue) {
        $pythonCmd = "python3"
    }
    # Check python
    elseif (Get-Command python -ErrorAction SilentlyContinue) {
        $pythonCmd = "python"
    }
    
    if ($pythonCmd) {
        try {
            $version = & $pythonCmd --version 2>&1 | Out-String
            if ($version -match "Python (\d+)\.(\d+)\.(\d+)") {
                $major = [int]$Matches[1]
                $minor = [int]$Matches[2]
                
                if ($major -eq 3 -and $minor -ge 7) {
                    Write-Success "Found Python $($Matches[1]).$($Matches[2]).$($Matches[3])"
                    return $pythonCmd
                }
                else {
                    Write-Warning-Custom "Found Python $($Matches[1]).$($Matches[2]), but need Python 3.7+"
                }
            }
        }
        catch {
            Write-Warning-Custom "Error checking Python version: $_"
        }
    }
    
    return $null
}

################################################################################
# Install Python (Windows)
################################################################################

function Install-Python {
    Write-Warning-Custom "Python 3.7+ not found. Installation required."
    Write-Info "Opening Python download page in browser..."
    
    # Open Python download page
    Start-Process "https://www.python.org/downloads/"
    
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host "  MANUAL INSTALLATION REQUIRED" -ForegroundColor Yellow
    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please download and install Python 3.7 or higher from the browser window." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "IMPORTANT: During installation, make sure to:" -ForegroundColor Yellow
    Write-Host "  ☑ Check 'Add Python to PATH'" -ForegroundColor Yellow
    Write-Host "  ☑ Check 'Install pip'" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "After installation, close this window and run the script again." -ForegroundColor Yellow
    Write-Host ""
    Write-Host "═══════════════════════════════════════════════════════════════════" -ForegroundColor Yellow
    Write-Host ""
    
    Read-Host "Press Enter to exit"
    exit 1
}

################################################################################
# Setup Virtual Environment
################################################################################

function Setup-VirtualEnvironment {
    param([string]$PythonCmd)
    
    Write-Info "Setting up virtual environment..."
    
    if (Test-Path $VenvDir) {
        Write-Success "Virtual environment already exists"
    }
    else {
        Write-Info "Creating virtual environment..."
        & $PythonCmd -m venv $VenvDir
        if ($LASTEXITCODE -ne 0) {
            Write-Error-Custom "Failed to create virtual environment"
            exit 1
        }
        Write-Success "Virtual environment created"
    }
}

################################################################################
# Install Dependencies
################################################################################

function Install-Dependencies {
    Write-Info "Installing Python dependencies..."
    
    # Activate virtual environment
    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
    
    if (Test-Path $activateScript) {
        & $activateScript
    }
    else {
        Write-Error-Custom "Virtual environment activation script not found"
        exit 1
    }
    
    # Upgrade pip
    python -m pip install --upgrade pip --quiet
    
    # Install requirements
    $requirementsFile = Join-Path $SrcDir "requirements.txt"
    if (Test-Path $requirementsFile) {
        pip install -r $requirementsFile
        if ($LASTEXITCODE -ne 0) {
            Write-Error-Custom "Failed to install dependencies"
            exit 1
        }
        Write-Success "Dependencies installed successfully"
    }
    else {
        Write-Error-Custom "requirements.txt not found at $requirementsFile"
        exit 1
    }
}

################################################################################
# Run Generator
################################################################################

function Run-Generator {
    param([string[]]$Arguments)
    
    Write-Info "Starting Multi-Pack Generator..."
    Write-Host ""
    
    # Activate virtual environment
    $activateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
    & $activateScript
    
    # Change to project directory
    Set-Location $ProjectDir
    
    # Run the generator with all passed arguments
    $generatorScript = Join-Path $SrcDir "multi_pack_generator.py"
    
    if ($Arguments.Count -gt 0) {
        & python $generatorScript $Arguments
    }
    else {
        & python $generatorScript
    }
    
    $exitCode = $LASTEXITCODE
    
    Write-Host ""
    if ($exitCode -eq 0) {
        Write-Success "Pack generation completed successfully!"
    }
    else {
        Write-Error-Custom "Pack generation failed with exit code $exitCode"
    }
    
    return $exitCode
}

################################################################################
# Main
################################################################################

function Main {
    param([string[]]$ScriptArgs)
    
    Write-Header
    
    # Check if Python is installed
    $pythonCmd = Test-PythonInstalled
    
    if (-not $pythonCmd) {
        Install-Python
        # Script will exit in Install-Python
    }
    
    # Setup virtual environment
    Setup-VirtualEnvironment -PythonCmd $pythonCmd
    
    # Install dependencies
    Install-Dependencies
    
    # Run the generator
    $exitCode = Run-Generator -Arguments $ScriptArgs
    
    # Pause before exit so user can see results
    Write-Host ""
    Write-Host "Press any key to exit..." -ForegroundColor Gray
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    
    exit $exitCode
}

# Run main function with all script arguments
Main -ScriptArgs $args
