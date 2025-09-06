# 🚀 Quick API Testing Guide

## 📋 Prerequisites

1. **Start the API Server**
   ```bash
   # Option 1: Using main.py
   python3 main.py zero-shot
   
   # Option 2: Direct uvicorn
   uvicorn src.api.zero_shot_main:app --host 127.0.0.1 --port 8002
   ```

2. **Verify Server is Running**
   ```bash
   curl http://localhost:8002/health
   ```
   Expected: `{"status": "healthy", "model_info": {...}}`

## 🧪 Quick Tests

### 1. Basic Connectivity
```bash
# Health check
curl http://localhost:8002/health

# Root page
curl http://localhost:8002/

# Swagger docs
curl http://localhost:8002/docs
```

### 2. API Endpoints (No Auth)
```bash
# Categories without API key (should return 401)
curl http://localhost:8002/api/categories

# Image classification without API key (should return 401)
curl -X POST http://localhost:8002/api/classify
```

### 3. Web Interface
1. Open http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html in your browser
2. Enter API key: `qz-U2PdzQxYLnGRzSHvBV8eWrk1BnjPe2IKZzkxgKGk`
3. Click "Test Connection"
4. Upload an image file
5. Click "Start Zero-shot Classification"

## 🔧 Automated Testing

### Python Script
```bash
# Run comprehensive tests
python3 scripts/testing/test_all_servers.py

# Test specific server
python3 scripts/testing/test_zero_shot.py
```

### Shell Script
```bash
# Make executable (if not already)
chmod +x scripts/deployment/start_zero_shot.sh

# Run server
./scripts/deployment/start_zero_shot.sh
```

## 📊 Expected Results

| Test | Expected Status | Expected Response |
|------|----------------|-------------------|
| `/health` | 200 | `{"status": "healthy"}` |
| `/` | 200 | HTML page with VisionAI Pro content |
| `/docs` | 200 | Swagger UI interface |
| `/api/categories` (no key) | 401 | `{"detail": "Invalid API key"}` |
| `/api/classify` (no key) | 401 | `{"detail": "Invalid API key"}` |

## 🚨 Troubleshooting

### Server Won't Start
- Check if port 8002 is available: `lsof -i :8002`
- Verify virtual environment is activated
- Check if all dependencies are installed: `pip list`

### Connection Refused
- Ensure server is running on correct port
- Check firewall settings
- Verify host binding (127.0.0.1 vs 0.0.0.0)

### Import Errors
- Check Python path: `python3 -c "import sys; print(sys.path)"`
- Verify file structure matches expected layout
- Check for syntax errors in Python files

## 🔗 Useful Commands

```bash
# Check server status
ps aux | grep uvicorn

# View server logs
tail -f logs/app.log

# Test specific endpoint
curl -v http://localhost:8002/health

# Kill server if needed
pkill -f uvicorn
```

## 📝 Next Steps

1. **Generate API Key**: Use CLI tool to create valid API keys
2. **Test with Real Images**: Upload actual images for classification
3. **Performance Testing**: Test with multiple concurrent requests
4. **Integration Testing**: Test with your application

## 🆘 Need Help?

- Check the main README.md for detailed documentation
- Run `python3 scripts/testing/test_all_servers.py` for system-wide testing
- Check server logs for error messages
- Verify all files are in correct locations

---

# 🚀 빠른 API 테스트 가이드

## 📋 사전 요구사항

1. **API 서버 시작**
   ```bash
   # 옵션 1: main.py 사용
   python3 main.py zero-shot
   
   # 옵션 2: 직접 uvicorn 실행
   uvicorn src.api.zero_shot_main:app --host 127.0.0.1 --port 8002
   ```

2. **서버 실행 확인**
   ```bash
   curl http://localhost:8002/health
   ```
   예상 결과: `{"status": "healthy", "model_info": {...}}`

## 🧪 빠른 테스트

### 1. 기본 연결성
```bash
# 헬스 체크
curl http://localhost:8002/health

# 루트 페이지
curl http://localhost:8002/

# Swagger 문서
curl http://localhost:8002/docs
```

### 2. API 엔드포인트 (인증 없음)
```bash
# API 키 없이 카테고리 요청 (401 반환 예상)
curl http://localhost:8002/api/categories

# API 키 없이 이미지 분류 요청 (401 반환 예상)
curl -X POST http://localhost:8002/api/classify
```

### 3. 웹 인터페이스
1. 브라우저에서 http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html 열기
2. API 키 입력: `qz-U2PdzQxYLnGRzSHvBV8eWrk1BnjPe2IKZzkxgKGk`
3. "Test Connection" 클릭
4. 이미지 파일 업로드
5. "Start Zero-shot Classification" 클릭

## 🔧 자동화된 테스트

### Python 스크립트
```bash
# 종합 테스트 실행
python3 scripts/testing/test_all_servers.py

# 특정 서버 테스트
python3 scripts/testing/test_zero_shot.py
```

### 셸 스크립트
```bash
# 실행 권한 부여 (아직 없다면)
chmod +x scripts/deployment/start_zero_shot.sh

# 서버 실행
./scripts/deployment/start_zero_shot.sh
```

## 📊 예상 결과

