@echo off
echo ========================================
echo VisionAI Pro - External Access Setup Script
echo ========================================
echo.

REM Check administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] This script must be run as administrator.
    echo Right-click and select "Run as administrator".
    pause
    exit /b 1
)

echo [INFO] Administrator privileges confirmed
echo.

REM Set environment variables
echo [INFO] Setting environment variables...
setx ENABLE_EXTERNAL_ACCESS "true" /M
setx ALLOWED_ORIGINS "http://localhost:3000,https://yourdomain.com" /M
setx ALLOWED_HOSTS "localhost,yourdomain.com" /M
setx RATE_LIMIT_PER_MINUTE "60" /M
setx MAX_REQUEST_SIZE "10485760" /M

echo [INFO] Environment variables set successfully
echo.

REM Add firewall rules
echo [INFO] Adding Windows firewall rules...

REM Use PowerShell to add firewall rules
powershell -Command "New-NetFirewallRule -DisplayName 'VisionAI Pro API - Inbound' -Direction Inbound -Protocol TCP -LocalPort 8002 -Action Allow -Profile Any" 2>nul
if %errorLevel% equ 0 (
    echo [SUCCESS] Inbound firewall rule added successfully
) else (
    echo [WARNING] Failed to add inbound firewall rule (may already exist)
)

powershell -Command "New-NetFirewallRule -DisplayName 'VisionAI Pro API - Outbound' -Direction Outbound -Protocol TCP -LocalPort 8002 -Action Allow -Profile Any" 2>nul
if %errorLevel% equ 0 (
    echo [SUCCESS] Outbound firewall rule added successfully
) else (
    echo [WARNING] Failed to add outbound firewall rule (may already exist)
)

echo.

REM Create .env file
echo [INFO] Creating .env file...
(
echo # VisionAI Pro External Access Configuration
echo ENABLE_EXTERNAL_ACCESS=true
echo.
echo # Allowed domains ^(comma-separated^)
echo ALLOWED_ORIGINS=http://localhost:3000,https://yourdomain.com
echo.
echo # Allowed hosts ^(comma-separated^)
echo ALLOWED_HOSTS=localhost,yourdomain.com
echo.
echo # Rate Limiting configuration
echo RATE_LIMIT_PER_MINUTE=60
echo.
echo # Request size limit ^(bytes^)
echo MAX_REQUEST_SIZE=10485760
echo.
echo # API security key ^(MUST CHANGE THIS!^)
echo API_SECRET_KEY=your-super-secret-key-change-this-now
echo.
echo # Server configuration
echo HOST=0.0.0.0
echo PORT=8002
) > .env

echo [SUCCESS] .env file created successfully
echo.

REM Check Redis installation and provide guidance
echo [INFO] Checking Redis installation...
redis-server --version >nul 2>&1
if %errorLevel% equ 0 (
    echo [SUCCESS] Redis is installed.
) else (
    echo [WARNING] Redis is not installed.
    echo Rate limiting will work with in-memory storage.
    echo Installing Redis will provide more stable rate limiting.
    echo.
    echo Redis installation methods:
    echo 1. Download from https://github.com/microsoftarchive/redis/releases
    echo 2. Or use Chocolatey: choco install redis-64
    echo 3. Or use Docker: docker run -d -p 6379:6379 redis:alpine
)

echo.

REM Display network information
echo [INFO] Network information:
ipconfig | findstr "IPv4"
echo.

REM Check port usage
echo [INFO] Checking port 8002 availability...
netstat -an | findstr ":8002" >nul 2>&1
if %errorLevel% equ 0 (
    echo [WARNING] Port 8002 is already in use.
    echo Please stop the server and try again.
) else (
    echo [SUCCESS] Port 8002 is available.
)

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Update domains and API key in .env file with actual values
echo 2. Start server: python main.py zero-shot
echo 3. Generate API key: curl -X POST "http://localhost:8002/api/keys/generate"
echo 4. Test external access
echo.
echo Security considerations:
echo - Use strong API keys
echo - Configure IP whitelist when possible
echo - Regular security updates
echo.
pause
