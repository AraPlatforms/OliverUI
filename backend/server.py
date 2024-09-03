from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
from oliver import WebpageCritique  # Assuming your class is in oliver.py
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

webpage_critic = WebpageCritique(llm_model='gpt-4o')

class CritiqueRequest(BaseModel):
    url: str
    description: str

class CritiqueResponse(BaseModel):
    critique: Dict
    markdown_report: str

@app.post("/api/critique", response_model=CritiqueResponse)
async def critique_webpage(request: CritiqueRequest):
    try:        
        critique = webpage_critic.critique_webpage(request.url, request.description)        
        markdown_report = webpage_critic.generate_markdown_report(critique)
        
        return CritiqueResponse(
            critique=critique, 
            markdown_report=markdown_report
        )
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
