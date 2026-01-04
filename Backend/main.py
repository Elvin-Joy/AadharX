from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the app
app = FastAPI(title="HealthChain API")

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "🚀 HealthChain API is LIVE!",
        "docs": "http://localhost:8000/docs",
        "endpoints": {
            "health": "/health",
            "emergency": "/emergency/{aadhaar}?hospital_key=HOSPITAL123",
            "forms": "/forms/{aadhaar}/{form_type}"
        }
    }

# Health check
@app.get("/health")
def health():
    return {"status": "healthy", "service": "HealthChain"}

# Emergency endpoint
@app.get("/emergency/{aadhaar}")
def emergency(aadhaar: str, hospital_key: str = ""):
    """Get medical data for emergency"""
    
    if hospital_key != "HOSPITAL123":
        return {"error": "Invalid hospital key", "hint": "Use hospital_key=HOSPITAL123"}
    
    # Mock patient data
    patients = {
        "123456789012": {
            "name": "Rajesh Kumar",
            "blood_type": "O+",
            "allergies": ["Penicillin"],
            "conditions": ["Diabetes"],
            "warning": "⚠️ CRITICAL: Penicillin allergy"
        }
    }
    
    patient = patients.get(aadhaar)
    if not patient:
        return {"error": "Patient not found", "try": "123456789012"}
    
    return {
        "success": True,
        "emergency_data": patient,
        "restricted": {
            "govt_data": "🔒 Encrypted",
            "financial_data": "🔒 Encrypted"
        }
    }

# Form auto-fill endpoint
@app.get("/forms/{aadhaar}/{form_type}")
def auto_fill_form(aadhaar: str, form_type: str):
    """Auto-fill government forms"""
    
    patients = {
        "123456789012": {
            "name": "Rajesh Kumar",
            "dob": "1990-05-15",
            "address": "Delhi 110045"
        }
    }
    
    patient = patients.get(aadhaar)
    if not patient:
        return {"error": "Patient not found"}
    
    return {
        "form_type": form_type,
        "auto_filled": {
            "name": patient.get("name"),
            "dob": patient.get("dob"),
            "address": patient.get("address")
        },
        "time_saved": "45 minutes",
        "status": "Ready to submit"
    }
# Add this endpoint to your main.py
@app.get("/vault/{aadhaar}")
def data_vault(aadhaar: str):
    """Show what data vaults are accessible for this Aadhaar"""
    
    # Mock patient data
    patients = {
        "123456789012": {
            "name": "Rajesh Kumar",
            "medical_data": {
                "accessible": True,
                "last_accessed": "2024-01-20 14:30:00",
                "accessor": "Apollo Hospital"
            },
            "govt_data": {
                "accessible": True,
                "last_accessed": "2024-01-19 10:15:00",
                "accessor": "Ration Office"
            },
            "financial_data": {
                "accessible": False,
                "last_accessed": "Never",
                "accessor": "None"
            }
        }
    }
    
    patient = patients.get(aadhaar)
    if not patient:
        return {"error": "Patient not found", "try": "123456789012"}
    
    return {
        "aadhaar": aadhaar,
        "name": patient["name"],
        "data_vaults": {
            "medical": {
                "status": "✅ Accessible to hospitals",
                "last_accessed": patient["medical_data"]["last_accessed"],
                "data_includes": ["Allergies", "Blood type", "Medical history"]
            },
            "government": {
                "status": "✅ Accessible to govt offices",
                "last_accessed": patient["govt_data"]["last_accessed"],
                "data_includes": ["PAN", "Voter ID", "Subsidy status"]
            },
            "financial": {
                "status": "🔒 No active access",
                "last_accessed": patient["financial_data"]["last_accessed"],
                "data_includes": ["Bank accounts", "Credit score", "Loan history"]
            }
        },
        "privacy_note": "Each vault is encrypted separately. Hospitals cannot access financial data."
    }


if __name__ == "__main__":
    import uvicorn
    print("✅ HealthChain Backend Ready!")
    print("🌐 Open: http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)
