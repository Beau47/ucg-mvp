# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify, redirect, session

# Import website functions
from problems import get_problem, PROBLEMS
from runner import run_problem, run_snippet

# Time import
from datetime import timedelta

# Authentication client
from supabase_client import supabase

# Lesson loader
from lessons import get_lesson, LESSONS


# =====================================================
# CREATE THE FLASK APPLICATION
# =====================================================

app = Flask(__name__)

app.secret_key = "ucg-secret-key"

#TODO add this later. remove app.secret_key and replace with below and move secret key to .env
##import os

##app.secret_key = os.environ.get(
##    "SECRET_KEY"
##)

# Log-ins are remembered for 7 days
app.permanent_session_lifetime = timedelta(days=7)


# =====================================================
# LOAD OR CREATE A USER PROFILE
# =====================================================

def get_or_create_profile(user_id):

    try:
        profile_data = (
            supabase
            .table("profiles")
            .select("*")
            .eq("id", user_id)
            .execute()
        )

        if profile_data.data:
            return profile_data.data[0]

        profile = {
            "id": user_id,
            "username": session.get("username", "Student"),
            "xp": 0,
            "streak": 0,
            "lessons_completed": 0,
            "problems_solved": 0
        }

        created_profile = (
            supabase
            .table("profiles")
            .insert(profile)
            .execute()
        )

        if created_profile.data:
            return created_profile.data[0]

        return profile

    except Exception:
        return None


# =====================================================
# SAVE LESSON COMPLETION
# =====================================================

def complete_lesson(user_id, lesson_id):

    # Add lesson completion
    supabase.table("lesson_progress").upsert({
        "user_id": user_id,
        "lesson_id": lesson_id,
        "completed": True
    }).execute()


    # Update profile counter
    lessons = (
        supabase
        .table("lesson_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()
    )


    supabase.table("profiles").update({

        "lessons_completed": len(lessons.data)

    }).eq(
        "id",
        user_id
    ).execute()



# =====================================================
# SAVE PROBLEM COMPLETION
# =====================================================

def complete_problem(user_id, problem_id):

    supabase.table("problem_progress").upsert({

        "user_id": user_id,
        "problem_id": problem_id,
        "passed": True

    }).execute()



    problems = (
        supabase
        .table("problem_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("passed", True)
        .execute()
    )



    supabase.table("profiles").update({

        "problems_solved": len(problems.data)

    }).eq(
        "id",
        user_id
    ).execute()


# =====================================================
# DASHBOARD ROUTE
# =====================================================

@app.route("/")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")


    user_id = session["user_id"]


    profile = get_or_create_profile(user_id)

    if profile is None:
        session.clear()
        return redirect("/login")


    return render_template(
        "dashboard.html",
        profile=profile
    )


# =====================================================
# LESSONS PAGE
# Displays the lessons page.
# =====================================================

@app.route("/lessons")
def lessons():

    if "user_id" not in session:
        return redirect("/login")


    completed_data = (
        supabase
        .table("lesson_progress")
        .select("lesson_id")
        .eq(
            "user_id",
            session["user_id"]
        )
        .execute()
    )


    completed_lessons = [

        item["lesson_id"]

        for item in completed_data.data

    ]


    return render_template(
        "lessons.html",
        lessons=LESSONS,
        completed_lessons=completed_lessons
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


    total_pages = max(
        block["page"] for block in lesson["blocks"]
    )


    # Check if user reached final page
    if (
        page == total_pages
        and "user_id" in session
    ):

        complete_lesson(
            session["user_id"],
            lesson_id
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

    if "user_id" not in session:
        return redirect("/login")


    completed_data = (
        supabase
        .table("problem_progress")
        .select("problem_id")
        .eq(
            "user_id",
            session["user_id"]
        )
        .execute()
    )


    completed_problems = [

        item["problem_id"]

        for item in completed_data.data

    ]


    return render_template(
        "exercises.html",
        problems=PROBLEMS,
        completed_problems=completed_problems
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


    # -------------------------------
    # Get profile information
    # -------------------------------

    profile = get_or_create_profile(user_id)

    if profile is None:
        session.clear()
        return redirect("/login")



    # -------------------------------
    # Count completed lessons
    # -------------------------------

    lessons = (
        supabase
        .table("lesson_progress")
        .select("id")
        .eq(
            "user_id",
            user_id
        )
        .eq(
            "completed",
            True
        )
        .execute()
    )


    lessons_completed = len(
        lessons.data
    )



    # -------------------------------
    # Count solved problems
    # -------------------------------

    problems = (
        supabase
        .table("problem_progress")
        .select("id")
        .eq(
            "user_id",
            user_id
        )
        .eq(
            "passed",
            True
        )
        .execute()
    )


    problems_solved = len(
        problems.data
    )



    # -------------------------------
    # Calculate XP
    # -------------------------------

    profile["lessons_completed"] = lessons_completed

    profile["problems_solved"] = problems_solved

    profile["xp"] = (
        lessons_completed * 100
        +
        problems_solved * 25
    )



    # -------------------------------
    # Email
    # -------------------------------

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


    if (
        result.get("passed")
        and "user_id" in session
    ):

        complete_problem(
            session["user_id"],
            problem_id
        )

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


    session.permanent = True

    session["user_id"] = response.user.id
    session["username"] = response.user.email.split("@")[0]

    if get_or_create_profile(response.user.id) is None:
        session.clear()
        return redirect("/login")


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
