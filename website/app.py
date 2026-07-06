# =====================================================
# IMPORTS
# Import the libraries needed for the Flask application.
# =====================================================

# Flask modules for creating routes and returning responses
from flask import Flask, render_template, request, jsonify
from problems import get_problem
from runner import run_problem


# =====================================================
# CREATE THE FLASK APPLICATION
# =====================================================

app = Flask(__name__)

@app.route("/")
def home():
    problem = get_problem()
    return render_template("index.html", problem=problem)

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
