const runButton = document.getElementById("run-button");
const codeEditor = document.getElementById("code-editor");
const consoleOutput = document.getElementById("console-output");
const testResults = document.getElementById("test-results");
const score = document.getElementById("score");

runButton.addEventListener("click", async () => {
    const code = codeEditor.value;

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
            problem_id: "add_one"
        })
    });

    const data = await response.json();

    consoleOutput.textContent = data.console;

    testResults.innerHTML = "";

    data.results.forEach(result => {
        const div = document.createElement("div");
        div.textContent = `Input=${result.input} | Expected=${result.expected} | Got=${result.actual}`;

        if (result.passed) {
            div.style.color = "green";
        } else {
            div.style.color = "red";
        }

        testResults.appendChild(div);
    });

    score.textContent = `Passed: ${data.passed}/${data.total} | Percentage: ${data.percentage}`;
});
