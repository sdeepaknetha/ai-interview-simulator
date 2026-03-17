from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from app.questions import questions

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def calculate_score(user_answer, correct_answer):
    user_words = set(user_answer.lower().split())
    correct_words = set(correct_answer.lower().split())
    if len(correct_words) == 0:
        return 0
    return round(len(user_words & correct_words) / len(correct_words) * 100, 2)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/questions")
def get_questions():
    return [{"question": q["question"]} for q in questions]

@app.post("/evaluate")
async def evaluate(data: dict):
    total = 0
    results = []

    for i, ans in enumerate(data["answers"]):
        correct = questions[i]["answer"]
        score = calculate_score(ans, correct)
        total += score

        results.append({
            "question": questions[i]["question"],
            "your_answer": ans,
            "score": score
        })

    avg = round(total / len(data["answers"]), 2)

    return JSONResponse({
        "average_score": avg,
        "results": results
    })
