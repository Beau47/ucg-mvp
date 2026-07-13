// =====================================================
// GET REFERENCES TO HTML ELEMENTS
// These allow JavaScript to interact with the webpage.
// =====================================================

// Run Code button
const runButton = document.getElementById("run-button");

// Monaco editor instance (created later)
let editor;

// Output panel elements
const consoleOutput = document.getElementById("console-output");
const testResults = document.getElementById("test-results");
const score = document.getElementById("score");

// =====================================================
// TRACK WHICH PROBLEM IS CURRENTLY LOADED
// This is sent to the backend when the user clicks Run.
// =====================================================
let currentProblem = "add_one";

// =====================================================
// CONFIGURE MONACO EDITOR
// Tells RequireJS where to download the Monaco files.
// =====================================================
require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

// =====================================================
// CREATE THE MONACO EDITOR
// Runs once Monaco has finished loading.
// =====================================================
require(["vs/editor/editor.main"], function () {

    editor = monaco.editor.create(
        document.getElementById("monaco-editor"),
        {

            // Initial code shown when the page loads
            value: window.problem.starter_code,

            // Editor settings
            language: "python",
            theme: "vs-dark",
            automaticLayout: true,
            fontSize: 15,
            fontFamily: "Consolas, Menlo, Monaco, 'Courier New', monospace",
            fontLigatures: false,
            minimap: { enabled: false }
        }
    );

});


// =====================================================
// LOAD A NEW PROBLEM
// Called whenever the user clicks a problem button.
// =====================================================
async function loadProblem(problemId) {

    // Remember which problem is currently active
    currentProblem = problemId;

    // Ask the Flask backend for the problem data
    const response = await fetch(`/problem/${problemId}`);
    const data = await response.json();

    // Load the starter code into Monaco
    editor.setValue(data.starter_code);

    // Clear previous console output and test results
    consoleOutput.textContent = "";
    testResults.innerHTML = "";
    score.textContent = "Passed: 0/0 | Percentage: N/A";

    // Update the lesson title shown in the sidebar
    const lessonTitle = document.querySelector(".lesson-card h2");

    if (lessonTitle) {
        lessonTitle.textContent =
            problemId === "add_one"
                ? "Add One"
                : "Square Number";
    }
}

// Make this function accessible from the HTML buttons
window.loadProblem = loadProblem;


// =====================================================
// RUN CODE BUTTON
// Sends the student's code to Flask for execution.
// =====================================================
runButton.addEventListener("click", async () => {

    // Do nothing if the editor hasn't finished loading
    if (!editor) return;

    // Get the code currently written in the editor
    const code = editor.getValue();

    // Reset the output panel while waiting
    consoleOutput.textContent = "Running code...";
    testResults.innerHTML = "";
    score.textContent = "Passed: 0/0 | Percentage: N/A";

    // Send the student's code and current problem ID
    // to the backend using a POST request
    const response = await fetch("/run", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            code: code,
            problem_id: window.problem.id
        })
    });

    // Receive the grading results
    const data = await response.json();

    if (data.error) {
        consoleOutput.textContent = data.error;
        return;
    }

    // Display anything the student's program printed
    consoleOutput.textContent = data.console;

    // Clear old test results
    testResults.innerHTML = "";

    // Display each individual test case
    data.results.forEach(result => {

        const div = document.createElement("div");

        div.textContent =
            `Input=${result.input} | Expected=${result.expected} | Got=${result.actual}`;

        // Green if passed, red if failed
        div.style.color = result.passed ? "green" : "red";

        // Add the test result to the output panel
        testResults.appendChild(div);

    });

    // Display the overall score
    score.textContent =
        `Passed: ${data.passed}/${data.total} | Percentage: ${data.percentage}`;

});
