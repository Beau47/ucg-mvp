require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});


window.lessonEditors = [];


require(["vs/editor/editor.main"], function () {

    document.querySelectorAll(".lesson-editor").forEach((element, index) => {

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
        CREATE RESIZE BAR
        Adds draggable divider between editor and output
        =====================================================
        */


        const lessonIDE =
            element.closest(".lesson-ide");


        if (!lessonIDE) {
            return;
        }



        const output =
            lessonIDE.querySelector(".ide-output");


        if (!output) {
            return;
        }



        const resizeBar =
            document.createElement("div");


        resizeBar.className =
            "ide-resize-bar";


        element.after(resizeBar);



        /*
        =====================================================
        LOAD SAVED EDITOR HEIGHT
        =====================================================
        */


        const savedHeight =
            localStorage.getItem(
                "ucg-lesson-editor-height"
            );


        if (savedHeight) {

            element.style.height =
                savedHeight + "px";

        }



        /*
        =====================================================
        DRAGGING LOGIC
        =====================================================
        */


        let dragging = false;



        resizeBar.addEventListener(
            "mousedown",
            () => {

                console.log("mousedown works");

                dragging = true;

                document.body.style.cursor =
                    "ns-resize";

            }
        );



        document.addEventListener(
            "mouseup",
            () => {

                dragging = false;

                document.body.style.cursor =
                    "default";

            }
        );



        document.addEventListener(
            "mousemove",
            (event) => {


                if (!dragging) {
                    return;
                }



                const rect =
                    lessonIDE.getBoundingClientRect();



                let newHeight =
                    event.clientY -
                    element.getBoundingClientRect().top;



                /*
                Minimum editor size
                */

                if (newHeight < 60) {

                    newHeight = 60;

                }



                /*
                Maximum editor size
                */

                if (newHeight > rect.height - 150) {

                    newHeight =
                        rect.height - 150;

                }



                element.style.height =
                    `${newHeight}px`;



                localStorage.setItem(
                    "ucg-lesson-editor-height",
                    newHeight
                );



                /*
                Tell Monaco the container changed
                */

                editor.layout();


            }
        );


    });


});