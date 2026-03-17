from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random

from app.questions import questions_data

app = FastAPI()

# Static + Templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/questions")
def get_questions(role: str, level: str, limit: int = Query(5)):
    data = questions_data.get(role, {}).get(level, [])
    random.shuffle(data)
    return data[:limit]


class AnswerModel(BaseModel):
    answers: list
    role: str


@app.post("/evaluate")
def evaluate(data: AnswerModel):
    scores = []
    feedback = []

    for ans in data.answers:
        length = len(ans.strip())

        if length > 80:
            score = random.randint(8, 10)
            fb = "Excellent answer with good depth."
        elif length > 40:
            score = random.randint(6, 8)
            fb = "Good answer but can be more structured."
        elif length > 15:
            score = random.randint(4, 6)
            fb = "Basic answer, try to improve explanation."
        else:
            score = random.randint(2, 4)
            fb = "Very short answer, needs improvement."

        scores.append(score)
        feedback.append(fb)

    avg = sum(scores) / len(scores)

    return {
        "average_score": round(avg * 10, 2),
        "feedback": feedback
    }
