# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify

# Utilities for capturing printed output (currently unused here,
# but may be used by the code runner)
import io
from contextlib import redirect_stdout

# Import the function that executes and grades user code
from runner import run_problem


# =====================================================
# CREATE THE FLASK APPLICATION
# =====================================================

app = Flask(__name__)


# =====================================================
# PROBLEM DATABASE
# Stores each coding problem, its starter code,
# function name, and test cases.
# =====================================================

PROBLEMS = {

    # Problem 1
    "add_one": {
        "function_name": "add_one",

        # Starter code loaded into the editor
        "starter_code": """def add_one(x):
    return x + 1""",

        # Test cases used to grade the solution
        "test_cases": [
            {"input": 1, "expected": 2},
            {"input": 5, "expected": 6},
            {"input": -1, "expected": 0},
        ]
    },

    # Problem 2
    "square_number": {
        "function_name": "square_number",

        # Starter code loaded into the editor
        "starter_code": """def square_number(x):
    return x""",

        # Test cases used to grade the solution
        "test_cases": [
            {"input": 2, "expected": 4},
            {"input": 3, "expected": 9},
            {"input": 10, "expected": 100},
        ]
    }
}


# =====================================================
# HOME PAGE
# Displays the main website.
# =====================================================

@app.route("/")
def home():
    return render_template("index.html")


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
    problem_id = data["problem_id"]

    # Retrieve the corresponding problem information
    problem = PROBLEMS[problem_id]

    # Execute the user's code and grade it
    result = run_problem(code, problem)

    # Send the results back to the frontend
    return jsonify(result)


# =====================================================
# LOAD A PROBLEM
# Sends the starter code and test cases for the
# selected problem to the frontend.
# =====================================================

@app.route("/problem/<problem_id>")
def get_problem(problem_id):

    return jsonify(PROBLEMS[problem_id])


# =====================================================
# START THE DEVELOPMENT SERVER
# Runs the Flask application locally.
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)
