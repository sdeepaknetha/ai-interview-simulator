from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from sentence_transformers import SentenceTransformer, util
from reportlab.pdfgen import canvas

from app.emotion import start_emotion_detection, stop_emotion_detection, get_emotion_score

app = FastAPI()

templates = Jinja2Templates(directory="templates")

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

results = []

question_bank = {

"python":[
{"question":"Explain generators in Python",
"answer":"Generators are functions that yield values using the yield keyword and generate values lazily."},

{"question":"What is list comprehension",
"answer":"List comprehension is a concise way to create lists using a single line expression."},

{"question":"What is dictionary",
"answer":"Dictionary is a data structure storing key value pairs."},

{"question":"What is exception handling",
"answer":"Exception handling manages runtime errors using try except blocks."},

{"question":"What is a module",
"answer":"A module is a python file containing functions variables and classes."}
],

"java":[
{"question":"What is JVM",
"answer":"Java Virtual Machine executes Java bytecode and enables platform independence."},

{"question":"What is OOP",
"answer":"Object oriented programming uses objects classes inheritance encapsulation and polymorphism."},

{"question":"What is inheritance",
"answer":"Inheritance allows one class to acquire properties of another class."},

{"question":"What is encapsulation",
"answer":"Encapsulation hides data using private variables and public methods."},

{"question":"What is polymorphism",
"answer":"Polymorphism allows methods to behave differently depending on the object."}
],

"data":[
{"question":"What is data analysis",
"answer":"Data analysis is inspecting transforming and modeling data to discover useful information."},

{"question":"What is SQL",
"answer":"SQL is a language used for querying relational databases."},

{"question":"What is data visualization",
"answer":"Data visualization represents data using graphs charts and dashboards."},

{"question":"What is dataset",
"answer":"Dataset is a structured collection of related data."},

{"question":"What is primary key",
"answer":"Primary key uniquely identifies each record in a table."}
],

"hr":[
{"question":"Tell me about yourself",
"answer":"Provide a short introduction about education skills and career goals."},

{"question":"Why should we hire you",
"answer":"Explain your strengths skills and ability to contribute to the company."},

{"question":"What are your strengths",
"answer":"Mention strengths such as problem solving communication and teamwork."},

{"question":"What are your weaknesses",
"answer":"Mention a weakness and explain how you are improving it."},

{"question":"Where do you see yourself in five years",
"answer":"Explain your career growth goals and professional development."}
]

}


@app.get("/",response_class=HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/get_question/")
async def get_question(interview_type:str=Form(...),q_index:int=Form(...)):

    questions = question_bank.get(interview_type,[])

    if q_index>=len(questions):
        return {"question":"Interview Completed"}

    return {"question":questions[q_index]["question"]}


@app.post("/submit_answer/")
async def submit_answer(interview_type:str=Form(...),q_index:int=Form(...),user_answer:str=Form(...)):

    correct = question_bank[interview_type][q_index]["answer"]

    emb1 = model.encode(user_answer,convert_to_tensor=True)
    emb2 = model.encode(correct,convert_to_tensor=True)

    similarity = util.cos_sim(emb1,emb2).item()

    score = int(similarity*100)

    if score<0:
        score=0
    if score>100:
        score=100

    if len(user_answer.strip())<5:
        score=0

    if score<60:
        suggestion="Try explaining more clearly."
    else:
        suggestion="Good answer."

    results.append(score)

    return {"score":score,"suggestion":suggestion}


@app.get("/start_emotion")
async def start_emotion():

    start_emotion_detection()

    return {"message":"Emotion detection started"}


@app.get("/stop_emotion")
async def stop_emotion():

    stop_emotion_detection()

    return {"message":"Emotion detection stopped"}


@app.get("/report")
async def report():

    stop_emotion_detection()

    emotion_score = get_emotion_score()

    avg = sum(results)/len(results)

    if avg>=80:
        performance="Excellent"
    elif avg>=60:
        performance="Good"
    else:
        performance="Needs Improvement"

    feedback = ""

    if avg>=70:
        feedback="You demonstrated good understanding of the concepts. Try adding more real world examples."
    else:
        feedback="You should practice explaining concepts clearly with structured answers."

    file_path="interview_report.pdf"

    c = canvas.Canvas(file_path)

    c.drawString(100,750,"AI Interview Report")

    c.drawString(100,720,f"Questions Attempted: {len(results)}")

    c.drawString(100,700,f"Average Score: {round(avg,2)}")

    c.drawString(100,680,f"Emotion Confidence Score: {emotion_score} / 100")

    c.drawString(100,660,f"Performance: {performance}")

    c.drawString(100,630,"AI Feedback:")

    c.drawString(100,610,feedback)

    c.save()

    return FileResponse(file_path,media_type="application/pdf",filename="Interview_Report.pdf")