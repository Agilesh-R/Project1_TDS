from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class QuestionRequest(BaseModel):
    question: str
    image: str = None  # optional base64 image

@app.post("/api/")
async def answer_question(request: QuestionRequest):
    # Extract the question and image (if any)
    question = request.question
    image_data = request.image  # You can decode if needed

    # TODO: Implement answer logic here using scraped data
    # For now, return a dummy response
    return {
        "answer": "This is a placeholder answer.",
        "links": [
            {
                "url": "https://discourse.onlinedegree.iitm.ac.in/example-post",
                "text": "Example link for context"
            }
        ]
    }
