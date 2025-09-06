# VisionAI Pro Image Classification System

🧠 **High-Performance Image Classification System** - Multi-classification engine utilizing Zero-shot Learning and pre-trained models

## 📁 Project Structure

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Web Applications
│   ├── zero_shot/                  # Zero-shot Classification Web App
│   ├── advanced/                  # Advanced Classification Web App
│   └── firebase/                  # Firebase-based Web App
├── 🚀 scripts/                     # Execution and Management Scripts
│   ├── deployment/                # Server Execution Scripts
│   ├── setup/                     # Installation and Setup Scripts
│   └── testing/                   # Testing Scripts
├── 📊 data/                        # Data and Models
│   ├── models/                    # Trained Model Files
│   ├── cache/                     # Cache Files
│   └── uploads/                   # Uploaded Images
├── ⚙️ config/                      # Configuration Files
│   ├── config.py                  # Main Configuration
│   ├── firebase_config.py         # Firebase Configuration
│   └── requirements.txt           # Dependencies List
├── 📚 docs/                        # Documentation
│   ├── setup/                     # Installation Guide
│   └── api/                       # API Documentation
├── 🔧 src/                         # Source Code
│   ├── api/                       # API Server
│   ├── auth/                      # Authentication Management
│   ├── models/                    # Model Classes
│   └── cli/                       # CLI Tools
└── 🧪 tests/                       # Test Files
```

## 🚀 Quick Start

### 1. Environment Setup
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r config/requirements.txt
```

### 2. Server Execution

#### Zero-shot Classification Server (Port 8002)
```bash
# Direct execution
python3 main.py zero-shot

# Or use script
./scripts/deployment/start_zero_shot.sh
```

#### Advanced Classification Server (Port 8001)
```bash
# Direct execution
python3 main.py advanced

# Or use script
./scripts/deployment/start_advanced.sh
```

#### Firebase Server (Port 8003)
```bash
# Direct execution
python3 main.py firebase

# Or use script
./scripts/deployment/start_firebase.sh
```

#### Main Server (Port 8000)
```bash
# Direct execution
python3 main.py main

# Or use script
./scripts/deployment/start_main.sh
```

## 🌐 Web Interface

After starting the server, you can access the web interface at the following URLs:

- **Zero-shot Classification**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Advanced Classification**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Configuration

### Environment Variables
```bash
# Create config/.env file or set environment variables
export API_SECRET_KEY="your-secret-key"
export HOST="0.0.0.0"
export PORT="8000"
export DEBUG="false"
export ENVIRONMENT="production"
```

### Model Configuration
- Zero-shot model: Uses `query/base_words.txt` file
- Advanced model: Uses pre-trained models in `data/models/` folder

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

## 🧪 Testing

```bash
# System test
python3 scripts/testing/test_system.py

# API test
python3 scripts/testing/test_api.py

# Authentication test
python3 scripts/testing/test_auth.py
```

## 📦 Deployment

### Register as System Service (Linux)
```bash
# Install service
sudo ./scripts/setup/install_service.sh

# Start service
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro
```

### Docker Deployment (Optional)
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

### Log Checking
```bash
# Check log file
tail -f logs/app.log

# Real-time log monitoring
journalctl -u visionai-pro -f
```

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.

## 🤝 Contributing

Bug reports, feature requests, and pull requests are welcome!

---

**VisionAI Pro** - The new standard for image classification 🚀

---

# VisionAI Pro 이미지 분류 시스템

🧠 **고성능 이미지 분류 시스템** - Zero-shot Learning과 사전 훈련된 모델을 활용한 다중 분류 엔진

## 📁 프로젝트 구조

```
VisionAI2025Pro/
├── 📱 web_apps/                    # 웹 애플리케이션
│   ├── zero_shot/                  # Zero-shot 분류 웹앱
│   ├── advanced/                  # 고급 분류 웹앱
│   └── firebase/                  # Firebase 기반 웹앱
├── 🚀 scripts/                     # 실행 및 관리 스크립트
│   ├── deployment/                # 서버 실행 스크립트
│   ├── setup/                     # 설치 및 설정 스크립트
│   └── testing/                   # 테스트 스크립트
├── 📊 data/                        # 데이터 및 모델
│   ├── models/                    # 훈련된 모델 파일
│   ├── cache/                     # 캐시 파일
│   └── uploads/                   # 업로드된 이미지
├── ⚙️ config/                      # 설정 파일
│   ├── config.py                  # 메인 설정
│   ├── firebase_config.py         # Firebase 설정
│   └── requirements.txt           # 의존성 목록
├── 📚 docs/                        # 문서
│   ├── setup/                     # 설치 가이드
│   └── api/                       # API 문서
├── 🔧 src/                         # 소스 코드
│   ├── api/                       # API 서버
│   ├── auth/                      # 인증 관리
│   ├── models/                    # 모델 클래스
│   └── cli/                       # CLI 도구
└── 🧪 tests/                       # 테스트 파일
```

