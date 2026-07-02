# =========================
# Receives website requests
# =========================
from flask import Flask, render_template, request, jsonify
import io
from contextlib import redirect_stdout
from runner import run_problem

app = Flask(__name__)

PROBLEMS = {
    "add_one": {
        "function_name": "add_one",
        "starter_code": """def add_one(x):
    return x + 1""",
        "test_cases": [
            {"input": 1, "expected": 2},
            {"input": 5, "expected": 6},
            {"input": -1, "expected": 0},
        ]
    },

    "square_number": {
        "function_name": "square_number",
        "starter_code": """def square_number(x):
    return x""",
        "test_cases": [
            {"input": 2, "expected": 4},
            {"input": 3, "expected": 9},
            {"input": 10, "expected": 100},
        ]
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data["code"]
    problem_id = data["problem_id"]

    problem = PROBLEMS[problem_id]

    result = run_problem(code, problem)
    return jsonify(result)

@app.route("/problem/<problem_id>")
def get_problem(problem_id):
    return jsonify(PROBLEMS[problem_id])

if __name__ == "__main__":
    app.run(debug=True)
