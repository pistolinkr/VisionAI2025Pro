# 🚀 VisionAI Pro - Quick Start Guide

## 📋 Organized Project Structure

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
├── 📚 docs/                        # Documentation
└── 🔧 src/                         # Source Code
```

## 🎯 Server Execution Methods

### 1. Environment Setup
```bash
# Activate virtual environment
source venv/bin/activate

# Check dependencies
pip install -r config/requirements.txt
```

### 2. System Testing
```bash
# Test all servers
python3 scripts/testing/test_all_servers.py
```

### 3. Server Execution

#### Zero-shot Classification Server (Port 8002) - Recommended!
```bash
# Direct execution
python3 main.py zero-shot

# Or use script
./scripts/deployment/start_zero_shot.sh
```

#### Advanced Classification Server (Port 8001)
```bash
python3 main.py advanced
```

#### Firebase Server (Port 8003)
```bash
python3 main.py firebase
```

#### Main Server (Port 8000)
```bash
python3 main.py main
```

## 🌐 Web Interface Access

After starting the server, access the web interface at the following URLs:

- **Zero-shot Classification**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Advanced Classification**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Key Features

### Zero-shot Classification Server (Port 8002)
- ✅ **Real-time category addition/removal**
- ✅ **1000+ category support**
- ✅ **Fast Mode (60+ core categories)**
- ✅ **Minimal dark theme UI**
- ✅ **Drag and drop image upload**

### API Endpoints
- `POST /api/classify` - Image classification
- `GET /api/categories` - Category list
- `POST /api/categories/add` - Add category
- `DELETE /api/categories/remove` - Remove category
- `GET /api/categories/search` - Search categories
- `GET /health` - Server status check

## 🎨 UI Features

- **Dark Theme**: #121212 background, #f5f5f5 text
- **Minimal Design**: Removed unnecessary elements
- **Monospace Font**: Developer-friendly
- **Small Size**: Compact interface
- **Sharp Corners**: 3-4px rounded corners

## 🚨 Troubleshooting

### Common Issues
1. **Port conflict**: Use different port or stop running service
2. **Model load failure**: Check `query/base_words.txt` file
3. **Permission error**: Check file permissions and directory access rights

### Log Checking
```bash
# Check log file
tail -f logs/app.log
```

## 📞 Support

If problems occur, check the following:
1. Whether virtual environment is activated
2. Whether all dependencies are installed
3. Whether required files are in correct locations

---

**VisionAI Pro** - Organized and optimized image classification system 🚀

---

# 🚀 VisionAI Pro - 빠른 시작 가이드

## 📋 정리된 프로젝트 구조

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
├── 📚 docs/                        # 문서
└── 🔧 src/                         # 소스 코드
```

## 🎯 서버 실행 방법

### 1. 환경 설정
```bash
# 가상환경 활성화
source venv/bin/activate

# 의존성 확인
pip install -r config/requirements.txt
```

### 2. 시스템 테스트
```bash
# 모든 서버 테스트
python3 scripts/testing/test_all_servers.py
```

### 3. 서버 실행

#### Zero-shot 분류 서버 (포트 8002) - 추천!
```bash
# 직접 실행
python3 main.py zero-shot

# 또는 스크립트 사용
./scripts/deployment/start_zero_shot.sh
```

#### 고급 분류 서버 (포트 8001)
```bash
python3 main.py advanced
```

#### Firebase 서버 (포트 8003)
```bash
python3 main.py firebase
```

#### 메인 서버 (포트 8000)
```bash
python3 main.py main
```

## 🌐 웹 인터페이스 접근

서버 실행 후 다음 URL에서 웹 인터페이스에 접근:

- **Zero-shot 분류**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **고급 분류**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 주요 기능

### Zero-shot 분류 서버 (포트 8002)
- ✅ **실시간 카테고리 추가/제거**
- ✅ **1000+ 카테고리 지원**
- ✅ **Fast Mode (60+ 핵심 카테고리)**
- ✅ **미니멀 다크 테마 UI**
- ✅ **드래그 앤 드롭 이미지 업로드**

### API 엔드포인트
- `POST /api/classify` - 이미지 분류
- `GET /api/categories` - 카테고리 목록
- `POST /api/categories/add` - 카테고리 추가
- `DELETE /api/categories/remove` - 카테고리 제거
- `GET /api/categories/search` - 카테고리 검색
- `GET /health` - 서버 상태 확인

## 🎨 UI 특징

- **다크 테마**: #121212 배경, #f5f5f5 텍스트
- **미니멀 디자인**: 불필요한 요소 제거
- **모노스페이스 폰트**: 개발자 친화적
- **작은 크기**: 컴팩트한 인터페이스
- **날카로운 모서리**: 3-4px 둥근 모서리

## 🚨 문제 해결

### 일반적인 문제
1. **포트 충돌**: 다른 포트 사용하거나 실행 중인 서비스 종료
2. **모델 로드 실패**: `query/base_words.txt` 파일 확인
3. **권한 오류**: 파일 권한 및 디렉토리 접근 권한 확인

### 로그 확인
```bash
# 로그 파일 확인
tail -f logs/app.log
```

## 📞 지원

문제가 발생하면 다음을 확인하세요:
1. 가상환경이 활성화되어 있는지
2. 모든 의존성이 설치되어 있는지
3. 필요한 파일들이 올바른 위치에 있는지

---

**VisionAI Pro** - 정리되고 최적화된 이미지 분류 시스템 🚀

---

# 🚀 VisionAI Pro - Guía de Inicio Rápido

## 📋 Estructura del Proyecto Organizada

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Aplicaciones Web
│   ├── zero_shot/                  # Aplicación Web de Clasificación Zero-shot
│   ├── advanced/                  # Aplicación Web de Clasificación Avanzada
│   └── firebase/                  # Aplicación Web basada en Firebase
├── 🚀 scripts/                     # Scripts de Ejecución y Gestión
│   ├── deployment/                # Scripts de Ejecución del Servidor
│   ├── setup/                     # Scripts de Instalación y Configuración
│   └── testing/                   # Scripts de Pruebas
├── 📊 data/                        # Datos y Modelos
│   ├── models/                    # Archivos de Modelos Entrenados
│   ├── cache/                     # Archivos de Caché
│   └── uploads/                   # Imágenes Subidas
├── ⚙️ config/                      # Archivos de Configuración
├── 📚 docs/                        # Documentación
└── 🔧 src/                         # Código Fuente
```

## 🎯 Métodos de Ejecución del Servidor

### 1. Configuración del Entorno
```bash
# Activar entorno virtual
source venv/bin/activate

# Verificar dependencias
pip install -r config/requirements.txt
```

### 2. Pruebas del Sistema
```bash
# Probar todos los servidores
python3 scripts/testing/test_all_servers.py
```

### 3. Ejecución del Servidor

#### Servidor de Clasificación Zero-shot (Puerto 8002) - ¡Recomendado!
```bash
# Ejecución directa
python3 main.py zero-shot

