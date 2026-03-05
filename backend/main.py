from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import UserProfile, TrainingPlan
from training_engine import TrainingEngine
import uvicorn

app = FastAPI(
    title="FitForge Pro API",
    description="Personalised training plan generator",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://fitforgepro.netlify.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = TrainingEngine()

@app.get("/")
async def root():
    return {"message": "FitForge Pro API is running", "status": "ok"}

@app.post("/generate-plan", response_model=TrainingPlan)
async def generate_plan(profile: UserProfile):
    try:
        plan = engine.generate(profile)
        return plan
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
