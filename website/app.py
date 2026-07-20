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

### CHECKING GLOBAL SESSION

@app.before_request
def check_session():

    # Pages that do not require login
    public_routes = [
        "login",
        "signup",
        "static",
        "forgot_password",
        "reset_password"
    ]


    # Allow public pages
    if request.endpoint in public_routes:
        return


    # If user session disappeared
    if "user_id" not in session:

        return redirect("/login?expired=true")

#TODO add this later. remove app.secret_key and replace with below and move secret key to .env
##import os

##app.secret_key = os.environ.get(
##    "SECRET_KEY"
##)

# Log-ins are remembered for 7 days
app.permanent_session_lifetime = timedelta(days=7)

@app.context_processor
def inject_user():
    return dict(
        logged_in="user_id" in session
    )


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

    # Check if already completed
    existing = (
        supabase
        .table("lesson_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("lesson_id", lesson_id)
        .eq("completed", True)
        .execute()
    )


    # Prevent duplicate completions
    if existing.data:
        return



    # Save completion
    supabase.table("lesson_progress").upsert(
        {
            "user_id": user_id,
            "lesson_id": lesson_id,
            "completed": True
        },
        on_conflict="user_id,lesson_id"
    ).execute()



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
# SAVE LESSON TASK COMPLETION
# =====================================================

def complete_task(user_id, lesson_id, task_id):

    existing = (
        supabase
        .table("lesson_tasks")
        .select("id")
        .eq("user_id", user_id)
        .eq("lesson_id", lesson_id)
        .eq("task_id", task_id)
        .execute()
    )


    if existing.data:
        return


    supabase.table("lesson_tasks").insert({

        "user_id": user_id,
        "lesson_id": lesson_id,
        "task_id": task_id,
        "completed": True

    }).execute()


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


    # -------------------------------
    # Completed lessons
    # -------------------------------

    completed_lessons_data = (
        supabase
        .table("lesson_progress")
        .select("lesson_id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()
    )


    completed_lessons = [

        item["lesson_id"]

        for item in completed_lessons_data.data

    ]


    # Find next lesson

    next_lesson = None

    for lesson in LESSONS.values():

        if lesson["id"] not in completed_lessons:

            next_lesson = lesson
            break



    # -------------------------------
    # Completed exercises
    # -------------------------------

    completed_problems_data = (
        supabase
        .table("problem_progress")
        .select("problem_id")
        .eq("user_id", user_id)
        .eq("passed", True)
        .execute()
    )


    completed_problems = [

        item["problem_id"]

        for item in completed_problems_data.data

    ]


    next_problem = None

    for problem in PROBLEMS.values():

        if problem["id"] not in completed_problems:

            next_problem = problem
            break



    # -------------------------------
    # XP
    # -------------------------------

    lessons_completed = len(completed_lessons)

    problems_completed = len(completed_problems)


    xp = (
        lessons_completed * 100
        +
        problems_completed * 25
    )


    profile["xp"] = xp

    profile["lessons_completed"] = lessons_completed

    profile["problems_solved"] = problems_completed



    return render_template(
        "dashboard.html",
        profile=profile,
        next_lesson=next_lesson,
        next_problem=next_problem,
        logged_in=True
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


    return render_template(
        "lesson.html",
        lesson=lesson,
        lesson_id=lesson_id,
        page=page,
        total_pages=total_pages,
        progress_owner=session.get("user_id", "guest")
    )


@app.route("/complete_task", methods=["POST"])
def complete_task_api():

    if "user_id" not in session:
        return jsonify({
            "error":"Not logged in"
        }),401


    data=request.get_json()


    complete_task(
        session["user_id"],
        data["lesson_id"],
        data["task_id"]
    )


    return jsonify({
        "success":True
    })


@app.route("/lesson/<lesson_id>/complete", methods=["POST"])
def complete_lesson_api(lesson_id):

    if "user_id" not in session:
        return jsonify({
            "error": "Log in to save lesson progress."
        }), 401


    if get_lesson(lesson_id) is None:
        return jsonify({
            "error": "Lesson not found."
        }), 404


    complete_lesson(
        session["user_id"],
        lesson_id
    )


    return jsonify({
        "success": True
    })

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
        completed_problems=completed_problems,
        progress_owner=session["user_id"]
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
        problem=problem,
        progress_owner=session.get("user_id", "guest")
    )


# =====================================================
# PROFILE PAGE
# Loads the student's profile info.
# =====================================================

@app.route("/profile")
def profile():

    user_id = session.get("user_id")

    if user_id is None:
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

    try:
        user = supabase.auth.get_user()
        profile["email"] = user.user.email

    except Exception:
        session.clear()
        return redirect("/login")



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
# SIGN-UP ROUTE
#
# =====================================================

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "GET":

        return render_template(
            "signup.html"
        )


    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    confirm_password = request.form["confirm_password"]


    if password != confirm_password:

        return render_template(
            "signup.html",
            error="Passwords do not match."
        )


    try:

        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,

                "options": {
                    "data": {
                        "username": username
                    }
                }
            }
        )


    except Exception as e:

        error_message = str(e)


        if "already registered" in error_message.lower():

            return render_template(
                "signup.html",
                error="An account with this email already exists. Please log in instead."
            )


        return render_template(
            "signup.html",
            error="Signup failed. Please try again."
        )


    # Check if Supabase actually created the account
    if (
        response.user is not None
        and len(response.user.identities) == 0
    ):

        return render_template(
            "signup.html",
            error="An account with this email already exists. Please log in instead."
        )


    return render_template(
        "signup.html",
        verification_sent=True
    )


# =====================================================
# LOG-IN ROUTE
#
# =====================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":

        return render_template(
            "login.html",
            expired=request.args.get("expired")
        )


    email = request.form["email"]
    password = request.form["password"]


    response = supabase.auth.sign_in_with_password(
        {
            "email": email,
            "password": password
        }
    )

    if response.user.email_confirmed_at is None:

        return render_template(
            "login.html",
            error="Please verify your email before logging in."
        )


    session.permanent = True

    session["user_id"] = response.user.id
    session["username"] = response.user.email.split("@")[0]

    if get_or_create_profile(response.user.id) is None:
        session.clear()
        return redirect("/login")


    return redirect("/")


# =====================================================
# LOG-OUT ROUTE
#
# =====================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")

# =====================================================
# USER FORGOT PASSWORD ROUTE
#
# =====================================================

@app.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():

    if request.method == "GET":

        return render_template(
            "forgot_password.html"
        )


    email = request.form["email"]


    try:

        supabase.auth.reset_password_email(
            email,
            {
                "redirect_to":
                "http://127.0.0.1:5000/reset-password"
            }
        )


        return render_template(
            "forgot_password.html",
            message="Password reset email sent. Check your inbox."
        )


    except Exception:

        return render_template(
            "forgot_password.html",
            message="Could not send reset email."
        )

# =====================================================
# RESET PASSWORD ROUTE
#
# =====================================================

@app.route("/reset-password")
def reset_password():

    return render_template(
        "reset_password.html"
    )

# =====================================================
# START THE DEVELOPMENT SERVER
# Runs the Flask application locally.
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
