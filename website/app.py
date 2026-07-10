# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify
from problems import get_problem, PROBLEMS
from runner import run_problem, run_snippet

# Lesson loader
from lessons import get_lesson, LESSONS


# =====================================================
# CREATE THE FLASK APPLICATION
# =====================================================

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("dashboard.html")


# =====================================================
# LESSONS PAGE
# Displays the lessons page.
# =====================================================

@app.route("/lessons")
def lessons():

    return render_template(
        "lessons.html",
        lessons=LESSONS
    )


# =====================================================
# INDIVIDUAL LESSON PAGE
# Displays a specific lesson.
# =====================================================

@app.route("/lesson/<lesson_id>/<int:page>")
def lesson(lesson_id, page):

    lesson = get_lesson(lesson_id)

    if lesson is None:
        return "Lesson not found.", 404

    # Find the total number of pages in this lesson
    total_pages = max(
        block["page"] for block in lesson["blocks"]
    )

    return render_template(
        "lesson.html",
        lesson=lesson,
        page=page,
        total_pages=total_pages
    )


# =====================================================
# EXERCISES PAGE
# Displays the exercises page.
# =====================================================

@app.route("/exercises")
def exercises():

    return render_template(
        "exercises.html",
        problems=PROBLEMS
    )


# =====================================================
# WORKSPACE PAGE
# Loads a specific coding problem into the workspace.
# =====================================================

@app.route("/workspace/<problem_id>")
def workspace(problem_id):

    problem = get_problem(problem_id)

    if problem is None:
        return "Problem not found.", 404

    return render_template(
        "index.html",
        problem=problem
    )


@app.route("/profile")
def profile():
    return "Profile page coming soon."


# =====================================================
# LIST PROBLEMS
# Sends summary data for all available problems.
# =====================================================

@app.route("/problems")
def problems_api():

    problem_summaries = []

    for problem in PROBLEMS.values():
        problem_summaries.append({
            "id": problem["id"],
            "lesson_number": problem["lesson_number"],
            "title": problem["title"],
            "description": problem["description"],
        })

    return jsonify(problem_summaries)


# =====================================================
# LOAD A PROBLEM
# Sends problem data to the frontend as JSON.
# =====================================================

@app.route("/problem/<problem_id>")
def problem_api(problem_id):

    problem = get_problem(problem_id)

    if problem is None:
        return jsonify({"error": "Problem not found."}), 404

    return jsonify(problem)


# =====================================================
# RUN USER CODE
# Receives code from the frontend, runs the tests,
# and returns the results as JSON.
# =====================================================

@app.route("/run", methods=["POST"])
def run_code():

    # Read the JSON data sent by JavaScript
    data = request.get_json()

    # Extract the user's code and selected problem
    code = data["code"]
    problem_id = data.get("problem_id", "add_one")

    problem = get_problem(problem_id)

    if problem is None:
        return jsonify({"error": "Problem not found."}), 404

    # Execute the student's code and grade it
    result = run_problem(code, problem)

    # Send the results back to the frontend
    return jsonify(result)

# =====================================================
# RUN QUICK CODE SNIPPETS
# Executes small pieces of code from lesson IDE blocks.
# Unlike exercises, snippets are not graded and only
# return the program output.
# =====================================================

@app.route("/run_snippet", methods=["POST"])
def run_snippet_api():

    data = request.get_json()

    code = data["code"]

    result = run_snippet(code)

    return jsonify({
        "output": result
    })


# =====================================================
# START THE DEVELOPMENT SERVER
# Runs the Flask application locally.
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
