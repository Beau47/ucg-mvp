# =========================
# runs code and grades tests
# =========================

import io
from contextlib import redirect_stdout


def run_problem(code, problem):
    """
    Executes student code, runs the problem's test cases,
    captures console output, and returns grading results.
    """

    output = io.StringIO()
    namespace = {}

    passed = 0
    total = len(problem["test_cases"])
    results = []

    try:
        with redirect_stdout(output):
            exec(code, namespace)

            function_name = problem["function_name"]

            if function_name not in namespace:
                raise Exception(f"Function '{function_name}' not found.")

            student_function = namespace[function_name]

            for test in problem["test_cases"]:
                test_input = test["input"]
                expected = test["expected"]

                actual = student_function(test_input)
                did_pass = actual == expected

                if did_pass:
                    passed += 1

                results.append({
                    "input": test_input,
                    "expected": expected,
                    "actual": actual,
                    "passed": did_pass
                })

        percentage = "N/A" if total == 0 else f"{(passed / total) * 100:.1f}%"

        return {
            "console": output.getvalue(),
            "results": results,
            "passed": passed,
            "total": total,
            "percentage": percentage,
            "error": None
        }

    except Exception as e:
        return {
            "console": output.getvalue(),
            "results": results,
            "passed": passed,
            "total": total,
            "percentage": "N/A",
            "error": str(e)
        }


# =====================================================
# RUN QUICK CODE SNIPPETS
# Executes small pieces of code from lesson IDE blocks.
# No grading or test cases are used.
# =====================================================

def run_snippet(code):

    import io
    from contextlib import redirect_stdout

    output = io.StringIO()

    try:

        with redirect_stdout(output):
            exec(code, {})

        return output.getvalue()

    except Exception as e:

        return str(e)
