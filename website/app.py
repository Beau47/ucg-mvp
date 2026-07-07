# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify
from problems import get_problem, PROBLEMS
from runner import run_problem

# Lesson loader
from lessons import get_lesson


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
    return render_template("lessons.html")


# =====================================================
# INDIVIDUAL LESSON PAGE
# Displays a specific lesson.
# =====================================================

@app.route("/lesson/<lesson_id>")
def lesson(lesson_id):

    lesson = get_lesson(lesson_id)

    if lesson is None:
        return "Lesson not found.", 404

    return render_template("lesson.html", lesson=lesson)

# =====================================================
# EXERCISES PAGE
# Displays the exercises page.
# =====================================================

@app.route("/exercises")
def exercises():

    return render_template(
        "exercises.html",
        problems=PROBLEMS.values()
    )

@app.route("/workspace")
def workspace():
    problem = get_problem("add_one")
    return render_template("index.html", problem=problem)


@app.route("/profile")
def profile():
    return "Profile page coming soon."

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

    # Execute the user's code and grade it
    result = run_problem(code, problem)

    # Send the results back to the frontend
    return jsonify(result)


# =====================================================
# START THE DEVELOPMENT SERVER
# Runs the Flask application locally.
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
