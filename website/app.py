# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify, redirect, session
from problems import get_problem, PROBLEMS
from runner import run_problem, run_snippet

# Authentication client
from supabase_client import supabase

# Lesson loader
from lessons import get_lesson, LESSONS


# =====================================================
# CREATE THE FLASK APPLICATION
# =====================================================

app = Flask(__name__)

app.secret_key = "ucg-secret-key"


# =====================================================
# DASHBOARD ROUTE
# =====================================================

@app.route("/")
def dashboard():

    if "user_id" not in session:

        return redirect("/login")


    return render_template(
        "dashboard.html"
    )


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


# =====================================================
# PROFILE PAGE
# Loads the student's profile info.
# =====================================================

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect("/login")


    user_id = session["user_id"]


    # Get profile data from Supabase database
    profile_data = (
        supabase
        .table("profiles")
        .select("*")
        .eq("id", user_id)
        .execute()
    )


    profile = profile_data.data[0]


    # Get email from Supabase Auth
    user = supabase.auth.get_user()

    profile["email"] = user.user.email


    return render_template(
        "profile.html",
        profile=profile
    )


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
# USER SIGN-UP ROUTE
#
# =====================================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "GET":

        return render_template(
            "signup.html"
        )


    email = request.form["email"]
    password = request.form["password"]


    response = supabase.auth.sign_up(
        {
            "email": email,
            "password": password
        }
    )

    user = response.user


    supabase.table("profiles").insert({

        "id": user.id,
        "username": email.split("@")[0],
        "xp": 0,
        "streak": 0,
        "lessons_completed": 0,
        "problems_solved": 0

    }).execute()


    return redirect("/login")


# =====================================================
# USER LOG-IN ROUTE
#
# =====================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":

        return render_template(
            "login.html"
        )


    email = request.form["email"]
    password = request.form["password"]


    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )


    session["user_id"] = response.user.id


    return redirect("/")


# =====================================================
# USER LOG-OUT ROUTE
#
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# =====================================================
# START THE DEVELOPMENT SERVER
# Runs the Flask application locally.
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
