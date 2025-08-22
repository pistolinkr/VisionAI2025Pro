#!/usr/bin/env python3
"""
ProRL V2 API Testing Script
Tests all API endpoints with various scenarios
"""

import requests
import json
import time
import os
from pathlib import Path

# API Configuration
BASE_URL = "http://localhost:8000"
API_KEY = None  # Will be set after generating one

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"🔍 {title}")
    print(f"{'='*60}")

def print_result(endpoint, success, response=None, error=None):
    """Print formatted test result"""
    status = "✅ PASS" if success else "❌ FAIL"
    print(f"{status} {endpoint}")
    if response:
        print(f"   Response: {json.dumps(response, indent=2)}")
    if error:
        print(f"   Error: {error}")

def test_health_check():
    """Test health check endpoint"""
    print_section("Health Check Test")
    
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print_result("/health", True, data)
            return True
        else:
            print_result("/health", False, error=f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_result("/health", False, error=str(e))
        return False

def test_root_page():
    """Test root page"""
    print_section("Root Page Test")
    
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print_result("/", True, {"status": "HTML page loaded"})
            return True
        else:
            print_result("/", False, error=f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_result("/", False, error=str(e))
        return False

def test_categories_without_key():
    """Test categories endpoint without API key"""
    print_section("Categories Test (No API Key)")
    
    try:
        response = requests.get(f"{BASE_URL}/api/categories")
        if response.status_code == 401:
            print_result("/api/categories (no key)", True, {"expected": "Unauthorized"})
            return True
        else:
            print_result("/api/categories (no key)", False, error=f"Expected 401, got {response.status_code}")
            return False
    except Exception as e:
        print_result("/api/categories (no key)", False, error=str(e))
        return False

def test_categories_with_invalid_key():
    """Test categories endpoint with invalid API key"""
    print_section("Categories Test (Invalid API Key)")
    
    try:
        headers = {"X-API-Key": "invalid-key-12345"}
        response = requests.get(f"{BASE_URL}/api/categories", headers=headers)
        if response.status_code == 401:
            print_result("/api/categories (invalid key)", True, {"expected": "Unauthorized"})
            return True
        else:
            print_result("/api/categories (invalid key)", False, error=f"Expected 401, got {response.status_code}")
            return False
    except Exception as e:
        print_result("/api/categories (invalid key)", False, error=str(e))
        return False

def test_image_classification_without_key():
    """Test image classification without API key"""
    print_section("Image Classification Test (No API Key)")
    
    try:
        # Create a dummy file for testing
        test_file = {"file": ("test.txt", "test content", "text/plain")}
        response = requests.post(f"{BASE_URL}/api/classify", files=test_file)
        if response.status_code == 401:
            print_result("/api/classify (no key)", True, {"expected": "Unauthorized"})
            return True
        else:
            print_result("/api/classify (no key)", False, error=f"Expected 401, got {response.status_code}")
            return False
    except Exception as e:
        print_result("/api/classify (no key)", False, error=str(e))
        return False

def test_image_classification_with_invalid_file():
    """Test image classification with non-image file"""
    print_section("Image Classification Test (Invalid File)")
    
    if not API_KEY:
        print("⚠️  Skipping - No API key available")
        return False
    
    try:
        headers = {"X-API-Key": API_KEY}
        # Try to upload a text file instead of image
        test_file = {"file": ("test.txt", "This is not an image", "text/plain")}
        data = {"top_k": "5"}
        response = requests.post(f"{BASE_URL}/api/classify", headers=headers, files=test_file, data=data)
        
        if response.status_code == 400:
            print_result("/api/classify (invalid file)", True, {"expected": "Bad Request"})
            return True
        else:
            print_result("/api/classify (invalid file)", False, error=f"Expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print_result("/api/classify (invalid file)", False, error=str(e))
        return False

def test_api_key_generation():
    """Test API key generation (requires admin key)"""
    print_section("API Key Generation Test")
    
    try:
        # This will fail without admin permissions, which is expected
        headers = {"X-API-Key": "test-key"}
        data = {
            "name": "Test Key",
            "permissions": "read,classify",
            "expiry_days": "30"
        }
        response = requests.post(f"{BASE_URL}/api/keys/generate", headers=headers, data=data)
        
        if response.status_code == 401:
            print_result("/api/keys/generate", True, {"expected": "Unauthorized - No valid admin key"})
            return True
        else:
            print_result("/api/keys/generate", False, error=f"Unexpected status: {response.status_code}")
            return False
    except Exception as e:
        print_result("/api/keys/generate", False, error=str(e))
        return False

def test_swagger_docs():
    """Test if Swagger documentation is accessible"""
    print_section("Swagger Documentation Test")
    
    try:
        response = requests.get(f"{BASE_URL}/docs")
        if response.status_code == 200:
            print_result("/docs", True, {"status": "Swagger UI accessible"})
            return True
        else:
            print_result("/docs", False, error=f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_result("/docs", False, error=str(e))
        return False

def test_redoc_docs():
    """Test if ReDoc documentation is accessible"""
    print_section("ReDoc Documentation Test")
    
    try:
        response = requests.get(f"{BASE_URL}/redoc")
        if response.status_code == 200:
            print_result("/redoc", True, {"status": "ReDoc accessible"})
            return True
        else:
            print_result("/redoc", False, error=f"Status: {response.status_code}")
            return False
    except Exception as e:
        print_result("/redoc", False, error=str(e))
        return False

def run_performance_test():
    """Run a simple performance test"""
    print_section("Performance Test")
    
    if not API_KEY:
        print("⚠️  Skipping - No API key available")
        return False
    
    try:
        headers = {"X-API-Key": API_KEY}
        start_time = time.time()
        
        # Make multiple requests to test performance
        responses = []
        for i in range(5):
            try:
                response = requests.get(f"{BASE_URL}/api/categories", headers=headers)
                responses.append(response.status_code)
            except Exception as e:
                responses.append(f"Error: {e}")
        
        end_time = time.time()
        total_time = end_time - start_time
        
        print_result("Performance Test", True, {
            "total_requests": 5,
            "total_time": f"{total_time:.2f}s",
            "avg_time_per_request": f"{total_time/5:.2f}s",
            "responses": responses
        })
        return True
        
    except Exception as e:
        print_result("Performance Test", False, error=str(e))
        return False

def main():
    """Run all API tests"""
    print("🚀 Starting ProRL V2 API Tests")
    print(f"📍 Testing API at: {BASE_URL}")
    print(f"⏰ Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test results
    results = []
    
    # Basic connectivity tests
    results.append(("Health Check", test_health_check()))
    results.append(("Root Page", test_root_page()))
    results.append(("Swagger Docs", test_swagger_docs()))
    results.append(("ReDoc", test_redoc_docs()))
    
    # API endpoint tests
    results.append(("Categories (No Key)", test_categories_without_key()))
    results.append(("Categories (Invalid Key)", test_categories_with_invalid_key()))
    results.append(("Image Classification (No Key)", test_image_classification_without_key()))
    results.append(("Image Classification (Invalid File)", test_image_classification_with_invalid_file()))
    results.append(("API Key Generation", test_api_key_generation()))
    
    # Performance test
    results.append(("Performance Test", run_performance_test()))
    
    # Summary
    print_section("Test Results Summary")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print(f"⚠️  {total - passed} tests failed. Check the API server and configuration.")
    
    print(f"\n💡 Tips:")
    print(f"   - Make sure the API server is running on {BASE_URL}")
    print(f"   - Check if all required packages are installed")
    print(f"   - Verify the virtual environment is activated")
    print(f"   - Check server logs for any error messages")

if __name__ == "__main__":
    main()
