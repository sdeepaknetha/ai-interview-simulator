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
    strengths = 0
    weaknesses = 0

    # Role-based keywords
    role_keywords = {
        "python": ["function", "loop", "list", "dictionary", "class", "object"],
        "java": ["class", "object", "jvm", "inheritance", "polymorphism"],
        "data_analyst": ["sql", "data", "analysis", "query", "table", "join"],
        "hr": ["team", "challenge", "experience", "learn", "growth"]
    }

    keywords = role_keywords.get(data.role, [])

    for ans in data.answers:
        ans_lower = ans.lower()
        length = len(ans.strip())

        keyword_score = sum(1 for k in keywords if k in ans_lower)

        # Smart scoring logic
        if length > 80 and keyword_score >= 2:
            score = 9
            fb = "Strong answer with technical depth and clarity."
            strengths += 1
        elif length > 40 and keyword_score >= 1:
            score = 7
            fb = "Good answer but can be more structured and detailed."
            strengths += 1
        elif length > 15:
            score = 5
            fb = "Basic answer, lacks technical depth."
            weaknesses += 1
        else:
            score = 3
            fb = "Very short answer, needs improvement."
            weaknesses += 1

        scores.append(score)
        feedback.append(fb)

    avg = sum(scores) / len(scores)

    # Final AI-style summary
    if strengths > weaknesses:
        summary = "You performed well with strong conceptual understanding."
    elif weaknesses > strengths:
        summary = "You need improvement in explaining concepts clearly."
    else:
        summary = "Balanced performance, but there is room to improve."

    return {
        "average_score": round(avg * 10, 2),
        "feedback": feedback,
        "summary": summary
    }