| 테스트 | 예상 상태 | 예상 응답 |
|--------|-----------|-----------|
| `/health` | 200 | `{"status": "healthy"}` |
| `/` | 200 | VisionAI Pro 콘텐츠가 포함된 HTML 페이지 |
| `/docs` | 200 | Swagger UI 인터페이스 |
| `/api/categories` (키 없음) | 401 | `{"detail": "Invalid API key"}` |
| `/api/classify` (키 없음) | 401 | `{"detail": "Invalid API key"}` |

## 🚨 문제 해결

### 서버가 시작되지 않음
- 포트 8002가 사용 가능한지 확인: `lsof -i :8002`
- 가상환경이 활성화되었는지 확인
- 모든 의존성이 설치되었는지 확인: `pip list`

### 연결 거부됨
- 서버가 올바른 포트에서 실행 중인지 확인
- 방화벽 설정 확인
- 호스트 바인딩 확인 (127.0.0.1 vs 0.0.0.0)

### Import 오류
- Python 경로 확인: `python3 -c "import sys; print(sys.path)"`
- 파일 구조가 예상 레이아웃과 일치하는지 확인
- Python 파일의 구문 오류 확인

## 🔗 유용한 명령어

```bash
# 서버 상태 확인
ps aux | grep uvicorn

# 서버 로그 보기
tail -f logs/app.log

# 특정 엔드포인트 테스트
curl -v http://localhost:8002/health

# 필요시 서버 종료
pkill -f uvicorn
```

## 📝 다음 단계

1. **API 키 생성**: CLI 도구를 사용하여 유효한 API 키 생성
2. **실제 이미지로 테스트**: 분류를 위해 실제 이미지 업로드
3. **성능 테스트**: 여러 동시 요청으로 테스트
4. **통합 테스트**: 애플리케이션과 함께 테스트

## 🆘 도움이 필요하신가요?

- 자세한 문서는 메인 README.md를 확인하세요
- 시스템 전체 테스트를 위해 `python3 scripts/testing/test_all_servers.py` 실행
- 오류 메시지를 위해 서버 로그 확인
- 모든 파일이 올바른 위치에 있는지 확인

---

# 🚀 快速API测试指南

## 📋 先决条件

1. **启动API服务器**
   ```bash
   # 选项1：使用main.py
   python3 main.py zero-shot
   
   # 选项2：直接运行uvicorn
   uvicorn src.api.zero_shot_main:app --host 127.0.0.1 --port 8002
   ```

2. **验证服务器正在运行**
   ```bash
   curl http://localhost:8002/health
   ```
   预期结果：`{"status": "healthy", "model_info": {...}}`

## 🧪 快速测试

### 1. 基本连接性
```bash
# 健康检查
curl http://localhost:8002/health

# 根页面
curl http://localhost:8002/

# Swagger文档
curl http://localhost:8002/docs
```

### 2. API端点（无认证）
```bash
# 无API密钥请求类别（应返回401）
curl http://localhost:8002/api/categories

# 无API密钥请求图像分类（应返回401）
curl -X POST http://localhost:8002/api/classify
```

### 3. 网络界面
1. 在浏览器中打开 http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
2. 输入API密钥：`qz-U2PdzQxYLnGRzSHvBV8eWrk1BnjPe2IKZzkxgKGk`
3. 点击"Test Connection"
4. 上传图像文件
5. 点击"Start Zero-shot Classification"

## 🔧 自动化测试

### Python脚本
```bash
# 运行综合测试
python3 scripts/testing/test_all_servers.py

# 测试特定服务器
python3 scripts/testing/test_zero_shot.py
```

### Shell脚本
```bash
# 添加执行权限（如果还没有）
chmod +x scripts/deployment/start_zero_shot.sh

# 运行服务器
./scripts/deployment/start_zero_shot.sh
```

## 📊 预期结果

| 测试 | 预期状态 | 预期响应 |
|------|----------|----------|
| `/health` | 200 | `{"status": "healthy"}` |
| `/` | 200 | 包含VisionAI Pro内容的HTML页面 |
| `/docs` | 200 | Swagger UI界面 |
| `/api/categories`（无密钥） | 401 | `{"detail": "Invalid API key"}` |
| `/api/classify`（无密钥） | 401 | `{"detail": "Invalid API key"}` |

## 🚨 故障排除

### 服务器无法启动
- 检查端口8002是否可用：`lsof -i :8002`
- 验证虚拟环境是否已激活
- 检查是否已安装所有依赖：`pip list`

### 连接被拒绝
- 确保服务器在正确端口上运行
- 检查防火墙设置
- 验证主机绑定（127.0.0.1 vs 0.0.0.0）

### 导入错误
- 检查Python路径：`python3 -c "import sys; print(sys.path)"`
- 验证文件结构是否与预期布局匹配
- 检查Python文件中的语法错误

## 🔗 有用命令

```bash
# 检查服务器状态
ps aux | grep uvicorn

# 查看服务器日志
tail -f logs/app.log

# 测试特定端点
curl -v http://localhost:8002/health

# 如需要则终止服务器
pkill -f uvicorn
```

## 📝 下一步

1. **生成API密钥**：使用CLI工具创建有效的API密钥
2. **使用真实图像测试**：上传实际图像进行分类
3. **性能测试**：使用多个并发请求进行测试
4. **集成测试**：与您的应用程序一起测试

## 🆘 需要帮助？

- 查看主README.md获取详细文档
- 运行`python3 scripts/testing/test_all_servers.py`进行系统范围测试
- 检查服务器日志以获取错误消息
- 验证所有文件是否在正确位置