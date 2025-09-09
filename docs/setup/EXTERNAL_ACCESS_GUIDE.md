# 🌐 VisionAI Pro - 외부 접근 설정 가이드

## 🚀 개요

이 가이드는 VisionAI Pro API 서버를 외부에서 안전하게 접근할 수 있도록 설정하는 방법을 설명합니다. 윈도우 환경에서 주로 사용되는 시나리오를 중심으로 작성되었습니다.

## 🔒 보안 기능

### 주요 보안 기능
- **API 키 기반 인증**: 모든 요청에 대한 API 키 검증
- **IP 화이트리스트**: 허용된 IP 주소에서만 접근 가능
- **Rate Limiting**: 분당 요청 수 제한 (기본 60회)
- **CORS 보안**: 허용된 도메인에서만 접근 가능
- **요청 크기 제한**: 최대 10MB 요청 크기 제한
- **사용량 추적**: API 사용량 모니터링 및 로깅

## ⚙️ 설정 방법

### 1. 환경 변수 설정

`.env` 파일을 생성하고 다음 설정을 추가합니다:

```env
# 외부 접근 활성화
ENABLE_EXTERNAL_ACCESS=true

# 허용된 도메인 (쉼표로 구분)
ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com,https://app.yourdomain.com

# 허용된 호스트 (쉼표로 구분)
ALLOWED_HOSTS=localhost,yourdomain.com,app.yourdomain.com

# Rate Limiting 설정
RATE_LIMIT_PER_MINUTE=60

# 요청 크기 제한 (바이트)
MAX_REQUEST_SIZE=10485760

# API 보안 키 (반드시 변경하세요!)
API_SECRET_KEY=your-super-secret-key-change-this-now

# 서버 설정
HOST=0.0.0.0
PORT=8002
```

### 2. 윈도우 방화벽 설정

#### PowerShell을 관리자 권한으로 실행하여 방화벽 규칙 추가:

```powershell
# 인바운드 규칙 추가 (포트 8002)
New-NetFirewallRule -DisplayName "VisionAI Pro API" -Direction Inbound -Protocol TCP -LocalPort 8002 -Action Allow

# 아웃바운드 규칙 추가 (선택사항)
New-NetFirewallRule -DisplayName "VisionAI Pro API Outbound" -Direction Outbound -Protocol TCP -LocalPort 8002 -Action Allow
```

#### 또는 GUI를 통한 설정:
1. **Windows 보안** → **방화벽 및 네트워크 보호**
2. **고급 설정** 클릭
3. **인바운드 규칙** → **새 규칙**
4. **포트** 선택 → **TCP** → **특정 로컬 포트** → `8002` 입력
5. **연결 허용** 선택
6. **도메인, 개인, 공용** 모두 선택
7. 이름: `VisionAI Pro API`

### 3. 라우터 포트 포워딩 (필요시)

외부 인터넷에서 접근하려면 라우터에서 포트 포워딩을 설정해야 합니다:

1. 라우터 관리 페이지 접속 (보통 `192.168.1.1` 또는 `192.168.0.1`)
2. **포트 포워딩** 또는 **가상 서버** 설정
3. 외부 포트: `8002` (또는 원하는 포트)
4. 내부 IP: 서버의 로컬 IP 주소
5. 내부 포트: `8002`
6. 프로토콜: `TCP`

## 🔑 API 키 관리

### API 키 생성

```bash
# 서버 실행 후 API 키 생성
curl -X POST "http://localhost:8002/api/keys/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "client_name": "My App",
    "permissions": ["classify", "categories"],
    "expires_days": 365
  }'
```

### 보안 API 키 생성 (IP 제한 포함)

```bash
curl -X POST "http://localhost:8002/api/keys/generate-secure" \
  -H "Content-Type: application/json" \
  -d '{
    "client_name": "Secure App",
    "permissions": ["classify"],
    "expires_days": 90,
    "ip_whitelist": ["192.168.1.100", "203.0.113.5"]
  }'
```

### API 키 검증

```bash
curl -X GET "http://localhost:8002/api/keys/validate?api_key=YOUR_API_KEY"
```

## 📊 사용량 모니터링

### API 사용량 통계 조회

```bash
curl -X GET "http://localhost:8002/api/keys/stats?api_key=YOUR_API_KEY&days=30"
```

### 사용량 통계 응답 예시

```json
{
  "total_requests": 1250,
  "error_requests": 15,
  "unique_ips": 3,
  "recent_activity": [
    {
      "ip_address": "192.168.1.100",
      "endpoint": "/classify",
      "timestamp": "2024-01-15T10:30:00",
      "response_code": 200
    }
  ]
}
```

## 🛡️ 보안 모범 사례

