# 🔍 VisionAI Pro - Image Classification System

A ProRL V2-based image category auto-recommendation system that provides a Pinterest-style web interface and REST API.

## 🌍 **Language / 언어 선택**

**[🇺🇸 English](#-key-features)** | **[🇰🇷 한국어](#-한국어-korean)** | **[🇨🇳 中文](#-中文-chinese)** | **[🇯🇵 日本語](#-日本語-japanese)** | **[🇪🇸 Español](#-español-spanish)** | **[🇫🇷 Français](#-français-french)** | **[🇷🇺 Русский](#-русский-russian)** | **[🇧🇷 Português](#-português-portuguese)**

## ✨ Key Features

- **AI Image Classification**: Accurate image category classification using ProRL V2 model
- **REST API**: Secure API service with API key-based authentication
- **Web Interface**: Intuitive Pinterest-style image search and classification interface
- **CLI Tool**: Command-line image classification and API key management
- **Real-time Analysis**: Immediate classification and result display of uploaded images

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone repository
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Variables

```bash
# Create .env file (refer to env_example.txt)
cp env_example.txt .env

# Edit .env file with actual values
API_SECRET_KEY=your-secret-key-here
DEVICE=cpu  # or cuda
```

### 3. Start Server

```bash
# Run main server
python run.py

# Or run uvicorn directly
uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Access Web Interface

Open `http://localhost:8000` in your browser

## 📚 Usage

### Web Interface

1. **Upload Image**: Click "Upload Image" button in top right
2. **Enter API Key**: Input valid API key
3. **Select Image**: Choose file or drag and drop
4. **Start Analysis**: Click "Start Analysis" button
5. **View Results**: Check classification results and confidence

### CLI Tool

```bash
# Image classification
python src/cli/main.py classify image.jpg --top-k 5

# Generate API key
python src/cli/main.py keys generate --name "Test Key" --permissions "read,classify,admin"

# List API keys
python src/cli/main.py keys list

# Revoke API key
python src/cli/main.py keys revoke --key "your-api-key"
```

### API Usage

#### Image Classification

```bash
curl -X POST "http://localhost:8000/api/classify" \
  -H "X-API-Key: your-api-key" \
  -F "file=@image.jpg" \
  -F "top_k=5"
```

#### Get Categories

```bash
curl -X GET "http://localhost:8000/api/categories" \
  -H "X-API-Key: your-api-key"
```

#### Generate API Key

```bash
curl -X POST "http://localhost:8000/api/keys/generate" \
  -H "X-API-Key: your-admin-api-key" \
  -F "name=NewKey" \
  -F "permissions=read,classify" \
  -F "expiry_days=365"
```

## 🏗️ Project Structure

```
ProRL V2 for catagorize images/
├── src/
│   ├── api/
│   │   └── main.py              # FastAPI main server
│   ├── models/
│   │   └── prorl_classifier.py  # ProRL V2 classification model
│   ├── auth/
│   │   └── api_key_manager.py   # API key management
│   └── cli/
│       └── main.py              # CLI tool
├── templates/
│   └── index.html               # Web interface
├── static/                      # Static files
├── models/                      # Model file storage
├── uploads/                     # Uploaded images
├── logs/                        # Log files
├── config.py                    # Configuration file
├── run.py                       # Execution script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## ⚙️ Configuration Options

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `API_SECRET_KEY` | `your-secret-key-change-this` | API security key |
| `DEVICE` | `cpu` | Device to use (cpu/cuda) |
| `PORT` | `8000` | Server port |
| `MODEL_PATH` | `./models/prorl_v2_model` | Model file path |
| `UPLOAD_DIR` | `./uploads` | Upload directory |
| `MAX_FILE_SIZE` | `10485760` | Maximum file size (10MB) |

### Model Configuration

Currently using a default CNN model. To replace with actual ProRL V2 model:

1. Save model file in `models/` directory
2. Set `MODEL_PATH` environment variable
3. Modify `load_model` method in `ProRLV2Classifier` class

## 🔑 API Key Management

### Permission Levels

- **read**: View categories
- **classify**: Image classification
- **admin**: API key generation/management

### Generate API Key

```python
from src.auth.api_key_manager import APIKeyManager

manager = APIKeyManager()
api_key = manager.generate_api_key(
    user_id="user123",
    name="Test Key",
    permissions=["read", "classify"],
    expiry_days=365
)
```

## 🧪 Testing

### Unit Tests

```bash
# Run unit tests
python -m pytest tests/

# API tests
python tests/test_api.py

# Model tests
python tests/test_classifier.py
```

### API Testing Guide

#### 1. Start the API Server

```bash
# Option 1: Using run.py
venv/bin/python run.py

# Option 2: Direct uvicorn
venv/bin/uvicorn src.api.main:app --host 127.0.0.1 --port 8000

# Option 3: With reload for development
venv/bin/uvicorn src.api.main:app --reload --host 127.0.0.1 --port 8000
```

#### 2. Test API Endpoints

##### Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "classifier_loaded": true,
  "api_key_manager_loaded": true
}
```

##### Get Available Categories
```bash
curl -H "X-API-Key: your-api-key" http://localhost:8000/api/categories
```

Expected response:
```json
{
  "success": true,
  "categories": ["Nature", "City", "People", "Animals", "Food", ...],
  "total_count": 20
}
```

##### Image Classification
```bash
curl -X POST "http://localhost:8000/api/classify" \
  -H "X-API-Key: your-api-key" \
  -F "file=@path/to/your/image.jpg" \
  -F "top_k=5"
```

Expected response:
```json
{
  "success": true,
  "image_name": "image.jpg",
  "predictions": [
    {"category": "Nature", "confidence": 0.85},
    {"category": "Mountains", "confidence": 0.12},
    {"category": "Ocean", "confidence": 0.03}
  ],
  "user_id": "user123",
  "timestamp": "2024-01-01T12:00:00"
}
```

##### Generate API Key (Admin only)
```bash
curl -X POST "http://localhost:8000/api/keys/generate" \
  -H "X-API-Key: admin-api-key" \
  -F "name=TestKey" \
  -F "permissions=read,classify" \
  -F "expiry_days=365"
```

Expected response:
```json
{
  "success": true,
  "api_key": "generated-api-key-here",
  "name": "TestKey",
  "permissions": ["read", "classify"],
  "expires_in_days": 365
}
```

##### Get API Key Info
```bash
curl -H "X-API-Key: your-api-key" http://localhost:8000/api/keys/info
```

##### Revoke API Key (Admin only)
```bash
curl -X DELETE "http://localhost:8000/api/keys/revoke" \
  -H "X-API-Key: admin-api-key" \
  -F "target_key=key-to-revoke"
```

#### 3. Web Interface Testing

1. Open http://localhost:8000 in your browser
2. Click "Upload Image" button
3. Enter a valid API key
4. Select an image file
5. Click "Start Analysis"
6. View the classification results

#### 4. CLI Tool Testing

```bash
# Test image classification
venv/bin/python src/cli/main.py classify path/to/image.jpg --top-k 3

# Test API key generation
venv/bin/python src/cli/main.py keys generate --name "CLI Test Key" --permissions "read,classify"

# Test API key listing
venv/bin/python src/cli/main.py keys list

# Test API key revocation
venv/bin/python src/cli/main.py keys revoke --key "your-api-key"
```

#### 5. Error Testing

Test various error scenarios:

```bash
# Test without API key
curl http://localhost:8000/api/classify

# Test with invalid API key
curl -H "X-API-Key: invalid-key" http://localhost:8000/api/classify

# Test with non-image file
curl -X POST "http://localhost:8000/api/classify" \
  -H "X-API-Key: your-api-key" \
  -F "file=@README.md"

# Test with expired API key
# (Create an expired key first, then test)
```

#### 6. Performance Testing

```bash
# Test with multiple concurrent requests
for i in {1..10}; do
  curl -X POST "http://localhost:8000/api/classify" \
    -H "X-API-Key: your-api-key" \
    -F "file=@test-image.jpg" &
done
wait
```

#### 7. Browser Developer Tools

1. Open browser developer tools (F12)
2. Go to Network tab
3. Upload an image and observe the API calls
4. Check response times and data
5. Verify error handling for invalid requests

## 🚀 Deployment

### Using Docker

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["python", "run.py"]
```

### Environment-specific Configuration

```bash
# Development environment
ENVIRONMENT=development python run.py

# Production environment
ENVIRONMENT=production python run.py

# Testing environment
ENVIRONMENT=testing python run.py
```

## 🤝 Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for details.

## 📞 Support

- **Issue Reports**: Use GitHub Issues
- **Documentation**: Refer to `/docs` directory
- **API Documentation**: `http://localhost:8000/docs` (Swagger UI)

## 🔮 Future Plans

- [ ] Integrate actual ProRL V2 model
- [ ] Batch image processing
- [ ] User management system
- [ ] Image database
- [ ] Advanced search filters
- [ ] Mobile app
- [ ] Cloud deployment guide

---

Start your new image analysis experience with the **VisionAI Pro Image Classification System**! 🎉

---

## 🌍 **Multilingual Support**

### 🇰🇷 한국어 (Korean)

**VisionAI Pro**는 ProRL V2 기반의 이미지 카테고리 자동 추천 시스템으로, 핀터레스트 스타일의 웹 인터페이스와 REST API를 제공합니다.

**주요 기능:**
- **AI 이미지 분류**: ProRL V2 모델을 사용한 정확한 이미지 카테고리 분류
- **REST API**: API 키 기반 인증을 통한 보안 API 서비스
- **웹 인터페이스**: 직관적인 핀터레스트 스타일의 이미지 검색 및 분류 인터페이스
- **CLI 도구**: 명령줄 이미지 분류 및 API 키 관리
- **실시간 분석**: 업로드된 이미지의 즉시 분류 및 결과 표시

**빠른 시작:**
```bash
# 저장소 클론
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서버 실행
python run.py
```

---

### 🇨🇳 中文 (Chinese)

**VisionAI Pro**是一个基于ProRL V2的图像分类自动推荐系统，提供Pinterest风格的Web界面和REST API。

**主要功能:**
- **AI图像分类**: 使用ProRL V2模型进行准确的图像类别分类
- **REST API**: 基于API密钥认证的安全API服务
- **Web界面**: 直观的Pinterest风格图像搜索和分类界面
- **CLI工具**: 命令行图像分类和API密钥管理
- **实时分析**: 上传图像的即时分类和结果显示

**快速开始:**
```bash
# 克隆仓库
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# 创建并激活虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 运行服务器
python run.py
```

---

### 🇯🇵 日本語 (Japanese)

**VisionAI Pro**は、ProRL V2ベースの画像カテゴリ自動推薦システムで、PinterestスタイルのWebインターフェースとREST APIを提供します。

**主な機能:**
- **AI画像分類**: ProRL V2モデルを使用した正確な画像カテゴリ分類
- **REST API**: APIキーベース認証によるセキュアなAPIサービス
- **Webインターフェース**: 直感的なPinterestスタイルの画像検索・分類インターフェース
- **CLIツール**: コマンドライン画像分類とAPIキー管理
- **リアルタイム分析**: アップロードされた画像の即座の分類と結果表示

**クイックスタート:**
```bash
# リポジトリをクローン
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# 仮想環境を作成・アクティベート
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係をインストール
pip install -r requirements.txt

# サーバーを起動
python run.py
```

---

### 🇪🇸 Español (Spanish)

**VisionAI Pro** es un sistema de recomendación automática de categorías de imágenes basado en ProRL V2 que proporciona una interfaz web estilo Pinterest y una API REST.

**Características principales:**
- **Clasificación de imágenes con IA**: Clasificación precisa de categorías de imágenes usando el modelo ProRL V2
- **API REST**: Servicio API seguro con autenticación basada en claves API
- **Interfaz web**: Interfaz intuitiva de búsqueda y clasificación de imágenes estilo Pinterest
- **Herramienta CLI**: Clasificación de imágenes por línea de comandos y gestión de claves API
- **Análisis en tiempo real**: Clasificación inmediata y visualización de resultados de imágenes subidas

**Inicio rápido:**
```bash
# Clonar repositorio
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python run.py
```

---

### 🇫🇷 Français (French)

**VisionAI Pro** est un système de recommandation automatique de catégories d'images basé sur ProRL V2 qui fournit une interface web de style Pinterest et une API REST.

**Fonctionnalités principales:**
- **Classification d'images par IA**: Classification précise des catégories d'images en utilisant le modèle ProRL V2
- **API REST**: Service API sécurisé avec authentification basée sur les clés API
- **Interface web**: Interface intuitive de recherche et de classification d'images de style Pinterest
- **Outil CLI**: Classification d'images en ligne de commande et gestion des clés API
- **Analyse en temps réel**: Classification immédiate et affichage des résultats des images téléchargées

**Démarrage rapide:**
```bash
# Cloner le dépôt
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# Créer et activer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Exécuter le serveur
python run.py
```

---

### 🇷🇺 Русский (Russian)

**VisionAI Pro** - это система автоматических рекомендаций по категориям изображений на основе ProRL V2, которая предоставляет веб-интерфейс в стиле Pinterest и REST API.

**Основные возможности:**
- **ИИ-классификация изображений**: Точная классификация категорий изображений с использованием модели ProRL V2
- **REST API**: Безопасный API-сервис с аутентификацией на основе API-ключей
- **Веб-интерфейс**: Интуитивный интерфейс поиска и классификации изображений в стиле Pinterest
- **CLI-инструмент**: Классификация изображений через командную строку и управление API-ключами
- **Анализ в реальном времени**: Мгновенная классификация и отображение результатов загруженных изображений

**Быстрый старт:**
```bash
# Клонировать репозиторий
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt

# Запустить сервер
python run.py
```

---

### 🇧🇷 Português (Portuguese)

**VisionAI Pro** é um sistema de recomendação automática de categorias de imagens baseado no ProRL V2 que fornece uma interface web estilo Pinterest e uma API REST.

**Recursos principais:**
- **Classificação de imagens com IA**: Classificação precisa de categorias de imagens usando o modelo ProRL V2
- **API REST**: Serviço API seguro com autenticação baseada em chaves API
- **Interface web**: Interface intuitiva de busca e classificação de imagens estilo Pinterest
- **Ferramenta CLI**: Classificação de imagens via linha de comando e gerenciamento de chaves API
- **Análise em tempo real**: Classificação imediata e exibição de resultados de imagens enviadas

**Início rápido:**
```bash
# Clonar repositório
git clone <repository-url>
cd "ProRL V2 for catagorize images"

# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python run.py
```

---

**🌍 Choose your language and start exploring VisionAI Pro! / 언어를 선택하고 VisionAI Pro를 탐험해보세요!**

