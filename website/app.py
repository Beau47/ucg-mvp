# =========================
# Receives website requests
# =========================
from flask import Flask, render_template, request, jsonify
from problems import get_problem
from runner import run_problem

app = Flask(__name__)

@app.route("/")
def home():
    problem = get_problem()
    return render_template("index.html", problem=problem)

@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json()
    code = data["code"]
    problem_id = data.get("problem_id", "add_one")
    problem = get_problem(problem_id)

    if problem is None:
        return jsonify({"error": "Problem not found."}), 404

    result = run_problem(code, problem)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
