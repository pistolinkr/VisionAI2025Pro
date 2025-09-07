# NVIDIA Jetson Setup Guide

## 📋 Prerequisites

### 1. System Check
```bash
# Check Jetson model
cat /proc/device-tree/model

# Check GPU status
nvidia-smi

# Check Python version
python3 --version
```

### 2. System Update
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install required system packages
sudo apt install -y python3-pip python3-venv git
```

## 🚀 Installation and Execution

### 1. Project Clone and Setup
```bash
# Navigate to project directory
cd /path/to/your/project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

### 2. Install Dependencies
```bash
# Install basic packages
pip install -r config/requirements.txt

# Additional packages for Jetson (if needed)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 3. Environment Variables Setup
```bash
# Create .env file
cp config/env_example.txt .env

# Edit .env file
nano .env
```

### 4. Server Execution
```bash
# Run Zero-shot server (recommended)
python3 main.py zero-shot

# Or run with Jetson optimization
python3 scripts/deployment/run_jetson.py
```

## 🔧 Jetson-Specific Optimizations

### 1. GPU Memory Management
```bash
# Set GPU memory growth
export TF_FORCE_GPU_ALLOW_GROWTH=true

# Set CUDA device
export CUDA_VISIBLE_DEVICES=0
```

### 2. Performance Tuning
```bash
# Set maximum power mode
sudo nvpmodel -m 0

# Set maximum clock speeds
sudo jetson_clocks
```

### 3. Thermal Management
```bash
# Monitor temperature
tegrastats

# Set fan control
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```

## 🧪 Testing

### 1. Basic Functionality Test
```bash
# Test server startup
python3 scripts/testing/test_all_servers.py

# Test GPU availability
python3 -c "import torch; print(torch.cuda.is_available())"
```

### 2. Performance Test
```bash
# Run performance benchmark
python3 scripts/testing/test_system.py

# Monitor resource usage
htop
```

## 🚨 Troubleshooting

### Common Issues
1. **CUDA not available**: Check NVIDIA drivers and CUDA installation
2. **Memory errors**: Reduce batch size or use CPU mode
3. **Thermal throttling**: Check temperature and fan settings
4. **Slow performance**: Enable maximum power mode

### Debug Commands
```bash
# Check GPU status
nvidia-smi

# Check memory usage
free -h

# Check temperature
cat /sys/class/thermal/thermal_zone*/temp
```

## 📊 Performance Optimization

### 1. Model Optimization
- Use TensorRT for inference acceleration
- Enable mixed precision training
- Optimize batch sizes for Jetson memory

### 2. System Optimization
- Use SSD storage for better I/O performance
- Enable swap file for memory management
- Optimize power settings for sustained performance

---

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
pip install -r config/requirements.txt

# 젯슨용 추가 패키지 (필요시)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 3. 환경 변수 설정
```bash
# .env 파일 생성
cp config/env_example.txt .env

# .env 파일 편집
nano .env
```

### 4. 서버 실행
```bash
# Zero-shot 서버 실행 (추천)
python3 main.py zero-shot

# 또는 젯슨 최적화로 실행
python3 scripts/deployment/run_jetson.py
```

## 🔧 젯슨 전용 최적화

### 1. GPU 메모리 관리
```bash
# GPU 메모리 증가 설정
export TF_FORCE_GPU_ALLOW_GROWTH=true

# CUDA 디바이스 설정
export CUDA_VISIBLE_DEVICES=0
```

### 2. 성능 튜닝
```bash
# 최대 전력 모드 설정
sudo nvpmodel -m 0

# 최대 클럭 속도 설정
sudo jetson_clocks
```

### 3. 열 관리
```bash
# 온도 모니터링
tegrastats

# 팬 제어 설정
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```

## 🧪 테스트

### 1. 기본 기능 테스트
```bash
# 서버 시작 테스트
python3 scripts/testing/test_all_servers.py

# GPU 사용 가능성 테스트
python3 -c "import torch; print(torch.cuda.is_available())"
```

### 2. 성능 테스트
```bash
# 성능 벤치마크 실행
python3 scripts/testing/test_system.py

