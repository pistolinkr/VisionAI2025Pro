# 엔비디아 젯슨 실행 가이드

## 📋 사전 요구사항

### 1. 시스템 확인
```bash
# 젯슨 모델 확인
cat /proc/device-tree/model

# GPU 상태 확인
nvidia-smi

# Python 버전 확인
python3 --version
```

### 2. 시스템 업데이트
```bash
# 시스템 패키지 업데이트
sudo apt update && sudo apt upgrade -y

# 필요한 시스템 패키지 설치
sudo apt install -y python3-pip python3-venv git
```

## 🚀 설치 및 실행

### 1. 프로젝트 클론 및 설정
```bash
# 프로젝트 디렉토리로 이동
cd /path/to/your/project

# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate
```

### 2. 의존성 설치
```bash
# 기본 패키지 설치
pip install -r requirements.txt

# 젯슨용 추가 패키지 (필요시)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 3. 환경 변수 설정
```bash
# 환경 변수 설정
export CUDA_VISIBLE_DEVICES=0
export TF_FORCE_GPU_ALLOW_GROWTH=true
export DEVICE=cuda
```

### 4. 서버 실행

#### 방법 1: 젯슨 최적화 스크립트 사용 (권장)
```bash
# 젯슨용 실행 스크립트 실행
python3 run_jetson.py
```

#### 방법 2: 기본 실행 스크립트 사용
```bash
# 기본 실행 스크립트 실행
python3 run.py
```

#### 방법 3: 직접 uvicorn 실행
```bash
# 직접 uvicorn으로 실행
uvicorn src.api.main:app --host 0.0.0.0 --port 8000 --workers 1
```

## 🔧 젯슨 특화 설정

### 1. GPU 메모리 최적화
```bash
# GPU 메모리 사용량 확인
nvidia-smi

# GPU 메모리 캐시 정리 (필요시)
sudo fuser -v /dev/nvidia*
```

### 2. 성능 모니터링
```bash
# 실시간 GPU 모니터링
watch -n 1 nvidia-smi

# 시스템 리소스 모니터링
htop
```

### 3. 네트워크 설정
```bash
# 방화벽 설정 (필요시)
sudo ufw allow 8000

# 포트 사용 확인
netstat -tlnp | grep 8000
```

## 🐛 문제 해결

### 1. CUDA 관련 오류
```bash
# CUDA 버전 확인
nvcc --version

# PyTorch CUDA 지원 확인
python3 -c "import torch; print(torch.cuda.is_available())"
```

### 2. 메모리 부족 오류
```bash
# 스왑 메모리 확인
free -h

# 스왑 메모리 생성 (필요시)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```

### 3. 포트 충돌
```bash
# 포트 사용 프로세스 확인
sudo lsof -i :8000

# 프로세스 종료
sudo kill -9 <PID>
```

## 📊 성능 최적화 팁

### 1. 모델 최적화
- TensorRT 변환 고려
- 모델 양자화 적용
- 배치 크기 조정

### 2. 시스템 최적화
- 불필요한 서비스 비활성화
- CPU 주파수 설정
- 메모리 사용량 모니터링

### 3. 네트워크 최적화
- 로컬 네트워크 사용
- 대역폭 모니터링
- 연결 풀 설정

## 🔍 로그 확인

```bash
# 애플리케이션 로그 확인
tail -f logs/app.log

# 시스템 로그 확인
journalctl -f

# GPU 로그 확인
dmesg | grep nvidia
```

## 📱 접속 테스트

서버 실행 후 다음 URL로 접속하여 테스트:

```bash
# 로컬 접속
curl http://localhost:8000/

# 네트워크 접속 (젯슨 IP 확인 후)
curl http://<JETSON_IP>:8000/
```

## 🛠️ 추가 도구

### 1. 시스템 모니터링
```bash
# 설치
sudo apt install htop iotop

# 실행
htop
iotop
```

### 2. 네트워크 모니터링
```bash
# 설치
sudo apt install iftop

# 실행
sudo iftop
```

### 3. GPU 모니터링
```bash
# 설치
sudo apt install nvtop

# 실행
nvtop
```

## 📞 지원

문제가 발생하면 다음을 확인하세요:

1. 로그 파일: `logs/app.log`
2. 시스템 로그: `journalctl -xe`
3. GPU 상태: `nvidia-smi`
4. 네트워크 상태: `netstat -tlnp`

---

**참고**: 젯슨 환경에서는 GPU 메모리가 제한적이므로, 대용량 모델 사용 시 주의가 필요합니다.
