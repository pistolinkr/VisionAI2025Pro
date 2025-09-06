# Jetson Ubuntu 18.04.6 Auto Server Startup Guide

## 🚀 Quick Start

### Method 1: Simple Execution (Recommended)
```bash
# From project folder
python3 main.py zero-shot
```

### Method 2: Detailed Execution
```bash
# Run with system check
./scripts/deployment/start_zero_shot.sh
```

### Method 3: Install as System Service (Auto-start on boot)
```bash
# Install service (run once only)
sudo ./scripts/setup/install_service.sh
```

## 📋 Script Descriptions

### 1. `main.py zero-shot` - Simple Execution
- **Purpose**: Quick server startup
- **Features**: Immediate execution with minimal setup
- **Usage**: `python3 main.py zero-shot`

### 2. `start_zero_shot.sh` - Detailed Execution
- **Purpose**: Safe execution with system check
- **Features**: 
  - System environment verification
  - GPU status check
  - Port conflict check
  - Automatic package installation
- **Usage**: `./scripts/deployment/start_zero_shot.sh`

### 3. `install_service.sh` - System Service Installation
- **Purpose**: Auto-start server on boot
- **Features**:
  - Register as systemd service
  - Auto-restart functionality
  - Log management
- **Usage**: `sudo ./scripts/setup/install_service.sh`

## 🔧 System Service Management

### Commands After Service Installation

```bash
# Start service
sudo systemctl start visionai-pro

# Stop service
sudo systemctl stop visionai-pro

# Restart service
sudo systemctl restart visionai-pro

# Check service status
sudo systemctl status visionai-pro

# Enable auto-start on boot
sudo systemctl enable visionai-pro

# Disable auto-start on boot
sudo systemctl disable visionai-pro

# View service logs
sudo journalctl -u visionai-pro -f
```

## 🧪 Testing

### 1. Manual Test
```bash
# Test server startup
python3 scripts/testing/test_all_servers.py

# Test web interface
curl http://localhost:8002/health
```

### 2. Service Test
```bash
# Start service
sudo systemctl start visionai-pro

# Check if running
sudo systemctl status visionai-pro

# Test API
curl http://localhost:8002/api/categories
```

## 🚨 Troubleshooting

### Common Issues
1. **Service won't start**: Check file permissions and paths
2. **Port conflict**: Change port in configuration
3. **Permission denied**: Run with sudo for service installation
4. **GPU not detected**: Check NVIDIA drivers

### Debug Commands
```bash
# Check service logs
sudo journalctl -u visionai-pro --no-pager

# Check system resources
htop

# Check GPU status
nvidia-smi

# Check port usage
sudo netstat -tlnp | grep 8002
```

## 📊 Performance Monitoring

### Resource Monitoring
```bash
# Monitor CPU and memory
htop

# Monitor GPU
watch -n 1 nvidia-smi

# Monitor temperature
tegrastats
```

### Log Monitoring
```bash
# Real-time service logs
sudo journalctl -u visionai-pro -f

# Application logs
tail -f logs/app.log
```

---

# 젯슨 우분투 18.04.6 자동 서버 실행 가이드

## 🚀 빠른 시작

### 방법 1: 간단한 실행 (권장)
```bash
# 프로젝트 폴더에서
python3 main.py zero-shot
```

### 방법 2: 상세한 실행
```bash
# 시스템 체크와 함께 실행
./scripts/deployment/start_zero_shot.sh
```

### 방법 3: 시스템 서비스로 설치 (부팅 시 자동 시작)
```bash
# 서비스 설치 (한 번만 실행)
sudo ./scripts/setup/install_service.sh
```

## 📋 각 스크립트 설명

### 1. `main.py zero-shot` - 간단한 실행
- **용도**: 빠르게 서버 시작
- **특징**: 최소한의 설정으로 즉시 실행
- **사용법**: `python3 main.py zero-shot`

### 2. `start_zero_shot.sh` - 상세한 실행
- **용도**: 시스템 체크와 함께 안전하게 실행
- **특징**: 
  - 시스템 환경 확인
  - GPU 상태 확인
  - 포트 충돌 확인
  - 자동 패키지 설치
- **사용법**: `./scripts/deployment/start_zero_shot.sh`

### 3. `install_service.sh` - 시스템 서비스 설치
- **용도**: 부팅 시 자동으로 서버 시작
- **특징**:
  - systemd 서비스로 등록
  - 자동 재시작 기능
  - 로그 관리
- **사용법**: `sudo ./scripts/setup/install_service.sh`

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

# 부팅 시 자동 시작 활성화
sudo systemctl enable visionai-pro

