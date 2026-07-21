require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});

window.lessonEditors = [];

require(["vs/editor/editor.main"], function () {

    console.log("lesson.js loaded");

    const editors =
        document.querySelectorAll(".lesson-editor");

    console.log("Editors found:", editors.length);

    editors.forEach((element, index) => {

        const editor = monaco.editor.create(element, {
            value: element.dataset.code || "",
            language: "python",
            theme: "vs-dark",
            automaticLayout: true,
            minimap: {
                enabled: false
            },
            fontSize: 14,
            lineNumbers: "on",
            scrollBeyondLastLine: false,
            wordWrap: "on",
            padding: {
                top: 10
            }
        });

        window.lessonEditors.push(editor);

        setTimeout(() => {
            editor.layout();
        }, 100);

        /*
        =====================================================
        FIND THE CORRECT CONTAINER
        =====================================================
        */

        const lessonIDE =
            element.closest(".lesson-ide");

        const editorContainer =
            element.closest(".editor-container");

        let resizeContainer;
        let output;

        /*
        Lesson page
        */

        if (lessonIDE) {

            resizeContainer = lessonIDE;

            output =
                lessonIDE.querySelector(".ide-output");

        }

        /*
        Exercise page
        */

        else if (editorContainer) {

            resizeContainer = document.querySelector(".main");

            output =
                document.querySelector(".output");

        }

        else {

            console.log("No resize container found.");

            return;

        }

        if (!output) {

            console.log("No output panel found.");

            return;

        }

        /*
        =====================================================
        CREATE RESIZE BAR
        =====================================================
        */

        let resizeBar =
            lessonIDE.querySelector(".ide-resize-bar");


        if (!resizeBar) {

            resizeBar =
                document.createElement("div");

            resizeBar.className =
                "ide-resize-bar";

            element.after(resizeBar);

            console.log("Resize bar created.");

        }

        else {

            console.log("Existing resize bar found.");

        }

        /*
        =====================================================
        DRAGGING
        =====================================================
        */

        let dragging = false;

        resizeBar.addEventListener("mousedown", function (e) {

            e.preventDefault();

            dragging = true;

            document.body.style.cursor = "ns-resize";

            console.log("Dragging started.");

        });

        document.addEventListener("mouseup", function () {

            if (!dragging) {
                return;
            }

            dragging = false;

            document.body.style.cursor = "default";

            console.log("Dragging stopped.");

        });

        document.addEventListener("mousemove", function (event) {

            if (!dragging) {
                return;
            }

            const rect =
                resizeContainer.getBoundingClientRect();

            const top =
                element.getBoundingClientRect().top;

            let newHeight =
                event.clientY - top;

            if (newHeight < 60) {
                newHeight = 60;
            }

            if (newHeight > rect.height - 150) {
                newHeight = rect.height - 150;
            }

            element.style.height =
                newHeight + "px";

            editor.layout();

        });



        // ==========================================
        // CONSOLE OUTPUT ↔ TEST RESULTS RESIZE
        // ==========================================

        const outputTestBar =
            lessonIDE.querySelector(".output-test-resize-bar");


        const consoleOutput =
            lessonIDE.querySelector("#console-output");


        const testResults =
            lessonIDE.querySelector("#test-results");


        if (outputTestBar && consoleOutput) {

            console.log("Output resize bar found");

            let resizingOutput = false;


            outputTestBar.addEventListener(
                "mousedown",
                function(e) {

                    e.preventDefault();

                    resizingOutput = true;

                    document.body.style.cursor =
                        "ns-resize";

                }
            );


            document.addEventListener(
                "mouseup",
                function() {

                    resizingOutput = false;

                    document.body.style.cursor =
                        "default";

                }
            );


            document.addEventListener(
                "mousemove",
                function(e) {

                    if (!resizingOutput) {
                        return;
                    }


                    const rect =
                        lessonIDE.getBoundingClientRect();


                    let newHeight =
                        e.clientY -
                        consoleOutput.getBoundingClientRect().top;


                    if (newHeight < 50) {
                        newHeight = 50;
                    }


                    if (newHeight > rect.height - 200) {
                        newHeight = rect.height - 200;
                    }


                    consoleOutput.style.flex =
                        "0 0 " + newHeight + "px";

                }
            );

        }


    });

});