# O usar script
./scripts/deployment/start_zero_shot.sh
```

#### Servidor de Clasificación Avanzada (Puerto 8001)
```bash
python3 main.py advanced
```

#### Servidor Firebase (Puerto 8003)
```bash
python3 main.py firebase
```

#### Servidor Principal (Puerto 8000)
```bash
python3 main.py main
```

## 🌐 Acceso a la Interfaz Web

Después de iniciar el servidor, accede a la interfaz web en las siguientes URLs:

- **Clasificación Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Clasificación Avanzada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Características Principales

### Servidor de Clasificación Zero-shot (Puerto 8002)
- ✅ **Adición/eliminación de categorías en tiempo real**
- ✅ **Soporte para 1000+ categorías**
- ✅ **Modo Rápido (60+ categorías principales)**
- ✅ **UI de tema oscuro minimalista**
- ✅ **Subida de imágenes por arrastrar y soltar**

### Endpoints de API
- `POST /api/classify` - Clasificación de imágenes
- `GET /api/categories` - Lista de categorías
- `POST /api/categories/add` - Agregar categoría
- `DELETE /api/categories/remove` - Eliminar categoría
- `GET /api/categories/search` - Buscar categorías
- `GET /health` - Verificar estado del servidor

## 🎨 Características de la UI

- **Tema Oscuro**: Fondo #121212, texto #f5f5f5
- **Diseño Minimalista**: Elementos innecesarios eliminados
- **Fuente Monospace**: Amigable para desarrolladores
- **Tamaño Pequeño**: Interfaz compacta
- **Esquinas Afiladas**: Bordes redondeados de 3-4px

## 🚨 Solución de Problemas

### Problemas Comunes
1. **Conflicto de puertos**: Usar puerto diferente o detener servicio en ejecución
2. **Fallo de carga del modelo**: Verificar archivo `query/base_words.txt`
3. **Error de permisos**: Verificar permisos de archivos y acceso a directorios

### Verificación de Logs
```bash
# Verificar archivo de log
tail -f logs/app.log
```

## 📞 Soporte

Si ocurren problemas, verifica lo siguiente:
1. Si el entorno virtual está activado
2. Si todas las dependencias están instaladas
3. Si los archivos necesarios están en las ubicaciones correctas

---

**VisionAI Pro** - Sistema de clasificación de imágenes organizado y optimizado 🚀

---

# 🚀 VisionAI Pro - Guide de Démarrage Rapide

## 📋 Structure du Projet Organisée

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Applications Web
│   ├── zero_shot/                  # Application Web de Classification Zero-shot
│   ├── advanced/                  # Application Web de Classification Avancée
│   └── firebase/                  # Application Web basée sur Firebase
├── 🚀 scripts/                     # Scripts d'Exécution et de Gestion
│   ├── deployment/                # Scripts d'Exécution du Serveur
│   ├── setup/                     # Scripts d'Installation et de Configuration
│   └── testing/                   # Scripts de Tests
├── 📊 data/                        # Données et Modèles
│   ├── models/                    # Fichiers de Modèles Entraînés
│   ├── cache/                     # Fichiers de Cache
│   └── uploads/                   # Images Téléchargées
├── ⚙️ config/                      # Fichiers de Configuration
├── 📚 docs/                        # Documentation
└── 🔧 src/                         # Code Source
```

## 🎯 Méthodes d'Exécution du Serveur

### 1. Configuration de l'Environnement
```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Vérifier les dépendances
pip install -r config/requirements.txt
```

### 2. Tests du Système
```bash
# Tester tous les serveurs
python3 scripts/testing/test_all_servers.py
```

### 3. Exécution du Serveur

#### Serveur de Classification Zero-shot (Port 8002) - Recommandé !
```bash
# Exécution directe
python3 main.py zero-shot

# Ou utiliser le script
./scripts/deployment/start_zero_shot.sh
```

#### Serveur de Classification Avancée (Port 8001)
```bash
python3 main.py advanced
```

#### Serveur Firebase (Port 8003)
```bash
python3 main.py firebase
```

#### Serveur Principal (Port 8000)
```bash
python3 main.py main
```

## 🌐 Accès à l'Interface Web

Après avoir démarré le serveur, accédez à l'interface web aux URLs suivantes :

- **Classification Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classification Avancée**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Caractéristiques Principales

### Serveur de Classification Zero-shot (Port 8002)
- ✅ **Ajout/suppression de catégories en temps réel**
- ✅ **Support pour 1000+ catégories**
- ✅ **Mode Rapide (60+ catégories principales)**
- ✅ **UI thème sombre minimaliste**
- ✅ **Téléchargement d'images par glisser-déposer**

### Points de Terminaison API
- `POST /api/classify` - Classification d'images
- `GET /api/categories` - Liste des catégories
- `POST /api/categories/add` - Ajouter une catégorie
- `DELETE /api/categories/remove` - Supprimer une catégorie
- `GET /api/categories/search` - Rechercher des catégories
- `GET /health` - Vérifier l'état du serveur

## 🎨 Caractéristiques de l'UI

- **Thème Sombre**: Arrière-plan #121212, texte #f5f5f5
- **Design Minimaliste**: Éléments inutiles supprimés
- **Police Monospace**: Convivial pour les développeurs
- **Taille Petite**: Interface compacte
- **Coins Tranchants**: Bordures arrondies de 3-4px

## 🚨 Dépannage

### Problèmes Courants
1. **Conflit de ports**: Utiliser un port différent ou arrêter le service en cours
2. **Échec de chargement du modèle**: Vérifier le fichier `query/base_words.txt`
3. **Erreur de permissions**: Vérifier les permissions des fichiers et l'accès aux répertoires

### Vérification des Logs
```bash
# Vérifier le fichier de log
tail -f logs/app.log
```

## 📞 Support

Si des problèmes surviennent, vérifiez ce qui suit :
1. Si l'environnement virtuel est activé
2. Si toutes les dépendances sont installées
3. Si les fichiers nécessaires sont aux bons emplacements

---

**VisionAI Pro** - Système de classification d'images organisé et optimisé 🚀

---

# 🚀 VisionAI Pro - Schnellstart-Anleitung

## 📋 Organisierte Projektstruktur

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Web-Anwendungen
│   ├── zero_shot/                  # Zero-shot Klassifizierungs-Web-App
│   ├── advanced/                  # Erweiterte Klassifizierungs-Web-App
│   └── firebase/                  # Firebase-basierte Web-App
├── 🚀 scripts/                     # Ausführungs- und Verwaltungsskripte
│   ├── deployment/                # Server-Ausführungsskripte
│   ├── setup/                     # Installations- und Konfigurationsskripte
│   └── testing/                   # Tests-Skripte
├── 📊 data/                        # Daten und Modelle
│   ├── models/                    # Trainierte Modell-Dateien
│   ├── cache/                     # Cache-Dateien
│   └── uploads/                   # Hochgeladene Bilder
├── ⚙️ config/                      # Konfigurationsdateien
├── 📚 docs/                        # Dokumentation
└── 🔧 src/                         # Quellcode
```

## 🎯 Server-Ausführungsmethoden

### 1. Umgebungseinrichtung
```bash
# Virtuelle Umgebung aktivieren
source venv/bin/activate

# Abhängigkeiten überprüfen
pip install -r config/requirements.txt
```

### 2. Systemtests
```bash
# Alle Server testen
python3 scripts/testing/test_all_servers.py
```

### 3. Server-Ausführung

#### Zero-shot Klassifizierungsserver (Port 8002) - Empfohlen!
```bash
# Direkte Ausführung
python3 main.py zero-shot

