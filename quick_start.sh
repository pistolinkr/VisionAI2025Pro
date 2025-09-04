#!/bin/bash

# VisionAI Pro Quick Start Script for Jetson

echo "🚀 Starting VisionAI Pro Server..."

# 현재 디렉토리로 이동
cd "$(dirname "$0")"

# 가상환경 활성화
source venv/bin/activate

# 환경 변수 설정
export CUDA_VISIBLE_DEVICES=0
export DEVICE=cuda
export HOST=0.0.0.0
export PORT=8000

# 서버 시작
python3 run_jetson.py
