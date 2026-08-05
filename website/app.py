# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify, redirect, session

# Import website functions
from problems import get_lesson_exercises, get_problem, PROBLEMS
from runner import run_problem, run_snippet

# Time import
from datetime import timedelta
from urllib.parse import urlencode

# Authentication client
from supabase_client import supabase

# Lesson loader
from lessons import get_lesson, LESSONS

# Imports for avatar images
from werkzeug.utils import secure_filename
import os

# Imports for password requirements
import re

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


# Log-ins are remembered for 7 days
app.permanent_session_lifetime = timedelta(days=7)

@app.context_processor
def inject_user():
    return dict(
        logged_in="user_id" in session
    )

# =====================================================
# XP SYSTEM
# Handles XP calculations, levels, and progress.
# =====================================================


def calculate_level(xp):

    """
    Converts total XP into a student level.

    Every 500 XP = one level.
    """

    return (xp // 500) + 1



def calculate_xp_progress(xp):

    """
    Calculates progress toward the next level.

    Returns a percentage.
    """

    current_level_xp = xp % 500

    progress = (
        current_level_xp / 500
    ) * 100


    return round(progress, 2)



def xp_until_next_level(xp):

    """
    Calculates remaining XP needed
    for the next level.
    """

    remaining = (
        500 - (xp % 500)
    )


    return remaining


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

    # Read any existing row instead of relying on a database-specific upsert
    # conflict target. Some deployed Supabase projects do not have that
    # composite unique constraint yet.
    existing = (
        supabase
        .table("lesson_progress")
        .select("id,completed")
        .eq("user_id", user_id)
        .eq("lesson_id", lesson_id)
        .execute()
    )


    # Already completed
    if any(row.get("completed") for row in existing.data):

        return False

    # Award XP for completing a lesson
    LESSON_XP_REWARD = 100

    progress_data = {
        "user_id": user_id,
        "lesson_id": lesson_id,
        "completed": True
    }

    if existing.data:
        (
            supabase
            .table("lesson_progress")
            .update(progress_data)
            .eq("id", existing.data[0]["id"])
            .execute()
        )
    else:
        (
            supabase
            .table("lesson_progress")
            .insert(progress_data)
            .execute()
        )


    # Count completed lessons
    lessons = (

        supabase
        .table("lesson_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()

    )


    # Count completed problems
    problems = (

        supabase
        .table("problem_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("passed", True)
        .execute()

    )


    lessons_completed = len(lessons.data)

    problems_solved = len(problems.data)


    # Calculate total XP
    xp = (

        lessons_completed * 100

        +

        problems_solved * 25

    )


    # Save all updated values to profiles
    supabase.table("profiles").update({

        "lessons_completed": lessons_completed,

        "problems_solved": problems_solved,

        "xp": xp

    }).eq(

        "id",

        user_id

    ).execute()


    # Tell frontend this was a new completion
    return True

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

    # Check if already completed
    existing = (
        supabase
        .table("problem_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("problem_id", problem_id)
        .eq("passed", True)
        .execute()
    )


    # Do not award XP twice
    if existing.data:

        return False


    # Save problem completion
    supabase.table("problem_progress").upsert({

        "user_id": user_id,

        "problem_id": problem_id,

        "passed": True

    }).execute()


    # Count completed lessons
    lessons = (

        supabase
        .table("lesson_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()

    )


    # Count completed problems
    problems = (

        supabase
        .table("problem_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("passed", True)
        .execute()

    )


    lessons_completed = len(lessons.data)

    problems_solved = len(problems.data)


    # Calculate total XP
    xp = (

        lessons_completed * 100

        +

        problems_solved * 25

    )


    # Save updated stats
    supabase.table("profiles").update({

        "lessons_completed": lessons_completed,

        "problems_solved": problems_solved,

        "xp": xp

    }).eq(

        "id",

        user_id

    ).execute()


    # Tell frontend this was a new completion
    return True

# =====================================================
# CALCULATE XP FUNCTION
# =====================================================

def calculate_xp(user_id):

    lessons = (
        supabase
        .table("lesson_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()
    )


    problems = (
        supabase
        .table("problem_progress")
        .select("id")
        .eq("user_id", user_id)
        .eq("passed", True)
        .execute()
    )


    lessons_completed = len(lessons.data)

    problems_solved = len(problems.data)


    xp = (
        lessons_completed * 100
        +
        problems_solved * 25
    )


    return xp


# =====================================================
# EXERCISE PREREQUISITES
# A completed unit unlocks all of its exercises for existing students. New
# page-completion tasks provide the finer Lesson 1.1/3.1/etc. unlock points.
# =====================================================

PAGE_COMPLETION_PREFIX = "page-complete-"


def get_required_page_task_ids(lesson_id, page):
    """Return the task IDs that prove a lesson page was completed."""

    lesson = get_lesson(lesson_id)

    if lesson is None:
        return set()

    required_task_ids = set()

    for block_index, block in enumerate(lesson["blocks"]):
        if block.get("page") != page:
            continue

        if block.get("type") == "quiz":
            required_task_ids.add(
                f"{lesson_id}-quiz-{block_index}"
            )
        elif block.get("type") == "ide":
            # Jinja's loop.index is one-based in lesson.html.
            required_task_ids.add(
                f"{lesson_id}-ide-{block_index + 1}"
            )

    return required_task_ids


def get_completed_lesson_access(user_id):
    """Return completed unit IDs and completed lesson-page pairs."""

    lesson_rows = (
        supabase
        .table("lesson_progress")
        .select("lesson_id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()
    )

    task_rows = (
        supabase
        .table("lesson_tasks")
        .select("lesson_id,task_id")
        .eq("user_id", user_id)
        .eq("completed", True)
        .execute()
    )

    completed_lessons = {
        row["lesson_id"]
        for row in lesson_rows.data
    }
    completed_pages = set()
    completed_task_ids = {}

    for row in task_rows.data:
        task_id = row.get("task_id", "")
        lesson_id = row["lesson_id"]

        completed_task_ids.setdefault(lesson_id, set()).add(task_id)

        if not task_id.startswith(PAGE_COMPLETION_PREFIX):
            continue

        page_text = task_id.removeprefix(PAGE_COMPLETION_PREFIX)

        if page_text.isdigit():
            completed_pages.add((lesson_id, int(page_text)))

    # Older accounts may have every quiz/IDE task saved without the newer
    # page-complete marker. Inferring the page also closes the brief race
    # between completing the final task and opening its featured exercise.
    for lesson_id, task_ids in completed_task_ids.items():
        lesson = get_lesson(lesson_id)

        if lesson is None:
            continue

        pages = {
            block["page"]
            for block in lesson["blocks"]
        }

        for page in pages:
            required_task_ids = get_required_page_task_ids(
                lesson_id,
                page
            )

            if (
                required_task_ids
                and required_task_ids.issubset(task_ids)
            ):
                completed_pages.add((lesson_id, page))

    return completed_lessons, completed_pages


def is_problem_unlocked(problem, completed_lessons, completed_pages):
    """Check whether the problem's assigned lesson has been completed."""

    lesson_id = problem["required_lesson_id"]
    lesson_page = problem["required_lesson_page"]

    return (
        lesson_id in completed_lessons
        or (lesson_id, lesson_page) in completed_pages
    )


def get_unlocked_problem_ids(user_id):
    """Return all problem IDs currently available to one student."""

    completed_lessons, completed_pages = get_completed_lesson_access(user_id)

    return {
        problem["id"]
        for problem in PROBLEMS.values()
        if is_problem_unlocked(
            problem,
            completed_lessons,
            completed_pages
        )
    }

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

    # Lesson progress percentage

    total_lessons = max(
        len(LESSONS),
        len(completed_lessons)
    )

    lesson_progress = 0


    if total_lessons > 0:

        lesson_progress = (
            len(completed_lessons)
            /
            total_lessons
        ) * 100


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

    # Exercise progress percentage

    total_problems = len(PROBLEMS)

    problem_progress = 0


    if total_problems > 0:

        problem_progress = (
            len(completed_problems)
            /
            total_problems
        ) * 100


    next_problem = None

    for problem in PROBLEMS.values():

        if problem["id"] not in completed_problems:

            next_problem = problem
            break


    # -------------------------------
    # XP AND LEVEL
    # -------------------------------

    lessons_completed = len(completed_lessons)

    problems_completed = len(completed_problems)


    xp = (
        lessons_completed * 100
        +
        problems_completed * 25
    )


    profile["xp"] = xp

    profile["level"] = calculate_level(xp)

    profile["xp_progress"] = calculate_xp_progress(xp)

    profile["xp_remaining"] = xp_until_next_level(xp)


    # XP inside current level
    profile["current_level_xp"] = xp % 500

    # XP needed to complete current level
    profile["next_level_xp"] = 500


    profile["lessons_completed"] = lessons_completed

    profile["problems_solved"] = problems_completed

    profile["total_lessons"] = total_lessons

    profile["lesson_progress"] = lesson_progress

    profile["total_problems"] = total_problems

    profile["problem_progress"] = problem_progress


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
        .eq("completed", True)
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

    if page < 1 or page > total_pages:
        return "Lesson page not found.", 404

    lesson_exercises = get_lesson_exercises(lesson_id, page)
    featured_exercise = next(
        (
            problem
            for problem in lesson_exercises
            if problem["is_featured"]
        ),
        None
    )


    return render_template(
        "lesson.html",
        lesson=lesson,
        lesson_id=lesson_id,
        page=page,
        total_pages=total_pages,
        progress_owner=session.get("user_id", "guest"),
        lesson_exercises=lesson_exercises,
        featured_exercise=featured_exercise
    )


@app.route("/complete_task", methods=["POST"])
def complete_task_api():

    if "user_id" not in session:
        return jsonify({
            "error":"Not logged in"
        }),401


    data = request.get_json() or {}
    lesson_id = data.get("lesson_id")
    task_id = data.get("task_id")

    lesson = get_lesson(lesson_id) if lesson_id else None

    if lesson is None or not task_id:
        return jsonify({
            "error": "A valid lesson and task are required."
        }), 400


    complete_task(
        session["user_id"],
        lesson_id,
        task_id
    )

    newly_completed = False

    # The same persisted page marker that unlocks exercises now also records
    # completion of the unit when it belongs to the final lesson page. This
    # keeps exercise access, lesson checkmarks, XP, and dashboard progress in
    # sync and backfills older accounts when they revisit a completed page.
    if task_id.startswith(PAGE_COMPLETION_PREFIX):
        page_text = task_id.removeprefix(PAGE_COMPLETION_PREFIX)

        if page_text.isdigit():
            page = int(page_text)
            final_page = max(
                block["page"] for block in lesson["blocks"]
            )

            if page == final_page:
                newly_completed = complete_lesson(
                    session["user_id"],
                    lesson_id
                )


    return jsonify({
        "success": True,
        "newly_completed": newly_completed
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


    newly_completed = complete_lesson(
        session["user_id"],
        lesson_id
    )


    return jsonify({

        "success": True,

        "newly_completed": newly_completed

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

    unlocked_problem_ids = get_unlocked_problem_ids(
        session["user_id"]
    )


    return render_template(
        "exercises.html",
        problems=PROBLEMS,
        completed_problems=completed_problems,
        unlocked_problem_ids=unlocked_problem_ids,
        locked_lesson=request.args.get("locked")
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


    user_id = session["user_id"]

    if problem_id not in get_unlocked_problem_ids(user_id):
        query = urlencode({
            "locked": problem["required_lesson_label"]
        })
        return redirect(f"/exercises?{query}")

    profile = get_or_create_profile(user_id)


    return render_template(
        "index.html",
        problem=problem,
        profile=profile
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
    # XP AND LEVEL
    # -------------------------------

    profile["lessons_completed"] = lessons_completed

    profile["problems_solved"] = problems_solved


    xp = (
        lessons_completed * 100
        +
        problems_solved * 25
    )


    profile["xp"] = xp

    profile["level"] = calculate_level(xp)




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
# EDIT PROFILE PAGE
# Allows student to change user and profile pic
# =====================================================

@app.route("/edit-profile", methods=["GET", "POST"])
def edit_profile():

    if "user_id" not in session:
        return redirect("/login")


    user_id = session["user_id"]


    profile = (
        supabase
        .table("profiles")
        .select("*")
        .eq("id", user_id)
        .single()
        .execute()
        .data
    )


    if request.method == "POST":

        username = request.form["username"]


        update_data = {
            "username": username
        }



        # Handle avatar upload

        if "avatar" in request.files:

            file = request.files["avatar"]


            if file.filename != "":


                filename = secure_filename(
                    f"{user_id}_{file.filename}"
                )


                path = f"avatars/{filename}"


                supabase.storage \
                    .from_("avatars") \
                    .upload(
                        path,
                        file.read(),
                        file_options={
                            "upsert": "true"
                        }
                    )


                avatar_url = (
                    supabase.storage
                    .from_("avatars")
                    .get_public_url(path)
                )


                update_data["avatar_url"] = avatar_url



        supabase \
            .table("profiles") \
            .update(update_data) \
            .eq("id", user_id) \
            .execute()


        return redirect("/profile")



    return render_template(
        "edit_profile.html",
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

    if problem_id not in get_unlocked_problem_ids(session["user_id"]):
        return jsonify({
            "error": (
                f"Complete {problem['required_lesson_label']} "
                "to unlock this exercise."
            )
        }), 403

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

    if problem_id not in get_unlocked_problem_ids(session["user_id"]):
        return jsonify({
            "error": (
                f"Complete {problem['required_lesson_label']} "
                "to unlock this exercise."
            )
        }), 403

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

    # Password requirements:
    # - At least 8 characters
    # - One lowercase letter
    # - One uppercase letter
    # - One number
    # - One symbol

    password_requirements = (
        len(password) >= 8
        and re.search(r"[a-z]", password)
        and re.search(r"[A-Z]", password)
        and re.search(r"\d", password)
        and re.search(r"[^A-Za-z0-9]", password)
    )


    if not password_requirements:

        return render_template(
            "signup.html",
            error="Password must be at least 8 characters and contain a lowercase letter, uppercase letter, number, and symbol."
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
    if response.user is None:
        return render_template(
            "signup.html",
            error="Signup failed."
        )

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


    try:

        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

    except Exception as e:

        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    if response.user.email_confirmed_at is None:

        return render_template(
            "login.html",
            error="Please verify your email before logging in."
        )


    session.permanent = True

    session["user_id"] = response.user.id

    session["username"] = (
        response.user.user_metadata.get("username")
        or response.user.email.split("@")[0]
    )

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
                "https://mriinda.pythonanywhere.com/reset-password"
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