# Oder Skript verwenden
./scripts/deployment/start_zero_shot.sh
```

#### Erweiterter Klassifizierungsserver (Port 8001)
```bash
python3 main.py advanced
```

#### Firebase-Server (Port 8003)
```bash
python3 main.py firebase
```

#### Hauptserver (Port 8000)
```bash
python3 main.py main
```

## 🌐 Web-Interface-Zugriff

Nach dem Start des Servers können Sie über die folgenden URLs auf die Web-Oberfläche zugreifen:

- **Zero-shot Klassifizierung**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Erweiterte Klassifizierung**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Hauptfunktionen

### Zero-shot Klassifizierungsserver (Port 8002)
- ✅ **Echtzeit-Kategorie hinzufügen/entfernen**
- ✅ **1000+ Kategorie-Unterstützung**
- ✅ **Schnellmodus (60+ Hauptkategorien)**
- ✅ **Minimalistisches dunkles UI-Design**
- ✅ **Drag-and-Drop-Bild-Upload**

### API-Endpunkte
- `POST /api/classify` - Bildklassifizierung
- `GET /api/categories` - Kategorieliste
- `POST /api/categories/add` - Kategorie hinzufügen
- `DELETE /api/categories/remove` - Kategorie entfernen
- `GET /api/categories/search` - Kategorien suchen
- `GET /health` - Serverstatus überprüfen

## 🎨 UI-Merkmale

- **Dunkles Design**: Hintergrund #121212, Text #f5f5f5
- **Minimalistisches Design**: Unnötige Elemente entfernt
- **Monospace-Schrift**: Entwicklerfreundlich
- **Kleine Größe**: Kompakte Benutzeroberfläche
- **Scharfe Ecken**: 3-4px abgerundete Ecken

## 🚨 Fehlerbehebung

### Häufige Probleme
1. **Port-Konflikt**: Anderen Port verwenden oder laufenden Dienst beenden
2. **Modell-Ladefehler**: `query/base_words.txt` Datei überprüfen
3. **Berechtigungsfehler**: Dateiberechtigungen und Verzeichniszugriff überprüfen

### Log-Überprüfung
```bash
# Log-Datei überprüfen
tail -f logs/app.log
```

## 📞 Support

Bei Problemen überprüfen Sie Folgendes:
1. Ob die virtuelle Umgebung aktiviert ist
2. Ob alle Abhängigkeiten installiert sind
3. Ob erforderliche Dateien an den richtigen Stellen sind

---

**VisionAI Pro** - Organisiertes und optimiertes Bildklassifizierungssystem 🚀

---

# 🚀 VisionAI Pro - Guia de Início Rápido

## 📋 Estrutura do Projeto Organizada

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Aplicações Web
│   ├── zero_shot/                  # Aplicação Web de Classificação Zero-shot
│   ├── advanced/                  # Aplicação Web de Classificação Avançada
│   └── firebase/                  # Aplicação Web baseada em Firebase
├── 🚀 scripts/                     # Scripts de Execução e Gerenciamento
│   ├── deployment/                # Scripts de Execução do Servidor
│   ├── setup/                     # Scripts de Instalação e Configuração
│   └── testing/                   # Scripts de Testes
├── 📊 data/                        # Dados e Modelos
│   ├── models/                    # Arquivos de Modelos Treinados
│   ├── cache/                     # Arquivos de Cache
│   └── uploads/                   # Imagens Carregadas
├── ⚙️ config/                      # Arquivos de Configuração
├── 📚 docs/                        # Documentação
└── 🔧 src/                         # Código Fonte
```

## 🎯 Métodos de Execução do Servidor

### 1. Configuração do Ambiente
```bash
# Ativar ambiente virtual
source venv/bin/activate

# Verificar dependências
pip install -r config/requirements.txt
```

### 2. Testes do Sistema
```bash
# Testar todos os servidores
python3 scripts/testing/test_all_servers.py
```

### 3. Execução do Servidor

#### Servidor de Classificação Zero-shot (Porta 8002) - Recomendado!
```bash
# Execução direta
python3 main.py zero-shot

# Ou usar script
./scripts/deployment/start_zero_shot.sh
```

#### Servidor de Classificação Avançada (Porta 8001)
```bash
python3 main.py advanced
```

#### Servidor Firebase (Porta 8003)
```bash
python3 main.py firebase
```

#### Servidor Principal (Porta 8000)
```bash
python3 main.py main
```

## 🌐 Acesso à Interface Web

Após iniciar o servidor, acesse a interface web nas seguintes URLs:

- **Classificação Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classificação Avançada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Características Principais

### Servidor de Classificação Zero-shot (Porta 8002)
- ✅ **Adição/remoção de categorias em tempo real**
- ✅ **Suporte para 1000+ categorias**
- ✅ **Modo Rápido (60+ categorias principais)**
- ✅ **UI de tema escuro minimalista**
- ✅ **Upload de imagens por arrastar e soltar**

### Endpoints da API
- `POST /api/classify` - Classificação de imagens
- `GET /api/categories` - Lista de categorias
- `POST /api/categories/add` - Adicionar categoria
- `DELETE /api/categories/remove` - Remover categoria
- `GET /api/categories/search` - Buscar categorias
- `GET /health` - Verificar status do servidor

## 🎨 Características da UI

- **Tema Escuro**: Fundo #121212, texto #f5f5f5
- **Design Minimalista**: Elementos desnecessários removidos
- **Fonte Monospace**: Amigável para desenvolvedores
- **Tamanho Pequeno**: Interface compacta
- **Cantos Afiados**: Bordas arredondadas de 3-4px

## 🚨 Solução de Problemas

### Problemas Comuns
1. **Conflito de portas**: Usar porta diferente ou parar serviço em execução
2. **Falha no carregamento do modelo**: Verificar arquivo `query/base_words.txt`
3. **Erro de permissões**: Verificar permissões de arquivos e acesso a diretórios

### Verificação de Logs
```bash
# Verificar arquivo de log
tail -f logs/app.log
```

## 📞 Suporte

Se ocorrerem problemas, verifique o seguinte:
1. Se o ambiente virtual está ativado
2. Se todas as dependências estão instaladas
3. Se os arquivos necessários estão nos locais corretos

---

**VisionAI Pro** - Sistema de classificação de imagens organizado e otimizado 🚀

---

# 🚀 VisionAI Pro - دليل البدء السريع

## 📋 هيكل المشروع المنظم

```
VisionAI2025Pro/
├── 📱 web_apps/                    # تطبيقات الويب
│   ├── zero_shot/                  # تطبيق ويب تصنيف Zero-shot
│   ├── advanced/                  # تطبيق ويب التصنيف المتقدم
│   └── firebase/                  # تطبيق ويب مبني على Firebase
├── 🚀 scripts/                     # سكريبتات التنفيذ والإدارة
│   ├── deployment/                # سكريبتات تشغيل الخادم
│   ├── setup/                     # سكريبتات التثبيت والإعداد
│   └── testing/                   # سكريبتات الاختبار
├── 📊 data/                        # البيانات والنماذج
│   ├── models/                    # ملفات النماذج المدربة
│   ├── cache/                     # ملفات التخزين المؤقت
│   └── uploads/                   # الصور المرفوعة
├── ⚙️ config/                      # ملفات التكوين
├── 📚 docs/                        # الوثائق
└── 🔧 src/                         # الكود المصدري
```

## 🎯 طرق تشغيل الخادم

### 1. إعداد البيئة
```bash
# تفعيل البيئة الافتراضية
source venv/bin/activate

# التحقق من التبعيات
pip install -r config/requirements.txt
```

### 2. اختبار النظام
```bash
# اختبار جميع الخوادم
python3 scripts/testing/test_all_servers.py
```

### 3. تشغيل الخادم

#### خادم تصنيف Zero-shot (المنفذ 8002) - موصى به!
```bash
# التشغيل المباشر
python3 main.py zero-shot

# أو استخدام السكريبت
./scripts/deployment/start_zero_shot.sh
```

#### خادم التصنيف المتقدم (المنفذ 8001)
```bash
python3 main.py advanced
```