## 🚀 빠른 시작

### 1. 환경 설정
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate     # Windows

# 의존성 설치
pip install -r config/requirements.txt
```

### 2. 서버 실행

#### Zero-shot 분류 서버 (포트 8002)
```bash
# 직접 실행
python3 main.py zero-shot

# 또는 스크립트 사용
./scripts/deployment/start_zero_shot.sh
```

#### 고급 분류 서버 (포트 8001)
```bash
# 직접 실행
python3 main.py advanced

# 또는 스크립트 사용
./scripts/deployment/start_advanced.sh
```

#### Firebase 서버 (포트 8003)
```bash
# 직접 실행
python3 main.py firebase

# 또는 스크립트 사용
./scripts/deployment/start_firebase.sh
```

#### 메인 서버 (포트 8000)
```bash
# 직접 실행
python3 main.py main

# 또는 스크립트 사용
./scripts/deployment/start_main.sh
```

## 🌐 웹 인터페이스

서버 실행 후 다음 URL에서 웹 인터페이스에 접근할 수 있습니다:

- **Zero-shot 분류**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **고급 분류**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 설정

### 환경 변수
```bash
# config/.env 파일 생성 또는 환경 변수 설정
export API_SECRET_KEY="your-secret-key"
export HOST="0.0.0.0"
export PORT="8000"
export DEBUG="false"
export ENVIRONMENT="production"
```

### 모델 설정
- Zero-shot 모델: `query/base_words.txt` 파일 사용
- 고급 모델: `data/models/` 폴더의 사전 훈련된 모델 사용

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

## 🧪 테스트

```bash
# 시스템 테스트
python3 scripts/testing/test_system.py

# API 테스트
python3 scripts/testing/test_api.py

# 인증 테스트
python3 scripts/testing/test_auth.py
```

## 📦 배포

### 시스템 서비스로 등록 (Linux)
```bash
# 서비스 설치
sudo ./scripts/setup/install_service.sh

# 서비스 시작
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro
```

### Docker 배포 (선택사항)
```bash
# Docker 이미지 빌드
docker build -t visionai-pro .

# 컨테이너 실행
docker run -p 8000:8000 visionai-pro
```

## 🔍 문제 해결

### 일반적인 문제
1. **포트 충돌**: 다른 포트를 사용하거나 실행 중인 서비스를 종료
2. **모델 로드 실패**: 모델 파일 경로 확인
3. **권한 오류**: 파일 권한 및 디렉토리 접근 권한 확인

### 로그 확인
```bash
# 로그 파일 확인
tail -f logs/app.log

# 실시간 로그 모니터링
journalctl -u visionai-pro -f
```

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 🤝 기여

버그 리포트, 기능 요청, 풀 리퀘스트를 환영합니다!

---

**VisionAI Pro** - 이미지 분류의 새로운 표준 🚀

---

# VisionAI Pro 图像分类系统

🧠 **高性能图像分类系统** - 利用零样本学习和预训练模型的多分类引擎

## 📁 项目结构

```
VisionAI2025Pro/
├── 📱 web_apps/                    # 网络应用程序
│   ├── zero_shot/                  # 零样本分类网络应用
│   ├── advanced/                  # 高级分类网络应用
│   └── firebase/                  # 基于Firebase的网络应用
├── 🚀 scripts/                     # 执行和管理脚本
│   ├── deployment/                # 服务器执行脚本
│   ├── setup/                     # 安装和设置脚本
│   └── testing/                   # 测试脚本
├── 📊 data/                        # 数据和模型
│   ├── models/                    # 训练模型文件
│   ├── cache/                     # 缓存文件
│   └── uploads/                   # 上传的图像
├── ⚙️ config/                      # 配置文件
│   ├── config.py                  # 主配置
│   ├── firebase_config.py         # Firebase配置
│   └── requirements.txt           # 依赖列表
├── 📚 docs/                        # 文档
│   ├── setup/                     # 安装指南
│   └── api/                       # API文档
├── 🔧 src/                         # 源代码
│   ├── api/                       # API服务器
│   ├── auth/                      # 认证管理
│   ├── models/                    # 模型类
│   └── cli/                       # CLI工具
└── 🧪 tests/                       # 测试文件
```

## 🚀 快速开始

### 1. 环境设置
```bash
# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r config/requirements.txt
```

### 2. 服务器执行

#### 零样本分类服务器 (端口 8002)
```bash
# 直接执行
python3 main.py zero-shot

