# 젯슨 우분투 18.04.6 자동 서버 실행 가이드

## 🚀 빠른 시작

### 방법 1: 간단한 실행 (권장)
```bash
# 프로젝트 폴더에서
./quick_start.sh
```

### 방법 2: 상세한 실행
```bash
# 시스템 체크와 함께 실행
./start_server.sh
```

### 방법 3: 시스템 서비스로 설치 (부팅 시 자동 시작)
```bash
# 서비스 설치 (한 번만 실행)
sudo ./install_service.sh
```

## 📋 각 스크립트 설명

### 1. `quick_start.sh` - 간단한 실행
- **용도**: 빠르게 서버 시작
- **특징**: 최소한의 설정으로 즉시 실행
- **사용법**: `./quick_start.sh`

### 2. `start_server.sh` - 상세한 실행
- **용도**: 시스템 체크와 함께 안전하게 실행
- **특징**: 
  - 시스템 환경 확인
  - GPU 상태 확인
  - 포트 충돌 확인
  - 자동 패키지 설치
- **사용법**: `./start_server.sh`

### 3. `install_service.sh` - 시스템 서비스 설치
- **용도**: 부팅 시 자동으로 서버 시작
- **특징**:
  - systemd 서비스로 등록
  - 자동 재시작 기능
  - 로그 관리
- **사용법**: `sudo ./install_service.sh`

## 🔧 시스템 서비스 관리

### 서비스 설치 후 사용 명령어

```bash
# 서비스 시작
sudo systemctl start visionai-pro

# 서비스 중지
sudo systemctl stop visionai-pro

# 서비스 재시작
sudo systemctl restart visionai-pro

# 서비스 상태 확인
sudo systemctl status visionai-pro

# 서비스 로그 확인
sudo journalctl -u visionai-pro -f

# 서비스 비활성화 (부팅 시 자동 시작 안함)
sudo systemctl disable visionai-pro
```

## 🐛 문제 해결

### 1. 권한 오류
```bash
# 실행 권한 설정
chmod +x *.sh

# 소유권 확인
ls -la *.sh
```

### 2. 포트 충돌
```bash
# 포트 사용 확인
sudo netstat -tlnp | grep 8000

# 프로세스 종료
sudo kill -9 <PID>
```

### 3. 가상환경 문제
```bash
# 가상환경 재생성
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. GPU 문제
```bash
# GPU 상태 확인
nvidia-smi

# CUDA 확인
python3 -c "import torch; print(torch.cuda.is_available())"
```

## 📊 모니터링

### 실시간 모니터링
```bash
# GPU 사용량 모니터링
watch -n 1 nvidia-smi

# 시스템 리소스 모니터링
htop

# 서비스 로그 모니터링
sudo journalctl -u visionai-pro -f
```

### 로그 확인
```bash
# 애플리케이션 로그
tail -f logs/app.log

# 시스템 로그
sudo journalctl -xe
```

## 🔄 자동화 스크립트

### crontab을 이용한 자동 재시작
```bash
# crontab 편집
crontab -e

# 매일 새벽 3시에 재시작
0 3 * * * sudo systemctl restart visionai-pro
```

### 모니터링 스크립트
```bash
# 서비스 상태 확인 스크립트 생성
cat > check_service.sh << 'EOF'
#!/bin/bash
if ! systemctl is-active --quiet visionai-pro; then
    echo "Service is down, restarting..."
    sudo systemctl restart visionai-pro
    echo "Service restarted at $(date)" >> /home/jetson/service_restart.log
fi
EOF

chmod +x check_service.sh

# 5분마다 확인
*/5 * * * * /home/jetson/check_service.sh
```

## 🌐 접속 테스트

서버 실행 후 다음 방법으로 테스트:

```bash
# 로컬 접속
curl http://localhost:8000/

# 네트워크 접속 (젯슨 IP 확인 후)
curl http://<JETSON_IP>:8000/

# 웹 브라우저에서
http://<JETSON_IP>:8000/
```

## 📱 젯슨 IP 확인

```bash
# IP 주소 확인
ip addr show

# 또는
hostname -I

# 네트워크 인터페이스 확인
ifconfig
```

## 🔒 보안 설정

### 방화벽 설정
```bash
# 포트 8000 허용
sudo ufw allow 8000

# 방화벽 상태 확인
sudo ufw status
```

### SSL 설정 (선택사항)
```bash
# Let's Encrypt 인증서 설치
sudo apt install certbot

# 인증서 발급
sudo certbot certonly --standalone -d your-domain.com
```

## 📈 성능 최적화

### 젯슨 성능 모드 설정
```bash
# 성능 모드로 설정
sudo nvpmodel -m 0

# 현재 모드 확인
sudo nvpmodel -q
```

### 메모리 최적화
```bash
# 스왑 메모리 확인
free -h

# 스왑 메모리 생성 (필요시)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

## 🎯 추천 사용법

### 개발 환경
```bash
# 개발 시에는 간단한 실행
./quick_start.sh
```

### 프로덕션 환경
```bash
# 프로덕션에서는 시스템 서비스 사용
sudo ./install_service.sh
```

### 테스트 환경
```bash
# 테스트 시에는 상세한 실행
./start_server.sh
```

---

**참고**: 젯슨 환경에서는 GPU 메모리가 제한적이므로, 대용량 모델 사용 시 주의가 필요합니다.
