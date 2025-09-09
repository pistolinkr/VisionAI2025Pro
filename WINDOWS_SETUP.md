# 🪟 Windows Setup Guide / 윈도우 설치 가이드

## English

### Prerequisites / 사전 요구사항

1. **Python 3.9+** - [Download from python.org](https://www.python.org/downloads/)
2. **Git** - [Download from git-scm.com](https://git-scm.com/download/win)
3. **Visual Studio Build Tools** (for some packages)

### Installation Steps / 설치 단계

#### 1. Clone Repository / 저장소 클론
```cmd
git clone https://github.com/your-username/VisionAI2025Pro.git
cd VisionAI2025Pro
```

#### 2. Create Virtual Environment / 가상환경 생성
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat
```

#### 3. Install Dependencies / 의존성 설치
```cmd
# Upgrade pip first
python -m pip install --upgrade pip

# Install requirements
pip install -r requirements.txt
```

#### 4. Run Server / 서버 실행
```cmd
# Zero-shot server
python main.py zero-shot

# Advanced server
python main.py advanced

# Firebase server
python main.py firebase
```

### Troubleshooting / 문제 해결

#### Common Issues / 일반적인 문제

1. **"Microsoft Visual C++ 14.0 is required"**
   - Download and install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

2. **"Failed to build wheel"**
   - Install Visual Studio Build Tools
   - Or use pre-compiled wheels: `pip install --only-binary=all -r requirements.txt`

3. **"Permission denied"**
   - Run Command Prompt as Administrator
   - Or use PowerShell with execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

4. **"Module not found"**
   - Ensure virtual environment is activated: `(venv)` should appear in prompt
   - Check PYTHONPATH: `set PYTHONPATH=%PYTHONPATH%;%CD%`

### Web Interface Access / 웹 인터페이스 접속

- **Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Advanced**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/firebase_web_app.html

---

## 한국어

### 사전 요구사항

1. **Python 3.9+** - [python.org에서 다운로드](https://www.python.org/downloads/)
2. **Git** - [git-scm.com에서 다운로드](https://git-scm.com/download/win)
3. **Visual Studio Build Tools** (일부 패키지용)

### 설치 단계

#### 1. 저장소 클론
```cmd
git clone https://github.com/your-username/VisionAI2025Pro.git
cd VisionAI2025Pro
```

#### 2. 가상환경 생성
```cmd
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate.bat
```

#### 3. 의존성 설치
```cmd
# pip 먼저 업그레이드
python -m pip install --upgrade pip

# 요구사항 설치
pip install -r requirements.txt
```

#### 4. 서버 실행
```cmd
# Zero-shot 서버
python main.py zero-shot

# Advanced 서버
python main.py advanced

# Firebase 서버
python main.py firebase
```

### 문제 해결

#### 일반적인 문제

1. **"Microsoft Visual C++ 14.0 is required"**
   - [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) 다운로드 및 설치

2. **"Failed to build wheel"**
   - Visual Studio Build Tools 설치
   - 또는 사전 컴파일된 휠 사용: `pip install --only-binary=all -r requirements.txt`

3. **"Permission denied"**
   - 관리자 권한으로 명령 프롬프트 실행
   - 또는 PowerShell에서 실행 정책 설정: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

4. **"Module not found"**
   - 가상환경이 활성화되었는지 확인: 프롬프트에 `(venv)` 표시
   - PYTHONPATH 확인: `set PYTHONPATH=%PYTHONPATH%;%CD%`

### 웹 인터페이스 접속

- **Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Advanced**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/firebase_web_app.html
