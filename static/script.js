let questions = [];
let current = 0;
let answers = [];

async function startInterview() {
    const res = await fetch("/questions");
    questions = await res.json();

    document.querySelector("button").style.display = "none";
    document.getElementById("quiz").classList.remove("hidden");

    showQuestion();
}

function showQuestion() {
    document.getElementById("question").innerText =
        `Question ${current + 1}: ${questions[current].question}`;
}

function submitAnswer() {
    let ans = document.getElementById("answer").value;
    answers.push(ans);
    document.getElementById("answer").value = "";

    current++;

    if (current < questions.length) {
        showQuestion();
    } else {
        finishInterview();
    }
}

async function finishInterview() {
    document.getElementById("quiz").classList.add("hidden");

    const res = await fetch("/evaluate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answers: answers})
    });

    const data = await res.json();

    document.getElementById("result").classList.remove("hidden");
    document.getElementById("score").innerText =
        data.average_score + "%";
}
