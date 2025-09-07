#!/bin/bash

# VisionAI Pro - 완전 재설치 스크립트 (Ubuntu 18.04)
# 기존 설치를 완전히 삭제하고 깨끗하게 재설치합니다

set -e  # 에러 발생시 스크립트 중단

echo "🗑️ VisionAI Pro 완전 재설치를 시작합니다..."

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

# 기존 설치 확인 및 삭제
if [ -d "VisionAI2025Pro" ]; then
    log_warning "기존 VisionAI2025Pro 디렉토리를 발견했습니다."
    read -p "기존 설치를 완전히 삭제하고 재설치하시겠습니까? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        log_info "기존 설치를 삭제합니다..."
        sudo rm -rf VisionAI2025Pro
        log_success "기존 설치가 삭제되었습니다."
    else
        log_info "설치를 취소합니다."
        exit 0
    fi
fi

# 시스템 업데이트
log_info "시스템 패키지를 업데이트합니다..."
sudo apt update && sudo apt upgrade -y

# Python 3 설치 (우분투 18.04 기본 Python 3 사용)
log_info "Python 3를 설치합니다..."
sudo apt install software-properties-common -y
sudo apt install python3 python3-venv python3-dev python3-pip -y

# 필수 시스템 패키지 설치
log_info "필수 시스템 패키지를 설치합니다..."
sudo apt install git build-essential libssl-dev libffi-dev python3-dev curl wget -y

# 프로젝트 클론
log_info "GitHub에서 프로젝트를 클론합니다..."
git clone https://github.com/pistolinkr/VisionAI2025Pro.git

cd VisionAI2025Pro

# 가상환경 생성
log_info "Python 가상환경을 생성합니다..."
python3 -m venv venv

# 가상환경 활성화
log_info "가상환경을 활성화합니다..."
source venv/bin/activate

# pip 업그레이드
log_info "pip을 업그레이드합니다..."
pip install --upgrade pip

# 의존성 설치 (우분투 18.04 호환 버전)
log_info "Python 의존성을 설치합니다..."
if [ -f "config/requirements_ubuntu18.txt" ]; then
    log_info "우분투 18.04 호환 버전을 사용합니다..."
    pip install -r config/requirements_ubuntu18.txt
else
    log_warning "기본 requirements.txt를 사용합니다..."
    pip install -r config/requirements.txt
fi

# 환경 변수 설정
log_info "환경 변수를 설정합니다..."
if [ ! -f ".env" ]; then
    cp config/env_example.txt .env
    log_success "환경 변수 파일(.env)이 생성되었습니다."
else
    log_warning "환경 변수 파일(.env)이 이미 존재합니다."
fi

# 실행 권한 부여
chmod +x run.py
chmod +x scripts/deployment/run*.py
chmod +x *.sh

log_success "완전 재설치가 완료되었습니다!"
echo ""
echo "🎉 VisionAI Pro가 성공적으로 재설치되었습니다!"
echo ""
echo "📋 사용 가능한 서버:"
echo "   • 기본 서버 (포트 8000): python3 run.py"
echo "   • 고성능 서버 (포트 8001): python3 scripts/deployment/run_advanced.py"
echo "   • Zero-shot 서버 (포트 8002): python3 scripts/deployment/run_zero_shot.py ⭐ 추천"
echo ""
echo "🚀 서버 실행 방법:"
echo "   source venv/bin/activate"
echo "   python3 scripts/deployment/run_zero_shot.py"
echo ""
echo "🌐 웹 인터페이스:"
echo "   http://서버IP:8002"
echo ""

# 서버 실행 여부 확인
read -p "지금 바로 Zero-shot 서버를 실행하시겠습니까? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    log_info "Zero-shot 서버를 시작합니다..."
    log_warning "서버를 중지하려면 Ctrl+C를 누르세요"
    echo ""
    python3 scripts/deployment/run_zero_shot.py
fi
