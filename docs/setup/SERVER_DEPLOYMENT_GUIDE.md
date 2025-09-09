# 🚀 VisionAI Pro - Server Deployment Guide

## 🌍 **Language Selection**

**[🇺🇸 English](#-VisionAI-Pro---Server-Deployment-Guide)** | **[🇰🇷 Korean](#-VisionAI-Pro---서버-배포-가이드)** | **[🇨🇳 Chinese](#-VisionAI-Pro---服务器部署指南)** | **[🇪🇸 Spanish](#-VisionAI-Pro---Guía-de-Despliegue-del-Servidor)** | **[🇫🇷 French](#-VisionAI-Pro---Guide-de-Déploiement-du-Serveur)** | **[🇩🇪 German](#-VisionAI-Pro---Server-Bereitstellungsanleitung)** | **[🇵🇹 Portuguese](#-VisionAI-Pro---Guia-de-Implantação-do-Servidor)** | **[🇸🇦 Arabic](#-VisionAI-Pro---دليل-نشر-الخادم)** | **[🇮🇳 Hindi](#-VisionAI-Pro---सर्वर-तैनाती-गाइड)** | **[🇯🇵 Japanese](#-VisionAI-Pro---サーバーデプロイガイド)** | **[🇷🇺 Russian](#-VisionAI-Pro---Руководство-по-развертыванию-сервера)** | **[🇮🇩 Indonesian](#-VisionAI-Pro---Panduan-Penyebaran-Server)** | **[🇻🇳 Vietnamese](#-VisionAI-Pro---Hướng-Dẫn-Triển-Khai-Máy-Chủ)** | **[🇹🇷 Turkish](#-VisionAI-Pro---Sunucu-Dağıtım-Kılavuzu)** | **[🇮🇹 Italian](#-VisionAI-Pro---Guida-alla-Distribuzione-del-Server)** | **[🇲🇽 Latin (Mexico)](#-VisionAI-Pro---Guía-de-Despliegue-del-Servidor)**

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment support

### 1. Clone Repository
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Environment Setup

#### Linux/macOS
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r config/requirements.txt
```

### 3. Server Execution

#### Method 1: Centralized Execution (Recommended)
```bash
# Zero-shot Classification Server (Port 8002)
python3 main.py zero-shot

# Advanced Classification Server (Port 8001)
python3 main.py advanced

# Firebase Server (Port 8003)
python3 main.py firebase

# Main Server (Port 8000)
python3 main.py main
```

#### Method 2: Direct uvicorn Execution
```bash
# Zero-shot Server
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Advanced Server
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase Server
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Method 3: Using Scripts
```bash
# Make scripts executable (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Execute servers
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Web Interface Access

After starting the server, access the web interface:

- **Zero-shot Classification**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Advanced Classification**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```bash
# Copy example file
cp config/env_example.txt .env

# Edit with your values
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # or cuda for GPU
```

### Model Configuration
- **Zero-shot model**: Uses `query/base_words.txt` file
- **Advanced model**: Uses pre-trained models in `data/models/` folder

## 📡 API Endpoints

### Zero-shot Classification API (Port 8002)
- `POST /api/classify` - Image classification
- `GET /api/categories` - Category list
- `POST /api/categories/add` - Add category
- `DELETE /api/categories/remove` - Remove category
- `GET /api/categories/search` - Search categories
- `GET /health` - Server status check

### Advanced Classification API (Port 8001)
- `POST /api/classify` - Image classification
- `GET /health` - Server status check

### Firebase API (Port 8003)
- `POST /api/classify` - Image classification with Firebase backend
- `GET /health` - Server status check

## 🧪 Testing

```bash
# System test
python3 scripts/testing/test_system.py

# API test
python3 scripts/testing/test_api.py

# Authentication test
python3 scripts/testing/test_auth.py

# Test all servers
python3 scripts/testing/test_all_servers.py
```

## 📦 Production Deployment

### Linux System Service
```bash
# Install service
sudo ./scripts/setup/install_service.sh

# Start service
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Check status
sudo systemctl status visionai-pro
```

### Docker Deployment
```bash
# Build Docker image
docker build -t visionai-pro .

# Run container
docker run -p 8000:8000 visionai-pro
```

## 🔍 Troubleshooting

### Common Issues
1. **Port conflict**: Use different port or stop running service
2. **Model load failure**: Check model file path
3. **Permission error**: Check file permissions and directory access rights
4. **Import error**: Ensure virtual environment is activated

### Log Checking
```bash
# Check log file
tail -f logs/app.log

# Real-time log monitoring (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - The new standard for image classification 🚀

---

# 🚀 VisionAI Pro - 서버 배포 가이드 {#korean}

## 🚀 빠른 시작

### 사전 요구사항
- Python 3.8 이상
- Git
- 가상환경 지원

### 1. 저장소 클론
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. 환경 설정

#### Linux/macOS
```bash
# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# 의존성 설치
pip install -r config/requirements.txt
```

#### Windows
```cmd
# 가상환경 생성
python -m venv venv

# 가상환경 활성화
venv\Scripts\activate

# 의존성 설치
pip install -r config/requirements.txt
```

### 3. 서버 실행

#### 방법 1: 중앙화된 실행 (추천)
```bash
# Zero-shot 분류 서버 (포트 8002)
python3 main.py zero-shot

# 고급 분류 서버 (포트 8001)
python3 main.py advanced

# Firebase 서버 (포트 8003)
python3 main.py firebase

# 메인 서버 (포트 8000)
python3 main.py main
```

#### 방법 2: 직접 uvicorn 실행
```bash
# Zero-shot 서버
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# 고급 서버
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase 서버
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### 방법 3: 스크립트 사용
```bash
# 스크립트 실행 권한 부여 (Linux/macOS)
chmod +x scripts/deployment/*.sh

# 서버 실행
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. 웹 인터페이스 접속

서버 시작 후 웹 인터페이스에 접속:

- **Zero-shot 분류**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **고급 분류**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 설정

### 환경 변수
프로젝트 루트에 `.env` 파일 생성:

```bash
# 예제 파일 복사
cp config/env_example.txt .env

# 실제 값으로 편집
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # 또는 GPU용 cuda
```

### 모델 설정
- **Zero-shot 모델**: `query/base_words.txt` 파일 사용
- **고급 모델**: `data/models/` 폴더의 사전 훈련된 모델 사용

## 📡 API 엔드포인트

### Zero-shot 분류 API (포트 8002)
- `POST /api/classify` - 이미지 분류
- `GET /api/categories` - 카테고리 목록
- `POST /api/categories/add` - 카테고리 추가
- `DELETE /api/categories/remove` - 카테고리 제거
- `GET /api/categories/search` - 카테고리 검색
- `GET /health` - 서버 상태 확인

### 고급 분류 API (포트 8001)
- `POST /api/classify` - 이미지 분류
- `GET /health` - 서버 상태 확인

### Firebase API (포트 8003)
- `POST /api/classify` - Firebase 백엔드로 이미지 분류
- `GET /health` - 서버 상태 확인

## 🧪 테스트

```bash
# 시스템 테스트
python3 scripts/testing/test_system.py

# API 테스트
python3 scripts/testing/test_api.py

# 인증 테스트
python3 scripts/testing/test_auth.py

# 모든 서버 테스트
python3 scripts/testing/test_all_servers.py
```

## 📦 프로덕션 배포

### Linux 시스템 서비스
```bash
# 서비스 설치
sudo ./scripts/setup/install_service.sh

# 서비스 시작
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# 상태 확인
sudo systemctl status visionai-pro
```

### Docker 배포
```bash
# Docker 이미지 빌드
docker build -t visionai-pro .

# 컨테이너 실행
docker run -p 8000:8000 visionai-pro
```

## 🔍 문제 해결

### 일반적인 문제
1. **포트 충돌**: 다른 포트 사용하거나 실행 중인 서비스 종료
2. **모델 로드 실패**: 모델 파일 경로 확인
3. **권한 오류**: 파일 권한 및 디렉토리 접근 권한 확인
4. **임포트 오류**: 가상환경이 활성화되었는지 확인

### 로그 확인
```bash
# 로그 파일 확인
tail -f logs/app.log

# 실시간 로그 모니터링 (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - 이미지 분류의 새로운 표준 🚀

---

# 🚀 VisionAI Pro - 服务器部署指南 {#chinese}

## 🚀 快速开始

### 先决条件
- Python 3.8 或更高版本
- Git
- 虚拟环境支持

### 1. 克隆存储库
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. 环境设置

#### Linux/macOS
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
pip install -r config/requirements.txt
```

#### Windows
```cmd
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
venv\Scripts\activate

# 安装依赖
pip install -r config/requirements.txt
```

### 3. 服务器执行

#### 方法1：集中执行（推荐）
```bash
# 零样本分类服务器（端口8002）
python3 main.py zero-shot

# 高级分类服务器（端口8001）
python3 main.py advanced

# Firebase服务器（端口8003）
python3 main.py firebase

# 主服务器（端口8000）
python3 main.py main
```

#### 方法2：直接uvicorn执行
```bash
# 零样本服务器
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# 高级服务器
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase服务器
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### 方法3：使用脚本
```bash
# 使脚本可执行（Linux/macOS）
chmod +x scripts/deployment/*.sh

# 执行服务器
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. 网络界面访问

启动服务器后，访问网络界面：

- **零样本分类**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **高级分类**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 配置

### 环境变量
在项目根目录创建`.env`文件：

```bash
# 复制示例文件
cp config/env_example.txt .env

# 用实际值编辑
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # 或GPU用cuda
```

### 模型配置
- **零样本模型**：使用`query/base_words.txt`文件
- **高级模型**：使用`data/models/`文件夹中的预训练模型

## 📡 API端点

### 零样本分类API（端口8002）
- `POST /api/classify` - 图像分类
- `GET /api/categories` - 类别列表
- `POST /api/categories/add` - 添加类别
- `DELETE /api/categories/remove` - 删除类别
- `GET /api/categories/search` - 搜索类别
- `GET /health` - 服务器状态检查

### 高级分类API（端口8001）
- `POST /api/classify` - 图像分类
- `GET /health` - 服务器状态检查

### Firebase API（端口8003）
- `POST /api/classify` - 使用Firebase后端进行图像分类
- `GET /health` - 服务器状态检查

## 🧪 测试

```bash
# 系统测试
python3 scripts/testing/test_system.py

# API测试
python3 scripts/testing/test_api.py

# 认证测试
python3 scripts/testing/test_auth.py

# 测试所有服务器
python3 scripts/testing/test_all_servers.py
```

## 📦 生产部署

### Linux系统服务
```bash
# 安装服务
sudo ./scripts/setup/install_service.sh

# 启动服务
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# 检查状态
sudo systemctl status visionai-pro
```

### Docker部署
```bash
# 构建Docker镜像
docker build -t visionai-pro .

# 运行容器
docker run -p 8000:8000 visionai-pro
```

## 🔍 故障排除

### 常见问题
1. **端口冲突**：使用不同端口或停止运行的服务
2. **模型加载失败**：检查模型文件路径
3. **权限错误**：检查文件权限和目录访问权限
4. **导入错误**：确保虚拟环境已激活

### 日志检查
```bash
# 检查日志文件
tail -f logs/app.log

# 实时日志监控（Linux）
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - 图像分类的新标准 🚀

---

# 🚀 VisionAI Pro - Guía de Despliegue del Servidor {#spanish}

## 🚀 Inicio Rápido

### Prerrequisitos
- Python 3.8 o superior
- Git
- Soporte de entorno virtual

### 1. Clonar Repositorio
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Configuración del Entorno

#### Linux/macOS
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r config/requirements.txt
```

### 3. Ejecución del Servidor

#### Método 1: Ejecución Centralizada (Recomendado)
```bash
# Servidor de Clasificación Zero-shot (Puerto 8002)
python3 main.py zero-shot

# Servidor de Clasificación Avanzada (Puerto 8001)
python3 main.py advanced

# Servidor Firebase (Puerto 8003)
python3 main.py firebase

# Servidor Principal (Puerto 8000)
python3 main.py main
```

#### Método 2: Ejecución Directa con uvicorn
```bash
# Servidor Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Servidor Avanzado
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Servidor Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Método 3: Usando Scripts
```bash
# Hacer scripts ejecutables (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Ejecutar servidores
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Acceso a la Interfaz Web

Después de iniciar el servidor, accede a la interfaz web:

- **Clasificación Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Clasificación Avanzada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuración

### Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:

```bash
# Copiar archivo de ejemplo
cp config/env_example.txt .env

# Editar con valores reales
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # o cuda para GPU
```

### Configuración del Modelo
- **Modelo Zero-shot**: Usa archivo `query/base_words.txt`
- **Modelo Avanzado**: Usa modelos preentrenados en carpeta `data/models/`

## 📡 Endpoints de API

### API de Clasificación Zero-shot (Puerto 8002)
- `POST /api/classify` - Clasificación de imágenes
- `GET /api/categories` - Lista de categorías
- `POST /api/categories/add` - Agregar categoría
- `DELETE /api/categories/remove` - Eliminar categoría
- `GET /api/categories/search` - Buscar categorías
- `GET /health` - Verificar estado del servidor

### API de Clasificación Avanzada (Puerto 8001)
- `POST /api/classify` - Clasificación de imágenes
- `GET /health` - Verificar estado del servidor

### API Firebase (Puerto 8003)
- `POST /api/classify` - Clasificación de imágenes con backend Firebase
- `GET /health` - Verificar estado del servidor

## 🧪 Pruebas

```bash
# Prueba del sistema
python3 scripts/testing/test_system.py

# Prueba de API
python3 scripts/testing/test_api.py

# Prueba de autenticación
python3 scripts/testing/test_auth.py

# Probar todos los servidores
python3 scripts/testing/test_all_servers.py
```

## 📦 Despliegue en Producción

### Servicio del Sistema Linux
```bash
# Instalar servicio
sudo ./scripts/setup/install_service.sh

# Iniciar servicio
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Verificar estado
sudo systemctl status visionai-pro
```

### Despliegue con Docker
```bash
# Construir imagen Docker
docker build -t visionai-pro .

# Ejecutar contenedor
docker run -p 8000:8000 visionai-pro
```

## 🔍 Solución de Problemas

### Problemas Comunes
1. **Conflicto de puertos**: Usar puerto diferente o detener servicio en ejecución
2. **Fallo de carga del modelo**: Verificar ruta del archivo del modelo
3. **Error de permisos**: Verificar permisos de archivos y acceso a directorios
4. **Error de importación**: Asegurar que el entorno virtual esté activado

### Verificación de Logs
```bash
# Verificar archivo de log
tail -f logs/app.log

# Monitoreo de logs en tiempo real (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - El nuevo estándar en clasificación de imágenes 🚀

---

# 🚀 VisionAI Pro - Guide de Déploiement du Serveur {#french}

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.8 ou supérieur
- Git
- Support d'environnement virtuel

### 1. Cloner le Dépôt
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Configuration de l'Environnement

#### Linux/macOS
```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
source venv/bin/activate

# Installer les dépendances
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
venv\Scripts\activate

# Installer les dépendances
pip install -r config/requirements.txt
```

### 3. Exécution du Serveur

#### Méthode 1: Exécution Centralisée (Recommandée)
```bash
# Serveur de Classification Zero-shot (Port 8002)
python3 main.py zero-shot

# Serveur de Classification Avancée (Port 8001)
python3 main.py advanced

# Serveur Firebase (Port 8003)
python3 main.py firebase

# Serveur Principal (Port 8000)
python3 main.py main
```

#### Méthode 2: Exécution Directe avec uvicorn
```bash
# Serveur Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Serveur Avancé
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Serveur Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Méthode 3: Utilisation de Scripts
```bash
# Rendre les scripts exécutables (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Exécuter les serveurs
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Accès à l'Interface Web

Après avoir démarré le serveur, accédez à l'interface web :

- **Classification Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classification Avancée**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuration

### Variables d'Environnement
Créer un fichier `.env` à la racine du projet :

```bash
# Copier le fichier d'exemple
cp config/env_example.txt .env

# Éditer avec les vraies valeurs
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # ou cuda pour GPU
```

### Configuration du Modèle
- **Modèle Zero-shot**: Utilise le fichier `query/base_words.txt`
- **Modèle Avancé**: Utilise les modèles pré-entraînés dans le dossier `data/models/`

## 📡 Points de Terminaison API

### API de Classification Zero-shot (Port 8002)
- `POST /api/classify` - Classification d'images
- `GET /api/categories` - Liste des catégories
- `POST /api/categories/add` - Ajouter une catégorie
- `DELETE /api/categories/remove` - Supprimer une catégorie
- `GET /api/categories/search` - Rechercher des catégories
- `GET /health` - Vérifier l'état du serveur

### API de Classification Avancée (Port 8001)
- `POST /api/classify` - Classification d'images
- `GET /health` - Vérifier l'état du serveur

### API Firebase (Port 8003)
- `POST /api/classify` - Classification d'images avec backend Firebase
- `GET /health` - Vérifier l'état du serveur

## 🧪 Tests

```bash
# Test du système
python3 scripts/testing/test_system.py

# Test de l'API
python3 scripts/testing/test_api.py

# Test d'authentification
python3 scripts/testing/test_auth.py

# Tester tous les serveurs
python3 scripts/testing/test_all_servers.py
```

## 📦 Déploiement en Production

### Service Système Linux
```bash
# Installer le service
sudo ./scripts/setup/install_service.sh

# Démarrer le service
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Vérifier l'état
sudo systemctl status visionai-pro
```

### Déploiement Docker
```bash
# Construire l'image Docker
docker build -t visionai-pro .

# Exécuter le conteneur
docker run -p 8000:8000 visionai-pro
```

## 🔍 Dépannage

### Problèmes Courants
1. **Conflit de ports**: Utiliser un port différent ou arrêter le service en cours
2. **Échec de chargement du modèle**: Vérifier le chemin du fichier du modèle
3. **Erreur de permissions**: Vérifier les permissions des fichiers et l'accès aux répertoires
4. **Erreur d'importation**: S'assurer que l'environnement virtuel est activé

### Vérification des Logs
```bash
# Vérifier le fichier de log
tail -f logs/app.log

# Surveillance des logs en temps réel (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Le nouveau standard en classification d'images 🚀

---

# 🚀 VisionAI Pro - Server-Bereitstellungsanleitung {#german}

## 🚀 Schnellstart

### Voraussetzungen
- Python 3.8 oder höher
- Git
- Virtuelle Umgebung Unterstützung

### 1. Repository Klonen
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Umgebungseinrichtung

#### Linux/macOS
```bash
# Virtuelle Umgebung erstellen
python3 -m venv venv

# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Abhängigkeiten installieren
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Virtuelle Umgebung erstellen
python -m venv venv

# Virtuelle Umgebung aktivieren
venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r config/requirements.txt
```

### 3. Server-Ausführung

#### Methode 1: Zentrale Ausführung (Empfohlen)
```bash
# Zero-shot Klassifizierungsserver (Port 8002)
python3 main.py zero-shot

# Erweiterte Klassifizierungsserver (Port 8001)
python3 main.py advanced

# Firebase Server (Port 8003)
python3 main.py firebase

# Hauptserver (Port 8000)
python3 main.py main
```

#### Methode 2: Direkte uvicorn Ausführung
```bash
# Zero-shot Server
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Erweiterte Server
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase Server
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Methode 3: Verwendung von Skripten
```bash
# Skripte ausführbar machen (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Server ausführen
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Web-Interface Zugriff

Nach dem Start des Servers, greifen Sie auf das Web-Interface zu:

- **Zero-shot Klassifizierung**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Erweiterte Klassifizierung**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Konfiguration

### Umgebungsvariablen
Erstellen Sie eine `.env` Datei im Projektverzeichnis:

```bash
# Beispiel-Datei kopieren
cp config/env_example.txt .env

# Mit echten Werten bearbeiten
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # oder cuda für GPU
```

### Modell-Konfiguration
- **Zero-shot Modell**: Verwendet `query/base_words.txt` Datei
- **Erweitertes Modell**: Verwendet vortrainierte Modelle im `data/models/` Ordner

## 📡 API-Endpunkte

### Zero-shot Klassifizierungs-API (Port 8002)
- `POST /api/classify` - Bildklassifizierung
- `GET /api/categories` - Kategorieliste
- `POST /api/categories/add` - Kategorie hinzufügen
- `DELETE /api/categories/remove` - Kategorie entfernen
- `GET /api/categories/search` - Kategorien suchen
- `GET /health` - Serverstatus prüfen

### Erweiterte Klassifizierungs-API (Port 8001)
- `POST /api/classify` - Bildklassifizierung
- `GET /health` - Serverstatus prüfen

### Firebase API (Port 8003)
- `POST /api/classify` - Bildklassifizierung mit Firebase Backend
- `GET /health` - Serverstatus prüfen

## 🧪 Tests

```bash
# Systemtest
python3 scripts/testing/test_system.py

# API-Test
python3 scripts/testing/test_api.py

# Authentifizierungstest
python3 scripts/testing/test_auth.py

# Alle Server testen
python3 scripts/testing/test_all_servers.py
```

## 📦 Produktions-Bereitstellung

### Linux Systemdienst
```bash
# Dienst installieren
sudo ./scripts/setup/install_service.sh

# Dienst starten
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Status prüfen
sudo systemctl status visionai-pro
```

### Docker-Bereitstellung
```bash
# Docker-Image erstellen
docker build -t visionai-pro .

# Container ausführen
docker run -p 8000:8000 visionai-pro
```

## 🔍 Fehlerbehebung

### Häufige Probleme
1. **Port-Konflikt**: Anderen Port verwenden oder laufenden Dienst stoppen
2. **Modell-Ladefehler**: Modell-Dateipfad prüfen
3. **Berechtigungsfehler**: Dateiberechtigungen und Verzeichniszugriff prüfen
4. **Import-Fehler**: Sicherstellen, dass virtuelle Umgebung aktiviert ist

### Log-Überprüfung
```bash
# Log-Datei prüfen
tail -f logs/app.log

# Echtzeit-Log-Überwachung (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Der neue Standard in der Bildklassifizierung 🚀

---

# 🚀 VisionAI Pro - Guia de Implantação do Servidor {#portuguese}

## 🚀 Início Rápido

### Pré-requisitos
- Python 3.8 ou superior
- Git
- Suporte a ambiente virtual

### 1. Clonar Repositório
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Configuração do Ambiente

#### Linux/macOS
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate

# Instalar dependências
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
venv\Scripts\activate

# Instalar dependências
pip install -r config/requirements.txt
```

### 3. Execução do Servidor

#### Método 1: Execução Centralizada (Recomendado)
```bash
# Servidor de Classificação Zero-shot (Porta 8002)
python3 main.py zero-shot

# Servidor de Classificação Avançada (Porta 8001)
python3 main.py advanced

# Servidor Firebase (Porta 8003)
python3 main.py firebase

# Servidor Principal (Porta 8000)
python3 main.py main
```

#### Método 2: Execução Direta com uvicorn
```bash
# Servidor Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Servidor Avançado
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Servidor Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Método 3: Usando Scripts
```bash
# Tornar scripts executáveis (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Executar servidores
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Acesso à Interface Web

Após iniciar o servidor, acesse a interface web:

- **Classificação Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classificação Avançada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuração

### Variáveis de Ambiente
Criar arquivo `.env` na raiz do projeto:

```bash
# Copiar arquivo de exemplo
cp config/env_example.txt .env

# Editar com valores reais
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # ou cuda para GPU
```

### Configuração do Modelo
- **Modelo Zero-shot**: Usa arquivo `query/base_words.txt`
- **Modelo Avançado**: Usa modelos pré-treinados na pasta `data/models/`

## 📡 Endpoints da API

### API de Classificação Zero-shot (Porta 8002)
- `POST /api/classify` - Classificação de imagens
- `GET /api/categories` - Lista de categorias
- `POST /api/categories/add` - Adicionar categoria
- `DELETE /api/categories/remove` - Remover categoria
- `GET /api/categories/search` - Buscar categorias
- `GET /health` - Verificar status do servidor

### API de Classificação Avançada (Porta 8001)
- `POST /api/classify` - Classificação de imagens
- `GET /health` - Verificar status do servidor

### API Firebase (Porta 8003)
- `POST /api/classify` - Classificação de imagens com backend Firebase
- `GET /health` - Verificar status do servidor

## 🧪 Testes

```bash
# Teste do sistema
python3 scripts/testing/test_system.py

# Teste da API
python3 scripts/testing/test_api.py

# Teste de autenticação
python3 scripts/testing/test_auth.py

# Testar todos os servidores
python3 scripts/testing/test_all_servers.py
```

## 📦 Implantação em Produção

### Serviço do Sistema Linux
```bash
# Instalar serviço
sudo ./scripts/setup/install_service.sh

# Iniciar serviço
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Verificar status
sudo systemctl status visionai-pro
```

### Implantação Docker
```bash
# Construir imagem Docker
docker build -t visionai-pro .

# Executar contêiner
docker run -p 8000:8000 visionai-pro
```

## 🔍 Solução de Problemas

### Problemas Comuns
1. **Conflito de portas**: Usar porta diferente ou parar serviço em execução
2. **Falha ao carregar modelo**: Verificar caminho do arquivo do modelo
3. **Erro de permissão**: Verificar permissões de arquivos e acesso a diretórios
4. **Erro de importação**: Garantir que ambiente virtual esteja ativado

### Verificação de Logs
```bash
# Verificar arquivo de log
tail -f logs/app.log

# Monitoramento de logs em tempo real (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - O novo padrão em classificação de imagens 🚀

---

# 🚀 VisionAI Pro - دليل نشر الخادم {#arabic}

## 🚀 البدء السريع

### المتطلبات المسبقة
- Python 3.8 أو أعلى
- Git
- دعم البيئة الافتراضية

### 1. استنساخ المستودع
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. إعداد البيئة

#### Linux/macOS
```bash
# إنشاء البيئة الافتراضية
python3 -m venv venv

# تفعيل البيئة الافتراضية
source venv/bin/activate

# تثبيت التبعيات
pip install -r config/requirements.txt
```

#### Windows
```cmd
# إنشاء البيئة الافتراضية
python -m venv venv

# تفعيل البيئة الافتراضية
venv\Scripts\activate

# تثبيت التبعيات
pip install -r config/requirements.txt
```

### 3. تشغيل الخادم

#### الطريقة 1: التشغيل المركزي (موصى به)
```bash
# خادم التصنيف Zero-shot (المنفذ 8002)
python3 main.py zero-shot

# خادم التصنيف المتقدم (المنفذ 8001)
python3 main.py advanced

# خادم Firebase (المنفذ 8003)
python3 main.py firebase

# الخادم الرئيسي (المنفذ 8000)
python3 main.py main
```

#### الطريقة 2: التشغيل المباشر مع uvicorn
```bash
# خادم Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# الخادم المتقدم
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# خادم Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### الطريقة 3: استخدام السكريبتات
```bash
# جعل السكريبتات قابلة للتنفيذ (Linux/macOS)
chmod +x scripts/deployment/*.sh

# تشغيل الخوادم
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. الوصول إلى واجهة الويب

بعد بدء الخادم، الوصول إلى واجهة الويب:

- **تصنيف Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **التصنيف المتقدم**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 التكوين

### متغيرات البيئة
إنشاء ملف `.env` في جذر المشروع:

```bash
# نسخ ملف المثال
cp config/env_example.txt .env

# التحرير بقيم حقيقية
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # أو cuda للـ GPU
```

### تكوين النموذج
- **نموذج Zero-shot**: يستخدم ملف `query/base_words.txt`
- **النموذج المتقدم**: يستخدم النماذج المدربة مسبقاً في مجلد `data/models/`

## 📡 نقاط نهاية API

### API تصنيف Zero-shot (المنفذ 8002)
- `POST /api/classify` - تصنيف الصور
- `GET /api/categories` - قائمة الفئات
- `POST /api/categories/add` - إضافة فئة
- `DELETE /api/categories/remove` - إزالة فئة
- `GET /api/categories/search` - البحث في الفئات
- `GET /health` - فحص حالة الخادم

### API التصنيف المتقدم (المنفذ 8001)
- `POST /api/classify` - تصنيف الصور
- `GET /health` - فحص حالة الخادم

### API Firebase (المنفذ 8003)
- `POST /api/classify` - تصنيف الصور مع خادم Firebase
- `GET /health` - فحص حالة الخادم

## 🧪 الاختبارات

```bash
# اختبار النظام
python3 scripts/testing/test_system.py

# اختبار API
python3 scripts/testing/test_api.py

# اختبار المصادقة
python3 scripts/testing/test_auth.py

# اختبار جميع الخوادم
python3 scripts/testing/test_all_servers.py
```

## 📦 النشر في الإنتاج

### خدمة نظام Linux
```bash
# تثبيت الخدمة
sudo ./scripts/setup/install_service.sh

# بدء الخدمة
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# فحص الحالة
sudo systemctl status visionai-pro
```

### النشر مع Docker
```bash
# بناء صورة Docker
docker build -t visionai-pro .

# تشغيل الحاوية
docker run -p 8000:8000 visionai-pro
```

## 🔍 استكشاف الأخطاء وإصلاحها

### المشاكل الشائعة
1. **تعارض المنافذ**: استخدام منفذ مختلف أو إيقاف الخدمة قيد التشغيل
2. **فشل تحميل النموذج**: فحص مسار ملف النموذج
3. **خطأ في الصلاحيات**: فحص صلاحيات الملفات والوصول إلى المجلدات
4. **خطأ في الاستيراد**: التأكد من تفعيل البيئة الافتراضية

### فحص السجلات
```bash
# فحص ملف السجل
tail -f logs/app.log

# مراقبة السجلات في الوقت الفعلي (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - المعيار الجديد في تصنيف الصور 🚀

---

# 🚀 VisionAI Pro - सर्वर तैनाती गाइड {#hindi}

## 🚀 त्वरित प्रारंभ

### आवश्यकताएं
- Python 3.8 या उच्चतर
- Git
- वर्चुअल एनवायरनमेंट समर्थन

### 1. रिपॉजिटरी क्लोन करें
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. एनवायरनमेंट सेटअप

#### Linux/macOS
```bash
# वर्चुअल एनवायरनमेंट बनाएं
python3 -m venv venv

# वर्चुअल एनवायरनमेंट सक्रिय करें
source venv/bin/activate

# निर्भरताएं स्थापित करें
pip install -r config/requirements.txt
```

#### Windows
```cmd
# वर्चुअल एनवायरनमेंट बनाएं
python -m venv venv

# वर्चुअल एनवायरनमेंट सक्रिय करें
venv\Scripts\activate

# निर्भरताएं स्थापित करें
pip install -r config/requirements.txt
```

### 3. सर्वर निष्पादन

#### विधि 1: केंद्रीकृत निष्पादन (अनुशंसित)
```bash
# Zero-shot वर्गीकरण सर्वर (पोर्ट 8002)
python3 main.py zero-shot

# उन्नत वर्गीकरण सर्वर (पोर्ट 8001)
python3 main.py advanced

# Firebase सर्वर (पोर्ट 8003)
python3 main.py firebase

# मुख्य सर्वर (पोर्ट 8000)
python3 main.py main
```

#### विधि 2: प्रत्यक्ष uvicorn निष्पादन
```bash
# Zero-shot सर्वर
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# उन्नत सर्वर
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase सर्वर
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### विधि 3: स्क्रिप्ट्स का उपयोग
```bash
# स्क्रिप्ट्स को निष्पादन योग्य बनाएं (Linux/macOS)
chmod +x scripts/deployment/*.sh

# सर्वर निष्पादित करें
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. वेब इंटरफेस पहुंच

सर्वर शुरू करने के बाद, वेब इंटरफेस तक पहुंचें:

- **Zero-shot वर्गीकरण**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **उन्नत वर्गीकरण**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 कॉन्फ़िगरेशन

### एनवायरनमेंट वेरिएबल्स
प्रोजेक्ट रूट में `.env` फ़ाइल बनाएं:

```bash
# उदाहरण फ़ाइल कॉपी करें
cp config/env_example.txt .env

# वास्तविक मूल्यों के साथ संपादित करें
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # या GPU के लिए cuda
```

### मॉडल कॉन्फ़िगरेशन
- **Zero-shot मॉडल**: `query/base_words.txt` फ़ाइल का उपयोग करता है
- **उन्नत मॉडल**: `data/models/` फ़ोल्डर में पूर्व-प्रशिक्षित मॉडल का उपयोग करता है

## 📡 API एंडपॉइंट्स

### Zero-shot वर्गीकरण API (पोर्ट 8002)
- `POST /api/classify` - छवि वर्गीकरण
- `GET /api/categories` - श्रेणी सूची
- `POST /api/categories/add` - श्रेणी जोड़ें
- `DELETE /api/categories/remove` - श्रेणी हटाएं
- `GET /api/categories/search` - श्रेणियां खोजें
- `GET /health` - सर्वर स्थिति जांचें

### उन्नत वर्गीकरण API (पोर्ट 8001)
- `POST /api/classify` - छवि वर्गीकरण
- `GET /health` - सर्वर स्थिति जांचें

### Firebase API (पोर्ट 8003)
- `POST /api/classify` - Firebase बैकएंड के साथ छवि वर्गीकरण
- `GET /health` - सर्वर स्थिति जांचें

## 🧪 परीक्षण

```bash
# सिस्टम परीक्षण
python3 scripts/testing/test_system.py

# API परीक्षण
python3 scripts/testing/test_api.py

# प्रमाणीकरण परीक्षण
python3 scripts/testing/test_auth.py

# सभी सर्वर परीक्षण
python3 scripts/testing/test_all_servers.py
```

## 📦 प्रोडक्शन तैनाती

### Linux सिस्टम सेवा
```bash
# सेवा स्थापित करें
sudo ./scripts/setup/install_service.sh

# सेवा शुरू करें
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# स्थिति जांचें
sudo systemctl status visionai-pro
```

### Docker तैनाती
```bash
# Docker इमेज बनाएं
docker build -t visionai-pro .

# कंटेनर चलाएं
docker run -p 8000:8000 visionai-pro
```

## 🔍 समस्या निवारण

### सामान्य समस्याएं
1. **पोर्ट संघर्ष**: अलग पोर्ट का उपयोग करें या चल रही सेवा को रोकें
2. **मॉडल लोड विफलता**: मॉडल फ़ाइल पथ जांचें
3. **अनुमति त्रुटि**: फ़ाइल अनुमतियों और निर्देशिका पहुंच अधिकारों की जांच करें
4. **आयात त्रुटि**: सुनिश्चित करें कि वर्चुअल एनवायरनमेंट सक्रिय है

### लॉग जांच
```bash
# लॉग फ़ाइल जांचें
tail -f logs/app.log

# रियल-टाइम लॉग मॉनिटरिंग (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - छवि वर्गीकरण में नया मानक 🚀

---

# 🚀 VisionAI Pro - サーバーデプロイガイド {#japanese}

## 🚀 クイックスタート

### 前提条件
- Python 3.8以上
- Git
- 仮想環境サポート

### 1. リポジトリのクローン
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. 環境設定

#### Linux/macOS
```bash
# 仮想環境を作成
python3 -m venv venv

# 仮想環境をアクティベート
source venv/bin/activate

# 依存関係をインストール
pip install -r config/requirements.txt
```

#### Windows
```cmd
# 仮想環境を作成
python -m venv venv

# 仮想環境をアクティベート
venv\Scripts\activate

# 依存関係をインストール
pip install -r config/requirements.txt
```

### 3. サーバー実行

#### 方法1: 中央集権的実行（推奨）
```bash
# Zero-shot分類サーバー（ポート8002）
python3 main.py zero-shot

# 高度な分類サーバー（ポート8001）
python3 main.py advanced

# Firebaseサーバー（ポート8003）
python3 main.py firebase

# メインサーバー（ポート8000）
python3 main.py main
```

#### 方法2: 直接uvicorn実行
```bash
# Zero-shotサーバー
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# 高度なサーバー
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebaseサーバー
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### 方法3: スクリプトの使用
```bash
# スクリプトを実行可能にする（Linux/macOS）
chmod +x scripts/deployment/*.sh

# サーバーを実行
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. ウェブインターフェースアクセス

サーバー開始後、ウェブインターフェースにアクセス：

- **Zero-shot分類**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **高度な分類**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 設定

### 環境変数
プロジェクトルートに`.env`ファイルを作成：

```bash
# サンプルファイルをコピー
cp config/env_example.txt .env

# 実際の値で編集
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # またはGPU用cuda
```

### モデル設定
- **Zero-shotモデル**: `query/base_words.txt`ファイルを使用
- **高度なモデル**: `data/models/`フォルダの事前訓練済みモデルを使用

## 📡 APIエンドポイント

### Zero-shot分類API（ポート8002）
- `POST /api/classify` - 画像分類
- `GET /api/categories` - カテゴリリスト
- `POST /api/categories/add` - カテゴリ追加
- `DELETE /api/categories/remove` - カテゴリ削除
- `GET /api/categories/search` - カテゴリ検索
- `GET /health` - サーバー状態確認

### 高度な分類API（ポート8001）
- `POST /api/classify` - 画像分類
- `GET /health` - サーバー状態確認

### Firebase API（ポート8003）
- `POST /api/classify` - Firebaseバックエンドでの画像分類
- `GET /health` - サーバー状態確認

## 🧪 テスト

```bash
# システムテスト
python3 scripts/testing/test_system.py

# APIテスト
python3 scripts/testing/test_api.py

# 認証テスト
python3 scripts/testing/test_auth.py

# 全サーバーテスト
python3 scripts/testing/test_all_servers.py
```

## 📦 本番デプロイ

### Linuxシステムサービス
```bash
# サービスをインストール
sudo ./scripts/setup/install_service.sh

# サービスを開始
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# 状態を確認
sudo systemctl status visionai-pro
```

### Dockerデプロイ
```bash
# Dockerイメージをビルド
docker build -t visionai-pro .

# コンテナを実行
docker run -p 8000:8000 visionai-pro
```

## 🔍 トラブルシューティング

### 一般的な問題
1. **ポート競合**: 異なるポートを使用するか、実行中のサービスを停止
2. **モデル読み込み失敗**: モデルファイルパスを確認
3. **権限エラー**: ファイル権限とディレクトリアクセス権を確認
4. **インポートエラー**: 仮想環境がアクティブであることを確認

### ログ確認
```bash
# ログファイルを確認
tail -f logs/app.log

# リアルタイムログ監視（Linux）
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - 画像分類の新しい標準 🚀

---

# 🚀 VisionAI Pro - Руководство по развертыванию сервера {#russian}

## 🚀 Быстрый старт

### Предварительные требования
- Python 3.8 или выше
- Git
- Поддержка виртуального окружения

### 1. Клонирование репозитория
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Настройка окружения

#### Linux/macOS
```bash
# Создать виртуальное окружение
python3 -m venv venv

# Активировать виртуальное окружение
source venv/bin/activate

# Установить зависимости
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Создать виртуальное окружение
python -m venv venv

# Активировать виртуальное окружение
venv\Scripts\activate

# Установить зависимости
pip install -r config/requirements.txt
```

### 3. Запуск сервера

#### Способ 1: Централизованный запуск (Рекомендуется)
```bash
# Сервер классификации Zero-shot (Порт 8002)
python3 main.py zero-shot

# Сервер продвинутой классификации (Порт 8001)
python3 main.py advanced

# Сервер Firebase (Порт 8003)
python3 main.py firebase

# Главный сервер (Порт 8000)
python3 main.py main
```

#### Способ 2: Прямой запуск с uvicorn
```bash
# Сервер Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Продвинутый сервер
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Сервер Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Способ 3: Использование скриптов
```bash
# Сделать скрипты исполняемыми (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Запустить серверы
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Доступ к веб-интерфейсу

После запуска сервера, получить доступ к веб-интерфейсу:

- **Классификация Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Продвинутая классификация**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Конфигурация

### Переменные окружения
Создать файл `.env` в корне проекта:

```bash
# Скопировать файл примера
cp config/env_example.txt .env

# Отредактировать с реальными значениями
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # или cuda для GPU
```

### Конфигурация модели
- **Модель Zero-shot**: Использует файл `query/base_words.txt`
- **Продвинутая модель**: Использует предобученные модели в папке `data/models/`

## 📡 API конечные точки

### API классификации Zero-shot (Порт 8002)
- `POST /api/classify` - Классификация изображений
- `GET /api/categories` - Список категорий
- `POST /api/categories/add` - Добавить категорию
- `DELETE /api/categories/remove` - Удалить категорию
- `GET /api/categories/search` - Поиск категорий
- `GET /health` - Проверить статус сервера

### API продвинутой классификации (Порт 8001)
- `POST /api/classify` - Классификация изображений
- `GET /health` - Проверить статус сервера

### API Firebase (Порт 8003)
- `POST /api/classify` - Классификация изображений с Firebase бэкендом
- `GET /health` - Проверить статус сервера

## 🧪 Тестирование

```bash
# Системный тест
python3 scripts/testing/test_system.py

# API тест
python3 scripts/testing/test_api.py

# Тест аутентификации
python3 scripts/testing/test_auth.py

# Тест всех серверов
python3 scripts/testing/test_all_servers.py
```

## 📦 Продакшн развертывание

### Linux системный сервис
```bash
# Установить сервис
sudo ./scripts/setup/install_service.sh

# Запустить сервис
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Проверить статус
sudo systemctl status visionai-pro
```

### Docker развертывание
```bash
# Собрать Docker образ
docker build -t visionai-pro .

# Запустить контейнер
docker run -p 8000:8000 visionai-pro
```

## 🔍 Устранение неполадок

### Общие проблемы
1. **Конфликт портов**: Использовать другой порт или остановить запущенный сервис
2. **Ошибка загрузки модели**: Проверить путь к файлу модели
3. **Ошибка разрешений**: Проверить разрешения файлов и доступ к директориям
4. **Ошибка импорта**: Убедиться, что виртуальное окружение активировано

### Проверка логов
```bash
# Проверить файл лога
tail -f logs/app.log

# Мониторинг логов в реальном времени (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Новый стандарт в классификации изображений 🚀

---

# 🚀 VisionAI Pro - Panduan Penyebaran Server {#indonesian}

## 🚀 Mulai Cepat

### Prasyarat
- Python 3.8 atau lebih tinggi
- Git
- Dukungan lingkungan virtual

### 1. Klon Repositori
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Pengaturan Lingkungan

#### Linux/macOS
```bash
# Buat lingkungan virtual
python3 -m venv venv

# Aktifkan lingkungan virtual
source venv/bin/activate

# Install dependensi
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Buat lingkungan virtual
python -m venv venv

# Aktifkan lingkungan virtual
venv\Scripts\activate

# Install dependensi
pip install -r config/requirements.txt
```

### 3. Eksekusi Server

#### Metode 1: Eksekusi Terpusat (Direkomendasikan)
```bash
# Server Klasifikasi Zero-shot (Port 8002)
python3 main.py zero-shot

# Server Klasifikasi Lanjutan (Port 8001)
python3 main.py advanced

# Server Firebase (Port 8003)
python3 main.py firebase

# Server Utama (Port 8000)
python3 main.py main
```

#### Metode 2: Eksekusi Langsung dengan uvicorn
```bash
# Server Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Server Lanjutan
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Server Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Metode 3: Menggunakan Script
```bash
# Buat script dapat dieksekusi (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Jalankan server
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Akses Interface Web

Setelah memulai server, akses interface web:

- **Klasifikasi Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Klasifikasi Lanjutan**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Konfigurasi

### Variabel Lingkungan
Buat file `.env` di root proyek:

```bash
# Salin file contoh
cp config/env_example.txt .env

# Edit dengan nilai sebenarnya
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # atau cuda untuk GPU
```

### Konfigurasi Model
- **Model Zero-shot**: Menggunakan file `query/base_words.txt`
- **Model Lanjutan**: Menggunakan model pra-terlatih di folder `data/models/`

## 📡 Endpoint API

### API Klasifikasi Zero-shot (Port 8002)
- `POST /api/classify` - Klasifikasi gambar
- `GET /api/categories` - Daftar kategori
- `POST /api/categories/add` - Tambah kategori
- `DELETE /api/categories/remove` - Hapus kategori
- `GET /api/categories/search` - Cari kategori
- `GET /health` - Periksa status server

### API Klasifikasi Lanjutan (Port 8001)
- `POST /api/classify` - Klasifikasi gambar
- `GET /health` - Periksa status server

### API Firebase (Port 8003)
- `POST /api/classify` - Klasifikasi gambar dengan backend Firebase
- `GET /health` - Periksa status server

## 🧪 Pengujian

```bash
# Uji sistem
python3 scripts/testing/test_system.py

# Uji API
python3 scripts/testing/test_api.py

# Uji autentikasi
python3 scripts/testing/test_auth.py

# Uji semua server
python3 scripts/testing/test_all_servers.py
```

## 📦 Penyebaran Produksi

### Layanan Sistem Linux
```bash
# Install layanan
sudo ./scripts/setup/install_service.sh

# Mulai layanan
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Periksa status
sudo systemctl status visionai-pro
```

### Penyebaran Docker
```bash
# Build image Docker
docker build -t visionai-pro .

# Jalankan kontainer
docker run -p 8000:8000 visionai-pro
```

## 🔍 Pemecahan Masalah

### Masalah Umum
1. **Konflik port**: Gunakan port berbeda atau hentikan layanan yang berjalan
2. **Gagal memuat model**: Periksa jalur file model
3. **Error izin**: Periksa izin file dan akses direktori
4. **Error impor**: Pastikan lingkungan virtual aktif

### Pemeriksaan Log
```bash
# Periksa file log
tail -f logs/app.log

# Pemantauan log real-time (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Standar baru dalam klasifikasi gambar 🚀

---

# 🚀 VisionAI Pro - Hướng Dẫn Triển Khai Máy Chủ {#vietnamese}

## 🚀 Bắt Đầu Nhanh

### Yêu Cầu Trước
- Python 3.8 trở lên
- Git
- Hỗ trợ môi trường ảo

### 1. Sao Chép Kho Lưu Trữ
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Thiết Lập Môi Trường

#### Linux/macOS
```bash
# Tạo môi trường ảo
python3 -m venv venv

# Kích hoạt môi trường ảo
source venv/bin/activate

# Cài đặt các phụ thuộc
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
venv\Scripts\activate

# Cài đặt các phụ thuộc
pip install -r config/requirements.txt
```

### 3. Thực Thi Máy Chủ

#### Phương Pháp 1: Thực Thi Tập Trung (Được Khuyến Nghị)
```bash
# Máy chủ Phân Loại Zero-shot (Cổng 8002)
python3 main.py zero-shot

# Máy chủ Phân Loại Nâng Cao (Cổng 8001)
python3 main.py advanced

# Máy chủ Firebase (Cổng 8003)
python3 main.py firebase

# Máy chủ Chính (Cổng 8000)
python3 main.py main
```

#### Phương Pháp 2: Thực Thi Trực Tiếp với uvicorn
```bash
# Máy chủ Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Máy chủ Nâng Cao
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Máy chủ Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Phương Pháp 3: Sử Dụng Script
```bash
# Làm cho script có thể thực thi (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Chạy máy chủ
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Truy Cập Giao Diện Web

Sau khi khởi động máy chủ, truy cập giao diện web:

- **Phân Loại Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Phân Loại Nâng Cao**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Cấu Hình

### Biến Môi Trường
Tạo file `.env` trong thư mục gốc của dự án:

```bash
# Sao chép file ví dụ
cp config/env_example.txt .env

# Chỉnh sửa với các giá trị thực
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # hoặc cuda cho GPU
```

### Cấu Hình Mô Hình
- **Mô hình Zero-shot**: Sử dụng file `query/base_words.txt`
- **Mô hình Nâng Cao**: Sử dụng các mô hình đã được huấn luyện trước trong thư mục `data/models/`

## 📡 Điểm Cuối API

### API Phân Loại Zero-shot (Cổng 8002)
- `POST /api/classify` - Phân loại hình ảnh
- `GET /api/categories` - Danh sách danh mục
- `POST /api/categories/add` - Thêm danh mục
- `DELETE /api/categories/remove` - Xóa danh mục
- `GET /api/categories/search` - Tìm kiếm danh mục
- `GET /health` - Kiểm tra trạng thái máy chủ

### API Phân Loại Nâng Cao (Cổng 8001)
- `POST /api/classify` - Phân loại hình ảnh
- `GET /health` - Kiểm tra trạng thái máy chủ

### API Firebase (Cổng 8003)
- `POST /api/classify` - Phân loại hình ảnh với backend Firebase
- `GET /health` - Kiểm tra trạng thái máy chủ

## 🧪 Kiểm Tra

```bash
# Kiểm tra hệ thống
python3 scripts/testing/test_system.py

# Kiểm tra API
python3 scripts/testing/test_api.py

# Kiểm tra xác thực
python3 scripts/testing/test_auth.py

# Kiểm tra tất cả máy chủ
python3 scripts/testing/test_all_servers.py
```

## 📦 Triển Khai Sản Xuất

### Dịch Vụ Hệ Thống Linux
```bash
# Cài đặt dịch vụ
sudo ./scripts/setup/install_service.sh

# Khởi động dịch vụ
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Kiểm tra trạng thái
sudo systemctl status visionai-pro
```

### Triển Khai Docker
```bash
# Xây dựng hình ảnh Docker
docker build -t visionai-pro .

# Chạy container
docker run -p 8000:8000 visionai-pro
```

## 🔍 Khắc Phục Sự Cố

### Vấn Đề Thường Gặp
1. **Xung đột cổng**: Sử dụng cổng khác hoặc dừng dịch vụ đang chạy
2. **Lỗi tải mô hình**: Kiểm tra đường dẫn file mô hình
3. **Lỗi quyền**: Kiểm tra quyền file và quyền truy cập thư mục
4. **Lỗi nhập khẩu**: Đảm bảo môi trường ảo được kích hoạt

### Kiểm Tra Log
```bash
# Kiểm tra file log
tail -f logs/app.log

# Giám sát log thời gian thực (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Tiêu chuẩn mới trong phân loại hình ảnh 🚀

---

# 🚀 VisionAI Pro - Sunucu Dağıtım Kılavuzu {#turkish}

## 🚀 Hızlı Başlangıç

### Ön Gereksinimler
- Python 3.8 veya üzeri
- Git
- Sanal ortam desteği

### 1. Depoyu Klonla
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Ortam Kurulumu

#### Linux/macOS
```bash
# Sanal ortam oluştur
python3 -m venv venv

# Sanal ortamı etkinleştir
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Sanal ortam oluştur
python -m venv venv

# Sanal ortamı etkinleştir
venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r config/requirements.txt
```

### 3. Sunucu Çalıştırma

#### Yöntem 1: Merkezi Çalıştırma (Önerilen)
```bash
# Zero-shot Sınıflandırma Sunucusu (Port 8002)
python3 main.py zero-shot

# Gelişmiş Sınıflandırma Sunucusu (Port 8001)
python3 main.py advanced

# Firebase Sunucusu (Port 8003)
python3 main.py firebase

# Ana Sunucu (Port 8000)
python3 main.py main
```

#### Yöntem 2: Doğrudan uvicorn Çalıştırma
```bash
# Zero-shot Sunucusu
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Gelişmiş Sunucu
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Firebase Sunucusu
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Yöntem 3: Script Kullanma
```bash
# Scriptleri çalıştırılabilir yap (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Sunucuları çalıştır
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Web Arayüzü Erişimi

Sunucuyu başlattıktan sonra, web arayüzüne erişin:

- **Zero-shot Sınıflandırma**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Gelişmiş Sınıflandırma**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Yapılandırma

### Ortam Değişkenleri
Proje kök dizininde `.env` dosyası oluşturun:

```bash
# Örnek dosyayı kopyala
cp config/env_example.txt .env

# Gerçek değerlerle düzenle
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # veya GPU için cuda
```

### Model Yapılandırması
- **Zero-shot Model**: `query/base_words.txt` dosyasını kullanır
- **Gelişmiş Model**: `data/models/` klasöründeki önceden eğitilmiş modelleri kullanır

## 📡 API Uç Noktaları

### Zero-shot Sınıflandırma API (Port 8002)
- `POST /api/classify` - Görüntü sınıflandırma
- `GET /api/categories` - Kategori listesi
- `POST /api/categories/add` - Kategori ekle
- `DELETE /api/categories/remove` - Kategori kaldır
- `GET /api/categories/search` - Kategori ara
- `GET /health` - Sunucu durumunu kontrol et

### Gelişmiş Sınıflandırma API (Port 8001)
- `POST /api/classify` - Görüntü sınıflandırma
- `GET /health` - Sunucu durumunu kontrol et

### Firebase API (Port 8003)
- `POST /api/classify` - Firebase backend ile görüntü sınıflandırma
- `GET /health` - Sunucu durumunu kontrol et

## 🧪 Test

```bash
# Sistem testi
python3 scripts/testing/test_system.py

# API testi
python3 scripts/testing/test_api.py

# Kimlik doğrulama testi
python3 scripts/testing/test_auth.py

# Tüm sunucuları test et
python3 scripts/testing/test_all_servers.py
```

## 📦 Üretim Dağıtımı

### Linux Sistem Servisi
```bash
# Servisi yükle
sudo ./scripts/setup/install_service.sh

# Servisi başlat
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Durumu kontrol et
sudo systemctl status visionai-pro
```

### Docker Dağıtımı
```bash
# Docker görüntüsü oluştur
docker build -t visionai-pro .

# Konteyner çalıştır
docker run -p 8000:8000 visionai-pro
```

## 🔍 Sorun Giderme

### Yaygın Sorunlar
1. **Port çakışması**: Farklı port kullan veya çalışan servisi durdur
2. **Model yükleme hatası**: Model dosya yolunu kontrol et
3. **İzin hatası**: Dosya izinlerini ve dizin erişim haklarını kontrol et
4. **İçe aktarma hatası**: Sanal ortamın etkin olduğundan emin ol

### Log Kontrolü
```bash
# Log dosyasını kontrol et
tail -f logs/app.log

# Gerçek zamanlı log izleme (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Görüntü sınıflandırmasında yeni standart 🚀

---

# 🚀 VisionAI Pro - Guida alla Distribuzione del Server {#italian}

## 🚀 Avvio Rapido

### Prerequisiti
- Python 3.8 o superiore
- Git
- Supporto ambiente virtuale

### 1. Clona il Repository
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Configurazione dell'Ambiente

#### Linux/macOS
```bash
# Crea ambiente virtuale
python3 -m venv venv

# Attiva ambiente virtuale
source venv/bin/activate

# Installa dipendenze
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Crea ambiente virtuale
python -m venv venv

# Attiva ambiente virtuale
venv\Scripts\activate

# Installa dipendenze
pip install -r config/requirements.txt
```

### 3. Esecuzione del Server

#### Metodo 1: Esecuzione Centralizzata (Raccomandato)
```bash
# Server Classificazione Zero-shot (Porta 8002)
python3 main.py zero-shot

# Server Classificazione Avanzata (Porta 8001)
python3 main.py advanced

# Server Firebase (Porta 8003)
python3 main.py firebase

# Server Principale (Porta 8000)
python3 main.py main
```

#### Metodo 2: Esecuzione Diretta con uvicorn
```bash
# Server Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Server Avanzato
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Server Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Metodo 3: Utilizzo degli Script
```bash
# Rendi gli script eseguibili (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Esegui i server
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Accesso all'Interfaccia Web

Dopo aver avviato il server, accedi all'interfaccia web:

- **Classificazione Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classificazione Avanzata**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configurazione

### Variabili d'Ambiente
Crea un file `.env` nella root del progetto:

```bash
# Copia il file di esempio
cp config/env_example.txt .env

# Modifica con valori reali
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # o cuda per GPU
```

### Configurazione del Modello
- **Modello Zero-shot**: Utilizza il file `query/base_words.txt`
- **Modello Avanzato**: Utilizza modelli pre-addestrati nella cartella `data/models/`

## 📡 Endpoint API

### API Classificazione Zero-shot (Porta 8002)
- `POST /api/classify` - Classificazione immagini
- `GET /api/categories` - Lista categorie
- `POST /api/categories/add` - Aggiungi categoria
- `DELETE /api/categories/remove` - Rimuovi categoria
- `GET /api/categories/search` - Cerca categorie
- `GET /health` - Controlla stato server

### API Classificazione Avanzata (Porta 8001)
- `POST /api/classify` - Classificazione immagini
- `GET /health` - Controlla stato server

### API Firebase (Porta 8003)
- `POST /api/classify` - Classificazione immagini con backend Firebase
- `GET /health` - Controlla stato server

## 🧪 Test

```bash
# Test del sistema
python3 scripts/testing/test_system.py

# Test API
python3 scripts/testing/test_api.py

# Test autenticazione
python3 scripts/testing/test_auth.py

# Testa tutti i server
python3 scripts/testing/test_all_servers.py
```

## 📦 Distribuzione Produzione

### Servizio Sistema Linux
```bash
# Installa servizio
sudo ./scripts/setup/install_service.sh

# Avvia servizio
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Controlla stato
sudo systemctl status visionai-pro
```

### Distribuzione Docker
```bash
# Costruisci immagine Docker
docker build -t visionai-pro .

# Esegui container
docker run -p 8000:8000 visionai-pro
```

## 🔍 Risoluzione Problemi

### Problemi Comuni
1. **Conflitto porte**: Usa porta diversa o ferma servizio in esecuzione
2. **Errore caricamento modello**: Controlla percorso file modello
3. **Errore permessi**: Controlla permessi file e accesso directory
4. **Errore importazione**: Assicurati che ambiente virtuale sia attivato

### Controllo Log
```bash
# Controlla file log
tail -f logs/app.log

# Monitoraggio log tempo reale (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - Il nuovo standard nella classificazione delle immagini 🚀

---

# 🚀 VisionAI Pro - Guía de Despliegue del Servidor {#latin-mexico}

## 🚀 Inicio Rápido

### Requisitos Previos
- Python 3.8 o superior
- Git
- Soporte de entorno virtual

### 1. Clonar Repositorio
```bash
git clone https://github.com/pistolinkr/VisionAI2025Pro.git
cd VisionAI2025Pro
```

### 2. Configuración del Entorno

#### Linux/macOS
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r config/requirements.txt
```

#### Windows
```cmd
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
venv\Scripts\activate

# Instalar dependencias
pip install -r config/requirements.txt
```

### 3. Ejecución del Servidor

#### Método 1: Ejecución Centralizada (Recomendado)
```bash
# Servidor de Clasificación Zero-shot (Puerto 8002)
python3 main.py zero-shot

# Servidor de Clasificación Avanzada (Puerto 8001)
python3 main.py advanced

# Servidor Firebase (Puerto 8003)
python3 main.py firebase

# Servidor Principal (Puerto 8000)
python3 main.py main
```

#### Método 2: Ejecución Directa con uvicorn
```bash
# Servidor Zero-shot
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002

# Servidor Avanzado
uvicorn src.api.advanced_main:app --reload --host 0.0.0.0 --port 8001

# Servidor Firebase
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

#### Método 3: Usando Scripts
```bash
# Hacer scripts ejecutables (Linux/macOS)
chmod +x scripts/deployment/*.sh

# Ejecutar servidores
./scripts/deployment/start_zero_shot.sh
./scripts/deployment/start_advanced.sh
./scripts/deployment/start_firebase.sh
./scripts/deployment/start_main.sh
```

### 4. Acceso a la Interfaz Web

Después de iniciar el servidor, accede a la interfaz web:

- **Clasificación Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Clasificación Avanzada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuración

### Variables de Entorno
Crear archivo `.env` en la raíz del proyecto:

```bash
# Copiar archivo de ejemplo
cp config/env_example.txt .env

# Editar con valores reales
API_SECRET_KEY=your-secret-key-here
HOST=0.0.0.0
PORT=8000
DEBUG=false
ENVIRONMENT=production
DEVICE=cpu  # o cuda para GPU
```

### Configuración del Modelo
- **Modelo Zero-shot**: Usa archivo `query/base_words.txt`
- **Modelo Avanzado**: Usa modelos preentrenados en carpeta `data/models/`

## 📡 Endpoints de API

### API de Clasificación Zero-shot (Puerto 8002)
- `POST /api/classify` - Clasificación de imágenes
- `GET /api/categories` - Lista de categorías
- `POST /api/categories/add` - Agregar categoría
- `DELETE /api/categories/remove` - Eliminar categoría
- `GET /api/categories/search` - Buscar categorías
- `GET /health` - Verificar estado del servidor

### API de Clasificación Avanzada (Puerto 8001)
- `POST /api/classify` - Clasificación de imágenes
- `GET /health` - Verificar estado del servidor

### API Firebase (Puerto 8003)
- `POST /api/classify` - Clasificación de imágenes con backend Firebase
- `GET /health` - Verificar estado del servidor

## 🧪 Pruebas

```bash
# Prueba del sistema
python3 scripts/testing/test_system.py

# Prueba de API
python3 scripts/testing/test_api.py

# Prueba de autenticación
python3 scripts/testing/test_auth.py

# Probar todos los servidores
python3 scripts/testing/test_all_servers.py
```

## 📦 Despliegue en Producción

### Servicio del Sistema Linux
```bash
# Instalar servicio
sudo ./scripts/setup/install_service.sh

# Iniciar servicio
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro

# Verificar estado
sudo systemctl status visionai-pro
```

### Despliegue con Docker
```bash
# Construir imagen Docker
docker build -t visionai-pro .

# Ejecutar contenedor
docker run -p 8000:8000 visionai-pro
```

## 🔍 Solución de Problemas

### Problemas Comunes
1. **Conflicto de puertos**: Usar puerto diferente o detener servicio en ejecución
2. **Fallo de carga del modelo**: Verificar ruta del archivo del modelo
3. **Error de permisos**: Verificar permisos de archivos y acceso a directorios
4. **Error de importación**: Asegurar que el entorno virtual esté activado

### Verificación de Logs
```bash
# Verificar archivo de log
tail -f logs/app.log

# Monitoreo de logs en tiempo real (Linux)
journalctl -u visionai-pro -f
```

---

**VisionAI Pro** - El nuevo estándar en clasificación de imágenes 🚀
