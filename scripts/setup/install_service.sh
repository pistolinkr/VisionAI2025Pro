#!/bin/bash

# VisionAI Pro Service Installation Script for Jetson Ubuntu 18.04.6

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

# Check current user
CURRENT_USER=$(whoami)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log_info "Installing VisionAI Pro Service..."
log_info "Current user: $CURRENT_USER"
log_info "Project directory: $PROJECT_DIR"

# Set service file path
SERVICE_FILE="/etc/systemd/system/visionai-pro.service"

# Create service file
create_service_file() {
    log_info "Creating service file..."
    
    cat > "$SERVICE_FILE" << EOF
[Unit]
Description=VisionAI Pro Image Classification Server
After=network.target
Wants=network.target

[Service]
Type=simple
User=$CURRENT_USER
Group=$CURRENT_USER
WorkingDirectory=$PROJECT_DIR
Environment=PATH=$PROJECT_DIR/venv/bin
Environment=CUDA_VISIBLE_DEVICES=0
Environment=TF_FORCE_GPU_ALLOW_GROWTH=true
Environment=DEVICE=cuda
Environment=HOST=0.0.0.0
Environment=PORT=8000
Environment=ENVIRONMENT=production
ExecStart=$PROJECT_DIR/venv/bin/python3 $PROJECT_DIR/run_jetson.py
ExecReload=/bin/kill -HUP \$MAINPID
Restart=always
RestartSec=10
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
EOF

    log_success "Service file created at $SERVICE_FILE"
}

# Install service
install_service() {
    log_info "Installing systemd service..."
    
    # Reload systemd
    sudo systemctl daemon-reload
    
    # Enable service
    sudo systemctl enable visionai-pro.service
    
    log_success "Service installed and enabled"
}

# Set permissions
set_permissions() {
    log_info "Setting file permissions..."
    
    # Set execute permissions
    chmod +x start_server.sh
    chmod +x run_jetson.py
    
    # Create log directory
    mkdir -p logs
    chmod 755 logs
    
    log_success "Permissions set"
}

# Check service status
check_service() {
    log_info "Checking service status..."
    
    sudo systemctl status visionai-pro.service --no-pager -l
}

# Start service
start_service() {
    log_info "Starting VisionAI Pro service..."
    
    sudo systemctl start visionai-pro.service
    
    # Wait briefly then check status
    sleep 3
    check_service
}

# Main execution
main() {
    echo "=========================================="
    echo "  VisionAI Pro Service Installation"
    echo "  Jetson Ubuntu 18.04.6"
    echo "=========================================="
    echo
    
    # Create service file
    create_service_file
    
    # Install service
    install_service
    
    # Set permissions
    set_permissions
    
    # Start service
    start_service
    
    echo
    log_success "Installation completed!"
    echo
    echo "Service commands:"
    echo "  Start:   sudo systemctl start visionai-pro"
    echo "  Stop:    sudo systemctl stop visionai-pro"
    echo "  Restart: sudo systemctl restart visionai-pro"
    echo "  Status:  sudo systemctl status visionai-pro"
    echo "  Logs:    sudo journalctl -u visionai-pro -f"
    echo
    echo "The service will start automatically on boot."
}

# Execute script
main "$@"
