# setup.ps1 - Complete HealthChain Backend Setup
Write-Host "🚀 Setting up HealthChain Backend..." -ForegroundColor Cyan

# 1. Create venv
Write-Host "1. Creating virtual environment..." -ForegroundColor Yellow
python -m venv venv

# 2. Activate
Write-Host "2. Activating virtual environment..." -ForegroundColor Yellow
.\venv\Scripts\Activate.ps1

# 3. Create files
Write-Host "3. Creating project files..." -ForegroundColor Yellow
New-Item main.py, requirements.txt, .env -ItemType File -Force
New-Item -Path "data" -ItemType Directory -Force
New-Item -Path "data\patients.json" -ItemType File -Force

# 4. Write requirements.txt
@"
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
"@ | Out-File -FilePath "requirements.txt" -Encoding UTF8

# 5. Write patients.json (simplified)
@"
{
  "123456789012": {
    "name": "Test Patient",
    "dob": "1990-01-01",
    "blood_type": "O+",
    "allergies": ["Penicillin"]
  }
}
"@ | Out-File -FilePath "data\patients.json" -Encoding UTF8

# 6. Write minimal main.py
@"
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home(): return {"message": "HealthChain is running!"}
@app.get("/health")
def health(): return {"status": "healthy"}
"@ | Out-File -FilePath "main.py" -Encoding UTF8

# 7. Install packages
Write-Host "4. Installing packages..." -ForegroundColor Yellow
pip install fastapi uvicorn python-dotenv

Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host "👉 Run: uvicorn main:app --reload" -ForegroundColor Yellow
Write-Host "👉 Docs: http://localhost:8000/docs" -ForegroundColor Yellow