#### خادم Firebase (المنفذ 8003)
```bash
python3 main.py firebase
```

#### الخادم الرئيسي (المنفذ 8000)
```bash
python3 main.py main
```

## 🌐 الوصول إلى واجهة الويب

بعد تشغيل الخادم، يمكن الوصول إلى واجهة الويب عبر الروابط التالية:

- **تصنيف Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **التصنيف المتقدم**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 الميزات الرئيسية

### خادم تصنيف Zero-shot (المنفذ 8002)
- ✅ **إضافة/إزالة الفئات في الوقت الفعلي**
- ✅ **دعم 1000+ فئة**
- ✅ **الوضع السريع (60+ فئة رئيسية)**
- ✅ **واجهة مستخدم مظلمة بسيطة**
- ✅ **رفع الصور بالسحب والإفلات**

### نقاط نهاية API
- `POST /api/classify` - تصنيف الصور
- `GET /api/categories` - قائمة الفئات
- `POST /api/categories/add` - إضافة فئة
- `DELETE /api/categories/remove` - إزالة فئة
- `GET /api/categories/search` - البحث في الفئات
- `GET /health` - التحقق من حالة الخادم

## 🎨 ميزات واجهة المستخدم

- **المظهر المظلم**: خلفية #121212، نص #f5f5f5
- **التصميم البسيط**: العناصر غير الضرورية محذوفة
- **خط أحادي المسافة**: مناسب للمطورين
- **الحجم الصغير**: واجهة مدمجة
- **الزوايا الحادة**: زوايا مدورة 3-4px

## 🚨 استكشاف الأخطاء وإصلاحها

### المشاكل الشائعة
1. **تعارض المنافذ**: استخدام منفذ مختلف أو إيقاف الخدمة قيد التشغيل
2. **فشل تحميل النموذج**: التحقق من ملف `query/base_words.txt`
3. **خطأ في الأذونات**: التحقق من أذونات الملفات والوصول إلى المجلدات

### فحص السجلات
```bash
# فحص ملف السجل
tail -f logs/app.log
```

## 📞 الدعم

إذا حدثت مشاكل، تحقق من التالي:
1. ما إذا كانت البيئة الافتراضية مفعلة
2. ما إذا كانت جميع التبعيات مثبتة
3. ما إذا كانت الملفات المطلوبة في المواقع الصحيحة

---

**VisionAI Pro** - نظام تصنيف الصور المنظم والمحسن 🚀

---

# 🚀 VisionAI Pro - त्वरित प्रारंभ गाइड

## 📋 संगठित परियोजना संरचना

```
VisionAI2025Pro/
├── 📱 web_apps/                    # वेब अनुप्रयोग
│   ├── zero_shot/                  # Zero-shot वर्गीकरण वेब ऐप
│   ├── advanced/                  # उन्नत वर्गीकरण वेब ऐप
│   └── firebase/                  # Firebase-आधारित वेब ऐप
├── 🚀 scripts/                     # निष्पादन और प्रबंधन स्क्रिप्ट
│   ├── deployment/                # सर्वर निष्पादन स्क्रिप्ट
│   ├── setup/                     # स्थापना और कॉन्फ़िगरेशन स्क्रिप्ट
│   └── testing/                   # परीक्षण स्क्रिप्ट
├── 📊 data/                        # डेटा और मॉडल
│   ├── models/                    # प्रशिक्षित मॉडल फ़ाइलें
│   ├── cache/                     # कैश फ़ाइलें
│   └── uploads/                   # अपलोड की गई छवियां
├── ⚙️ config/                      # कॉन्फ़िगरेशन फ़ाइलें
├── 📚 docs/                        # दस्तावेज़ीकरण
└── 🔧 src/                         # स्रोत कोड
```

## 🎯 सर्वर निष्पादन विधियां

### 1. पर्यावरण सेटअप
```bash
# वर्चुअल पर्यावरण सक्रिय करें
source venv/bin/activate

# निर्भरताओं की जांच करें
pip install -r config/requirements.txt
```

### 2. सिस्टम परीक्षण
```bash
# सभी सर्वरों का परीक्षण करें
python3 scripts/testing/test_all_servers.py
```

### 3. सर्वर निष्पादन

#### Zero-shot वर्गीकरण सर्वर (पोर्ट 8002) - अनुशंसित!
```bash
# प्रत्यक्ष निष्पादन
python3 main.py zero-shot

# या स्क्रिप्ट का उपयोग करें
./scripts/deployment/start_zero_shot.sh
```

#### उन्नत वर्गीकरण सर्वर (पोर्ट 8001)
```bash
python3 main.py advanced
```

#### Firebase सर्वर (पोर्ट 8003)
```bash
python3 main.py firebase
```

#### मुख्य सर्वर (पोर्ट 8000)
```bash
python3 main.py main
```

## 🌐 वेब इंटरफेस पहुंच

सर्वर शुरू करने के बाद, निम्नलिखित URLs पर वेब इंटरफेस तक पहुंचें:

- **Zero-shot वर्गीकरण**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **उन्नत वर्गीकरण**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 मुख्य विशेषताएं

### Zero-shot वर्गीकरण सर्वर (पोर्ट 8002)
- ✅ **रियल-टाइम श्रेणी जोड़ना/हटाना**
- ✅ **1000+ श्रेणी समर्थन**
- ✅ **फास्ट मोड (60+ मुख्य श्रेणियां)**
- ✅ **न्यूनतम डार्क थीम UI**
- ✅ **ड्रैग और ड्रॉप छवि अपलोड**

### API एंडपॉइंट्स
- `POST /api/classify` - छवि वर्गीकरण
- `GET /api/categories` - श्रेणी सूची
- `POST /api/categories/add` - श्रेणी जोड़ें
- `DELETE /api/categories/remove` - श्रेणी हटाएं
- `GET /api/categories/search` - श्रेणियां खोजें
- `GET /health` - सर्वर स्थिति जांचें

## 🎨 UI विशेषताएं

- **डार्क थीम**: पृष्ठभूमि #121212, पाठ #f5f5f5
- **न्यूनतम डिज़ाइन**: अनावश्यक तत्व हटाए गए
- **मोनोस्पेस फ़ॉन्ट**: डेवलपर-अनुकूल
- **छोटा आकार**: कॉम्पैक्ट इंटरफेस
- **तीक्ष्ण कोने**: 3-4px गोल कोने

## 🚨 समस्या निवारण

### सामान्य समस्याएं
1. **पोर्ट संघर्ष**: अलग पोर्ट का उपयोग करें या चल रही सेवा को रोकें
2. **मॉडल लोड विफलता**: `query/base_words.txt` फ़ाइल जांचें
3. **अनुमति त्रुटि**: फ़ाइल अनुमतियों और निर्देशिका पहुंच अधिकारों की जांच करें

### लॉग जांच
```bash
# लॉग फ़ाइल जांचें
tail -f logs/app.log
```

## 📞 सहायता

यदि समस्याएं आती हैं, तो निम्नलिखित की जांच करें:
1. क्या वर्चुअल पर्यावरण सक्रिय है
2. क्या सभी निर्भरताएं स्थापित हैं
3. क्या आवश्यक फ़ाइलें सही स्थानों पर हैं

---

**VisionAI Pro** - संगठित और अनुकूलित छवि वर्गीकरण प्रणाली 🚀

---

# 🚀 VisionAI Pro - 快速入门指南

