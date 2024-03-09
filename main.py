from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
from fastapi.middleware.cors import CORSMiddleware
import markdown

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust this to your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel('gemini-pro')

class Question(BaseModel):
    question: str

@app.post("/get_legal_advice")
def get_legal_advice(question: Question):
    response = model.generate_content(question.question)
    
    # Use markdown to format the response
    formatted_response = markdown.markdown(response.text)
    
    return {"legal_advice": formatted_response}
