# 🌟 VisionAI Pro Zero-Shot API - 외부 사용 가이드

## 🎯 개요

VisionAI Pro Zero-Shot API는 **11,710개 카테고리**를 지원하는 고성능 이미지 분류 API입니다. Pinterest, Cosmos.so 등 외부 플랫폼에서 쉽게 사용할 수 있습니다.

## 🚀 주요 특징

- **Zero-shot Learning**: 훈련하지 않은 카테고리로도 분류 가능
- **11,710개 카테고리**: base_words.txt 기반 대규모 카테고리 지원
- **실시간 학습**: 새로운 카테고리 즉시 추가 가능
- **고정밀 분류**: CLIP 모델 기반 사람 눈 수준의 정확도
- **CORS 지원**: 모든 도메인에서 접근 가능

## 📋 API 엔드포인트

### 🔑 인증
- `POST /api/keys/generate` - API 키 생성
- `GET /api/keys/validate` - API 키 유효성 검증

### 🖼️ 이미지 분류
- `POST /api/classify` - 이미지 분류 (메인 기능)

### 📂 카테고리 관리
- `GET /api/categories` - 카테고리 목록 조회
- `GET /api/categories/search` - 카테고리 검색
- `POST /api/categories/add` - 카테고리 추가
- `DELETE /api/categories/remove` - 카테고리 제거

### 📊 시스템 정보
- `GET /health` - 서버 상태 확인
- `GET /api/stats` - 시스템 통계
- `GET /api/models` - 사용 가능한 모델

## 🔧 빠른 시작

### 1. API 키 생성

```javascript
const formData = new FormData();
formData.append('client_name', 'MyApp');
formData.append('email', 'user@example.com');
formData.append('description', '외부 웹앱');

const response = await fetch('http://your-server:8002/api/keys/generate', {
    method: 'POST',
    body: formData
});

const result = await response.json();
const apiKey = result.api_key;
```

### 2. 이미지 분류

```javascript
const formData = new FormData();
formData.append('image', imageFile);
formData.append('api_key', apiKey);
formData.append('top_k', '5');

const response = await fetch('http://your-server:8002/api/classify', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log(result.predictions);
```

## 📦 JavaScript 라이브러리 사용

### 설치

```bash
npm install visionai-pro-api
```

또는 CDN 사용:

```html
<script src="https://unpkg.com/visionai-pro-api@latest/dist/visionai-pro-api.js"></script>
```

### 사용 예제

```javascript
import VisionAIProAPI from 'visionai-pro-api';

// API 인스턴스 생성
const api = new VisionAIProAPI('http://your-server:8002');

// API 키 생성
await api.generateAPIKey('MyApp', 'user@example.com');

// 이미지 분류
const result = await api.classifyImage(imageFile, 5);
console.log(result.predictions);

// 카테고리 검색
const categories = await api.searchCategories('animal', 10);
console.log(categories);
```

## 🎨 React/Vue.js 컴포넌트 예제

### React 컴포넌트

```jsx
import React, { useState, useEffect } from 'react';
import VisionAIProAPI from 'visionai-pro-api';

function ImageClassifier() {
    const [api, setApi] = useState(null);
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const initAPI = async () => {
            const apiInstance = new VisionAIProAPI('http://your-server:8002');
            await apiInstance.generateAPIKey('ReactApp');
            setApi(apiInstance);
        };
        initAPI();
    }, []);

    const handleImageUpload = async (event) => {
        const file = event.target.files[0];
        if (file && api) {
            setLoading(true);
            try {
                const result = await api.classifyImage(file, 5);
                setResults(result);
            } catch (error) {
                console.error('분류 실패:', error);
            } finally {
                setLoading(false);
            }
        }
    };

    return (
        <div>
            <input type="file" onChange={handleImageUpload} accept="image/*" />
            {loading && <p>분류 중...</p>}
            {results && (
                <div>
                    <h3>분류 결과:</h3>
                    {results.predictions.map((pred, index) => (
                        <div key={index}>
                            {pred.category}: {pred.confidence.toFixed(2)}%
                        </div>
                    ))}
                </div>
            )}
        </div>
    );
}

export default ImageClassifier;
```

### Vue.js 컴포넌트

