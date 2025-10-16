#!/usr/bin/env bash
################################################################################
# CustomPosters Multi-Pack Generator - Linux/macOS Wrapper
################################################################################
# 
# This script automatically sets up Python environment and runs the 
# multi-pack generator for CustomPosters mod.
#
# Usage:
#   ./generate-packs.sh [options]
#
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR"
SRC_DIR="$PROJECT_DIR/src"
VENV_DIR="$PROJECT_DIR/venv"

################################################################################
# Helper Functions
################################################################################

print_header() {
    echo -e "${BLUE}"
    echo "╔════════════════════════════════════════════════════════════════════╗"
    echo "║        CustomPosters Multi-Pack Generator - Setup Script          ║"
    echo "╚════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

################################################################################
# Check Python Installation
################################################################################

check_python() {
    print_info "Checking Python installation..."
    
    # Try to find Python 3
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
        PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
        print_success "Found Python $PYTHON_VERSION"
        return 0
    elif command -v python &> /dev/null; then
        # Check if 'python' is Python 3
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        PYTHON_MAJOR=$(echo "$PYTHON_VERSION" | cut -d. -f1)
        if [ "$PYTHON_MAJOR" = "3" ]; then
            PYTHON_CMD="python"
            print_success "Found Python $PYTHON_VERSION"
            return 0
        fi
    fi
    
    return 1
}

################################################################################
# Install Python (if needed)
################################################################################

install_python() {
    print_warning "Python 3 not found. Attempting to install..."
    
    # Detect OS
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        if command -v apt-get &> /dev/null; then
            # Debian/Ubuntu
            print_info "Detected Debian/Ubuntu. Installing Python..."
            sudo apt-get update
            sudo apt-get install -y python3 python3-pip python3-venv
            print_success "Python installed successfully"
        elif command -v dnf &> /dev/null; then
            # Fedora
            print_info "Detected Fedora. Installing Python..."
            sudo dnf install -y python3 python3-pip
            print_success "Python installed successfully"
        elif command -v yum &> /dev/null; then
            # CentOS/RHEL
            print_info "Detected CentOS/RHEL. Installing Python..."
            sudo yum install -y python3 python3-pip
            print_success "Python installed successfully"
        elif command -v pacman &> /dev/null; then
            # Arch Linux
            print_info "Detected Arch Linux. Installing Python..."
            sudo pacman -S --noconfirm python python-pip
            print_success "Python installed successfully"
        else
            print_error "Unable to detect package manager"
            print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            print_info "Installing Python via Homebrew..."
            brew install python3
            print_success "Python installed successfully"
        else
            print_error "Homebrew not found"
            print_info "Install Homebrew from: https://brew.sh/"
            print_info "Or install Python from: https://www.python.org/downloads/"
            exit 1
        fi
    else
        print_error "Unsupported operating system: $OSTYPE"
        print_info "Please install Python 3.7+ manually from: https://www.python.org/downloads/"
        exit 1
    fi
}

################################################################################
# Setup Virtual Environment
################################################################################

setup_venv() {
    print_info "Setting up virtual environment..."
    
    if [ -d "$VENV_DIR" ]; then
        print_success "Virtual environment already exists"
    else
        print_info "Creating virtual environment..."
        $PYTHON_CMD -m venv "$VENV_DIR"
        print_success "Virtual environment created"
    fi
}

################################################################################
# Install Dependencies
################################################################################

install_dependencies() {
    print_info "Installing Python dependencies..."
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Upgrade pip
    pip install --upgrade pip > /dev/null 2>&1
    
    # Install requirements
    if [ -f "$SRC_DIR/requirements.txt" ]; then
        pip install -r "$SRC_DIR/requirements.txt"
        print_success "Dependencies installed successfully"
    else
        print_error "requirements.txt not found at $SRC_DIR/requirements.txt"
        exit 1
    fi
}

################################################################################
# Run Generator
################################################################################

run_generator() {
    print_info "Starting Multi-Pack Generator..."
    echo ""
    
    # Activate virtual environment
    source "$VENV_DIR/bin/activate"
    
    # Change to project directory
    cd "$PROJECT_DIR"
    
    # Run the generator with all passed arguments
    python "$SRC_DIR/multi_pack_generator.py" "$@"
    
    exit_code=$?
    echo ""
    if [ $exit_code -eq 0 ]; then
        print_success "Pack generation completed successfully!"
    else
        print_error "Pack generation failed with exit code $exit_code"
    fi
    
    return $exit_code
}

################################################################################
# Main
################################################################################

main() {
    print_header
    
    # Check if Python is installed
    if ! check_python; then
        install_python
        # Re-check after installation
        if ! check_python; then
            print_error "Python installation failed"
            exit 1
        fi
    fi
    
    # Setup virtual environment
    setup_venv
    
    # Install dependencies
    install_dependencies
    
    # Run the generator
    run_generator "$@"
}

# Run main function with all script arguments
main "$@"
