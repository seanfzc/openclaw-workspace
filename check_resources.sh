#!/bin/bash

BASE_URL="http://192.168.2.6"
RESOURCES=(
    "/"
    "/static/js/api.js"
    "/static/js/baseline.js"
    "/static/js/navigation.js"
    "/static/css/style.css"
    "/api/v1/system/health"
    "/api/v1/scans"
)

echo "Checking resources at $BASE_URL"
echo "=============================="

for resource in "${RESOURCES[@]}"; do
    url="${BASE_URL}${resource}"
    status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
    if [ "$status" -eq 200 ] || [ "$status" -eq 201 ] || [ "$status" -eq 204 ]; then
        echo "✅ $resource → $status"
    else
        echo "❌ $resource → $status"
    fi
done

# Test POST to scans endpoint
echo -e "\nTesting POST to /api/v1/scans:"
echo "%PDF dummy" > /tmp/test.pdf
post_status=$(curl -X POST -F "week=1" -F "file=@/tmp/test.pdf" -s -o /dev/null -w "%{http_code}" "$BASE_URL/api/v1/scans")
if [ "$post_status" -eq 200 ]; then
    echo "✅ POST /api/v1/scans → $post_status"
else
    echo "❌ POST /api/v1/scans → $post_status"
fi

# Check baseline page HTML contains required elements
echo -e "\nChecking baseline page elements:"
html=$(curl -s "$BASE_URL/#baseline")
if echo "$html" | grep -q "baseline-file"; then
    echo "✅ baseline-file input found"
else
    echo "❌ baseline-file input NOT found"
fi

if echo "$html" | grep -q "upload-baseline-form"; then
    echo "✅ upload-baseline-form found"
else
    echo "❌ upload-baseline-form NOT found"
fi

echo -e "\nDone."