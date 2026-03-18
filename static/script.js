let questions = [];
let current = 0;
let answers = [];

let time = 30;
let timerInterval;

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
    time = 30;
    startTimer();

    document.getElementById("progress").innerText =
        `Question ${current + 1} / ${questions.length}`;

    document.getElementById("question").innerText =
        questions[current].question;
}

function startTimer() {
    clearInterval(timerInterval);

    timerInterval = setInterval(() => {
        time--;
        document.getElementById("timer").innerText = "⏳ " + time;

        if (time === 0) {
            clearInterval(timerInterval);
            submitAnswer(true);
        }
    }, 1000);
}

function submitAnswer(auto = false) {
    clearInterval(timerInterval);

    let ans = document.getElementById("answer").value;

    if (!auto && !ans.trim()) {
        alert("Enter answer!");
        return;
    }

    answers.push(ans || "No Answer");
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

    let role = document.getElementById("role").value;

    const res = await fetch("/evaluate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answers: answers, role: role})
    });

    const data = await res.json();

    console.log("FULL RESPONSE:", data); // 🔥 DEBUG

    document.getElementById("result").classList.remove("hidden");

    document.getElementById("score").innerText = data.average_score + "%";

    renderChart(data.average_score);

    // ✅ FORCE SUMMARY DISPLAY
    const summaryEl = document.getElementById("summary");

    if (summaryEl) {
        summaryEl.innerText = data.summary ? data.summary : "No summary available";
    } else {
        console.error("SUMMARY ELEMENT NOT FOUND");
    }

    let fbHTML = "<h3>Feedback:</h3>";
    data.feedback.forEach(f => {
        fbHTML += `<p>• ${f}</p>`;
    });

    document.getElementById("feedbackBox").innerHTML = fbHTML;
}