```vue
<template>
    <div>
        <input type="file" @change="handleImageUpload" accept="image/*" />
        <div v-if="loading">분류 중...</div>
        <div v-if="results">
            <h3>분류 결과:</h3>
            <div v-for="(pred, index) in results.predictions" :key="index">
                {{ pred.category }}: {{ pred.confidence.toFixed(2) }}%
            </div>
        </div>
    </div>
</template>

<script>
import VisionAIProAPI from 'visionai-pro-api';

export default {
    data() {
        return {
            api: null,
            results: null,
            loading: false
        };
    },
    async mounted() {
        this.api = new VisionAIProAPI('http://your-server:8002');
        await this.api.generateAPIKey('VueApp');
    },
    methods: {
        async handleImageUpload(event) {
            const file = event.target.files[0];
            if (file && this.api) {
                this.loading = true;
                try {
                    this.results = await this.api.classifyImage(file, 5);
                } catch (error) {
                    console.error('분류 실패:', error);
                } finally {
                    this.loading = false;
                }
            }
        }
    }
};
</script>
```

## 🔌 Node.js 서버 예제

```javascript
const express = require('express');
const multer = require('multer');
const fetch = require('node-fetch');
const FormData = require('form-data');

const app = express();
const upload = multer();

app.post('/classify', upload.single('image'), async (req, res) => {
    try {
        const formData = new FormData();
        formData.append('image', req.file.buffer, {
            filename: req.file.originalname,
            contentType: req.file.mimetype
        });
        formData.append('api_key', 'your-api-key');

        const response = await fetch('http://your-server:8002/api/classify', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        res.json(result);
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.listen(3000, () => {
    console.log('서버가 포트 3000에서 실행 중입니다.');
});
```

## 🌐 CORS 설정

API는 모든 도메인에서 접근 가능하도록 CORS가 설정되어 있습니다:

```javascript
// 지원되는 도메인
- "*" (모든 도메인)
- "http://localhost:3000"
- "http://localhost:8080"
- "http://localhost:5173"
- "https://pinterest.com"
- "https://cosmos.so"
- "https://*.vercel.app"
- "https://*.netlify.app"
- "https://*.github.io"
```

## 📊 응답 형식

### 이미지 분류 응답

```json
{
    "success": true,
    "predictions": [
        {
            "category": "person",
            "confidence": 0.95,
            "rank": 1
        },
        {
            "category": "human",
            "confidence": 0.92,
            "rank": 2
        }
    ],
    "processing_time": 1.23,
    "model_info": {
        "model_type": "zero_shot_clip",
        "categories_count": 11710
    }
}
```

### 카테고리 검색 응답

```json
{
    "success": true,
    "categories": ["animal", "dog", "cat", "bird"],
    "count": 4,
    "total_count": 11710,
    "search_query": "animal"
}
```

## ⚙️ 설정 옵션

### 서버 설정

```python
# run_zero_shot.py
host = "0.0.0.0"  # 외부 접근 허용
port = 8002       # 포트 번호
```

### 환경 변수

```bash
BASE_WORDS_PATH=query/base_words.txt  # 카테고리 파일 경로
```

## 🔒 보안

- 모든 요청에 API 키 필요
- API 키는 `/api/keys/generate` 엔드포인트로 생성
- 요청 제한: 1000 requests/hour
- 최대 이미지 크기: 10MB

## 📞 지원

- API 문서: `http://your-server:8002/docs`
- Swagger UI: `http://your-server:8002/docs`
- ReDoc: `http://your-server:8002/redoc`

## 🚀 배포

### 로컬 실행

```bash
python3 run_zero_shot.py
```

### Docker 실행

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8002
CMD ["python3", "run_zero_shot.py"]
```

```bash
docker build -t visionai-pro-api .
docker run -p 8002:8002 visionai-pro-api
```

### 클라우드 배포

- **AWS**: EC2 + Load Balancer
- **Google Cloud**: Compute Engine + Cloud Load Balancing
- **Azure**: Virtual Machine + Application Gateway
- **Vercel**: Serverless Functions
- **Netlify**: Serverless Functions

## 📈 성능

- **처리 시간**: 1-3초
- **정확도**: Zero-shot 성능 우수
- **동시 요청**: 100+ requests/second
- **메모리 사용량**: ~2GB RAM
- **CPU 사용량**: 중간 (CLIP 모델)

## 🎯 사용 사례

1. **Pinterest 스타일 앱**: 이미지 태깅 및 분류
2. **Cosmos.so 스타일 앱**: 문서 이미지 분석
3. **이커머스**: 상품 이미지 자동 분류
4. **소셜 미디어**: 콘텐츠 자동 태깅
5. **연구**: 이미지 데이터셋 분석

## 📝 라이선스

MIT License - 자유롭게 사용 가능