### 1. API 키 보안
- **강력한 API 키 사용**: `vai_` 접두사가 있는 보안 키 사용
- **정기적인 키 갱신**: 90일마다 API 키 갱신
- **최소 권한 원칙**: 필요한 권한만 부여
- **IP 화이트리스트**: 가능한 경우 IP 제한 설정

### 2. 네트워크 보안
- **HTTPS 사용**: 프로덕션 환경에서는 반드시 HTTPS 사용
- **방화벽 설정**: 필요한 포트만 열기
- **VPN 사용**: 가능한 경우 VPN을 통한 접근

### 3. 모니터링
- **사용량 모니터링**: 정기적으로 API 사용량 확인
- **로그 검토**: 비정상적인 접근 패턴 감지
- **알림 설정**: 오류율이 높을 때 알림

## 🚨 문제 해결

### 일반적인 문제

#### 1. 연결 거부됨
```
Error: Connection refused
```
**해결 방법:**
- 방화벽 설정 확인
- 서버가 실행 중인지 확인
- 포트가 올바른지 확인

#### 2. CORS 오류
```
Access to fetch at 'http://server:8002/api/classify' from origin 'http://localhost:3000' has been blocked by CORS policy
```
**해결 방법:**
- `ALLOWED_ORIGINS`에 클라이언트 도메인 추가
- `ENABLE_EXTERNAL_ACCESS=true` 설정 확인

#### 3. Rate Limit 초과
```
HTTP 429: Rate limit exceeded
```
**해결 방법:**
- 요청 빈도 줄이기
- `RATE_LIMIT_PER_MINUTE` 값 증가 (권장하지 않음)

#### 4. IP 차단됨
```
HTTP 403: IP address not allowed
```
**해결 방법:**
- API 키의 IP 화이트리스트에 현재 IP 추가
- 또는 IP 제한이 없는 API 키 사용

### 로그 확인

```bash
# 서버 로그 확인
tail -f logs/app.log

# 보안 로그 확인
grep "Security" logs/app.log
grep "Rate limit" logs/app.log
```

## 📝 예제 코드

### JavaScript (브라우저)

```javascript
const API_BASE_URL = 'http://your-server:8002';
const API_KEY = 'your-api-key';

async function classifyImage(imageFile) {
  const formData = new FormData();
  formData.append('file', imageFile);
  formData.append('api_key', API_KEY);
  formData.append('top_k', '5');

  try {
    const response = await fetch(`${API_BASE_URL}/api/classify`, {
      method: 'POST',
      body: formData
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const result = await response.json();
    return result;
  } catch (error) {
    console.error('Classification failed:', error);
    throw error;
  }
}
```

### Python

```python
import requests

API_BASE_URL = 'http://your-server:8002'
API_KEY = 'your-api-key'

def classify_image(image_path):
    url = f"{API_BASE_URL}/api/classify"
    
    with open(image_path, 'rb') as f:
        files = {'file': f}
        data = {
            'api_key': API_KEY,
            'top_k': 5
        }
        
        response = requests.post(url, files=files, data=data)
        response.raise_for_status()
        
        return response.json()

# 사용 예시
result = classify_image('image.jpg')
print(result)
```

### cURL

```bash
curl -X POST "http://your-server:8002/api/classify" \
  -F "file=@image.jpg" \
  -F "api_key=your-api-key" \
  -F "top_k=5"
```

## 🔧 고급 설정

### Nginx 리버스 프록시 (선택사항)

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /api/ {
        proxy_pass http://localhost:8002;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # CORS 헤더
        add_header Access-Control-Allow-Origin *;
        add_header Access-Control-Allow-Methods "GET, POST, OPTIONS";
        add_header Access-Control-Allow-Headers "Content-Type, Authorization";
    }
}
```

### SSL 인증서 설정 (Let's Encrypt)

```bash
# Certbot 설치 (Ubuntu/Debian)
sudo apt install certbot python3-certbot-nginx

# SSL 인증서 발급
sudo certbot --nginx -d your-domain.com
```

## 📞 지원

문제가 발생하거나 추가 도움이 필요한 경우:

1. **로그 확인**: `logs/app.log` 파일 검토
2. **설정 검증**: 환경 변수 설정 확인
3. **네트워크 테스트**: `telnet your-server 8002` 명령으로 연결 테스트
4. **API 테스트**: `curl` 명령으로 API 엔드포인트 테스트

---

**⚠️ 보안 주의사항:**
- 프로덕션 환경에서는 반드시 강력한 API 키 사용
- 정기적으로 보안 업데이트 적용
- 사용하지 않는 API 키는 즉시 삭제
- 네트워크 접근 로그를 정기적으로 검토