## 📋 整理的项目结构

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
├── 📚 docs/                        # 文档
└── 🔧 src/                         # 源代码
```

## 🎯 服务器执行方法

### 1. 环境设置
```bash
# 激活虚拟环境
source venv/bin/activate

# 检查依赖
pip install -r config/requirements.txt
```

### 2. 系统测试
```bash
# 测试所有服务器
python3 scripts/testing/test_all_servers.py
```

### 3. 服务器执行

#### 零样本分类服务器 (端口 8002) - 推荐！
```bash
# 直接执行
python3 main.py zero-shot

# 或使用脚本
./scripts/deployment/start_zero_shot.sh
```

#### 高级分类服务器 (端口 8001)
```bash
python3 main.py advanced
```

#### Firebase服务器 (端口 8003)
```bash
python3 main.py firebase
```

#### 主服务器 (端口 8000)
```bash
python3 main.py main
```

## 🌐 网络界面访问

启动服务器后，通过以下URL访问网络界面：

- **零样本分类**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **高级分类**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 主要功能

### 零样本分类服务器 (端口 8002)
- ✅ **实时类别添加/删除**
- ✅ **1000+类别支持**
- ✅ **快速模式 (60+核心类别)**
- ✅ **极简深色主题UI**
- ✅ **拖放图像上传**

### API端点
- `POST /api/classify` - 图像分类
- `GET /api/categories` - 类别列表
- `POST /api/categories/add` - 添加类别
- `DELETE /api/categories/remove` - 删除类别
- `GET /api/categories/search` - 搜索类别
- `GET /health` - 服务器状态检查

## 🎨 UI特点

- **深色主题**: #121212背景，#f5f5f5文本
- **极简设计**: 移除不必要元素
- **等宽字体**: 开发者友好
- **小尺寸**: 紧凑界面
- **锐角**: 3-4px圆角

## 🚨 故障排除

### 常见问题
1. **端口冲突**: 使用不同端口或停止运行的服务
2. **模型加载失败**: 检查`query/base_words.txt`文件
3. **权限错误**: 检查文件权限和目录访问权限

### 日志检查
```bash
# 检查日志文件
tail -f logs/app.log
```

## 📞 支持

如果出现问题，请检查以下内容：
1. 虚拟环境是否已激活
2. 是否已安装所有依赖
3. 必需文件是否在正确位置

---

**VisionAI Pro** - 整理和优化的图像分类系统 🚀

---

# 🚀 VisionAI Pro - クイックスタートガイド

## 📋 整理されたプロジェクト構造

```
VisionAI2025Pro/
├── 📱 web_apps/                    # ウェブアプリケーション
│   ├── zero_shot/                  # Zero-shot分類ウェブアプリ
│   ├── advanced/                  # 高度な分類ウェブアプリ
│   └── firebase/                  # Firebaseベースのウェブアプリ
├── 🚀 scripts/                     # 実行・管理スクリプト
│   ├── deployment/                # サーバー実行スクリプト
│   ├── setup/                     # インストール・設定スクリプト
│   └── testing/                   # テストスクリプト
├── 📊 data/                        # データ・モデル
│   ├── models/                    # 訓練済みモデルファイル
│   ├── cache/                     # キャッシュファイル
│   └── uploads/                   # アップロードされた画像
├── ⚙️ config/                      # 設定ファイル
├── 📚 docs/                        # ドキュメント
└── 🔧 src/                         # ソースコード
```

## 🎯 サーバー実行方法

### 1. 環境設定
```bash
# 仮想環境をアクティベート
source venv/bin/activate

# 依存関係を確認
pip install -r config/requirements.txt
```

### 2. システムテスト
```bash
# すべてのサーバーをテスト
python3 scripts/testing/test_all_servers.py
```

### 3. サーバー実行

#### Zero-shot分類サーバー (ポート 8002) - 推奨！
```bash
# 直接実行
python3 main.py zero-shot

# またはスクリプトを使用
./scripts/deployment/start_zero_shot.sh
```

#### 高度な分類サーバー (ポート 8001)
```bash
python3 main.py advanced
```

#### Firebaseサーバー (ポート 8003)
```bash
python3 main.py firebase
```

#### メインサーバー (ポート 8000)
```bash
python3 main.py main
```

## 🌐 ウェブインターフェースアクセス

サーバー開始後、以下のURLでウェブインターフェースにアクセス：

- **Zero-shot分類**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **高度な分類**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 主要機能

### Zero-shot分類サーバー (ポート 8002)
- ✅ **リアルタイムカテゴリ追加/削除**
- ✅ **1000+カテゴリサポート**
- ✅ **高速モード (60+メインカテゴリ)**
- ✅ **ミニマルダークテーマUI**
- ✅ **ドラッグ&ドロップ画像アップロード**

### APIエンドポイント
- `POST /api/classify` - 画像分類
- `GET /api/categories` - カテゴリリスト
- `POST /api/categories/add` - カテゴリ追加
- `DELETE /api/categories/remove` - カテゴリ削除
- `GET /api/categories/search` - カテゴリ検索
- `GET /health` - サーバー状態確認

## 🎨 UI特徴

- **ダークテーマ**: 背景 #121212、テキスト #f5f5f5
- **ミニマルデザイン**: 不要な要素を削除
- **等幅フォント**: 開発者フレンドリー
- **小さなサイズ**: コンパクトなインターフェース
- **鋭い角**: 3-4pxの角丸

## 🚨 トラブルシューティング

### 一般的な問題
1. **ポート競合**: 異なるポートを使用するか、実行中のサービスを停止
2. **モデル読み込み失敗**: `query/base_words.txt`ファイルを確認
3. **権限エラー**: ファイル権限とディレクトリアクセス権限を確認

### ログ確認
```bash
# ログファイルを確認
tail -f logs/app.log
```

## 📞 サポート

問題が発生した場合、以下を確認してください：
1. 仮想環境がアクティベートされているか
2. すべての依存関係がインストールされているか
3. 必要なファイルが正しい場所にあるか

---

**VisionAI Pro** - 整理・最適化された画像分類システム 🚀

---

# 🚀 VisionAI Pro - Руководство по быстрому запуску

## 📋 Организованная структура проекта

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Веб-приложения
│   ├── zero_shot/                  # Веб-приложение классификации Zero-shot
│   ├── advanced/                  # Веб-приложение расширенной классификации
│   └── firebase/                  # Веб-приложение на основе Firebase
├── 🚀 scripts/                     # Скрипты выполнения и управления
│   ├── deployment/                # Скрипты запуска сервера
│   ├── setup/                     # Скрипты установки и настройки
│   └── testing/                   # Скрипты тестирования
├── 📊 data/                        # Данные и модели
│   ├── models/                    # Файлы обученных моделей
│   ├── cache/                     # Файлы кэша
│   └── uploads/                   # Загруженные изображения
├── ⚙️ config/                      # Файлы конфигурации
├── 📚 docs/                        # Документация
└── 🔧 src/                         # Исходный код
```

## 🎯 Методы запуска сервера

### 1. Настройка окружения
```bash
# Активировать виртуальное окружение
source venv/bin/activate

# Проверить зависимости
pip install -r config/requirements.txt
```

### 2. Тестирование системы
```bash
# Тестировать все серверы
python3 scripts/testing/test_all_servers.py
```

### 3. Запуск сервера

#### Сервер классификации Zero-shot (Порт 8002) - Рекомендуется!
```bash
# Прямой запуск
python3 main.py zero-shot

# Или использовать скрипт
./scripts/deployment/start_zero_shot.sh
```

#### Сервер расширенной классификации (Порт 8001)
```bash
python3 main.py advanced
```

