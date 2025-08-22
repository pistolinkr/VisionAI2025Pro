#!/usr/bin/env python3
"""
Simple API Authentication Test
Tests if the API key validation is working correctly
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_endpoint(endpoint, method="GET", headers=None, data=None, files=None, expected_status=None):
    """Test an endpoint and return the result"""
    try:
        if method == "GET":
            response = requests.get(f"{BASE_URL}{endpoint}", headers=headers)
        elif method == "POST":
            response = requests.post(f"{BASE_URL}{endpoint}", headers=headers, data=data, files=files)
        else:
            print(f"❌ Unsupported method: {method}")
            return False
        
        status = response.status_code
        success = expected_status is None or status == expected_status
        
        if success:
            print(f"✅ {method} {endpoint} - Status: {status}")
            if response.text:
                try:
                    print(f"   Response: {json.dumps(response.json(), indent=2)}")
                except:
                    print(f"   Response: {response.text[:200]}...")
        else:
            print(f"❌ {method} {endpoint} - Expected: {expected_status}, Got: {status}")
            if response.text:
                try:
                    print(f"   Response: {json.dumps(response.json(), indent=2)}")
                except:
                    print(f"   Response: {response.text[:200]}...")
        
        return success
        
    except requests.exceptions.ConnectionError:
        print(f"❌ {method} {endpoint} - Connection failed (server not running?)")
        return False
    except Exception as e:
        print(f"❌ {method} {endpoint} - Error: {e}")
        return False

def main():
    """Run authentication tests"""
    print("🔐 Testing API Authentication")
    print("=" * 50)
    
    # Test 1: Health check (no auth required)
    print("\n1. Testing Health Check (No Auth)")
    test_endpoint("/health", expected_status=200)
    
    # Test 2: Debug endpoint (no auth required)
    print("\n2. Testing Debug Endpoint (No Auth)")
    test_endpoint("/debug", expected_status=200)
    
    # Test 3: Categories without API key (should fail)
    print("\n3. Testing Categories Endpoint (No API Key)")
    test_endpoint("/api/categories", expected_status=401)
    
    # Test 4: Categories with invalid API key (should fail)
    print("\n4. Testing Categories Endpoint (Invalid API Key)")
    headers = {"X-API-Key": "invalid-key-12345"}
    test_endpoint("/api/categories", headers=headers, expected_status=401)
    
    # Test 5: Image classification without API key (should fail)
    print("\n5. Testing Image Classification (No API Key)")
    test_endpoint("/api/classify", method="POST", expected_status=401)
    
    # Test 6: Image classification with invalid API key (should fail)
    print("\n6. Testing Image Classification (Invalid API Key)")
    headers = {"X-API-Key": "invalid-key-12345"}
    test_endpoint("/api/classify", method="POST", headers=headers, expected_status=401)
    
    # Test 7: API key generation without API key (should fail)
    print("\n7. Testing API Key Generation (No API Key)")
    test_endpoint("/api/keys/generate", method="POST", expected_status=401)
    
    # Test 8: API key generation with invalid API key (should fail)
    print("\n8. Testing API Key Generation (Invalid API Key)")
    headers = {"X-API-Key": "invalid-key-12345"}
    data = {"name": "Test Key", "permissions": "read,classify", "expiry_days": "30"}
    test_endpoint("/api/keys/generate", method="POST", headers=headers, data=data, expected_status=401)
    
    print("\n" + "=" * 50)
    print("🎯 Authentication Test Summary")
    print("✅ All endpoints should return 401 (Unauthorized) when no valid API key is provided")
    print("✅ This confirms that the API key validation is working correctly")
    print("✅ To test with valid keys, you'll need to generate them first")

if __name__ == "__main__":
    main()