# 或使用脚本
./scripts/deployment/start_zero_shot.sh
```

#### 高级分类服务器 (端口 8001)
```bash
# 直接执行
python3 main.py advanced

# 或使用脚本
./scripts/deployment/start_advanced.sh
```

#### Firebase服务器 (端口 8003)
```bash
# 直接执行
python3 main.py firebase

# 或使用脚本
./scripts/deployment/start_firebase.sh
```

#### 主服务器 (端口 8000)
```bash
# 直接执行
python3 main.py main

# 或使用脚本
./scripts/deployment/start_main.sh
```

## 🌐 网络界面

启动服务器后，您可以通过以下URL访问网络界面：

- **零样本分类**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **高级分类**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 配置

### 环境变量
```bash
# 创建config/.env文件或设置环境变量
export API_SECRET_KEY="your-secret-key"
export HOST="0.0.0.0"
export PORT="8000"
export DEBUG="false"
export ENVIRONMENT="production"
```

### 模型配置
- 零样本模型：使用`query/base_words.txt`文件
- 高级模型：使用`data/models/`文件夹中的预训练模型

## 📡 API端点

### 零样本分类API (端口 8002)
- `POST /api/classify` - 图像分类
- `GET /api/categories` - 类别列表
- `POST /api/categories/add` - 添加类别
- `DELETE /api/categories/remove` - 删除类别
- `GET /api/categories/search` - 搜索类别
- `GET /health` - 服务器状态检查

### 高级分类API (端口 8001)
- `POST /api/classify` - 图像分类
- `GET /health` - 服务器状态检查

## 🧪 测试

```bash
# 系统测试
python3 scripts/testing/test_system.py

# API测试
python3 scripts/testing/test_api.py

# 认证测试
python3 scripts/testing/test_auth.py
```

## 📦 部署

### 注册为系统服务 (Linux)
```bash
# 安装服务
sudo ./scripts/setup/install_service.sh

# 启动服务
sudo systemctl start visionai-pro
sudo systemctl enable visionai-pro
```

### Docker部署 (可选)
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

### 日志检查
```bash
# 检查日志文件
tail -f logs/app.log

# 实时日志监控
journalctl -u visionai-pro -f
```

## 📄 许可证

本项目在MIT许可证下分发。详情请参阅`LICENSE`文件。

## 🤝 贡献

欢迎错误报告、功能请求和拉取请求！

---

**VisionAI Pro** - 图像分类的新标准 🚀

---

# 🔍 VisionAI Pro - Sistema de Clasificación de Imágenes

Un sistema de clasificación de imágenes basado en ProRL V2 que proporciona una interfaz web estilo Pinterest y API REST con **soporte de backend Firebase**.

## 🔥 Integración Firebase

Este sistema ahora admite **Firebase Firestore** como base de datos backend, proporcionando:

- **Almacenamiento en la Nube**: Todos los datos almacenados de forma segura en Firebase Firestore
- **Sincronización en Tiempo Real**: Sincronización automática de datos entre dispositivos
- **Escalabilidad**: Construido para aplicaciones de alto tráfico
- **Gestión de Usuarios**: Perfiles de usuario avanzados y estadísticas de uso
- **Analíticas**: Seguimiento detallado de uso y métricas de rendimiento
- **Historial**: Historial completo de clasificación para cada usuario

## ✨ Características Principales

- **Clasificación de Imágenes IA**: Clasificación precisa de categorías de imágenes usando el modelo ProRL V2
- **API REST**: Servicio API seguro con autenticación basada en clave API
- **Interfaz Web**: Interfaz intuitiva estilo Pinterest para búsqueda y clasificación de imágenes
- **Herramienta CLI**: Clasificación de imágenes desde línea de comandos y gestión de claves API
- **Análisis en Tiempo Real**: Clasificación inmediata y visualización de resultados de imágenes subidas

## 🚀 Inicio Rápido

### 1. Configuración del Entorno

```bash
# Clonar repositorio
git clone <repository-url>
cd VisionAI2025Pro

# Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r config/requirements.txt
```

### 2. Variables de Entorno

```bash
# Crear archivo .env (referirse a env_example.txt)
cp config/env_example.txt .env

# Editar archivo .env con valores reales
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # o cuda
```

### 3. Iniciar Servidor

#### Opción A: SQLite (Predeterminado)
```bash
# Ejecutar servidor principal con SQLite
python3 main.py zero-shot

