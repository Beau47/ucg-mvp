# =========================
# Coding problem definitions
# =========================

PROBLEMS = {

    # =====================================================
    # LESSON 1
    # =====================================================

    "print_greeting": {
        "id": "print_greeting",
        "lesson_number": "LESSON 1 OF 8",
        "title": "Print Greeting",
        "description": 'Print exactly: Hello, Urban Coders Guild!',
        "function_name": "print_greeting",
        "starter_code": '''def print_greeting():
    """
    Print exactly:
    Hello, Urban Coders Guild!
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Program Runs",
            "Correct Output",
            "No Extra Output",
        ],
        "expected_output": [
        {"input": None, "expected": "Hello, Urban Coders Guild!"}
    ],
    },

    "favorite_place": {
        "id": "favorite_place",
        "lesson_number": "LESSON 1 OF 8",
        "title": "Favorite Place",
        "description": 'Print exactly: I love learning Python!',
        "function_name": "favorite_place",
        "starter_code": '''def favorite_place():
    """
    Print exactly:
    I love learning Python!
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Program Runs",
            "Correct Output",
            "No Extra Output",
        ],
        "expected_output": [
        {"input": None, "expected": "I love learning Python!"}
    ],
    },

    # =====================================================
    # LESSON 2
    # =====================================================

    "add_one": {
        "id": "add_one",
        "lesson_number": "LESSON 2 OF 8",
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
            {"input": 100, "expected": 101},
        ],
    },

    "double_number": {
        "id": "double_number",
        "lesson_number": "LESSON 2 OF 8",
        "title": "Double Number",
        "description": "Write a function called double_number that returns twice the value of x.",
        "function_name": "double_number",
        "starter_code": '''def double_number(x):
    """
    Given an integer x,
    return x multiplied by 2.

    Examples:
    double_number(5) -> 10
    double_number(-3) -> -6
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
            {"input": 7, "expected": 14},
            {"input": -5, "expected": -10},
            {"input": 0, "expected": 0},
            {"input": 20, "expected": 40},
        ],
    },

    # =====================================================
    # LESSON 3
    # =====================================================

    "is_adult": {
        "id": "is_adult",
        "lesson_number": "LESSON 3 OF 8",
        "title": "Is Adult",
        "description": "Return True if the person's age is 18 or older. Otherwise, return False.",
        "function_name": "is_adult",
        "starter_code": '''def is_adult(age):
    """
    Given a person's age,
    return True if they are at least 18 years old.
    Otherwise return False.

    Examples:
    is_adult(18) -> True
    is_adult(15) -> False
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns Correct Boolean",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": 18, "expected": True},
            {"input": 17, "expected": False},
            {"input": 25, "expected": True},
            {"input": 0, "expected": False},
            {"input": 100, "expected": True},
        ],
    },

    "largest_number": {
        "id": "largest_number",
        "lesson_number": "LESSON 3 OF 8",
        "title": "Largest Number",
        "description": "Return the larger of the two numbers. If they are equal, return either one.",
        "function_name": "largest_number",
        "starter_code": '''def largest_number(a, b):
    """
    Given two integers,
    return the larger one.

    Examples:
    largest_number(5, 3) -> 5
    largest_number(8, 10) -> 10
    largest_number(4, 4) -> 4
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns Larger Number",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": (5, 3), "expected": 5},
            {"input": (2, 9), "expected": 9},
            {"input": (4, 4), "expected": 4},
            {"input": (-1, -7), "expected": -1},
            {"input": (100, 99), "expected": 100},
        ],
    },
        # =====================================================
    # LESSON 4
    # =====================================================

    "square_number": {
        "id": "square_number",
        "lesson_number": "LESSON 4 OF 8",
        "title": "Square Number",
        "description": "Write a function called square_number that returns the square of its integer input.",
        "function_name": "square_number",
        "starter_code": '''def square_number(x):
    """
    Given an integer x,
    return x squared.

    Examples:
    square_number(5) -> 25
    square_number(-1) -> 1
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

    "rectangle_area": {
        "id": "rectangle_area",
        "lesson_number": "LESSON 4 OF 8",
        "title": "Rectangle Area",
        "description": "Write a function that returns the area of a rectangle.",
        "function_name": "rectangle_area",
        "starter_code": '''def rectangle_area(length, width):
    """
    Given the length and width of a rectangle,
    return its area.

    Examples:
    rectangle_area(4, 3) -> 12
    rectangle_area(10, 5) -> 50
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns Correct Area",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": (4, 3), "expected": 12},
            {"input": (10, 5), "expected": 50},
            {"input": (7, 2), "expected": 14},
            {"input": (1, 9), "expected": 9},
            {"input": (0, 8), "expected": 0},
        ],
    },

    # =====================================================
    # LESSON 5
    # =====================================================

    "count_to_n": {
        "id": "count_to_n",
        "lesson_number": "LESSON 5 OF 8",
        "title": "Count to N",
        "description": "Return a list containing every number from 1 through n.",
        "function_name": "count_to_n",
        "starter_code": '''def count_to_n(n):
    """
    Given an integer n,
    return a list containing the numbers
    from 1 through n.

    Example:
    count_to_n(5) -> [1, 2, 3, 4, 5]
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses a Loop",
            "Returns Correct List",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": 1, "expected": [1]},
            {"input": 3, "expected": [1, 2, 3]},
            {"input": 5, "expected": [1, 2, 3, 4, 5]},
            {"input": 7, "expected": [1, 2, 3, 4, 5, 6, 7]},
        ],
    },

    "sum_list": {
        "id": "sum_list",
        "lesson_number": "LESSON 5 OF 8",
        "title": "Sum List",
        "description": "Return the sum of all the numbers in a list.",
        "function_name": "sum_list",
        "starter_code": '''def sum_list(numbers):
    """
    Given a list of integers,
    return the sum of all the numbers.

    Examples:
    sum_list([1, 2, 3]) -> 6
    sum_list([5]) -> 5
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses a Loop",
            "Returns Correct Sum",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": [1, 2, 3], "expected": 6},
            {"input": [5], "expected": 5},
            {"input": [10, 20], "expected": 30},
            {"input": [0, 0, 0], "expected": 0},
            {"input": [7, 1, 4, 8], "expected": 20},
        ],
    },
        # =====================================================
    # LESSON 6
    # =====================================================

    "first_item": {
        "id": "first_item",
        "lesson_number": "LESSON 6 OF 8",
        "title": "First Item",
        "description": "Return the first item in a list.",
        "function_name": "first_item",
        "starter_code": '''def first_item(items):
    """
    Given a list,
    return the first item.

    Examples:
    first_item([3, 4, 5]) -> 3
    first_item(["a", "b"]) -> "a"
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns Correct Item",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": [1, 2, 3], "expected": 1},
            {"input": ["apple", "banana"], "expected": "apple"},
            {"input": [True, False], "expected": True},
            {"input": [99], "expected": 99},
        ],
    },

    "dictionary_lookup": {
        "id": "dictionary_lookup",
        "lesson_number": "LESSON 6 OF 8",
        "title": "Dictionary Lookup",
        "description": "Return the value associated with a given key in a dictionary.",
        "function_name": "dictionary_lookup",
        "starter_code": '''def dictionary_lookup(data, key):
    """
    Given a dictionary and a key,
    return the value stored at that key.

    Examples:
    dictionary_lookup({"a": 1}, "a") -> 1
    dictionary_lookup({"dog": "bark"}, "dog") -> "bark"
    """

    # Your code here
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Dictionary Access",
            "Returns Correct Value",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": ({"name": "Alex"}, "name"), "expected": "Alex"},
            {"input": ({"age": 16}, "age"), "expected": 16},
            {"input": ({"x": 10, "y": 20}, "y"), "expected": 20},
            {"input": ({"green": "#00FF00"}, "green"), "expected": "#00FF00"},
        ],
    },

    # =====================================================
    # LESSON 7
    # =====================================================

    "countdown": {
        "id": "countdown",
        "lesson_number": "LESSON 7 OF 8",
        "title": "Countdown",
        "description": "Use recursion to count down from n to 1.",
        "function_name": "countdown",
        "starter_code": '''def countdown(n):
    """
    Given a positive integer n,
    return a list counting down from n to 1.

    Examples:
    countdown(3) -> [3, 2, 1]
    countdown(1) -> [1]
    """

    # Base case goes here

    # Recursive case goes here
''',
        "challenges": [
            "Function Exists",
            "Uses Recursion",
            "Returns Correct List",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": 1, "expected": [1]},
            {"input": 2, "expected": [2, 1]},
            {"input": 4, "expected": [4, 3, 2, 1]},
            {"input": 6, "expected": [6, 5, 4, 3, 2, 1]},
        ],
    },

    "repeat_word": {
        "id": "repeat_word",
        "lesson_number": "LESSON 7 OF 8",
        "title": "Repeat Word",
        "description": "Use recursion to repeat a word n times.",
        "function_name": "repeat_word",
        "starter_code": '''def repeat_word(word, n):
    """
    Given a word and a positive integer n,
    return the word repeated n times.

    Examples:
    repeat_word("Hi", 3) -> "HiHiHi"
    repeat_word("Go", 2) -> "GoGo"
    """

    # Base case goes here

    # Recursive case goes here
''',
        "challenges": [
            "Function Exists",
            "Uses Recursion",
            "Returns Correct String",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": ("A", 1), "expected": "A"},
            {"input": ("Hi", 3), "expected": "HiHiHi"},
            {"input": ("Go", 2), "expected": "GoGo"},
            {"input": ("Python", 4), "expected": "PythonPythonPythonPython"},
        ],
    }

}

def get_problem(problem_id="add_one"):
    return PROBLEMS.get(problem_id)
