let questions = [];
let current = 0;
let answers = [];
let timerInterval = null;
let timeLeft = 60; // 60 seconds per question

function startTimer() {
    clearInterval(timerInterval);
    timeLeft = 60;
    updateTimerDisplay();
    timerInterval = setInterval(() => {
        timeLeft--;
        updateTimerDisplay();
        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            alert("Time's up! Moving to next question.");
            submitAnswer();
        }
    }, 1000);
}

function updateTimerDisplay() {
    const timerEl = document.getElementById("timer");
    if (timerEl) {
        timerEl.innerText = `⏱ Time Left: ${timeLeft}s`;
        timerEl.style.color = timeLeft <= 10 ? "red" : "white";
    }
}

async function startInterview() {
    let role = document.getElementById("role").value;
    let level = document.getElementById("level").value;
    let limit = document.getElementById("limit").value;
    const res = await fetch(`/questions?role=${role}&level=${level}&limit=${limit}`);
    questions = await res.json();
    current = 0;
    answers = [];
    document.querySelector(".controls").style.display = "none";
    document.getElementById("quiz").classList.remove("hidden");
    showQuestion();
}

function showQuestion() {
    document.getElementById("progress").innerText =
        `Question ${current + 1} / ${questions.length}`;
    document.getElementById("question").innerText =
        questions[current].question;
    startTimer(); // ✅ Start timer for each question
}

function submitAnswer() {
    clearInterval(timerInterval); // ✅ Stop timer on submit
    let ans = document.getElementById("answer").value;
    if (!ans.trim()) {
        ans = "No answer provided";
    }
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
    clearInterval(timerInterval); // ✅ Stop timer
    document.getElementById("quiz").classList.add("hidden");
    let role = document.getElementById("role").value;
    const res = await fetch("/evaluate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answers: answers, role: role})
    });
    const data = await res.json();
    console.log("DATA:", data);
    document.getElementById("result").classList.remove("hidden");
    document.getElementById("score").innerText = data.average_score + "%";
    document.getElementById("summary").innerText = data.summary;
    let fbHTML = "<h3>Feedback:</h3>";
    data.feedback.forEach(f => {
        fbHTML += `<p>• ${f}</p>`;
    });
    document.getElementById("feedbackBox").innerHTML = fbHTML;
    try {
        renderChart(data.average_score);
    } catch (e) {
        console.log("Chart error:", e);
    }
}
