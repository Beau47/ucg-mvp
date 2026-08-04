(function () {
    // The template supplies page identity through data attributes so this
    // controller can be reused by every lesson without inline JavaScript.
    const configScript = document.currentScript;

    document.addEventListener("DOMContentLoaded", function () {
        const lessonId = configScript.dataset.lessonId;
        const page = Number(configScript.dataset.page);
        const totalPages = Number(configScript.dataset.totalPages);
        const progressOwner = configScript.dataset.progressOwner;

        const quizzes =
            document.querySelectorAll(".quiz-card[data-required='true']");
        const ides = document.querySelectorAll(".lesson-ide");
        const nextButton = document.getElementById("next-button");
        const nextLink = document.getElementById("next-link");
        // Browser state restores the exact page UI. The API calls below remain
        // the source of truth for account progress and XP in Supabase.
        const progressKey =
            `ucg:lesson-progress:${progressOwner}:${lessonId}:${page}`;
        const isFinalPage = page === totalPages;

        let pageCompletionRequestSent = false;
        let completionRequestSent = false;
        let savedProgress = {};

        try {
            savedProgress = JSON.parse(
                localStorage.getItem(progressKey) || "{}"
            );
        }
        catch (error) {
            console.warn("Could not read lesson progress:", error);
        }

        const quizProgress =
            savedProgress.quizzes || Array(quizzes.length).fill(false);
        const ideProgress =
            savedProgress.ides || Array(ides.length).fill(false);

        let completedQuizzes = quizProgress.filter(Boolean).length;
        let completedIDEs = ideProgress.filter(Boolean).length;

        function saveProgress() {
            localStorage.setItem(
                progressKey,
                JSON.stringify({
                    quizzes: quizProgress,
                    ides: ideProgress
                })
            );
        }

        // Page completion is stored as a normal lesson task so sub-lessons
        // such as 1.1 and 3.2 can unlock their own exercise groups.
        async function savePageCompletion() {
            if (
                progressOwner === "guest" ||
                pageCompletionRequestSent
            ) {
                return;
            }

            pageCompletionRequestSent = true;

            try {
                const response = await fetch("/complete_task", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        lesson_id: lessonId,
                        task_id: `page-complete-${page}`
                    })
                });

                if (!response.ok) {
                    pageCompletionRequestSent = false;
                }
            }
            catch (error) {
                console.error("Could not save page completion:", error);
                pageCompletionRequestSent = false;
            }
        }

        // A lesson is recorded only after the required tasks on its final page
        // are complete. The guard prevents duplicate requests and XP effects.
        async function saveLessonCompletion() {
            if (
                !isFinalPage ||
                progressOwner === "guest" ||
                completionRequestSent
            ) {
                return;
            }

            completionRequestSent = true;

            try {
                const response = await fetch(
                    `/lesson/${lessonId}/complete`,
                    { method: "POST" }
                );
                const data = await response.json();

                if (!response.ok) {
                    completionRequestSent = false;
                    return;
                }

                if (
                    data.newly_completed &&
                    typeof window.celebrateXP === "function"
                ) {
                    window.celebrateXP(100);
                }
            }
            catch (error) {
                console.error("Could not save lesson completion:", error);
                completionRequestSent = false;
            }
        }

        // Navigation stays locked until every required quiz and IDE on this
        // page is complete. Pages without tasks remain immediately navigable.
        function checkRequirements() {
            const quizzesComplete =
                completedQuizzes === quizzes.length;
            const idesComplete = completedIDEs === ides.length;

            if (!quizzesComplete || !idesComplete) {
                return;
            }

            savePageCompletion();
            saveLessonCompletion();

            if (nextButton && nextLink) {
                nextButton.disabled = false;
                nextLink.style.pointerEvents = "auto";
                nextLink.style.opacity = "1";
            }
        }

        if (
            nextButton &&
            nextLink &&
            (quizzes.length > 0 || ides.length > 0)
        ) {
            nextButton.disabled = true;
            nextLink.style.pointerEvents = "none";
            nextLink.style.opacity = "0.5";
        }

        // Rebuild completed controls before attaching interaction handlers.
        quizzes.forEach(function (quiz, quizIndex) {
            if (!quizProgress[quizIndex]) {
                return;
            }

            quiz.dataset.completed = "true";
            quiz.querySelector(".quiz-feedback").textContent = "Correct!";

            quiz.querySelectorAll(".quiz-option").forEach(function (button) {
                if (button.dataset.answer === button.dataset.correct) {
                    button.style.backgroundColor = "#2ecc71";
                    button.style.color = "white";
                }

                button.disabled = true;
            });
        });

        ides.forEach(function (ide, ideIndex) {
            if (!ideProgress[ideIndex]) {
                return;
            }

            ide.dataset.completed = "true";
            ide.querySelector(".ide-output").textContent =
                "Completed previously. You can run it again if you want.";
        });

        checkRequirements();

        // Quiz attempts are retryable until correct; only correct answers are
        // persisted and sent to the account-progress endpoint.
        quizzes.forEach(function (quiz, quizIndex) {
            const feedback = quiz.querySelector(".quiz-feedback");

            quiz.querySelectorAll(".quiz-option").forEach(function (button) {
                button.addEventListener("click", async function () {
                    if (quiz.dataset.completed === "true") {
                        return;
                    }

                    quiz.querySelectorAll(".quiz-option").forEach(
                        function (option) {
                            option.style.backgroundColor = "";
                            option.style.color = "";
                        }
                    );

                    if (button.dataset.answer !== button.dataset.correct) {
                        button.style.backgroundColor = "#e74c3c";
                        button.style.color = "white";
                        feedback.textContent =
                            "\u274c Incorrect. Try again!";
                        return;
                    }

                    button.style.backgroundColor = "#2ecc71";
                    button.style.color = "white";
                    feedback.textContent = "\u2705 Correct!";
                    quiz.dataset.completed = "true";

                    try {
                        await fetch("/complete_task", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                lesson_id: lessonId,
                                task_id: quiz.dataset.taskId
                            })
                        });
                    }
                    catch (error) {
                        console.error("Could not save quiz completion:", error);
                    }

                    quizProgress[quizIndex] = true;
                    saveProgress();
                    completedQuizzes += 1;

                    quiz.querySelectorAll(".quiz-option").forEach(
                        function (option) {
                            option.disabled = true;
                        }
                    );

                    checkRequirements();
                });
            });
        });

        // Running an IDE once completes its page requirement. The editor value
        // comes from the Monaco instances created by lesson.js.
        document.querySelectorAll(".ide-run").forEach(
            function (button, ideIndex) {
                button.addEventListener("click", async function () {
                    const ide = button.closest(".lesson-ide");
                    const index = Array.from(
                        document.querySelectorAll(".lesson-ide")
                    ).indexOf(ide);
                    const editor = window.lessonEditors[index];
                    const output = ide.querySelector(".ide-output");

                    if (!editor) {
                        output.textContent = "Editor is still loading.";
                        return;
                    }

                    output.textContent = "Running...";

                    try {
                        const response = await fetch("/run_snippet", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                code: editor.getValue()
                            })
                        });
                        const data = await response.json();
                        output.textContent = data.output;
                    }
                    catch (error) {
                        output.textContent = "Could not run this code.";
                        console.error("Could not run lesson code:", error);
                        return;
                    }

                    if (ide.dataset.completed === "true") {
                        return;
                    }

                    ide.dataset.completed = "true";

                    try {
                        await fetch("/complete_task", {
                            method: "POST",
                            headers: {
                                "Content-Type": "application/json"
                            },
                            body: JSON.stringify({
                                lesson_id: lessonId,
                                task_id: ide.dataset.taskId
                            })
                        });
                    }
                    catch (error) {
                        console.error("Could not save IDE completion:", error);
                    }

                    ideProgress[ideIndex] = true;
                    saveProgress();
                    completedIDEs += 1;
                    checkRequirements();
                });
            }
        );
    });
})();
