(function () {
    // Both exercise pages load this file and describe their differing layout
    // through data attributes on the script tag.
    const script = document.currentScript;
    const progressOwner = script.dataset.progressOwner;
    const lockTarget = script.dataset.lockTarget;
    const wrapInMain = script.dataset.wrapMain === "true";

    // Lesson 0.5 currently uses two required quizzes. Keep this key and task
    // count aligned with the functions_preview lesson until gating moves to
    // server-side Supabase progress.
    const progressKey =
        `ucg:lesson-progress:${progressOwner}:functions_preview:1`;

    let progress = {};

    try {
        progress = JSON.parse(
            localStorage.getItem(progressKey) || "{}"
        );
    }
    catch (error) {
        console.warn("Could not read Lesson 0.5 progress:", error);
    }

    const unlocked =
        Array.isArray(progress.quizzes) &&
        progress.quizzes.length >= 2 &&
        progress.quizzes.every(Boolean);

    // The workspace bootstrap reads this before loading Monaco and app.js.
    window.exerciseAccessUnlocked = unlocked;

    if (unlocked) {
        return;
    }

    const target = document.querySelector(lockTarget);

    if (!target) {
        console.error("Exercise lock target was not found:", lockTarget);
        return;
    }

    // Keep one lock message for the exercise list and individual workspace.
    const lockContent = `
        <section class="page-header">
            <h1>Exercises Locked</h1>
            <p>Complete Lesson 0.5 to unlock coding exercises.</p>
        </section>

        <div class="content-card">
            <h2>Complete Lesson 0.5 to unlock</h2>
            <p>
                Lesson 0.5 explains how exercise functions work.
                Finish it first, then come back to start coding.
            </p>
            <a href="/lesson/functions_preview/1">
                <button>Go to Lesson 0.5 &rarr;</button>
            </a>
        </div>
    `;

    target.innerHTML = wrapInMain
        ? `<main class="main content-page">${lockContent}</main>`
        : lockContent;
})();
