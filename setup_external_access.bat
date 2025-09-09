@echo off
echo ========================================
echo VisionAI Pro - 외부 접근 설정 스크립트
echo ========================================
echo.

REM 관리자 권한 확인
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] 이 스크립트는 관리자 권한으로 실행해야 합니다.
    echo 마우스 우클릭으로 "관리자 권한으로 실행"을 선택하세요.
    pause
    exit /b 1
)

echo [INFO] 관리자 권한 확인 완료
echo.

REM 환경 변수 설정
echo [INFO] 환경 변수 설정 중...
setx ENABLE_EXTERNAL_ACCESS "true" /M
setx ALLOWED_ORIGINS "http://localhost:3000,https://yourdomain.com" /M
setx ALLOWED_HOSTS "localhost,yourdomain.com" /M
setx RATE_LIMIT_PER_MINUTE "60" /M
setx MAX_REQUEST_SIZE "10485760" /M

echo [INFO] 환경 변수 설정 완료
echo.

REM 방화벽 규칙 추가
echo [INFO] 윈도우 방화벽 규칙 추가 중...

REM PowerShell을 사용하여 방화벽 규칙 추가
powershell -Command "New-NetFirewallRule -DisplayName 'VisionAI Pro API - Inbound' -Direction Inbound -Protocol TCP -LocalPort 8002 -Action Allow -Profile Any" 2>nul
if %errorLevel% equ 0 (
    echo [SUCCESS] 인바운드 방화벽 규칙 추가 완료
) else (
    echo [WARNING] 인바운드 방화벽 규칙 추가 실패 (이미 존재할 수 있음)
)

powershell -Command "New-NetFirewallRule -DisplayName 'VisionAI Pro API - Outbound' -Direction Outbound -Protocol TCP -LocalPort 8002 -Action Allow -Profile Any" 2>nul
if %errorLevel% equ 0 (
    echo [SUCCESS] 아웃바운드 방화벽 규칙 추가 완료
) else (
    echo [WARNING] 아웃바운드 방화벽 규칙 추가 실패 (이미 존재할 수 있음)
)

echo.

REM .env 파일 생성
echo [INFO] .env 파일 생성 중...
(
echo # VisionAI Pro External Access Configuration
echo ENABLE_EXTERNAL_ACCESS=true
echo.
echo # 허용된 도메인 ^(쉼표로 구분^)
echo ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
echo.
echo # 허용된 호스트 ^(쉼표로 구분^)
echo ALLOWED_HOSTS=localhost,yourdomain.com
echo.
echo # Rate Limiting 설정
echo RATE_LIMIT_PER_MINUTE=60
echo.
echo # 요청 크기 제한 ^(바이트^)
echo MAX_REQUEST_SIZE=10485760
echo.
echo # API 보안 키 ^(반드시 변경하세요!^)
echo API_SECRET_KEY=your-super-secret-key-change-this-now
echo.
echo # 서버 설정
echo HOST=0.0.0.0
echo PORT=8002
) > .env

echo [SUCCESS] .env 파일 생성 완료
echo.

REM Redis 설치 확인 및 안내
echo [INFO] Redis 설치 확인 중...
redis-server --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [SUCCESS] Redis가 설치되어 있습니다.
) else (
    echo [WARNING] Redis가 설치되어 있지 않습니다.
    echo Rate limiting은 메모리 기반으로 작동합니다.
    echo Redis를 설치하면 더 안정적인 Rate limiting을 사용할 수 있습니다.
    echo.
    echo Redis 설치 방법:
    echo 1. https://github.com/microsoftarchive/redis/releases 에서 다운로드
    echo 2. 또는 Chocolatey 사용: choco install redis-64
    echo 3. 또는 Docker 사용: docker run -d -p 6379:6379 redis:alpine
)

echo.

REM 네트워크 정보 표시
echo [INFO] 네트워크 정보:
ipconfig | findstr "IPv4"
echo.

REM 포트 사용 확인
echo [INFO] 포트 8002 사용 확인 중...
netstat -an | findstr ":8002" >nul 2>&1
if %errorLevel% equ 0 (
    echo [WARNING] 포트 8002가 이미 사용 중입니다.
    echo 서버를 중지하고 다시 시도하세요.
) else (
    echo [SUCCESS] 포트 8002가 사용 가능합니다.
)

echo.
echo ========================================
echo 설정 완료!
echo ========================================
echo.
echo 다음 단계:
echo 1. .env 파일에서 도메인과 API 키를 실제 값으로 수정
echo 2. 서버 실행: python main.py zero-shot
echo 3. API 키 생성: curl -X POST "http://localhost:8002/api/keys/generate"
echo 4. 외부에서 접근 테스트
echo.
echo 보안 주의사항:
echo - 강력한 API 키 사용
echo - IP 화이트리스트 설정 권장
echo - 정기적인 보안 업데이트
echo.
pause
