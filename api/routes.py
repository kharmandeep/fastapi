from fastapi import APIRouter
from pydantic import BaseModel
from openai_client.client import get_openai_response

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

@router.post("/generate")
def generate(request: QuestionRequest):
    answer = get_openai_response(request.question)
    return {"question": request.question, "answer": answer}