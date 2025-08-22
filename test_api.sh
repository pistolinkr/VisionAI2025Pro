#!/bin/bash

# ProRL V2 API Testing Script
# Tests all API endpoints with various scenarios

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# API Configuration
BASE_URL="http://localhost:8000"
API_KEY=""

echo -e "${BLUE}🚀 Starting ProRL V2 API Tests${NC}"
echo -e "${BLUE}📍 Testing API at: ${BASE_URL}${NC}"
echo -e "${BLUE}⏰ Started at: $(date)${NC}"

# Function to print section headers
print_section() {
    echo -e "\n${YELLOW}============================================================${NC}"
    echo -e "${YELLOW}🔍 $1${NC}"
    echo -e "${YELLOW}============================================================${NC}"
}

# Function to print test results
print_result() {
    local endpoint="$1"
    local success="$2"
    local response="$3"
    local error="$4"
    
    if [ "$success" = "true" ]; then
        echo -e "${GREEN}✅ PASS${NC} $endpoint"
    else
        echo -e "${RED}❌ FAIL${NC} $endpoint"
    fi
    
    if [ -n "$response" ]; then
        echo "   Response: $response"
    fi
    
    if [ -n "$error" ]; then
        echo -e "   ${RED}Error: $error${NC}"
    fi
}

# Test 1: Health Check
print_section "Health Check Test"
if response=$(curl -s "$BASE_URL/health" 2>/dev/null); then
    if echo "$response" | grep -q "healthy"; then
        print_result "/health" "true" "$response"
        HEALTH_PASS=true
    else
        print_result "/health" "false" "" "Unexpected response"
        HEALTH_PASS=false
    fi
else
    print_result "/health" "false" "" "Connection failed"
    HEALTH_PASS=false
fi

# Test 2: Root Page
print_section "Root Page Test"
if response=$(curl -s "$BASE_URL/" 2>/dev/null); then
    if echo "$response" | grep -q "ProRL V2"; then
        print_result "/" "true" "HTML page loaded successfully"
        ROOT_PASS=true
    else
        print_result "/" "false" "" "Unexpected content"
        ROOT_PASS=false
    fi
else
    print_result "/" "false" "" "Connection failed"
    ROOT_PASS=false
fi

# Test 3: Categories without API key
print_section "Categories Test (No API Key)"
if response=$(curl -s -w "%{http_code}" "$BASE_URL/api/categories" 2>/dev/null); then
    http_code="${response: -3}"
    if [ "$http_code" = "401" ]; then
        print_result "/api/categories (no key)" "true" "Expected: Unauthorized"
        CATEGORIES_NO_KEY_PASS=true
    else
        print_result "/api/categories (no key)" "false" "" "Expected 401, got $http_code"
        CATEGORIES_NO_KEY_PASS=false
    fi
else
    print_result "/api/categories (no key)" "false" "" "Connection failed"
    CATEGORIES_NO_KEY_PASS=false
fi

# Test 4: Categories with invalid API key
print_section "Categories Test (Invalid API Key)"
if response=$(curl -s -w "%{http_code}" -H "X-API-Key: invalid-key-12345" "$BASE_URL/api/categories" 2>/dev/null); then
    http_code="${response: -3}"
    if [ "$http_code" = "401" ]; then
        print_result "/api/categories (invalid key)" "true" "Expected: Unauthorized"
        CATEGORIES_INVALID_KEY_PASS=true
    else
        print_result "/api/categories (invalid key)" "false" "" "Expected 401, got $http_code"
        CATEGORIES_INVALID_KEY_PASS=false
    fi
else
    print_result "/api/categories (invalid key)" "false" "" "Connection failed"
    CATEGORIES_INVALID_KEY_PASS=false
fi

