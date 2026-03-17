let questions = [];
let current = 0;
let answers = [];

async function startInterview() {
    let role = document.getElementById("role").value;
    let level = document.getElementById("level").value;
    let limit = document.getElementById("limit").value;

    const res = await fetch(`/questions?role=${role}&level=${level}&limit=${limit}`);
    questions = await res.json();

    document.querySelector(".controls").style.display = "none";
    document.getElementById("quiz").classList.remove("hidden");

    showQuestion();
}

function showQuestion() {
    document.getElementById("progress").innerText =
        `Question ${current + 1} / ${questions.length}`;

    document.getElementById("question").innerText =
        questions[current].question;
}

function submitAnswer() {
    let ans = document.getElementById("answer").value;

    if (!ans.trim()) {
        alert("Enter answer!");
        return;
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
    document.getElementById("quiz").classList.add("hidden");

    let role = document.getElementById("role").value;

    const res = await fetch("/evaluate", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({answers: answers, role: role})
    });

    const data = await res.json();

    document.getElementById("result").classList.remove("hidden");
    document.getElementById("score").innerText = data.average_score + "%";

    let fbHTML = "<h3>Feedback:</h3>";
    data.feedback.forEach(f => {
        fbHTML += `<p>• ${f}</p>`;
    });

    document.getElementById("feedbackBox").innerHTML = fbHTML;
}