#### Сервер Firebase (Порт 8003)
```bash
python3 main.py firebase
```

#### Главный сервер (Порт 8000)
```bash
python3 main.py main
```

## 🌐 Доступ к веб-интерфейсу

После запуска сервера доступ к веб-интерфейсу по следующим URL:

- **Классификация Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Расширенная классификация**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Основные функции

### Сервер классификации Zero-shot (Порт 8002)
- ✅ **Добавление/удаление категорий в реальном времени**
- ✅ **Поддержка 1000+ категорий**
- ✅ **Быстрый режим (60+ основных категорий)**
- ✅ **Минималистичный темный UI**
- ✅ **Загрузка изображений перетаскиванием**

### API конечные точки
- `POST /api/classify` - Классификация изображений
- `GET /api/categories` - Список категорий
- `POST /api/categories/add` - Добавить категорию
- `DELETE /api/categories/remove` - Удалить категорию
- `GET /api/categories/search` - Поиск категорий
- `GET /health` - Проверка состояния сервера

## 🎨 Особенности UI

- **Темная тема**: Фон #121212, текст #f5f5f5
- **Минималистичный дизайн**: Удалены ненужные элементы
- **Моноширинный шрифт**: Удобен для разработчиков
- **Маленький размер**: Компактный интерфейс
- **Острые углы**: Скругленные углы 3-4px

## 🚨 Устранение неполадок

### Распространенные проблемы
1. **Конфликт портов**: Использовать другой порт или остановить запущенную службу
2. **Ошибка загрузки модели**: Проверить файл `query/base_words.txt`
3. **Ошибка разрешений**: Проверить разрешения файлов и доступ к каталогам

### Проверка логов
```bash
# Проверить файл лога
tail -f logs/app.log
```

## 📞 Поддержка

При возникновении проблем проверьте следующее:
1. Активировано ли виртуальное окружение
2. Установлены ли все зависимости
3. Находятся ли необходимые файлы в правильных местах

---

**VisionAI Pro** - Организованная и оптимизированная система классификации изображений 🚀

---

# 🚀 VisionAI Pro - Panduan Mulai Cepat

## 📋 Struktur Proyek yang Terorganisir

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Aplikasi Web
│   ├── zero_shot/                  # Aplikasi Web Klasifikasi Zero-shot
│   ├── advanced/                  # Aplikasi Web Klasifikasi Lanjutan
│   └── firebase/                  # Aplikasi Web berbasis Firebase
├── 🚀 scripts/                     # Skrip Eksekusi dan Manajemen
│   ├── deployment/                # Skrip Eksekusi Server
│   ├── setup/                     # Skrip Instalasi dan Konfigurasi
│   └── testing/                   # Skrip Pengujian
├── 📊 data/                        # Data dan Model
│   ├── models/                    # File Model Terlatih
│   ├── cache/                     # File Cache
│   └── uploads/                   # Gambar yang Diunggah
├── ⚙️ config/                      # File Konfigurasi
├── 📚 docs/                        # Dokumentasi
└── 🔧 src/                         # Kode Sumber
```

## 🎯 Metode Eksekusi Server

### 1. Pengaturan Lingkungan
```bash
# Aktifkan lingkungan virtual
source venv/bin/activate

# Periksa dependensi
pip install -r config/requirements.txt
```

### 2. Pengujian Sistem
```bash
# Uji semua server
python3 scripts/testing/test_all_servers.py
```

### 3. Eksekusi Server

#### Server Klasifikasi Zero-shot (Port 8002) - Direkomendasikan!
```bash
# Eksekusi langsung
python3 main.py zero-shot

# Atau gunakan skrip
./scripts/deployment/start_zero_shot.sh
```

#### Server Klasifikasi Lanjutan (Port 8001)
```bash
python3 main.py advanced
```

#### Server Firebase (Port 8003)
```bash
python3 main.py firebase
```

#### Server Utama (Port 8000)
```bash
python3 main.py main
```

## 🌐 Akses Antarmuka Web

Setelah memulai server, akses antarmuka web di URL berikut:

- **Klasifikasi Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Klasifikasi Lanjutan**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Fitur Utama

### Server Klasifikasi Zero-shot (Port 8002)
- ✅ **Penambahan/penghapusan kategori real-time**
- ✅ **Dukungan 1000+ kategori**
- ✅ **Mode Cepat (60+ kategori utama)**
- ✅ **UI tema gelap minimalis**
- ✅ **Upload gambar drag-and-drop**

### Endpoint API
- `POST /api/classify` - Klasifikasi gambar
- `GET /api/categories` - Daftar kategori
- `POST /api/categories/add` - Tambah kategori
- `DELETE /api/categories/remove` - Hapus kategori
- `GET /api/categories/search` - Cari kategori
- `GET /health` - Periksa status server

## 🎨 Fitur UI

- **Tema Gelap**: Latar belakang #121212, teks #f5f5f5
- **Desain Minimalis**: Elemen yang tidak perlu dihapus
- **Font Monospace**: Ramah pengembang
- **Ukuran Kecil**: Antarmuka kompak
- **Sudut Tajam**: Sudut melengkung 3-4px

## 🚨 Pemecahan Masalah

### Masalah Umum
1. **Konflik port**: Gunakan port berbeda atau hentikan layanan yang berjalan
2. **Gagal memuat model**: Periksa file `query/base_words.txt`
3. **Kesalahan izin**: Periksa izin file dan akses direktori

### Pemeriksaan Log
```bash
# Periksa file log
tail -f logs/app.log
```

## 📞 Dukungan

Jika masalah terjadi, periksa hal berikut:
1. Apakah lingkungan virtual diaktifkan
2. Apakah semua dependensi terinstall
3. Apakah file yang diperlukan berada di lokasi yang benar

---

**VisionAI Pro** - Sistem klasifikasi gambar yang terorganisir dan dioptimalkan 🚀

---

# 🚀 VisionAI Pro - Hướng Dẫn Khởi Động Nhanh

## 📋 Cấu Trúc Dự Án Được Tổ Chức

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Ứng Dụng Web
│   ├── zero_shot/                  # Ứng Dụng Web Phân Loại Zero-shot
│   ├── advanced/                  # Ứng Dụng Web Phân Loại Nâng Cao
│   └── firebase/                  # Ứng Dụng Web Dựa Trên Firebase
├── 🚀 scripts/                     # Script Thực Thi và Quản Lý
│   ├── deployment/                # Script Thực Thi Server
│   ├── setup/                     # Script Cài Đặt và Cấu Hình
│   └── testing/                   # Script Kiểm Tra
├── 📊 data/                        # Dữ Liệu và Mô Hình
│   ├── models/                    # File Mô Hình Đã Huấn Luyện
│   ├── cache/                     # File Cache
│   └── uploads/                   # Hình Ảnh Đã Tải Lên
├── ⚙️ config/                      # File Cấu Hình
├── 📚 docs/                        # Tài Liệu
└── 🔧 src/                         # Mã Nguồn
```

## 🎯 Phương Pháp Thực Thi Server

### 1. Thiết Lập Môi Trường
```bash
# Kích hoạt môi trường ảo
source venv/bin/activate

# Kiểm tra các phụ thuộc
pip install -r config/requirements.txt
```

### 2. Kiểm Tra Hệ Thống
```bash
# Kiểm tra tất cả server
python3 scripts/testing/test_all_servers.py
```

### 3. Thực Thi Server

#### Server Phân Loại Zero-shot (Cổng 8002) - Được Khuyến Nghị!
```bash
# Thực thi trực tiếp
python3 main.py zero-shot

# Hoặc sử dụng script
./scripts/deployment/start_zero_shot.sh
```

