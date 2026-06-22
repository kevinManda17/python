from fastapi import FastAPI
from pydantic import BaseModel
from app.model import load_model, generate_response

app = FastAPI()

model, tokenizer = load_model()

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    response = generate_response(req.message, model, tokenizer)
    return {"response": response}