# O ejecutar uvicorn directamente
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Opción B: Firebase
```bash
# Ejecutar servidor basado en Firebase
python3 main.py firebase

# O ejecutar uvicorn directamente
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Nuevo estándar en clasificación de imágenes 🚀

---

# 🔍 VisionAI Pro - Système de Classification d'Images

Un système de classification d'images basé sur ProRL V2 qui fournit une interface web style Pinterest et une API REST avec **support de backend Firebase**.

## 🔥 Intégration Firebase

Ce système prend maintenant en charge **Firebase Firestore** comme base de données backend, fournissant :

- **Stockage Cloud** : Toutes les données stockées de manière sécurisée dans Firebase Firestore
- **Synchronisation en Temps Réel** : Synchronisation automatique des données entre appareils
- **Évolutivité** : Construit pour les applications à fort trafic
- **Gestion des Utilisateurs** : Profils d'utilisateurs avancés et statistiques d'utilisation
- **Analytiques** : Suivi détaillé de l'utilisation et métriques de performance
- **Historique** : Historique complet de classification pour chaque utilisateur

## ✨ Caractéristiques Principales

- **Classification d'Images IA** : Classification précise des catégories d'images utilisant le modèle ProRL V2
- **API REST** : Service API sécurisé avec autenticación basée sur la clé API
- **Interface Web** : Interface intuitive style Pinterest pour la recherche et classification d'images
- **Outil CLI** : Classification d'images en ligne de commande et gestion des clés API
- **Analyse en Temps Réel** : Classification immédiate et affichage des résultats des images téléchargées

## 🚀 Démarrage Rapide

### 1. Configuration de l'Environnement

```bash
# Cloner le dépôt
git clone <repository-url>
cd VisionAI2025Pro

# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r config/requirements.txt
```

### 2. Variables d'Environnement

```bash
# Créer le fichier .env (se référer à env_example.txt)
cp config/env_example.txt .env

# Éditer le fichier .env avec les vraies valeurs
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # ou cuda
```

### 3. Démarrer le Serveur

#### Option A : SQLite (Par défaut)
```bash
# Exécuter le serveur principal avec SQLite
python3 main.py zero-shot

# Ou exécuter uvicorn directement
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Option B : Firebase
```bash
# Exécuter le serveur basé sur Firebase
python3 main.py firebase

# Ou exécuter uvicorn directement
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Nouveau standard en classification d'images 🚀

---

# 🔍 VisionAI Pro - Bildklassifizierungssystem

Ein ProRL V2-basiertes Bildklassifizierungssystem, das eine Pinterest-ähnliche Web-Oberfläche und REST-API mit **Firebase Backend-Unterstützung** bietet.

## 🔥 Firebase-Integration

Dieses System unterstützt jetzt **Firebase Firestore** als Backend-Datenbank und bietet:

- **Cloud-Speicher**: Alle Daten sicher in Firebase Firestore gespeichert
- **Echtzeit-Synchronisation**: Automatische Datensynchronisation zwischen Geräten
- **Skalierbarkeit**: Für hochfrequente Anwendungen entwickelt
- **Benutzerverwaltung**: Erweiterte Benutzerprofile und Nutzungsstatistiken
- **Analytik**: Detailliertes Nutzungstracking und Leistungsmetriken
- **Verlauf**: Vollständiger Klassifizierungsverlauf für jeden Benutzer

## ✨ Hauptmerkmale

- **KI-Bildklassifizierung**: Präzise Bildkategorienklassifizierung mit dem ProRL V2-Modell
- **REST-API**: Sicherer API-Service mit API-Schlüssel-basierter Authentifizierung
- **Web-Interface**: Intuitive Pinterest-ähnliche Bildsuch- und Klassifizierungsoberfläche
- **CLI-Tool**: Befehlszeilen-Bildklassifizierung und API-Schlüsselverwaltung
- **Echtzeit-Analyse**: Sofortige Klassifizierung und Ergebnisanzeige hochgeladener Bilder

## 🚀 Schnellstart

### 1. Umgebungseinrichtung

```bash
# Repository klonen
git clone <repository-url>
cd VisionAI2025Pro

# Virtuelle Umgebung erstellen und aktivieren
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r config/requirements.txt
```

### 2. Umgebungsvariablen

```bash
# .env-Datei erstellen (siehe env_example.txt)
cp config/env_example.txt .env

# .env-Datei mit echten Werten bearbeiten
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # oder cuda
```

### 3. Server starten

#### Option A: SQLite (Standard)
```bash
# Hauptserver mit SQLite ausführen
python3 main.py zero-shot

# Oder uvicorn direkt ausführen
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Option B: Firebase
```bash
# Firebase-basierten Server ausführen
python3 main.py firebase

# Oder uvicorn direkt ausführen
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Neuer Standard in der Bildklassifizierung 🚀