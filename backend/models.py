from pydantic import BaseModel, Field
from typing import Optional, List

class SymptomRequest(BaseModel):
    """Request model for symptom analysis"""
    symptoms: str = Field(..., description="Description of symptoms", min_length=1)
    age: Optional[int] = Field(None, description="Patient's age", ge=0, le=120)
    gender: Optional[str] = Field(None, description="Patient's gender")
    duration: Optional[str] = Field(None, description="Duration of symptoms")
    
    class Config:
        json_schema_extra = {
            "example": {
                "symptoms": "headache, fever, cough",
                "age": 25,
                "gender": "male",
                "duration": "3 days"
            }
        }

class Disease(BaseModel):
    """Model for a single disease prediction"""
    name: str = Field(..., description="Name of the disease")
    likelihood: str = Field(..., description="Likelihood: high, medium, or low")
    description: str = Field(..., description="Brief description of the condition")
    
class AnalysisResponse(BaseModel):
    """Response model for symptom analysis"""
    possible_diseases: List[Disease] = Field(..., description="List of possible diseases")
    precautions: List[str] = Field(..., description="Recommended precautions")
    when_to_seek_help: str = Field(..., description="When to seek immediate medical attention")
    disclaimer: str = Field(..., description="Medical disclaimer")
    
    class Config:
        json_schema_extra = {
            "example": {
                "possible_diseases": [
                    {
                        "name": "Common Cold",
                        "likelihood": "high",
                        "description": "A viral infection of the upper respiratory tract"
                    }
                ],
                "precautions": [
                    "Get plenty of rest",
                    "Stay hydrated",
                    "Take over-the-counter pain relievers if needed"
                ],
                "when_to_seek_help": "Seek immediate help if symptoms worsen or persist beyond 10 days",
                "disclaimer": "This is not a medical diagnosis. Please consult a healthcare professional."
            }
        }