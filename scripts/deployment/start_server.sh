#!/bin/bash

# VisionAI Pro Image Classification System - Auto Start Script for Jetson
# Ubuntu 18.04.6 Compatible

set -e

# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

log_info "Starting VisionAI Pro Server on Jetson..."
log_info "Script directory: $SCRIPT_DIR"

# System check
check_system() {
    log_info "Checking system environment..."
    
    # Check Ubuntu version
    UBUNTU_VERSION=$(lsb_release -rs)
    log_info "Ubuntu version: $UBUNTU_VERSION"
    
    # Check Jetson
    if [ -f "/proc/device-tree/model" ]; then
        JETSON_MODEL=$(cat /proc/device-tree/model)
        log_info "Jetson model: $JETSON_MODEL"
    else
        log_warning "Not running on Jetson or model file not found"
    fi
    
    # Check GPU
    if command -v nvidia-smi &> /dev/null; then
        log_success "NVIDIA GPU detected"
        nvidia-smi --query-gpu=name,memory.total --format=csv,noheader,nounits
    else
        log_warning "NVIDIA GPU not detected"
    fi
    
    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        log_info "Python version: $PYTHON_VERSION"
    else
        log_error "Python3 not found!"
        exit 1
    fi
}

# Check and activate virtual environment
setup_environment() {
    log_info "Setting up Python environment..."
    
    if [ ! -d "venv" ]; then
        log_warning "Virtual environment not found. Creating..."
        python3 -m venv venv
    fi
    
    # Activate virtual environment
    source venv/bin/activate
    
    # Check package installation
    if ! python3 -c "import torch, fastapi, uvicorn" &> /dev/null; then
        log_warning "Required packages not found. Installing..."
        pip install -r requirements.txt
    fi
    
    log_success "Environment setup completed"
}

# Port check
check_port() {
    local PORT=${1:-8000}
    log_info "Checking port $PORT..."
    
    if netstat -tlnp | grep ":$PORT " > /dev/null; then
        log_warning "Port $PORT is already in use"
        netstat -tlnp | grep ":$PORT "
        return 1
    else
        log_success "Port $PORT is available"
        return 0
    fi
}

# Environment variables setup
setup_environment_variables() {
    log_info "Setting up environment variables..."
    
    export CUDA_VISIBLE_DEVICES=0
    export TF_FORCE_GPU_ALLOW_GROWTH=true
    export DEVICE=cuda
    export HOST=0.0.0.0
    export PORT=8000
    export ENVIRONMENT=production
    
    log_success "Environment variables set"
}

# Start server
start_server() {
    log_info "Starting VisionAI Pro server..."
    
    # Check port
    if ! check_port 8000; then
        log_error "Cannot start server: port 8000 is in use"
        exit 1
    fi
    
    # Start server
    if [ -f "run_jetson.py" ]; then
        log_info "Using Jetson optimized script..."
        python3 run_jetson.py
    elif [ -f "run.py" ]; then
        log_info "Using standard script..."
        python3 run.py
    else
        log_info "Using direct uvicorn..."
        uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --workers 1
    fi
}

# Main execution
main() {
    echo "=========================================="
    echo "  VisionAI Pro Server Auto Start Script"
    echo "  Jetson Ubuntu 18.04.6 Compatible"
    echo "=========================================="
    echo
    
    # System check
    check_system
    
    # Environment setup
    setup_environment
    
    # Environment variables setup
    setup_environment_variables
    
    # Start server
    start_server
}

# Execute script
main "$@"
