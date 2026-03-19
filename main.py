from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

class TextInput(BaseModel):
    text: str

# Get API key from environment
API_KEY = os.getenv("API_KEY")

@app.get("/")
def home():
    return {"message": "AI Research Summary API is running"}

@app.post("/summarize")
def summarize(data: TextInput):
    text = data.text

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "user", "content": f"Summarize this:\n{text}"}
            ]
        }
    )

    result = response.json()
    summary = result["choices"][0]["message"]["content"]

    return {"summary": summary}
