/**
 * VisionAI Pro Zero-Shot API 외부 사용 예제
 * Pinterest, Cosmos.so 등 외부 플랫폼에서 사용 가능
 */

class VisionAIProAPI {
    constructor(baseUrl = 'http://your-server:8002', apiKey = null) {
        this.baseUrl = baseUrl;
        this.apiKey = apiKey;
    }

    /**
     * API 키 생성
     */
    async generateAPIKey(clientName, email = null, description = null) {
        const formData = new FormData();
        formData.append('client_name', clientName);
        if (email) formData.append('email', email);
        if (description) formData.append('description', description);

        const response = await fetch(`${this.baseUrl}/api/keys/generate`, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        if (result.success) {
            this.apiKey = result.api_key;
            return result;
        } else {
            throw new Error('API 키 생성 실패');
        }
    }

    /**
     * API 키 유효성 검증
     */
    async validateAPIKey(apiKey = this.apiKey) {
        const response = await fetch(`${this.baseUrl}/api/keys/validate?api_key=${apiKey}`);
        return await response.json();
    }

    /**
     * 이미지 분류
     */
    async classifyImage(imageFile, topK = 5) {
        if (!this.apiKey) {
            throw new Error('API 키가 필요합니다. generateAPIKey()를 먼저 호출하세요.');
        }

        const formData = new FormData();
        formData.append('image', imageFile);
        formData.append('api_key', this.apiKey);
        formData.append('top_k', topK.toString());

        const response = await fetch(`${this.baseUrl}/api/classify`, {
            method: 'POST',
            body: formData
        });

        return await response.json();
    }

    /**
     * 카테고리 목록 조회
     */
    async getCategories(limit = 20, offset = 0) {
        const response = await fetch(
            `${this.baseUrl}/api/categories?limit=${limit}&offset=${offset}${this.apiKey ? `&api_key=${this.apiKey}` : ''}`
        );
        return await response.json();
    }

    /**
     * 카테고리 검색
     */
    async searchCategories(query, limit = 10) {
        const response = await fetch(
            `${this.baseUrl}/api/categories/search?query=${encodeURIComponent(query)}&limit=${limit}${this.apiKey ? `&api_key=${this.apiKey}` : ''}`
        );
        return await response.json();
    }

    /**
     * 카테고리 추가
     */
    async addCategory(category) {
        if (!this.apiKey) {
            throw new Error('API 키가 필요합니다.');
        }

        const formData = new FormData();
        formData.append('category', category);
        formData.append('api_key', this.apiKey);

        const response = await fetch(`${this.baseUrl}/api/categories/add`, {
            method: 'POST',
            body: formData
        });

        return await response.json();
    }

    /**
     * 카테고리 제거
     */
    async removeCategory(category) {
        if (!this.apiKey) {
            throw new Error('API 키가 필요합니다.');
        }

        const formData = new FormData();
        formData.append('category', category);
        formData.append('api_key', this.apiKey);

        const response = await fetch(`${this.baseUrl}/api/categories/remove`, {
            method: 'DELETE',
            body: formData
        });

        return await response.json();
    }

    /**
     * 시스템 통계 조회
     */
    async getStats() {
        const response = await fetch(
            `${this.baseUrl}/api/stats${this.apiKey ? `?api_key=${this.apiKey}` : ''}`
        );
        return await response.json();
    }

    /**
     * 헬스 체크
     */
    async healthCheck() {
        const response = await fetch(`${this.baseUrl}/health`);
        return await response.json();
    }
}

// 사용 예제
async function exampleUsage() {
    try {
        // API 인스턴스 생성
        const api = new VisionAIProAPI('http://your-server:8002');

        // 1. API 키 생성
        const keyResult = await api.generateAPIKey('MyApp', 'user@example.com', '외부 웹앱');
        console.log('생성된 API 키:', keyResult.api_key);

        // 2. 헬스 체크
        const health = await api.healthCheck();
        console.log('서버 상태:', health);

        // 3. 이미지 분류 (파일 입력에서)
        const fileInput = document.getElementById('imageInput');
        if (fileInput.files[0]) {
            const result = await api.classifyImage(fileInput.files[0], 5);
            console.log('분류 결과:', result.predictions);
        }

        // 4. 카테고리 검색
        const searchResult = await api.searchCategories('animal', 10);
        console.log('검색 결과:', searchResult.categories);

        // 5. 새로운 카테고리 추가
        const addResult = await api.addCategory('my_custom_category');
        console.log('카테고리 추가:', addResult);

        // 6. 시스템 통계
        const stats = await api.getStats();
        console.log('시스템 통계:', stats);

    } catch (error) {
        console.error('API 사용 중 오류:', error);
    }
}

// React/Vue.js 컴포넌트 예제
function ImageClassifierComponent() {
    const [api, setApi] = useState(null);
    const [results, setResults] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        // 컴포넌트 마운트 시 API 초기화
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

// Node.js 서버 예제
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

// 모듈 내보내기 (ES6)
export default VisionAIProAPI;

// CommonJS
module.exports = VisionAIProAPI;
