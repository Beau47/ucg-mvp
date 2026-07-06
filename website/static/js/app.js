const runButton = document.getElementById("run-button");
let editor;
const consoleOutput = document.getElementById("console-output");
const testResults = document.getElementById("test-results");
const score = document.getElementById("score");


require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

require(["vs/editor/editor.main"], function () {

    editor = monaco.editor.create(
        document.getElementById("monaco-editor"),
        {
            value: window.problem.starter_code,

            language: "python",

            theme: "vs-dark",

            automaticLayout: true,

            fontSize: 16,

            fontFamily: "JetBrains Mono",

            minimap: {
                enabled: false
            }
        }
    );

});


runButton.addEventListener("click", async () => {
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
            problem_id: window.problem.id
        })
    });

    const data = await response.json();

    if (data.error) {
        consoleOutput.textContent = data.error;
        return;
    }

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
