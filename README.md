# VisionAI Pro Image Classification System

## 🌍 **Language Selection**

**[🇺🇸 English](#visionai-pro-image-classification-system)** | **[🇰🇷 Korean](#korean)** | **[🇨🇳 Chinese](#chinese)** | **[🇪🇸 Spanish](#spanish)** | **[🇫🇷 French](#french)** | **[🇩🇪 German](#german)** | **[🇵🇹 Portuguese](#portuguese)** | **[🇸🇦 Arabic](#arabic)** | **[🇮🇳 Hindi](#hindi)** | **[🇯🇵 Japanese](#japanese)** | **[🇷🇺 Russian](#russian)** | **[🇮🇩 Indonesian](#indonesian)** | **[🇻🇳 Vietnamese](#vietnamese)** | **[🇹🇷 Turkish](#turkish)** | **[🇮🇹 Italian](#italian)** | **[🇲🇽 Latin (Mexico)](#latin-mexico)**

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

# VisionAI Pro 이미지 분류 시스템 {#korean}

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

# VisionAI Pro 图像分类系统 {#chinese}

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

# 🔍 VisionAI Pro - Sistema de Clasificación de Imágenes {#spanish}

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

# 🔍 VisionAI Pro - Système de Classification d'Images {#french}

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

# 🔍 VisionAI Pro - Bildklassifizierungssystem {#german}

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

---

# 🔍 VisionAI Pro - Sistema de Classificação de Imagens {#portuguese}

Um sistema de classificação de imagens baseado em ProRL V2 que fornece uma interface web estilo Pinterest e API REST com **suporte de backend Firebase**.

## 🔥 Integração Firebase

Este sistema agora suporta **Firebase Firestore** como banco de dados backend, fornecendo:

- **Armazenamento em Nuvem**: Todos os dados armazenados com segurança no Firebase Firestore
- **Sincronização em Tempo Real**: Sincronização automática de dados entre dispositivos
- **Escalabilidade**: Construído para aplicações de alto tráfego
- **Gestão de Usuários**: Perfis de usuário avançados e estatísticas de uso
- **Analytics**: Rastreamento detalhado de uso e métricas de performance
- **Histórico**: Histórico completo de classificação para cada usuário

## ✨ Características Principais

- **Classificação de Imagens IA**: Classificação precisa de categorias de imagens usando o modelo ProRL V2
- **API REST**: Serviço API seguro com autenticação baseada em chave API
- **Interface Web**: Interface intuitiva estilo Pinterest para busca e classificação de imagens
- **Ferramenta CLI**: Classificação de imagens via linha de comando e gestão de chaves API
- **Análise em Tempo Real**: Classificação imediata e visualização de resultados de imagens carregadas

## 🚀 Início Rápido

### 1. Configuração do Ambiente

```bash
# Clonar repositório
git clone <repository-url>
cd VisionAI2025Pro

# Criar e ativar ambiente virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r config/requirements.txt
```

### 2. Variáveis de Ambiente

```bash
# Criar arquivo .env (referir-se ao env_example.txt)
cp config/env_example.txt .env

# Editar arquivo .env com valores reais
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # ou cuda
```

### 3. Iniciar Servidor

#### Opção A: SQLite (Padrão)
```bash
# Executar servidor principal com SQLite
python3 main.py zero-shot

# Ou executar uvicorn diretamente
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Opção B: Firebase
```bash
# Executar servidor baseado em Firebase
python3 main.py firebase

# Ou executar uvicorn diretamente
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Novo padrão em classificação de imagens 🚀

---

# 🔍 VisionAI Pro - نظام تصنيف الصور {#arabic}

نظام تصنيف الصور القائم على ProRL V2 الذي يوفر واجهة ويب على طراز Pinterest وواجهة برمجة تطبيقات REST مع **دعم خادم Firebase**.

## 🔥 تكامل Firebase

يدعم هذا النظام الآن **Firebase Firestore** كقاعدة بيانات خلفية، مما يوفر:

- **التخزين السحابي**: جميع البيانات مخزنة بأمان في Firebase Firestore
- **المزامنة في الوقت الفعلي**: مزامنة تلقائية للبيانات بين الأجهزة
- **القابلية للتوسع**: مصمم للتطبيقات عالية الحركة
- **إدارة المستخدمين**: ملفات مستخدمين متقدمة وإحصائيات الاستخدام
- **التحليلات**: تتبع مفصل للاستخدام ومقاييس الأداء
- **السجل**: سجل كامل للتصنيف لكل مستخدم

## ✨ الميزات الرئيسية

- **تصنيف الصور بالذكاء الاصطناعي**: تصنيف دقيق لفئات الصور باستخدام نموذج ProRL V2
- **واجهة برمجة تطبيقات REST**: خدمة API آمنة مع المصادقة القائمة على مفتاح API
- **واجهة الويب**: واجهة بديهية على طراز Pinterest للبحث وتصنيف الصور
- **أداة CLI**: تصنيف الصور من سطر الأوامر وإدارة مفاتيح API
- **التحليل في الوقت الفعلي**: تصنيف فوري وعرض نتائج الصور المرفوعة

## 🚀 البدء السريع

### 1. إعداد البيئة

```bash
# استنساخ المستودع
git clone <repository-url>
cd VisionAI2025Pro

# إنشاء وتفعيل البيئة الافتراضية
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# تثبيت التبعيات
pip install -r config/requirements.txt
```

### 2. متغيرات البيئة

```bash
# إنشاء ملف .env (الرجوع إلى env_example.txt)
cp config/env_example.txt .env

# تحرير ملف .env بقيم حقيقية
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # أو cuda
```

### 3. بدء الخادم

#### الخيار أ: SQLite (افتراضي)
```bash
# تشغيل الخادم الرئيسي مع SQLite
python3 main.py zero-shot

# أو تشغيل uvicorn مباشرة
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### الخيار ب: Firebase
```bash
# تشغيل الخادم القائم على Firebase
python3 main.py firebase

# أو تشغيل uvicorn مباشرة
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - معيار جديد في تصنيف الصور 🚀

---

# 🔍 VisionAI Pro - छवि वर्गीकरण प्रणाली {#hindi}

ProRL V2 आधारित छवि वर्गीकरण प्रणाली जो **Firebase बैकएंड समर्थन** के साथ Pinterest-शैली वेब इंटरफेस और REST API प्रदान करती है।

## 🔥 Firebase एकीकरण

यह प्रणाली अब **Firebase Firestore** को बैकएंड डेटाबेस के रूप में समर्थन करती है, प्रदान करती है:

- **क्लाउड स्टोरेज**: सभी डेटा Firebase Firestore में सुरक्षित रूप से संग्रहीत
- **रियल-टाइम सिंक्रनाइज़ेशन**: डिवाइसों के बीच डेटा का स्वचालित सिंक्रनाइज़ेशन
- **स्केलेबिलिटी**: उच्च-ट्रैफिक अनुप्रयोगों के लिए निर्मित
- **उपयोगकर्ता प्रबंधन**: उन्नत उपयोगकर्ता प्रोफाइल और उपयोग आंकड़े
- **एनालिटिक्स**: विस्तृत उपयोग ट्रैकिंग और प्रदर्शन मेट्रिक्स
- **इतिहास**: प्रत्येक उपयोगकर्ता के लिए पूर्ण वर्गीकरण इतिहास

## ✨ मुख्य विशेषताएं

- **AI छवि वर्गीकरण**: ProRL V2 मॉडल का उपयोग करके छवि श्रेणियों का सटीक वर्गीकरण
- **REST API**: API कुंजी-आधारित प्रमाणीकरण के साथ सुरक्षित API सेवा
- **वेब इंटरफेस**: छवि खोज और वर्गीकरण के लिए सहज Pinterest-शैली इंटरफेस
- **CLI उपकरण**: कमांड लाइन छवि वर्गीकरण और API कुंजी प्रबंधन
- **रियल-टाइम विश्लेषण**: अपलोड की गई छवियों का तत्काल वर्गीकरण और परिणाम प्रदर्शन

## 🚀 त्वरित प्रारंभ

### 1. पर्यावरण सेटअप

```bash
# रिपॉजिटरी क्लोन करें
git clone <repository-url>
cd VisionAI2025Pro

# वर्चुअल एनवायरनमेंट बनाएं और सक्रिय करें
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# निर्भरताएं स्थापित करें
pip install -r config/requirements.txt
```

### 2. पर्यावरण चर

```bash
# .env फ़ाइल बनाएं (env_example.txt देखें)
cp config/env_example.txt .env

# .env फ़ाइल को वास्तविक मूल्यों के साथ संपादित करें
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # या cuda
```

### 3. सर्वर शुरू करें

#### विकल्प ए: SQLite (डिफ़ॉल्ट)
```bash
# SQLite के साथ मुख्य सर्वर चलाएं
python3 main.py zero-shot

# या सीधे uvicorn चलाएं
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### विकल्प बी: Firebase
```bash
# Firebase-आधारित सर्वर चलाएं
python3 main.py firebase

# या सीधे uvicorn चलाएं
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - छवि वर्गीकरण में नया मानक 🚀

---

# 🔍 VisionAI Pro - 画像分類システム {#japanese}

ProRL V2ベースの画像分類システムで、**Firebaseバックエンドサポート**付きのPinterestスタイルのWebインターフェースとREST APIを提供します。

## 🔥 Firebase統合

このシステムは現在、バックエンドデータベースとして**Firebase Firestore**をサポートし、以下を提供します：

- **クラウドストレージ**: すべてのデータがFirebase Firestoreに安全に保存
- **リアルタイム同期**: デバイス間でのデータの自動同期
- **スケーラビリティ**: 高トラフィックアプリケーション向けに構築
- **ユーザー管理**: 高度なユーザープロファイルと使用統計
- **アナリティクス**: 詳細な使用追跡とパフォーマンスメトリクス
- **履歴**: 各ユーザーの完全な分類履歴

## ✨ 主な機能

- **AI画像分類**: ProRL V2モデルを使用した画像カテゴリの正確な分類
- **REST API**: APIキーベースの認証による安全なAPIサービス
- **Webインターフェース**: 画像検索と分類のための直感的なPinterestスタイルインターフェース
- **CLIツール**: コマンドライン画像分類とAPIキー管理
- **リアルタイム分析**: アップロードされた画像の即座の分類と結果表示

## 🚀 クイックスタート

### 1. 環境セットアップ

```bash
# リポジトリをクローン
git clone <repository-url>
cd VisionAI2025Pro

# 仮想環境を作成してアクティベート
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係をインストール
pip install -r config/requirements.txt
```

### 2. 環境変数

```bash
# .envファイルを作成（env_example.txtを参照）
cp config/env_example.txt .env

# .envファイルを実際の値で編集
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # または cuda
```

### 3. サーバー開始

#### オプションA: SQLite（デフォルト）
```bash
# SQLiteでメインサーバーを実行
python3 main.py zero-shot

# またはuvicornを直接実行
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### オプションB: Firebase
```bash
# Firebaseベースのサーバーを実行
python3 main.py firebase

# またはuvicornを直接実行
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - 画像分類の新しい標準 🚀

---

# 🔍 VisionAI Pro - Система классификации изображений {#russian}

Система классификации изображений на основе ProRL V2, которая предоставляет веб-интерфейс в стиле Pinterest и REST API с **поддержкой Firebase бэкенда**.

## 🔥 Интеграция Firebase

Эта система теперь поддерживает **Firebase Firestore** в качестве бэкенд базы данных, предоставляя:

- **Облачное хранилище**: Все данные безопасно хранятся в Firebase Firestore
- **Синхронизация в реальном времени**: Автоматическая синхронизация данных между устройствами
- **Масштабируемость**: Построена для высоконагруженных приложений
- **Управление пользователями**: Расширенные профили пользователей и статистика использования
- **Аналитика**: Детальное отслеживание использования и метрики производительности
- **История**: Полная история классификации для каждого пользователя

## ✨ Основные функции

- **ИИ классификация изображений**: Точная классификация категорий изображений с использованием модели ProRL V2
- **REST API**: Безопасный API сервис с аутентификацией на основе API ключа
- **Веб-интерфейс**: Интуитивный интерфейс в стиле Pinterest для поиска и классификации изображений
- **CLI инструмент**: Классификация изображений из командной строки и управление API ключами
- **Анализ в реальном времени**: Мгновенная классификация и отображение результатов загруженных изображений

## 🚀 Быстрый старт

### 1. Настройка окружения

```bash
# Клонировать репозиторий
git clone <repository-url>
cd VisionAI2025Pro

# Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r config/requirements.txt
```

### 2. Переменные окружения

```bash
# Создать файл .env (см. env_example.txt)
cp config/env_example.txt .env

# Отредактировать файл .env с реальными значениями
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # или cuda
```

### 3. Запуск сервера

#### Вариант А: SQLite (по умолчанию)
```bash
# Запустить основной сервер с SQLite
python3 main.py zero-shot

# Или запустить uvicorn напрямую
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Вариант Б: Firebase
```bash
# Запустить сервер на основе Firebase
python3 main.py firebase

# Или запустить uvicorn напрямую
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Новый стандарт в классификации изображений 🚀

---

# 🔍 VisionAI Pro - Sistem Klasifikasi Gambar {#indonesian}

Sistem klasifikasi gambar berbasis ProRL V2 yang menyediakan antarmuka web bergaya Pinterest dan REST API dengan **dukungan backend Firebase**.

## 🔥 Integrasi Firebase

Sistem ini sekarang mendukung **Firebase Firestore** sebagai database backend, menyediakan:

- **Penyimpanan Cloud**: Semua data disimpan dengan aman di Firebase Firestore
- **Sinkronisasi Real-time**: Sinkronisasi otomatis data antar perangkat
- **Skalabilitas**: Dibangun untuk aplikasi ber-traffic tinggi
- **Manajemen Pengguna**: Profil pengguna canggih dan statistik penggunaan
- **Analitik**: Pelacakan penggunaan detail dan metrik kinerja
- **Riwayat**: Riwayat klasifikasi lengkap untuk setiap pengguna

## ✨ Fitur Utama

- **Klasifikasi Gambar AI**: Klasifikasi akurat kategori gambar menggunakan model ProRL V2
- **REST API**: Layanan API aman dengan autentikasi berbasis kunci API
- **Antarmuka Web**: Antarmuka intuitif bergaya Pinterest untuk pencarian dan klasifikasi gambar
- **Tool CLI**: Klasifikasi gambar dari baris perintah dan manajemen kunci API
- **Analisis Real-time**: Klasifikasi instan dan tampilan hasil gambar yang diunggah

## 🚀 Mulai Cepat

### 1. Pengaturan Lingkungan

```bash
# Klon repositori
git clone <repository-url>
cd VisionAI2025Pro

# Buat dan aktifkan lingkungan virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependensi
pip install -r config/requirements.txt
```

### 2. Variabel Lingkungan

```bash
# Buat file .env (lihat env_example.txt)
cp config/env_example.txt .env

# Edit file .env dengan nilai yang sebenarnya
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # atau cuda
```

### 3. Mulai Server

#### Opsi A: SQLite (Default)
```bash
# Jalankan server utama dengan SQLite
python3 main.py zero-shot

# Atau jalankan uvicorn langsung
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Opsi B: Firebase
```bash
# Jalankan server berbasis Firebase
python3 main.py firebase

# Atau jalankan uvicorn langsung
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Standar baru dalam klasifikasi gambar 🚀

---

# 🔍 VisionAI Pro - Hệ Thống Phân Loại Hình Ảnh {#vietnamese}

Hệ thống phân loại hình ảnh dựa trên ProRL V2 cung cấp giao diện web kiểu Pinterest và REST API với **hỗ trợ backend Firebase**.

## 🔥 Tích Hợp Firebase

Hệ thống này hiện hỗ trợ **Firebase Firestore** làm cơ sở dữ liệu backend, cung cấp:

- **Lưu Trữ Đám Mây**: Tất cả dữ liệu được lưu trữ an toàn trong Firebase Firestore
- **Đồng Bộ Thời Gian Thực**: Đồng bộ tự động dữ liệu giữa các thiết bị
- **Khả Năng Mở Rộng**: Được xây dựng cho các ứng dụng có lưu lượng cao
- **Quản Lý Người Dùng**: Hồ sơ người dùng nâng cao và thống kê sử dụng
- **Phân Tích**: Theo dõi chi tiết việc sử dụng và các chỉ số hiệu suất
- **Lịch Sử**: Lịch sử phân loại đầy đủ cho mỗi người dùng

## ✨ Tính Năng Chính

- **Phân Loại Hình Ảnh AI**: Phân loại chính xác các danh mục hình ảnh sử dụng mô hình ProRL V2
- **REST API**: Dịch vụ API an toàn với xác thực dựa trên khóa API
- **Giao Diện Web**: Giao diện trực quan kiểu Pinterest để tìm kiếm và phân loại hình ảnh
- **Công Cụ CLI**: Phân loại hình ảnh từ dòng lệnh và quản lý khóa API
- **Phân Tích Thời Gian Thực**: Phân loại tức thì và hiển thị kết quả hình ảnh đã tải lên

## 🚀 Bắt Đầu Nhanh

### 1. Thiết Lập Môi Trường

```bash
# Sao chép kho lưu trữ
git clone <repository-url>
cd VisionAI2025Pro

# Tạo và kích hoạt môi trường ảo
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Cài đặt các phụ thuộc
pip install -r config/requirements.txt
```

### 2. Biến Môi Trường

```bash
# Tạo file .env (tham khảo env_example.txt)
cp config/env_example.txt .env

# Chỉnh sửa file .env với các giá trị thực
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # hoặc cuda
```

### 3. Khởi Động Máy Chủ

#### Tùy Chọn A: SQLite (Mặc Định)
```bash
# Chạy máy chủ chính với SQLite
python3 main.py zero-shot

# Hoặc chạy uvicorn trực tiếp
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Tùy Chọn B: Firebase
```bash
# Chạy máy chủ dựa trên Firebase
python3 main.py firebase

# Hoặc chạy uvicorn trực tiếp
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Tiêu chuẩn mới trong phân loại hình ảnh 🚀

---

# 🔍 VisionAI Pro - Görüntü Sınıflandırma Sistemi {#turkish}

ProRL V2 tabanlı görüntü sınıflandırma sistemi, **Firebase backend desteği** ile Pinterest tarzı web arayüzü ve REST API sağlar.

## 🔥 Firebase Entegrasyonu

Bu sistem artık backend veritabanı olarak **Firebase Firestore**'u destekliyor ve şunları sağlıyor:

- **Bulut Depolama**: Tüm veriler Firebase Firestore'da güvenli bir şekilde saklanıyor
- **Gerçek Zamanlı Senkronizasyon**: Cihazlar arası veri otomatik senkronizasyonu
- **Ölçeklenebilirlik**: Yüksek trafikli uygulamalar için inşa edilmiş
- **Kullanıcı Yönetimi**: Gelişmiş kullanıcı profilleri ve kullanım istatistikleri
- **Analitik**: Detaylı kullanım takibi ve performans metrikleri
- **Geçmiş**: Her kullanıcı için tam sınıflandırma geçmişi

## ✨ Ana Özellikler

- **AI Görüntü Sınıflandırması**: ProRL V2 modelini kullanarak görüntü kategorilerinin doğru sınıflandırması
- **REST API**: API anahtarı tabanlı kimlik doğrulama ile güvenli API hizmeti
- **Web Arayüzü**: Görüntü arama ve sınıflandırma için sezgisel Pinterest tarzı arayüz
- **CLI Aracı**: Komut satırı görüntü sınıflandırması ve API anahtarı yönetimi
- **Gerçek Zamanlı Analiz**: Yüklenen görüntülerin anında sınıflandırması ve sonuç görüntüleme

## 🚀 Hızlı Başlangıç

### 1. Ortam Kurulumu

```bash
# Depoyu klonla
git clone <repository-url>
cd VisionAI2025Pro

# Sanal ortam oluştur ve etkinleştir
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r config/requirements.txt
```

### 2. Ortam Değişkenleri

```bash
# .env dosyası oluştur (env_example.txt'ye bakın)
cp config/env_example.txt .env

# .env dosyasını gerçek değerlerle düzenle
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # veya cuda
```

### 3. Sunucuyu Başlat

#### Seçenek A: SQLite (Varsayılan)
```bash
# SQLite ile ana sunucuyu çalıştır
python3 main.py zero-shot

# Veya uvicorn'u doğrudan çalıştır
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Seçenek B: Firebase
```bash
# Firebase tabanlı sunucuyu çalıştır
python3 main.py firebase

# Veya uvicorn'u doğrudan çalıştır
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Görüntü sınıflandırmasında yeni standart 🚀

---

# 🔍 VisionAI Pro - Sistema di Classificazione delle Immagini {#italian}

Sistema di classificazione delle immagini basato su ProRL V2 che fornisce un'interfaccia web in stile Pinterest e API REST con **supporto backend Firebase**.

## 🔥 Integrazione Firebase

Questo sistema ora supporta **Firebase Firestore** come database backend, fornendo:

- **Archiviazione Cloud**: Tutti i dati archiviati in modo sicuro in Firebase Firestore
- **Sincronizzazione in Tempo Reale**: Sincronizzazione automatica dei dati tra dispositivi
- **Scalabilità**: Costruito per applicazioni ad alto traffico
- **Gestione Utenti**: Profili utente avanzati e statistiche di utilizzo
- **Analytics**: Tracciamento dettagliato dell'utilizzo e metriche delle prestazioni
- **Cronologia**: Cronologia completa di classificazione per ogni utente

## ✨ Caratteristiche Principali

- **Classificazione Immagini AI**: Classificazione accurata delle categorie di immagini utilizzando il modello ProRL V2
- **REST API**: Servizio API sicuro con autenticazione basata su chiave API
- **Interfaccia Web**: Interfaccia intuitiva in stile Pinterest per ricerca e classificazione delle immagini
- **Strumento CLI**: Classificazione delle immagini da riga di comando e gestione delle chiavi API
- **Analisi in Tempo Reale**: Classificazione istantanea e visualizzazione dei risultati delle immagini caricate

## 🚀 Avvio Rapido

### 1. Configurazione dell'Ambiente

```bash
# Clona il repository
git clone <repository-url>
cd VisionAI2025Pro

# Crea e attiva l'ambiente virtuale
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installa le dipendenze
pip install -r config/requirements.txt
```

### 2. Variabili d'Ambiente

```bash
# Crea il file .env (riferimento a env_example.txt)
cp config/env_example.txt .env

# Modifica il file .env con valori reali
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # o cuda
```

### 3. Avvia il Server

#### Opzione A: SQLite (Predefinito)
```bash
# Esegui il server principale con SQLite
python3 main.py zero-shot

# Oppure esegui uvicorn direttamente
uvicorn src.api.zero_shot_main:app --reload --host 0.0.0.0 --port 8002
```

#### Opzione B: Firebase
```bash
# Esegui il server basato su Firebase
python3 main.py firebase

# Oppure esegui uvicorn direttamente
uvicorn src.api.firebase_main:app --reload --host 0.0.0.0 --port 8003
```

---

**VisionAI Pro** - Nuovo standard nella classificazione delle immagini 🚀

---

# 🔍 VisionAI Pro - Sistema de Clasificación de Imágenes (México) {#latin-mexico}

Sistema de clasificación de imágenes basado en ProRL V2 que proporciona una interfaz web estilo Pinterest y API REST con **soporte de backend Firebase**.

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
