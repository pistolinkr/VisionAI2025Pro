# 🌟 VisionAI Pro Zero-Shot API - External Usage Guide

## 🎯 Overview

VisionAI Pro Zero-Shot API is a high-performance image classification API supporting **11,710 categories**. It can be easily used on external platforms like Pinterest, Cosmos.so, etc.

## 🚀 Key Features

- **Zero-shot Learning**: Classify untrained categories
- **11,710 Categories**: Large-scale category support based on base_words.txt
- **Real-time Learning**: Instantly add new categories
- **High Precision Classification**: Human-eye level accuracy based on CLIP model
- **CORS Support**: Accessible from all domains

## 📋 API Endpoints

### 🔑 Authentication
- `POST /api/keys/generate` - Generate API key
- `GET /api/keys/validate` - Validate API key

### 🖼️ Image Classification
- `POST /api/classify` - Image classification (main feature)

### 📂 Category Management
- `GET /api/categories` - Get category list
- `GET /api/categories/search` - Search categories
- `POST /api/categories/add` - Add category
- `DELETE /api/categories/remove` - Remove category

### 📊 System Information
- `GET /health` - Server status check
- `GET /api/stats` - System statistics
- `GET /api/models` - Available models

## 🔧 Quick Start

### 1. Generate API Key

```javascript
const formData = new FormData();
formData.append('client_name', 'MyApp');
formData.append('email', 'user@example.com');
formData.append('description', 'External web app');

const response = await fetch('http://your-server:8002/api/keys/generate', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log('API Key:', result.api_key);
```

### 2. Image Classification

```javascript
const formData = new FormData();
formData.append('file', imageFile);
formData.append('api_key', 'your-api-key');
formData.append('top_k', '5');

const response = await fetch('http://your-server:8002/api/classify', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log('Classification Results:', result.predictions);
```

### 3. Category Management

```javascript
// Get all categories
const categories = await fetch('http://your-server:8002/api/categories?api_key=your-api-key');

// Search categories
const searchResults = await fetch('http://your-server:8002/api/categories/search?query=food&api_key=your-api-key');

// Add new category
const formData = new FormData();
formData.append('category', 'new_category');
formData.append('api_key', 'your-api-key');
await fetch('http://your-server:8002/api/categories/add', {
    method: 'POST',
    body: formData
});
```

## 🌐 Integration Examples

### React Component
```jsx
import React, { useState } from 'react';

const ImageClassifier = () => {
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const classifyImage = async (file) => {
        setLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', 'your-api-key');
        formData.append('top_k', '5');

        try {
            const response = await fetch('http://your-server:8002/api/classify', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            setResults(result.predictions);
        } catch (error) {
            console.error('Classification error:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <input type="file" onChange={(e) => classifyImage(e.target.files[0])} />
            {loading && <p>Classifying...</p>}
            {results && (
                <ul>
                    {results.map((pred, index) => (
                        <li key={index}>
                            {pred.category}: {(pred.confidence * 100).toFixed(1)}%
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};
```

### Vue.js Component
```vue
<template>
  <div>
    <input type="file" @change="handleFileUpload" />
    <div v-if="loading">Classifying...</div>
    <div v-if="results">
      <div v-for="(pred, index) in results" :key="index">
        {{ pred.category }}: {{ (pred.confidence * 100).toFixed(1) }}%
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      results: null,
      loading: false
    };
  },
  methods: {
    async handleFileUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      this.loading = true;
      const formData = new FormData();
      formData.append('file', file);
      formData.append('api_key', 'your-api-key');
      formData.append('top_k', '5');

      try {
        const response = await fetch('http://your-server:8002/api/classify', {
          method: 'POST',
          body: formData
        });
        const result = await response.json();
        this.results = result.predictions;
      } catch (error) {
        console.error('Classification error:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>
```

## 🔒 Security & Best Practices

### API Key Management
- Store API keys securely (environment variables)
- Rotate keys regularly
- Use different keys for different environments
- Monitor API usage

### Error Handling
```javascript
const classifyImage = async (file, apiKey) => {
    try {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', apiKey);

        const response = await fetch('http://your-server:8002/api/classify', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Classification failed:', error);
        throw error;
    }
};
```

### Rate Limiting
- Implement client-side rate limiting
- Use exponential backoff for retries
- Cache results when appropriate

## 📊 Response Format

### Classification Response
```json
{
    "success": true,
    "predictions": [
        {
            "category": "dog",
            "confidence": 0.9234
        },
        {
            "category": "animal",
            "confidence": 0.8567
        }
    ],
    "image_name": "uploaded_image.jpg",
    "processing_time": 1.23,
    "model_info": {
        "model_name": "CLIP",
        "categories_count": 11710
    }
}
```

### Error Response
```json
{
    "detail": "Invalid API key",
    "error_code": "INVALID_API_KEY"
}
```

## 🚀 Deployment Options

### Self-hosted
- Deploy on your own server
- Full control over data and processing
- Custom configuration possible

### Cloud Deployment
- AWS EC2, Google Cloud, Azure
- Docker containerization supported
- Auto-scaling capabilities

