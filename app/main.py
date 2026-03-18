from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import random

from app.questions import questions_data

app = FastAPI()

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
            score = 9
            fb = "Strong answer with good explanation."
        elif length > 40:
            score = 7
            fb = "Good answer but needs more detail."
        elif length > 15:
            score = 5
            fb = "Basic answer."
        else:
            score = 3
            fb = "Very short answer."

        scores.append(score)
        feedback.append(fb)

    avg = (sum(scores) / len(scores)) * 10

    # ✅ ALWAYS RETURN SUMMARY
    summary = "You need improvement."
    if avg >= 70:
        summary = "Excellent performance!"
    elif avg >= 50:
        summary = "Good, but can improve."
    else:
        summary = "Needs more practice."

    return {
        "average_score": round(avg, 2),
        "feedback": feedback,
        "summary": summary
    }
