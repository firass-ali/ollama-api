from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import Response
import ollama

app = FastAPI()

@app.get('/')
def home():
    return "Hello world"

@app.post("/chat")
async def chat(query: str):
    if not query:
        return {"error": "Message cannot be empty."}

    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": query}])
    return {"response": response['message']['content']}