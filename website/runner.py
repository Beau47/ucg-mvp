# =========================
# runs code and grades tests
# =========================

import ast
import io
from copy import deepcopy
from contextlib import redirect_stdout
from unittest.mock import patch


def _validate_source_requirements(code, problem):
    """Validate optional structural requirements before running tests."""

    tree = ast.parse(code)
    function_name = problem["function_name"]
    function_nodes = [
        node
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    helper_nodes = [
        node for node in function_nodes if node.name != function_name
    ]

    if problem.get("require_recursion"):
        target_functions = [
            node for node in function_nodes if node.name == function_name
        ]
        calls_itself = any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == function_name
            for target in target_functions
            for node in ast.walk(target)
        )
        if not calls_itself:
            raise Exception(
                f"Function '{function_name}' must call itself recursively."
            )

    minimum_helpers = problem.get("min_helper_functions", 0)
    if len(helper_nodes) < minimum_helpers:
        raise Exception(
            f"Create at least {minimum_helpers} helper functions."
        )

    if problem.get("require_helper_docstrings"):
        missing_docstrings = [
            node.name
            for node in helper_nodes
            if ast.get_docstring(node) is None
        ]
        if missing_docstrings:
            names = ", ".join(missing_docstrings)
            raise Exception(f"Add docstrings to helper functions: {names}.")

    forbidden_calls = set(problem.get("forbidden_calls", ()))
    used_forbidden_calls = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        if isinstance(node.func, ast.Name):
            called_name = node.func.id
        elif isinstance(node.func, ast.Attribute):
            called_name = node.func.attr
        else:
            called_name = None

        if called_name in forbidden_calls:
            used_forbidden_calls.add(called_name)

    if used_forbidden_calls:
        names = ", ".join(sorted(used_forbidden_calls))
        raise Exception(f"Do not use these functions: {names}.")

    if problem.get("forbid_global_variables"):
        has_global_statement = any(
            isinstance(node, ast.Global) for node in ast.walk(tree)
        )
        has_module_assignment = any(
            isinstance(node, (ast.Assign, ast.AnnAssign, ast.AugAssign))
            for node in tree.body
        )
        if has_global_statement or has_module_assignment:
            raise Exception("Do not use global variables.")


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
    validation_error = None

    try:
        try:
            _validate_source_requirements(code, problem)
        except Exception as error:
            # Keep testing so students can still see prints and functional
            # feedback, but report the unmet structural requirement.
            validation_error = str(error)

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
                    if isinstance(test_input, tuple) and len(test_input) > 0
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
            "error": validation_error
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
