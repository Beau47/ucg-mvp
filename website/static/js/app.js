const runButton = document.getElementById("run-button");
let editor;

const consoleOutput = document.getElementById("console-output");
const testResults = document.getElementById("test-results");
const score = document.getElementById("score");

// 🔥 TRACK CURRENT PROBLEM
let currentProblem = "add_one";

require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {

    editor = monaco.editor.create(
        document.getElementById("monaco-editor"),
        {
            value:
`def add_one(x):
    return x + 1`,

            language: "python",
            theme: "vs-dark",
            automaticLayout: true,
            fontSize: 16,
            fontFamily: "JetBrains Mono",
            minimap: { enabled: false }
        }
    );

});


// =========================
// LOAD PROBLEM FUNCTION
// =========================
async function loadProblem(problemId) {

    currentProblem = problemId;

    const response = await fetch(`/problem/${problemId}`);
    const data = await response.json();

    // 🔥 update editor with starter code
    editor.setValue(data.starter_code);

    // reset UI
    consoleOutput.textContent = "";
    testResults.innerHTML = "";
    score.textContent = "Passed: 0/0 | Percentage: N/A";

    // optional: update lesson title if exists
    const lessonTitle = document.querySelector(".lesson-card h2");
    if (lessonTitle) {
        lessonTitle.textContent =
            problemId === "add_one"
                ? "Add One"
                : "Square Number";
    }
}

// expose to HTML buttons
window.loadProblem = loadProblem;


// =========================
// RUN CODE BUTTON
// =========================
runButton.addEventListener("click", async () => {

    if (!editor) return;

    const code = editor.getValue();

    consoleOutput.textContent = "Running code...";
    testResults.innerHTML = "";
    score.textContent = "Passed: 0/0 | Percentage: N/A";

    const response = await fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code,
            problem_id: currentProblem
        })
    });

    const data = await response.json();

    consoleOutput.textContent = data.console;

    testResults.innerHTML = "";

    data.results.forEach(result => {
        const div = document.createElement("div");
        div.textContent =
            `Input=${result.input} | Expected=${result.expected} | Got=${result.actual}`;

        div.style.color = result.passed ? "green" : "red";

        testResults.appendChild(div);
    });

    score.textContent =
        `Passed: ${data.passed}/${data.total} | Percentage: ${data.percentage}`;
});