# 부팅 시 자동 시작 비활성화
sudo systemctl disable visionai-pro

# 서비스 로그 보기
sudo journalctl -u visionai-pro -f
```

## 🧪 테스트

### 1. 수동 테스트
```bash
# 서버 시작 테스트
python3 scripts/testing/test_all_servers.py

# 웹 인터페이스 테스트
curl http://localhost:8002/health
```

### 2. 서비스 테스트
```bash
# 서비스 시작
sudo systemctl start visionai-pro

# 실행 상태 확인
sudo systemctl status visionai-pro

# API 테스트
curl http://localhost:8002/api/categories
```

## 🚨 문제 해결

### 일반적인 문제
1. **서비스가 시작되지 않음**: 파일 권한 및 경로 확인
2. **포트 충돌**: 설정에서 포트 변경
3. **권한 거부**: 서비스 설치 시 sudo로 실행
4. **GPU 감지되지 않음**: NVIDIA 드라이버 확인

### 디버그 명령어
```bash
# 서비스 로그 확인
sudo journalctl -u visionai-pro --no-pager

# 시스템 리소스 확인
htop

# GPU 상태 확인
nvidia-smi

# 포트 사용량 확인
sudo netstat -tlnp | grep 8002
```

## 📊 성능 모니터링

### 리소스 모니터링
```bash
# CPU 및 메모리 모니터링
htop

# GPU 모니터링
watch -n 1 nvidia-smi

# 온도 모니터링
tegrastats
```

### 로그 모니터링
```bash
# 실시간 서비스 로그
sudo journalctl -u visionai-pro -f

# 애플리케이션 로그
tail -f logs/app.log
```

---

# Jetson Ubuntu 18.04.6 自动服务器启动指南

## 🚀 快速开始

### 方法1：简单执行（推荐）
```bash
# 从项目文件夹
python3 main.py zero-shot
```

### 方法2：详细执行
```bash
# 带系统检查运行
./scripts/deployment/start_zero_shot.sh
```

### 方法3：安装为系统服务（启动时自动开始）
```bash
# 安装服务（仅运行一次）
sudo ./scripts/setup/install_service.sh
```

## 📋 脚本说明

### 1. `main.py zero-shot` - 简单执行
- **用途**：快速启动服务器
- **特点**：最少设置立即执行
- **用法**：`python3 main.py zero-shot`

### 2. `start_zero_shot.sh` - 详细执行
- **用途**：带系统检查安全执行
- **特点**：
  - 系统环境验证
  - GPU状态检查
  - 端口冲突检查
  - 自动包安装
- **用法**：`./scripts/deployment/start_zero_shot.sh`

### 3. `install_service.sh` - 系统服务安装
- **用途**：启动时自动启动服务器
- **特点**：
  - 注册为systemd服务
  - 自动重启功能
  - 日志管理
- **用法**：`sudo ./scripts/setup/install_service.sh`

## 🔧 系统服务管理

### 服务安装后的使用命令

```bash
# 启动服务
sudo systemctl start visionai-pro

# 停止服务
sudo systemctl stop visionai-pro

# 重启服务
sudo systemctl restart visionai-pro

# 检查服务状态
sudo systemctl status visionai-pro

# 启用启动时自动开始
sudo systemctl enable visionai-pro

# 禁用启动时自动开始
sudo systemctl disable visionai-pro

# 查看服务日志
sudo journalctl -u visionai-pro -f
```

## 🧪 测试

### 1. 手动测试
```bash
# 测试服务器启动
python3 scripts/testing/test_all_servers.py

# 测试网络界面
curl http://localhost:8002/health
```

### 2. 服务测试
```bash
# 启动服务
sudo systemctl start visionai-pro

# 检查是否运行
sudo systemctl status visionai-pro

# 测试API
curl http://localhost:8002/api/categories
```

## 🚨 故障排除

### 常见问题
1. **服务无法启动**：检查文件权限和路径
2. **端口冲突**：在配置中更改端口
3. **权限被拒绝**：服务安装时使用sudo运行
4. **GPU未检测到**：检查NVIDIA驱动程序

### 调试命令
```bash
# 检查服务日志
sudo journalctl -u visionai-pro --no-pager

# 检查系统资源
htop

# 检查GPU状态
nvidia-smi

# 检查端口使用
sudo netstat -tlnp | grep 8002
```

## 📊 性能监控

### 资源监控
```bash
# 监控CPU和内存
htop

# 监控GPU
watch -n 1 nvidia-smi

# 监控温度
tegrastats
```

### 日志监控
```bash
# 实时服务日志
sudo journalctl -u visionai-pro -f

# 应用程序日志
tail -f logs/app.log