# 리소스 사용량 모니터링
htop
```

## 🚨 문제 해결

### 일반적인 문제
1. **CUDA 사용 불가**: NVIDIA 드라이버 및 CUDA 설치 확인
2. **메모리 오류**: 배치 크기 줄이기 또는 CPU 모드 사용
3. **열 스로틀링**: 온도 및 팬 설정 확인
4. **느린 성능**: 최대 전력 모드 활성화

### 디버그 명령어
```bash
# GPU 상태 확인
nvidia-smi

# 메모리 사용량 확인
free -h

# 온도 확인
cat /sys/class/thermal/thermal_zone*/temp
```

## 📊 성능 최적화

### 1. 모델 최적화
- 추론 가속을 위해 TensorRT 사용
- 혼합 정밀도 훈련 활성화
- 젯슨 메모리에 맞게 배치 크기 최적화

### 2. 시스템 최적화
- 더 나은 I/O 성능을 위해 SSD 스토리지 사용
- 메모리 관리를 위해 스왑 파일 활성화
- 지속적인 성능을 위해 전력 설정 최적화

---

# NVIDIA Jetson 设置指南

## 📋 先决条件

### 1. 系统检查
```bash
# 检查Jetson型号
cat /proc/device-tree/model

# 检查GPU状态
nvidia-smi

# 检查Python版本
python3 --version
```

### 2. 系统更新
```bash
# 更新系统包
sudo apt update && sudo apt upgrade -y

# 安装必需的系统包
sudo apt install -y python3-pip python3-venv git
```

## 🚀 安装和执行

### 1. 项目克隆和设置
```bash
# 导航到项目目录
cd /path/to/your/project

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate
```

### 2. 安装依赖
```bash
# 安装基本包
pip install -r config/requirements.txt

# Jetson额外包（如需要）
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

### 3. 环境变量设置
```bash
# 创建.env文件
cp config/env_example.txt .env

# 编辑.env文件
nano .env
```

### 4. 服务器执行
```bash
# 运行零样本服务器（推荐）
python3 main.py zero-shot

# 或使用Jetson优化运行
python3 scripts/deployment/run_jetson.py
```

## 🔧 Jetson特定优化

### 1. GPU内存管理
```bash
# 设置GPU内存增长
export TF_FORCE_GPU_ALLOW_GROWTH=true

# 设置CUDA设备
export CUDA_VISIBLE_DEVICES=0
```

### 2. 性能调优
```bash
# 设置最大功率模式
sudo nvpmodel -m 0

# 设置最大时钟速度
sudo jetson_clocks
```

### 3. 热管理
```bash
# 监控温度
tegrastats

# 设置风扇控制
sudo sh -c 'echo 255 > /sys/devices/pwm-fan/target_pwm'
```

## 🧪 测试

### 1. 基本功能测试
```bash
# 测试服务器启动
python3 scripts/testing/test_all_servers.py

# 测试GPU可用性
python3 -c "import torch; print(torch.cuda.is_available())"
```

### 2. 性能测试
```bash
# 运行性能基准测试
python3 scripts/testing/test_system.py

# 监控资源使用
htop
```

## 🚨 故障排除

### 常见问题
1. **CUDA不可用**：检查NVIDIA驱动程序和CUDA安装
2. **内存错误**：减少批处理大小或使用CPU模式
3. **热节流**：检查温度和风扇设置
4. **性能慢**：启用最大功率模式

### 调试命令
```bash
# 检查GPU状态
nvidia-smi

# 检查内存使用
free -h

# 检查温度
cat /sys/class/thermal/thermal_zone*/temp
```

## 📊 性能优化

### 1. 模型优化
- 使用TensorRT进行推理加速
- 启用混合精度训练
- 为Jetson内存优化批处理大小

### 2. 系统优化
- 使用SSD存储以获得更好的I/O性能
- 启用交换文件进行内存管理
- 为持续性能优化电源设置