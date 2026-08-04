# =========================
# runs code and grades tests
# =========================

import io
from copy import deepcopy
from contextlib import redirect_stdout
from unittest.mock import patch


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
                # Student functions may mutate lists or dictionaries. Give
                # every run a fresh value so shared problem data stays clean.
                test_input = deepcopy(test["input"])
                original_input = deepcopy(test_input)
                expected = test["expected"]
                output_start = output.tell()

                def call_student_function():
                    if isinstance(test_input, tuple):
                        return student_function(*test_input)

                    return student_function(test_input)

                stdin_values = test.get("stdin")

                if stdin_values is not None:
                    with patch(
                        "builtins.input",
                        side_effect=stdin_values
                    ) as mocked_input:
                        returned = call_student_function()

                    used_expected_inputs = (
                        mocked_input.call_count == len(stdin_values)
                    )
                else:
                    returned = call_student_function()
                    used_expected_inputs = True

                printed = output.getvalue()[output_start:]
                actual = (
                    printed
                    if test.get("compare_output")
                    else returned
                )

                input_was_preserved = (
                    not test.get("preserve_input")
                    or test_input == original_input
                )
                original_result_object = (
                    test_input[0]
                    if isinstance(test_input, tuple)
                    else test_input
                )
                returned_new_object = (
                    not test.get("require_new_result")
                    or returned is not original_result_object
                )

                did_pass = (
                    actual == expected
                    and used_expected_inputs
                    and input_was_preserved
                    and returned_new_object
                )

                if did_pass:
                    passed += 1

                results.append({
                    "input": test_input,
                    "expected": expected,
                    "actual": actual,
                    "passed": did_pass,
                    "input_preserved": input_was_preserved,
                    "returned_new_object": returned_new_object
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
