#!/bin/bash

# VisionAI Pro Service Installation Script for Jetson Ubuntu 18.04.6

set -e

# 색상 정의
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 로그 함수
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

# 현재 사용자 확인
CURRENT_USER=$(whoami)
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

log_info "Installing VisionAI Pro Service..."
log_info "Current user: $CURRENT_USER"
log_info "Project directory: $PROJECT_DIR"

# 서비스 파일 경로 설정
SERVICE_FILE="/etc/systemd/system/visionai-pro.service"

# 서비스 파일 생성
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

# 서비스 설치
install_service() {
    log_info "Installing systemd service..."
    
    # systemd 리로드
    sudo systemctl daemon-reload
    
    # 서비스 활성화
    sudo systemctl enable visionai-pro.service
    
    log_success "Service installed and enabled"
}

# 권한 설정
set_permissions() {
    log_info "Setting file permissions..."
    
    # 실행 권한 설정
    chmod +x start_server.sh
    chmod +x run_jetson.py
    
    # 로그 디렉토리 생성
    mkdir -p logs
    chmod 755 logs
    
    log_success "Permissions set"
}

# 서비스 상태 확인
check_service() {
    log_info "Checking service status..."
    
    sudo systemctl status visionai-pro.service --no-pager -l
}

# 서비스 시작
start_service() {
    log_info "Starting VisionAI Pro service..."
    
    sudo systemctl start visionai-pro.service
    
    # 잠시 대기 후 상태 확인
    sleep 3
    check_service
}

# 메인 실행
main() {
    echo "=========================================="
    echo "  VisionAI Pro Service Installation"
    echo "  Jetson Ubuntu 18.04.6"
    echo "=========================================="
    echo
    
    # 서비스 파일 생성
    create_service_file
    
    # 서비스 설치
    install_service
    
    # 권한 설정
    set_permissions
    
    # 서비스 시작
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

# 스크립트 실행
main "$@"
