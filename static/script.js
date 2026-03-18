let questions = [];
let current = 0;
let answers = [];

let time = 30;
let timerInterval;

async function startInterview() {
    try {
        let role = document.getElementById("role").value;
        let level = document.getElementById("level").value;
        let limit = document.getElementById("limit").value;

        const res = await fetch(`/questions?role=${role}&level=${level}&limit=${limit}`);
        questions = await res.json();

        if (!questions || questions.length === 0) {
            alert("No questions found!");
            return;
        }

        current = 0;
        answers = [];

        document.querySelector(".controls").style.display = "none";
        document.getElementById("quiz").classList.remove("hidden");

        showQuestion();

    } catch (err) {
        console.error("Start Error:", err);
        alert("Error starting interview");
    }
}

function showQuestion() {
    try {
        time = 30;
        startTimer();

        document.getElementById("progress").innerText =
            `Question ${current + 1} / ${questions.length}`;

        document.getElementById("question").innerText =
            questions[current].question;

    } catch (err) {
        console.error("Show Question Error:", err);
    }
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
    try {
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

    } catch (err) {
        console.error("Submit Error:", err);
    }
}

async function finishInterview() {
    try {
        document.getElementById("quiz").classList.add("hidden");

        let role = document.getElementById("role").value;

        const res = await fetch("/evaluate", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({answers: answers, role: role})
        });

        const data = await res.json();

        console.log("FULL RESPONSE:", data);

        document.getElementById("result").classList.remove("hidden");

        // ✅ SAFE SCORE
        document.getElementById("score").innerText =
            (data.average_score ? data.average_score : 0) + "%";

        // ✅ SAFE SUMMARY
        const summaryEl = document.getElementById("summary");
        if (summaryEl) {
            summaryEl.innerText =
                data.summary || "Performance summary not available.";
        }

        // ✅ SAFE FEEDBACK
        let fbHTML = "<h3>Feedback:</h3>";

        if (data.feedback && data.feedback.length > 0) {
            data.feedback.forEach(f => {
                fbHTML += `<p>• ${f}</p>`;
            });
        } else {
            fbHTML += "<p>No feedback available</p>";
        }

        document.getElementById("feedbackBox").innerHTML = fbHTML;

        // ✅ SAFE CHART (no crash)
        if (typeof renderChart === "function") {
            renderChart(data.average_score || 0);
        }

    } catch (err) {
        console.error("Finish Error:", err);
        alert("Something went wrong while finishing interview!");
    }
}
