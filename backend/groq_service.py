from groq import Groq
import os
import json
from models import AnalysisResponse, Disease
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables. Please check your .env file.")
    
client = Groq(api_key=api_key)

async def analyze_symptoms(
    symptoms: str,
    age: Optional[int] = None,
    gender: Optional[str] = None,
    duration: Optional[str] = None
) -> AnalysisResponse:
    """
    Analyze symptoms using Groq API and return structured response
    
    Args:
        symptoms: Description of symptoms
        age: Patient's age (optional)
        gender: Patient's gender (optional)
        duration: Duration of symptoms (optional)
        
    Returns:
        AnalysisResponse with disease predictions and precautions
    """
    
    # Build the prompt for Groq
    prompt = f"""You are a medical symptom analysis assistant. Analyze the following symptoms and provide a structured response.

Symptoms: {symptoms}
{f"Age: {age}" if age else ""}
{f"Gender: {gender}" if gender else ""}
{f"Duration: {duration}" if duration else ""}

Provide your response in the following JSON format ONLY (no additional text, no markdown formatting):
{{
  "possible_diseases": [
    {{
      "name": "disease name",
      "likelihood": "high/medium/low",
      "description": "brief description of the condition"
    }}
  ],
  "precautions": [
    "precaution 1",
    "precaution 2",
    "precaution 3"
  ],
  "when_to_seek_help": "description of when to seek immediate medical attention",
  "disclaimer": "This is not a medical diagnosis. Please consult a healthcare professional for proper evaluation."
}}

Important:
- Provide 2-4 possible diseases ranked by likelihood
- Each disease should have a clear description
- Provide 4-6 practical precautions
- Be clear about when to seek immediate medical help
- Always include the disclaimer"""

    try:
        # Call Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful medical assistant that analyzes symptoms and provides structured health information. Always respond with valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.3-70b-versatile",  # Using Llama 3.3 70B for better medical reasoning
            temperature=0.3,  # Lower temperature for more consistent, factual responses
            max_tokens=2000,
        )
        
        # Extract response
        response_text = chat_completion.choices[0].message.content.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        response_text = response_text.strip()
        
        # Parse JSON response
        parsed_response = json.loads(response_text)
        
        # Convert to Pydantic models
        diseases = [Disease(**disease) for disease in parsed_response["possible_diseases"]]
        
        return AnalysisResponse(
            possible_diseases=diseases,
            precautions=parsed_response["precautions"],
            when_to_seek_help=parsed_response["when_to_seek_help"],
            disclaimer=parsed_response["disclaimer"]
        )
        
    except json.JSONDecodeError as e:
        # If JSON parsing fails, return a default error response
        return AnalysisResponse(
            possible_diseases=[
                Disease(
                    name="Unable to analyze",
                    likelihood="unknown",
                    description="The system encountered an error analyzing your symptoms."
                )
            ],
            precautions=[
                "Please consult a healthcare professional",
                "Monitor your symptoms closely",
                "Seek immediate help if symptoms worsen"
            ],
            when_to_seek_help="Seek immediate medical attention if you experience severe symptoms",
            disclaimer="This is not a medical diagnosis. Please consult a healthcare professional."
        )
    except Exception as e:
        raise Exception(f"Error calling Groq API: {str(e)}")