# =========================
# Coding problem definitions
# =========================

PROBLEMS = {
    "add_one": {
        "id": "add_one",
        "lesson_number": "LESSON 3 OF 8",
        "title": "Add One",
        "description": "Write a function called add_one that returns x + 1.",
        "function_name": "add_one",
        "starter_code": '''def add_one(x):
    """
    Given an integer x,
    return x + 1.

    Examples:
    add_one(5) -> 6
    add_one(-1) -> 0
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns Correct Value",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": 1, "expected": 2},
            {"input": 5, "expected": 6},
            {"input": -1, "expected": 0},
        ],
    }
}


def get_problem(problem_id="add_one"):
    return PROBLEMS.get(problem_id)