# Test 5: Image classification without API key
print_section "Image Classification Test (No API Key)"
if response=$(curl -s -w "%{http_code}" -F "file=@README.md" "$BASE_URL/api/classify" 2>/dev/null); then
    http_code="${response: -3}"
    if [ "$http_code" = "401" ]; then
        print_result "/api/classify (no key)" "true" "Expected: Unauthorized"
        CLASSIFY_NO_KEY_PASS=true
    else
        print_result "/api/classify (no key)" "false" "" "Expected 401, got $http_code"
        CLASSIFY_NO_KEY_PASS=false
    fi
else
    print_result "/api/classify (no key)" "false" "" "Connection failed"
    CLASSIFY_NO_KEY_PASS=false
fi

# Test 6: Swagger Documentation
print_section "Swagger Documentation Test"
if response=$(curl -s -w "%{http_code}" "$BASE_URL/docs" 2>/dev/null); then
    http_code="${response: -3}"
    if [ "$http_code" = "200" ]; then
        print_result "/docs" "true" "Swagger UI accessible"
        SWAGGER_PASS=true
    else
        print_result "/docs" "false" "" "Status: $http_code"
        SWAGGER_PASS=false
    fi
else
    print_result "/docs" "false" "" "Connection failed"
    SWAGGER_PASS=false
fi

# Test 7: ReDoc Documentation
print_section "ReDoc Documentation Test"
if response=$(curl -s -w "%{http_code}" "$BASE_URL/redoc" 2>/dev/null); then
    http_code="${response: -3}"
    if [ "$http_code" = "200" ]; then
        print_result "/redoc" "true" "ReDoc accessible"
        REDOC_PASS=true
    else
        print_result "/redoc" "false" "" "Status: $http_code"
        REDOC_PASS=false
    fi
else
    print_result "/redoc" "false" "" "Connection failed"
    REDOC_PASS=false
fi

# Performance Test
print_section "Performance Test"
start_time=$(date +%s.%N)
responses=()
for i in {1..5}; do
    if response=$(curl -s -w "%{http_code}" "$BASE_URL/health" 2>/dev/null); then
        http_code="${response: -3}"
        responses+=("$http_code")
    else
        responses+=("Error")
    fi
done
end_time=$(date +%s.%N)

# Calculate execution time
execution_time=$(echo "$end_time - $start_time" | bc -l 2>/dev/null || echo "0")
avg_time=$(echo "$execution_time / 5" | bc -l 2>/dev/null || echo "0")

print_result "Performance Test" "true" "5 requests in ${execution_time}s (avg: ${avg_time}s per request)"

# Summary
print_section "Test Results Summary"

# Count passed tests
passed=0
total=0

if [ "$HEALTH_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$ROOT_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$CATEGORIES_NO_KEY_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$CATEGORIES_INVALID_KEY_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$CLASSIFY_NO_KEY_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$SWAGGER_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))
if [ "$REDOC_PASS" = "true" ]; then passed=$((passed + 1)); fi; total=$((total + 1))

echo -e "${BLUE}📊 Results: ${passed}/${total} tests passed${NC}"

if [ $passed -eq $total ]; then
    echo -e "${GREEN}🎉 All tests passed! API is working correctly.${NC}"
else
    echo -e "${RED}⚠️  $((total - passed)) tests failed. Check the API server and configuration.${NC}"
fi

echo -e "\n${BLUE}💡 Tips:${NC}"
echo -e "   - Make sure the API server is running on ${BASE_URL}"
echo -e "   - Check if all required packages are installed"
echo -e "   - Verify the virtual environment is activated"
echo -e "   - Check server logs for any error messages"
echo -e "   - Run 'python test_api.py' for more detailed Python-based testing"

echo -e "\n${BLUE}🔗 Useful URLs:${NC}"
echo -e "   - API Root: ${BASE_URL}"
echo -e "   - Health Check: ${BASE_URL}/health"
echo -e "   - Swagger UI: ${BASE_URL}/docs"
echo -e "   - ReDoc: ${BASE_URL}/redoc"
