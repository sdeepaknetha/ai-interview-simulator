from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.questions import questions
from reportlab.pdfgen import canvas

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Smart scoring function
def calculate_score(user_answer, correct_answer):
    user_words = set(user_answer.lower().split())
    correct_words = set(correct_answer.lower().split())

    if len(correct_words) == 0:
        return 0

    score = len(user_words & correct_words) / len(correct_words)
    return round(score * 100, 2)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/evaluate")
async def evaluate(data: dict):
    results = []
    total_score = 0

    for i, ans in enumerate(data["answers"]):
        correct = questions[i]["answer"]
        score = calculate_score(ans, correct)
        total_score += score

        results.append({
            "question": questions[i]["question"],
            "your_answer": ans,
            "score": score
        })

    avg_score = round(total_score / len(data["answers"]), 2)

    return JSONResponse({
        "results": results,
        "average_score": avg_score
    })
