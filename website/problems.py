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
    },
    "square_number": {
        "id": "square_number",
        "lesson_number": "LESSON 4 OF 8",
        "title": "Square Number",
        "description": "Write a function called square that returns the square of its integer input.",
        "function_name": "square_number",
        "starter_code": '''def square(x):
    """
    Given an integer x,
    return x squared.

    Examples:
    square(5) -> 25
    square(-1) -> 1
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
        {"input": 1, "expected": 1},
        {"input": 6, "expected": 36},
        {"input": 0, "expected": 0},
        {"input": 11, "expected": 121},
        {"input": 30, "expected": 900},
    ],
},
}


def get_problem(problem_id="add_one"):
    return PROBLEMS.get(problem_id)