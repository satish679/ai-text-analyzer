# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ai_utils import analyze_sentiment, summarize_text
 
app = FastAPI()
 
# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
class TextRequest(BaseModel):
    text: str
 
@app.get("/")
def read_root():
    return {"message": "Hello from AI Text Analyzer Backend!"}
 
@app.post("/sentiment")
def sentiment_endpoint(request: TextRequest):
    result = analyze_sentiment(request.text)
    return {"sentiment": result}
 
@app.post("/summarize")
def summarize_endpoint(request: TextRequest):
    result = summarize_text(request.text)
    return {"summary": result}
 