#### Server Phân Loại Nâng Cao (Cổng 8001)
```bash
python3 main.py advanced
```

#### Server Firebase (Cổng 8003)
```bash
python3 main.py firebase
```

#### Server Chính (Cổng 8000)
```bash
python3 main.py main
```

## 🌐 Truy Cập Giao Diện Web

Sau khi khởi động server, truy cập giao diện web tại các URL sau:

- **Phân Loại Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Phân Loại Nâng Cao**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Tính Năng Chính

### Server Phân Loại Zero-shot (Cổng 8002)
- ✅ **Thêm/xóa danh mục thời gian thực**
- ✅ **Hỗ trợ 1000+ danh mục**
- ✅ **Chế Độ Nhanh (60+ danh mục chính)**
- ✅ **UI chủ đề tối tối giản**
- ✅ **Tải lên hình ảnh kéo và thả**

### Điểm Cuối API
- `POST /api/classify` - Phân loại hình ảnh
- `GET /api/categories` - Danh sách danh mục
- `POST /api/categories/add` - Thêm danh mục
- `DELETE /api/categories/remove` - Xóa danh mục
- `GET /api/categories/search` - Tìm kiếm danh mục
- `GET /health` - Kiểm tra trạng thái server

## 🎨 Tính Năng UI

- **Chủ Đề Tối**: Nền #121212, văn bản #f5f5f5
- **Thiết Kế Tối Giản**: Các yếu tố không cần thiết được loại bỏ
- **Phông Chữ Monospace**: Thân thiện với nhà phát triển
- **Kích Thước Nhỏ**: Giao diện nhỏ gọn
- **Góc Sắc Nét**: Góc bo tròn 3-4px

## 🚨 Khắc Phục Sự Cố

### Vấn Đề Thường Gặp
1. **Xung đột cổng**: Sử dụng cổng khác hoặc dừng dịch vụ đang chạy
2. **Lỗi tải mô hình**: Kiểm tra tệp `query/base_words.txt`
3. **Lỗi quyền**: Kiểm tra quyền tệp và quyền truy cập thư mục

### Kiểm Tra Nhật Ký
```bash
# Kiểm tra tệp nhật ký
tail -f logs/app.log
```

## 📞 Hỗ Trợ

Nếu xảy ra vấn đề, hãy kiểm tra những điều sau:
1. Môi trường ảo có được kích hoạt không
2. Tất cả các phụ thuộc có được cài đặt không
3. Các tệp cần thiết có ở đúng vị trí không

---

**VisionAI Pro** - Hệ thống phân loại hình ảnh được tổ chức và tối ưu hóa 🚀

---

# 🚀 VisionAI Pro - Hızlı Başlangıç Kılavuzu

## 📋 Düzenlenmiş Proje Yapısı

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Web Uygulamaları
│   ├── zero_shot/                  # Zero-shot Sınıflandırma Web Uygulaması
│   ├── advanced/                  # Gelişmiş Sınıflandırma Web Uygulaması
│   └── firebase/                  # Firebase Tabanlı Web Uygulaması
├── 🚀 scripts/                     # Yürütme ve Yönetim Komut Dosyaları
│   ├── deployment/                # Sunucu Yürütme Komut Dosyaları
│   ├── setup/                     # Kurulum ve Yapılandırma Komut Dosyaları
│   └── testing/                   # Test Komut Dosyaları
├── 📊 data/                        # Veri ve Modeller
│   ├── models/                    # Eğitilmiş Model Dosyaları
│   ├── cache/                     # Önbellek Dosyaları
│   └── uploads/                   # Yüklenen Görüntüler
├── ⚙️ config/                      # Yapılandırma Dosyaları
├── 📚 docs/                        # Dokümantasyon
└── 🔧 src/                         # Kaynak Kod
```

## 🎯 Sunucu Yürütme Yöntemleri

### 1. Ortam Kurulumu
```bash
# Sanal ortamı etkinleştir
source venv/bin/activate

# Bağımlılıkları kontrol et
pip install -r config/requirements.txt
```

### 2. Sistem Testleri
```bash
# Tüm sunucuları test et
python3 scripts/testing/test_all_servers.py
```

### 3. Sunucu Yürütme

#### Zero-shot Sınıflandırma Sunucusu (Port 8002) - Önerilen!
```bash
# Doğrudan yürütme
python3 main.py zero-shot

# Veya komut dosyası kullan
./scripts/deployment/start_zero_shot.sh
```

#### Gelişmiş Sınıflandırma Sunucusu (Port 8001)
```bash
python3 main.py advanced
```

#### Firebase Sunucusu (Port 8003)
```bash
python3 main.py firebase
```

#### Ana Sunucu (Port 8000)
```bash
python3 main.py main
```

## 🌐 Web Arayüzü Erişimi

Sunucuyu başlattıktan sonra, aşağıdaki URL'lerde web arayüzüne erişin:

- **Zero-shot Sınıflandırma**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Gelişmiş Sınıflandırma**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Ana Özellikler

### Zero-shot Sınıflandırma Sunucusu (Port 8002)
- ✅ **Gerçek zamanlı kategori ekleme/kaldırma**
- ✅ **1000+ kategori desteği**
- ✅ **Hızlı Mod (60+ ana kategori)**
- ✅ **Minimalist karanlık tema UI**
- ✅ **Sürükle ve bırak görüntü yükleme**

### API Uç Noktaları
- `POST /api/classify` - Görüntü sınıflandırma
- `GET /api/categories` - Kategori listesi
- `POST /api/categories/add` - Kategori ekle
- `DELETE /api/categories/remove` - Kategori kaldır
- `GET /api/categories/search` - Kategori ara
- `GET /health` - Sunucu durumunu kontrol et

## 🎨 UI Özellikleri

- **Karanlık Tema**: Arka plan #121212, metin #f5f5f5
- **Minimalist Tasarım**: Gereksiz öğeler kaldırıldı
- **Monospace Yazı Tipi**: Geliştirici dostu
- **Küçük Boyut**: Kompakt arayüz
- **Keskin Köşeler**: 3-4px yuvarlatılmış köşeler

## 🚨 Sorun Giderme

### Yaygın Sorunlar
1. **Port çakışması**: Farklı port kullan veya çalışan hizmeti durdur
2. **Model yükleme hatası**: `query/base_words.txt` dosyasını kontrol et
3. **İzin hatası**: Dosya izinlerini ve dizin erişim haklarını kontrol et

### Log Kontrolü
```bash
# Log dosyasını kontrol et
tail -f logs/app.log
```

## 📞 Destek

Sorunlar oluşursa, aşağıdakileri kontrol edin:
1. Sanal ortamın etkinleştirilip etkinleştirilmediği
2. Tüm bağımlılıkların yüklenip yüklenmediği
3. Gerekli dosyaların doğru konumlarda olup olmadığı

---

**VisionAI Pro** - Düzenlenmiş ve optimize edilmiş görüntü sınıflandırma sistemi 🚀

---

# 🚀 VisionAI Pro - Guida di Avvio Rapido

## 📋 Struttura del Progetto Organizzata

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Applicazioni Web
│   ├── zero_shot/                  # Applicazione Web di Classificazione Zero-shot
│   ├── advanced/                  # Applicazione Web di Classificazione Avanzata
│   └── firebase/                  # Applicazione Web basata su Firebase
├── 🚀 scripts/                     # Script di Esecuzione e Gestione
│   ├── deployment/                # Script di Esecuzione del Server
│   ├── setup/                     # Script di Installazione e Configurazione
│   └── testing/                   # Script di Test
├── 📊 data/                        # Dati e Modelli
│   ├── models/                    # File di Modelli Addestrati
│   ├── cache/                     # File di Cache
│   └── uploads/                   # Immagini Caricate
├── ⚙️ config/                      # File di Configurazione
├── 📚 docs/                        # Documentazione
└── 🔧 src/                         # Codice Sorgente
```

