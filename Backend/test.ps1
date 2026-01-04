Write-Host "🧪 Testing HealthChain API..." -ForegroundColor Cyan

$base = "http://localhost:8000"

# Test 1: Home
try {
    $response = Invoke-RestMethod -Uri "$base/" -Method Get
    Write-Host "✅ Home: $($response.message)" -ForegroundColor Green
} catch {
    Write-Host "❌ Home failed: $_" -ForegroundColor Red
}

# Test 2: Health
try {
    $response = Invoke-RestMethod -Uri "$base/health" -Method Get
    Write-Host "✅ Health: $($response.status)" -ForegroundColor Green
} catch {
    Write-Host "❌ Health failed" -ForegroundColor Red
}

# Test 3: Emergency
try {
    $response = Invoke-RestMethod -Uri "$base/emergency/123456789012?hospital_key=HOSPITAL123" -Method Get
    Write-Host "✅ Emergency: Patient $($response.emergency_data.name)" -ForegroundColor Green
} catch {
    Write-Host "❌ Emergency failed" -ForegroundColor Red
}

Write-Host "🎉 Testing complete!" -ForegroundColor Cyan