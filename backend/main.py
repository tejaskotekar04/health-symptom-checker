from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import SymptomRequest, AnalysisResponse
from groq_service import analyze_symptoms
from database import db
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load environment variables
load_dotenv()

# Lifespan handler (replaces on_event startup/shutdown)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to database on startup
    db.connect()
    print("Database connected on startup")

    yield  # FastAPI app runs here

    # Disconnect from database on shutdown
    db.disconnect()
    print("Database disconnected on shutdown")

# Initialize FastAPI app
app = FastAPI(
    title="Health Symptom Checker API",
    description="API for analyzing health symptoms and providing disease predictions",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint - API health check"""
    return {
        "message": "Health Symptom Checker API",
        "status": "active",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.post("/analyze-symptoms", response_model=AnalysisResponse)
async def analyze_symptoms_endpoint(request: SymptomRequest):
    """
    Analyze symptoms and return possible diseases with precautions
    Also saves the analysis to database
    
    Args:
        request: SymptomRequest containing symptoms, age, gender, duration
        
    Returns:
        AnalysisResponse with possible diseases and precautions
    """
    try:
        # Validate that symptoms are provided
        if not request.symptoms or request.symptoms.strip() == "":
            raise HTTPException(status_code=400, detail="Symptoms are required")
        
        # Call Groq service to analyze symptoms
        result = await analyze_symptoms(
            symptoms=request.symptoms,
            age=request.age,
            gender=request.gender,
            duration=request.duration
        )
        
        # Save analysis to database
        try:
            analysis_id = db.save_analysis(
                symptoms=request.symptoms,
                age=request.age,
                gender=request.gender,
                duration=request.duration,
                analysis_result=result.dict()
            )
            print(f"Analysis saved to database with ID: {analysis_id}")
        except Exception as db_error:
            print(f"Warning: Failed to save to database: {db_error}")
            # Continue even if database save fails
        
        return result
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)