## 🎯 Metodi di Esecuzione del Server

### 1. Configurazione dell'Ambiente
```bash
# Attiva l'ambiente virtuale
source venv/bin/activate

# Verifica le dipendenze
pip install -r config/requirements.txt
```

### 2. Test del Sistema
```bash
# Testa tutti i server
python3 scripts/testing/test_all_servers.py
```

### 3. Esecuzione del Server

#### Server di Classificazione Zero-shot (Porta 8002) - Raccomandato!
```bash
# Esecuzione diretta
python3 main.py zero-shot

# O usa lo script
./scripts/deployment/start_zero_shot.sh
```

#### Server di Classificazione Avanzata (Porta 8001)
```bash
python3 main.py advanced
```

#### Server Firebase (Porta 8003)
```bash
python3 main.py firebase
```

#### Server Principale (Porta 8000)
```bash
python3 main.py main
```

## 🌐 Accesso all'Interfaccia Web

Dopo aver avviato il server, accedi all'interfaccia web ai seguenti URL:

- **Classificazione Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Classificazione Avanzata**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Caratteristiche Principali

### Server di Classificazione Zero-shot (Porta 8002)
- ✅ **Aggiunta/rimozione categorie in tempo reale**
- ✅ **Supporto per 1000+ categorie**
- ✅ **Modalità Veloce (60+ categorie principali)**
- ✅ **UI tema scuro minimalista**
- ✅ **Caricamento immagini drag-and-drop**

### Endpoint API
- `POST /api/classify` - Classificazione immagini
- `GET /api/categories` - Lista categorie
- `POST /api/categories/add` - Aggiungi categoria
- `DELETE /api/categories/remove` - Rimuovi categoria
- `GET /api/categories/search` - Cerca categorie
- `GET /health` - Controlla stato server

## 🎨 Caratteristiche UI

- **Tema Scuro**: Sfondo #121212, testo #f5f5f5
- **Design Minimalista**: Elementi non necessari rimossi
- **Font Monospace**: Amichevole per sviluppatori
- **Dimensione Piccola**: Interfaccia compatta
- **Angoli Affilati**: Angoli arrotondati 3-4px

## 🚨 Risoluzione Problemi

### Problemi Comuni
1. **Conflitto di porte**: Usa una porta diversa o ferma il servizio in esecuzione
2. **Errore caricamento modello**: Controlla il file `query/base_words.txt`
3. **Errore permessi**: Controlla i permessi dei file e l'accesso alle directory

### Controllo Log
```bash
# Controlla il file di log
tail -f logs/app.log
```

## 📞 Supporto

Se si verificano problemi, controlla quanto segue:
1. Se l'ambiente virtuale è attivato
2. Se tutte le dipendenze sono installate
3. Se i file necessari sono nelle posizioni corrette

---

**VisionAI Pro** - Sistema di classificazione immagini organizzato e ottimizzato 🚀

---

# 🚀 VisionAI Pro - Guía de Inicio Rápido (Latino México)

## 📋 Estructura del Proyecto Organizada

```
VisionAI2025Pro/
├── 📱 web_apps/                    # Aplicaciones Web
│   ├── zero_shot/                  # Aplicación Web de Clasificación Zero-shot
│   ├── advanced/                  # Aplicación Web de Clasificación Avanzada
│   └── firebase/                  # Aplicación Web basada en Firebase
├── 🚀 scripts/                     # Scripts de Ejecución y Gestión
│   ├── deployment/                # Scripts de Ejecución del Servidor
│   ├── setup/                     # Scripts de Instalación y Configuración
│   └── testing/                   # Scripts de Pruebas
├── 📊 data/                        # Datos y Modelos
│   ├── models/                    # Archivos de Modelos Entrenados
│   ├── cache/                     # Archivos de Caché
│   └── uploads/                   # Imágenes Subidas
├── ⚙️ config/                      # Archivos de Configuración
├── 📚 docs/                        # Documentación
└── 🔧 src/                         # Código Fuente
```

## 🎯 Métodos de Ejecución del Servidor

### 1. Configuración del Entorno
```bash
# Activar entorno virtual
source venv/bin/activate

# Verificar dependencias
pip install -r config/requirements.txt
```

### 2. Pruebas del Sistema
```bash
# Probar todos los servidores
python3 scripts/testing/test_all_servers.py
```

### 3. Ejecución del Servidor

#### Servidor de Clasificación Zero-shot (Puerto 8002) - ¡Recomendado!
```bash
# Ejecución directa
python3 main.py zero-shot

# O usar script
./scripts/deployment/start_zero_shot.sh
```

#### Servidor de Clasificación Avanzada (Puerto 8001)
```bash
python3 main.py advanced
```

#### Servidor Firebase (Puerto 8003)
```bash
python3 main.py firebase
```

#### Servidor Principal (Puerto 8000)
```bash
python3 main.py main
```

## 🌐 Acceso a la Interfaz Web

Después de iniciar el servidor, accede a la interfaz web en las siguientes URLs:

- **Clasificación Zero-shot**: http://localhost:8002/web_apps/zero_shot/zero_shot_web_app.html
- **Clasificación Avanzada**: http://localhost:8001/web_apps/advanced/advanced_web_app.html
- **Firebase**: http://localhost:8003/web_apps/firebase/

## 🔧 Características Principales

### Servidor de Clasificación Zero-shot (Puerto 8002)
- ✅ **Adición/eliminación de categorías en tiempo real**
- ✅ **Soporte para 1000+ categorías**
- ✅ **Modo Rápido (60+ categorías principales)**
- ✅ **UI de tema oscuro minimalista**
- ✅ **Subida de imágenes por arrastrar y soltar**

### Endpoints de API
- `POST /api/classify` - Clasificación de imágenes
- `GET /api/categories` - Lista de categorías
- `POST /api/categories/add` - Agregar categoría
- `DELETE /api/categories/remove` - Eliminar categoría
- `GET /api/categories/search` - Buscar categorías
- `GET /health` - Verificar estado del servidor

## 🎨 Características de la UI

- **Tema Oscuro**: Fondo #121212, texto #f5f5f5
- **Diseño Minimalista**: Elementos innecesarios eliminados
- **Fuente Monospace**: Amigable para desarrolladores
- **Tamaño Pequeño**: Interfaz compacta
- **Esquinas Afiladas**: Bordes redondeados de 3-4px

## 🚨 Solución de Problemas

### Problemas Comunes
1. **Conflicto de puertos**: Usar puerto diferente o detener servicio en ejecución
2. **Fallo de carga del modelo**: Verificar archivo `query/base_words.txt`
3. **Error de permisos**: Verificar permisos de archivos y acceso a directorios

### Verificación de Logs
```bash
# Verificar archivo de log
tail -f logs/app.log
```

## 📞 Soporte

Si ocurren problemas, verifica lo siguiente:
1. Si el entorno virtual está activado
2. Si todas las dependencias están instaladas
3. Si los archivos necesarios están en las ubicaciones correctas

---

**VisionAI Pro** - Sistema de clasificación de imágenes organizado y optimizado 🚀