## 📞 Support

- **Documentation**: Check main README.md
- **Issues**: Report bugs and feature requests
- **API Status**: Monitor `/health` endpoint
- **Performance**: Check `/api/stats` endpoint

---

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
console.log('API Key:', result.api_key);
```

### 2. 이미지 분류

```javascript
const formData = new FormData();
formData.append('file', imageFile);
formData.append('api_key', 'your-api-key');
formData.append('top_k', '5');

const response = await fetch('http://your-server:8002/api/classify', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log('Classification Results:', result.predictions);
```

### 3. 카테고리 관리

```javascript
// 모든 카테고리 조회
const categories = await fetch('http://your-server:8002/api/categories?api_key=your-api-key');

// 카테고리 검색
const searchResults = await fetch('http://your-server:8002/api/categories/search?query=food&api_key=your-api-key');

// 새 카테고리 추가
const formData = new FormData();
formData.append('category', 'new_category');
formData.append('api_key', 'your-api-key');
await fetch('http://your-server:8002/api/categories/add', {
    method: 'POST',
    body: formData
});
```

## 🌐 통합 예제

### React 컴포넌트
```jsx
import React, { useState } from 'react';

const ImageClassifier = () => {
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const classifyImage = async (file) => {
            setLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', 'your-api-key');
        formData.append('top_k', '5');

        try {
            const response = await fetch('http://your-server:8002/api/classify', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            setResults(result.predictions);
            } catch (error) {
            console.error('Classification error:', error);
            } finally {
                setLoading(false);
        }
    };

    return (
        <div>
            <input type="file" onChange={(e) => classifyImage(e.target.files[0])} />
            {loading && <p>분류 중...</p>}
            {results && (
                <ul>
                    {results.map((pred, index) => (
                        <li key={index}>
                            {pred.category}: {(pred.confidence * 100).toFixed(1)}%
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};
```

### Vue.js 컴포넌트
```vue
<template>
    <div>
    <input type="file" @change="handleFileUpload" />
        <div v-if="loading">분류 중...</div>
        <div v-if="results">
      <div v-for="(pred, index) in results" :key="index">
        {{ pred.category }}: {{ (pred.confidence * 100).toFixed(1) }}%
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            results: null,
            loading: false
        };
    },
    methods: {
    async handleFileUpload(event) {
            const file = event.target.files[0];
      if (!file) return;

                this.loading = true;
      const formData = new FormData();
      formData.append('file', file);
      formData.append('api_key', 'your-api-key');
      formData.append('top_k', '5');

      try {
        const response = await fetch('http://your-server:8002/api/classify', {
          method: 'POST',
          body: formData
        });
        const result = await response.json();
        this.results = result.predictions;
                } catch (error) {
        console.error('Classification error:', error);
                } finally {
                    this.loading = false;
            }
        }
    }
};
</script>
```

## 🔒 보안 및 모범 사례

### API 키 관리
- API 키를 안전하게 저장 (환경 변수)
- 정기적으로 키 교체
- 환경별로 다른 키 사용
- API 사용량 모니터링

### 오류 처리
```javascript
const classifyImage = async (file, apiKey) => {
    try {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', apiKey);

        const response = await fetch('http://your-server:8002/api/classify', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Classification failed:', error);
        throw error;
    }
};
```

### 속도 제한
- 클라이언트 측 속도 제한 구현
- 재시도 시 지수 백오프 사용
- 적절한 경우 결과 캐싱

## 📊 응답 형식

### 분류 응답
```json
{
    "success": true,
    "predictions": [
        {
            "category": "dog",
            "confidence": 0.9234
        },
        {
            "category": "animal",
            "confidence": 0.8567
        }
    ],
    "image_name": "uploaded_image.jpg",
    "processing_time": 1.23,
    "model_info": {
        "model_name": "CLIP",
        "categories_count": 11710
    }
}
```

### 오류 응답
```json
{
    "detail": "Invalid API key",
    "error_code": "INVALID_API_KEY"
}
```

## 🚀 배포 옵션

### 자체 호스팅
- 자체 서버에 배포
- 데이터 및 처리에 대한 완전한 제어
- 사용자 정의 구성 가능

### 클라우드 배포
- AWS EC2, Google Cloud, Azure
- Docker 컨테이너화 지원
- 자동 확장 기능

## 📞 지원

- **문서**: 메인 README.md 확인
- **이슈**: 버그 및 기능 요청 보고
- **API 상태**: `/health` 엔드포인트 모니터링
- **성능**: `/api/stats` 엔드포인트 확인

---

# 🌟 VisionAI Pro Zero-Shot API - 外部使用指南

## 🎯 概述

VisionAI Pro Zero-Shot API是一个支持**11,710个类别**的高性能图像分类API。可以轻松在Pinterest、Cosmos.so等外部平台上使用。

## 🚀 主要特点

- **零样本学习**：可以分类未训练的类别
- **11,710个类别**：基于base_words.txt的大规模类别支持
- **实时学习**：可以立即添加新类别
- **高精度分类**：基于CLIP模型的人眼级别精度
- **CORS支持**：可从所有域访问

## 📋 API端点

### 🔑 认证
- `POST /api/keys/generate` - 生成API密钥
- `GET /api/keys/validate` - 验证API密钥

### 🖼️ 图像分类
- `POST /api/classify` - 图像分类（主要功能）

### 📂 类别管理
- `GET /api/categories` - 获取类别列表
- `GET /api/categories/search` - 搜索类别
- `POST /api/categories/add` - 添加类别
- `DELETE /api/categories/remove` - 删除类别

### 📊 系统信息
- `GET /health` - 服务器状态检查
- `GET /api/stats` - 系统统计
- `GET /api/models` - 可用模型

## 🔧 快速开始

### 1. 生成API密钥

```javascript
const formData = new FormData();
formData.append('client_name', 'MyApp');
formData.append('email', 'user@example.com');
formData.append('description', '外部网络应用');

const response = await fetch('http://your-server:8002/api/keys/generate', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log('API Key:', result.api_key);
```

### 2. 图像分类

```javascript
const formData = new FormData();
formData.append('file', imageFile);
formData.append('api_key', 'your-api-key');
formData.append('top_k', '5');

const response = await fetch('http://your-server:8002/api/classify', {
    method: 'POST',
    body: formData
});

const result = await response.json();
console.log('Classification Results:', result.predictions);
```

### 3. 类别管理

```javascript
// 获取所有类别
const categories = await fetch('http://your-server:8002/api/categories?api_key=your-api-key');

// 搜索类别
const searchResults = await fetch('http://your-server:8002/api/categories/search?query=food&api_key=your-api-key');

// 添加新类别
const formData = new FormData();
formData.append('category', 'new_category');
formData.append('api_key', 'your-api-key');
await fetch('http://your-server:8002/api/categories/add', {
    method: 'POST',
    body: formData
});
```

## 🌐 集成示例

### React组件
```jsx
import React, { useState } from 'react';

const ImageClassifier = () => {
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    const classifyImage = async (file) => {
        setLoading(true);
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', 'your-api-key');
        formData.append('top_k', '5');

        try {
            const response = await fetch('http://your-server:8002/api/classify', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            setResults(result.predictions);
        } catch (error) {
            console.error('Classification error:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <input type="file" onChange={(e) => classifyImage(e.target.files[0])} />
            {loading && <p>分类中...</p>}
            {results && (
                <ul>
                    {results.map((pred, index) => (
                        <li key={index}>
                            {pred.category}: {(pred.confidence * 100).toFixed(1)}%
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};
```

### Vue.js组件
```vue
<template>
  <div>
    <input type="file" @change="handleFileUpload" />
    <div v-if="loading">分类中...</div>
    <div v-if="results">
      <div v-for="(pred, index) in results" :key="index">
        {{ pred.category }}: {{ (pred.confidence * 100).toFixed(1) }}%
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      results: null,
      loading: false
    };
  },
  methods: {
    async handleFileUpload(event) {
      const file = event.target.files[0];
      if (!file) return;

      this.loading = true;
      const formData = new FormData();
      formData.append('file', file);
      formData.append('api_key', 'your-api-key');
      formData.append('top_k', '5');

      try {
        const response = await fetch('http://your-server:8002/api/classify', {
          method: 'POST',
          body: formData
        });
        const result = await response.json();
        this.results = result.predictions;
      } catch (error) {
        console.error('Classification error:', error);
      } finally {
        this.loading = false;
      }
    }
  }
};
</script>
```

## 🔒 安全和最佳实践

### API密钥管理
- 安全存储API密钥（环境变量）
- 定期轮换密钥
- 不同环境使用不同密钥
- 监控API使用情况

### 错误处理
```javascript
const classifyImage = async (file, apiKey) => {
    try {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('api_key', apiKey);

        const response = await fetch('http://your-server:8002/api/classify', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        return await response.json();
    } catch (error) {
        console.error('Classification failed:', error);
        throw error;
    }
};
```

### 速率限制
- 实现客户端速率限制
- 重试时使用指数退避
- 适当时缓存结果

## 📊 响应格式

### 分类响应
```json
{
    "success": true,
    "predictions": [
        {
            "category": "dog",
            "confidence": 0.9234
        },
        {
            "category": "animal",
            "confidence": 0.8567
        }
    ],
    "image_name": "uploaded_image.jpg",
    "processing_time": 1.23,
    "model_info": {
        "model_name": "CLIP",
        "categories_count": 11710
    }
}
```

### 错误响应
```json
{
    "detail": "Invalid API key",
    "error_code": "INVALID_API_KEY"
}
```

## 🚀 部署选项

### 自托管
- 在您自己的服务器上部署
- 对数据和处理的完全控制
- 可以自定义配置

### 云部署
- AWS EC2、Google Cloud、Azure
- 支持Docker容器化
- 自动扩展功能

## 📞 支持

- **文档**：查看主README.md
- **问题**：报告错误和功能请求
- **API状态**：监控`/health`端点
- **性能**：检查`/api/stats`端点