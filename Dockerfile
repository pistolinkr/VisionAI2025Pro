# Docker를 사용한 간단한 실행 방법
# Dockerfile 생성

FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# 프로젝트 클론
RUN git clone https://github.com/pistolinkr/VisionAI2025Pro.git .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 환경 변수 설정
RUN cp env_example.txt .env

# 포트 노출
EXPOSE 8000 8001 8002

# 실행 권한 부여
RUN chmod +x run*.py

# 기본 명령어
CMD ["python3", "run_zero_shot.py"]
