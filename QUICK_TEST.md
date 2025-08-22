# 🚀 Quick API Testing Guide

## 📋 Prerequisites

1. **Start the API Server**
   ```bash
   # Option 1: Using run.py
   venv/bin/python run.py
   
   # Option 2: Direct uvicorn
   venv/bin/uvicorn src.api.main:app --host 127.0.0.1 --port 8000
   ```

2. **Verify Server is Running**
   ```bash
   curl http://localhost:8000/health
   ```
   Expected: `{"status": "healthy", "classifier_loaded": true, "api_key_manager_loaded": true}`

## 🧪 Quick Tests

### 1. Basic Connectivity
```bash
# Health check
curl http://localhost:8000/health

# Root page
curl http://localhost:8000/

# Swagger docs
curl http://localhost:8000/docs
```

### 2. API Endpoints (No Auth)
```bash
# Categories without API key (should return 401)
curl http://localhost:8000/api/categories

# Image classification without API key (should return 401)
curl -X POST http://localhost:8000/api/classify
```

### 3. Web Interface
1. Open http://localhost:8000 in your browser
2. Click "Upload Image"
3. Enter any API key (for testing)
4. Select an image file
5. Click "Start Analysis"

## 🔧 Automated Testing

### Python Script
```bash
# Install requests if not available
venv/bin/pip install requests

# Run comprehensive tests
venv/bin/python test_api.py
```

### Shell Script
```bash
# Make executable (if not already)
chmod +x test_api.sh

# Run tests
./test_api.sh
```

## 📊 Expected Results

| Test | Expected Status | Expected Response |
|------|----------------|-------------------|
| `/health` | 200 | `{"status": "healthy"}` |
| `/` | 200 | HTML page with ProRL V2 content |
| `/docs` | 200 | Swagger UI interface |
| `/api/categories` (no key) | 401 | `{"detail": "Invalid API key"}` |
| `/api/classify` (no key) | 401 | `{"detail": "Invalid API key"}` |

## 🚨 Troubleshooting

### Server Won't Start
- Check if port 8000 is available: `lsof -i :8000`
- Verify virtual environment is activated
- Check if all dependencies are installed: `venv/bin/pip list`

### Connection Refused
- Ensure server is running on correct port
- Check firewall settings
- Verify host binding (127.0.0.1 vs 0.0.0.0)

### Import Errors
- Check Python path: `venv/bin/python -c "import sys; print(sys.path)"`
- Verify file structure matches expected layout
- Check for syntax errors in Python files

## 🔗 Useful Commands

```bash
# Check server status
ps aux | grep uvicorn

# View server logs
tail -f logs/app.log

# Test specific endpoint
curl -v http://localhost:8000/health

# Kill server if needed
pkill -f uvicorn
```

## 📝 Next Steps

1. **Generate API Key**: Use CLI tool to create valid API keys
2. **Test with Real Images**: Upload actual images for classification
3. **Performance Testing**: Test with multiple concurrent requests
4. **Integration Testing**: Test with your application

## 🆘 Need Help?

- Check the main README.md for detailed documentation
- Run `python test_system.py` for system-wide testing
- Check server logs for error messages
- Verify all files are in correct locations
