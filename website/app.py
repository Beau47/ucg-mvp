# =========================
# Receives website requests
# =========================
from flask import Flask, render_template, request, jsonify
import io
from contextlib import redirect_stdout
from runner import run_problem

app = Flask(__name__)

problem = {
    "function_name": "add_one",
    "test_cases": [
        {"input": 1, "expected": 2},
        {"input": 5, "expected": 6},
        {"input": -1, "expected": 0},
    ]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data["code"]

    result = run_problem(code, problem)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
