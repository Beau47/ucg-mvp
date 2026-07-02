from flask import Flask, render_template, request, jsonify
import io
from contextlib import redirect_stdout

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

    output = io.StringIO()
    namespace = {}
    results = []
    passed = 0
    total = len(problem["test_cases"])

    try:
        with redirect_stdout(output):
            exec(code, namespace)

            func_name = problem["function_name"]

            if func_name not in namespace:
                raise Exception(f"Function '{func_name}' not found.")

            student_func = namespace[func_name]

            for test in problem["test_cases"]:
                actual = student_func(test["input"])
                expected = test["expected"]
                did_pass = actual == expected

                if did_pass:
                    passed += 1

                results.append({
                    "input": test["input"],
                    "expected": expected,
                    "actual": actual,
                    "passed": did_pass
                })

        percentage = "N/A" if total == 0 else f"{(passed / total) * 100:.1f}%"

        return jsonify({
            "console": output.getvalue(),
            "results": results,
            "passed": passed,
            "total": total,
            "percentage": percentage
        })

    except Exception as e:
        return jsonify({
            "console": output.getvalue(),
            "results": [],
            "passed": 0,
            "total": total,
            "percentage": "N/A",
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)
