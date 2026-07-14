require.config({
    paths: {
        vs: "https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.52.2/min/vs"
    }
});


window.lessonEditors = [];


require(["vs/editor/editor.main"], function () {

    document.querySelectorAll(".lesson-editor").forEach((element) => {

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

    });

});