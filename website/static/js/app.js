// =====================================================
// GET REFERENCES TO HTML ELEMENTS
// These allow JavaScript to interact with the webpage.
// =====================================================

// Run Code button
const runButton = document.getElementById("run-button");


const consoleOutput =
    document.getElementById("console-output");


const testResults =
    document.getElementById("test-results");


const score =
    document.getElementById("score");



runButton.addEventListener("click", async () => {


    const editor =
        window.lessonEditors[0];


    if (!editor) {

        console.error("Editor not ready.");

        return;

    }


    const code =
        editor.getValue();



    consoleOutput.textContent =
        "Running...";


    testResults.innerHTML =
        "";


    score.textContent =
        "Passed: 0/0 | Percentage: N/A";



    const response =
        await fetch("/run", {

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                code:code,

                problem_id:window.problem.id

            })

        });



    const data =
        await response.json();

    console.log(data);
    console.log(data.results);

    const consoleMessages = [];

    if (data.console) {

        consoleMessages.push(data.console);

    }

    if (data.error) {

        consoleMessages.push(`Error: ${data.error}`);

        const errorResult =
            document.createElement("div");

        errorResult.textContent =
            `Could not grade submission: ${data.error}`;

        errorResult.style.color =
            "red";

        testResults.appendChild(errorResult);

    }

    consoleOutput.textContent =
        consoleMessages.join("\n") || "No console output.";



    const results =
        Array.isArray(data.results)
            ? data.results
            : [];



    results.forEach(result => {


        const div =
            document.createElement("div");



        div.textContent =
            `Input=${result.input} | Expected=${result.expected} | Got=${result.actual}`;



        div.style.color =
            result.passed
                ? "green"
                : "red";



        testResults.appendChild(div);


    });



    score.textContent =
        `Passed: ${data.passed ?? 0}/${data.total ?? 0} | Percentage: ${data.percentage ?? "N/A"}`;



});
