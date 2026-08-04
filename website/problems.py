# =========================
# Coding problem definitions
# =========================

PROBLEMS = {

    # =====================================================
    # LESSON 1
    # =====================================================

    "print_greeting": {
        "id": "print_greeting",
        "lesson_number": "LESSON 1.0",
        "title": "Print Greeting",
        "description": 'Return exactly: Hello, Urban Coders Guild!',
        "function_name": "print_greeting",
        "starter_code": '''def print_greeting():
    """
    Return exactly:
    Hello, Urban Coders Guild!
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Program Runs",
            "Returns Correct Text",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": (), "expected": "Hello, Urban Coders Guild!"}
        ],
    },

    "favorite_place": {
        "id": "favorite_place",
        "lesson_number": "LESSON 1.0",
        "title": "Favorite Place",
        "description": "Return a sentence that says you love learning Python in a place.",
        "function_name": "favorite_place",
        "starter_code": '''def favorite_place(place):
    """
    Given a place, return:
    I love learning Python in [place]!

    Example:
    favorite_place("Tulsa")
    -> "I love learning Python in Tulsa!"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses the Place Parameter",
            "Returns Correct Text",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": "Tulsa", "expected": "I love learning Python in Tulsa!"},
            {"input": "Greenwood", "expected": "I love learning Python in Greenwood!"},
            {"input": "class", "expected": "I love learning Python in class!"},
        ],
    },

    "food_truck_total": {
        "id": "food_truck_total",
        "lesson_number": "LESSON 1.1",
        "title": "Food Truck Total",
        "description": "Return the total cost for a food truck order.",
        "function_name": "food_truck_total",
        "starter_code": '''def food_truck_total(quantity, price):
    """
    Given a quantity and price,
    return the total cost.

    Example:
    food_truck_total(3, 8) -> 24
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Arithmetic",
            "Returns Correct Total",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": (3, 8), "expected": 24},
            {"input": (1, 12), "expected": 12},
            {"input": (5, 4), "expected": 20},
            {"input": (0, 10), "expected": 0},
        ],
    },

    "format_receipt_line": {
        "id": "format_receipt_line",
        "lesson_number": "LESSON 1.1",
        "title": "Format Receipt Line",
        "description": "Use an f-string to return one clean receipt line.",
        "function_name": "format_receipt_line",
        "starter_code": '''def format_receipt_line(customer, item, quantity):
    """
    Given a customer, item, and quantity,
    return:
    [customer] ordered [quantity] [item]

    Example:
    format_receipt_line("Maria", "Frybread Taco", 3)
    -> "Maria ordered 3 Frybread Taco"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Variables",
            "Formats Text Correctly",
            "No Extra Output",
        ],
        "test_cases": [
            {
                "input": ("Maria", "Frybread Taco", 3),
                "expected": "Maria ordered 3 Frybread Taco"
            },
            {
                "input": ("Jordan", "Chicken & Waffles", 2),
                "expected": "Jordan ordered 2 Chicken & Waffles"
            },
            {
                "input": ("Ari", "Kendall Whittier Taco", 1),
                "expected": "Ari ordered 1 Kendall Whittier Taco"
            },
        ],
    },

    "clean_menu_item": {
        "id": "clean_menu_item",
        "lesson_number": "LESSON 1.1",
        "title": "Clean Menu Item",
        "description": "Clean up a menu item using string methods.",
        "function_name": "clean_menu_item",
        "starter_code": '''def clean_menu_item(item):
    """
    Given a menu item with messy spacing or lowercase words,
    remove extra spaces and title-case the item.

    Example:
    clean_menu_item("  frybread taco  ")
    -> "Frybread Taco"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses strip()",
            "Uses title()",
            "Returns Clean Text",
        ],
        "test_cases": [
            {"input": "  frybread taco  ", "expected": "Frybread Taco"},
            {"input": "chicken & waffles", "expected": "Chicken & Waffles"},
            {"input": "  kendall whittier taco", "expected": "Kendall Whittier Taco"},
        ],
    },

    "reverse_word": {
        "id": "reverse_word",
        "lesson_number": "LESSON 1.1",
        "title": "Reverse Word",
        "description": "Use slicing to return a word backwards.",
        "function_name": "reverse_word",
        "starter_code": '''def reverse_word(word):
    """
    Given a word,
    return the word reversed.

    Example:
    reverse_word("Urban") -> "nabrU"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Slicing",
            "Returns Reversed Text",
            "No Extra Output",
        ],
        "test_cases": [
            {"input": "Urban", "expected": "nabrU"},
            {"input": "Python", "expected": "nohtyP"},
            {"input": "Tulsa", "expected": "asluT"},
            {"input": "", "expected": ""},
        ],
    },

    "first_initial": {
        "id": "first_initial",
        "lesson_number": "LESSON 1.1",
        "title": "First Initial",
        "description": "Use indexing and string methods to return the first initial.",
        "function_name": "first_initial",
        "starter_code": '''def first_initial(name):
    """
    Given a name,
    remove extra spaces and return the first initial
    as an uppercase letter.

    Example:
    first_initial("  maria") -> "M"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Indexing",
            "Uses strip()",
            "Returns Uppercase Initial",
        ],
        "test_cases": [
            {"input": "Maria", "expected": "M"},
            {"input": "  jordan", "expected": "J"},
            {"input": "alex", "expected": "A"},
            {"input": "  Tulsa", "expected": "T"},
        ],
    },

    "last_character": {
        "id": "last_character",
        "lesson_number": "LESSON 1.1",
        "title": "Last Character",
        "description": "Use negative indexing to return the final character.",
        "function_name": "last_character",
        "starter_code": '''def last_character(text):
    """
    Given text,
    remove extra spaces and return the last character.

    Example:
    last_character("Python  ") -> "n"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses strip()",
            "Uses Negative Indexing",
            "Returns Last Character",
        ],
        "test_cases": [
            {"input": "Python", "expected": "n"},
            {"input": "Tulsa  ", "expected": "a"},
            {"input": "  Urban", "expected": "n"},
            {"input": "Guild", "expected": "d"},
        ],
    },

    "every_other_character": {
        "id": "every_other_character",
        "lesson_number": "LESSON 1.1",
        "title": "Every Other Character",
        "description": "Use slicing with a step to return every other character.",
        "function_name": "every_other_character",
        "starter_code": '''def every_other_character(text):
    """
    Given text,
    return every other character starting at index 0.

    Example:
    every_other_character("Programming") -> "Pormig"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Step Slicing",
            "Starts at Index 0",
            "Returns Correct Text",
        ],
        "test_cases": [
            {"input": "Programming", "expected": "Pormig"},
            {"input": "Python", "expected": "Pto"},
            {"input": "Urban", "expected": "Ubn"},
            {"input": "abcdef", "expected": "ace"},
        ],
    },

    "repeat_chant": {
        "id": "repeat_chant",
        "lesson_number": "LESSON 1.1",
        "title": "Repeat Chant",
        "description": "Use string repetition to repeat a chant.",
        "function_name": "repeat_chant",
        "starter_code": '''def repeat_chant(word, times):
    """
    Given a word and a number of times,
    return the word repeated that many times.

    Example:
    repeat_chant("Go", 3) -> "GoGoGo"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses String Repetition",
            "Uses the times Parameter",
            "Returns Correct Text",
        ],
        "test_cases": [
            {"input": ("Go", 3), "expected": "GoGoGo"},
            {"input": ("Python", 2), "expected": "PythonPython"},
            {"input": ("UCG", 1), "expected": "UCG"},
            {"input": ("Hi", 0), "expected": ""},
        ],
    },

    "make_order_code": {
        "id": "make_order_code",
        "lesson_number": "LESSON 1.1",
        "title": "Make Order Code",
        "description": "Create a short order code using string methods, slicing, and indexing.",
        "function_name": "make_order_code",
        "starter_code": '''def make_order_code(customer, item):
    """
    Given a customer name and menu item,
    return an order code made from:
    - the first two letters of the customer's name
    - a dash
    - the last letter of the menu item

    The code should be uppercase and ignore extra spaces.

    Example:
    make_order_code("Maria", "Frybread Taco") -> "MA-O"
    """
    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses strip()",
            "Uses Slicing",
            "Uses Negative Indexing",
            "Returns Uppercase Code",
        ],
        "test_cases": [
            {"input": ("Maria", "Frybread Taco"), "expected": "MA-O"},
            {"input": ("  jordan", "Chicken & Waffles  "), "expected": "JO-S"},
            {"input": ("Alex", "taco"), "expected": "AL-O"},
            {"input": ("Tulsa", "Menu"), "expected": "TU-U"},
        ],
    },

    # =====================================================
    # LESSON 2
    # =====================================================

    "add_one": {
        "id": "add_one",
        "lesson_number": "LESSON 2",
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
        "lesson_number": "LESSON 2",
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
        "lesson_number": "LESSON 3",
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
        "lesson_number": "LESSON 3",
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

    "letter_grade": {
        "id": "letter_grade",
        "lesson_number": "LESSON 2.0",
        "title": "Letter Grade",
        "description": "Return the corresponding letter grade for a student's numerical score.",
        "function_name": "letter_grade",
        "starter_code": '''def letter_grade(score):
    """
    Given a student's numerical score,
    return the corresponding letter grade.

    Grading Scale:
    90-100 -> "A"
    80-89 -> "B"
    70-79 -> "C"
    60-69 -> "D"
    Below 60 -> "F"

    Example:
    letter_grade(86)
    -> "B"
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Conditional Logic",
            "Handles Grade Boundaries",
            "Returns Correct Letter Grade",
        ],
        "test_cases": [
            {"input": 100, "expected": "A"},
            {"input": 90, "expected": "A"},
            {"input": 89, "expected": "B"},
            {"input": 80, "expected": "B"},
            {"input": 79, "expected": "C"},
            {"input": 70, "expected": "C"},
            {"input": 69, "expected": "D"},
            {"input": 60, "expected": "D"},
            {"input": 59, "expected": "F"},
            {"input": 0, "expected": "F"},
        ],
    },

    "validate_coordinates": {
        "id": "validate_coordinates",
        "lesson_number": "LESSON 2.0",
        "title": "Validate Coordinates",
        "description": "Return Valid when both latitude and longitude are in range; otherwise return Invalid.",
        "function_name": "validate_coordinates",
        "starter_code": '''def validate_coordinates(latitude, longitude):
    """
    Given a latitude and longitude,
    return:
    "Valid" if the latitude is between -90 and 90 (inclusive)
    and the longitude is between -180 and 180 (inclusive).

    Otherwise, return "Invalid".

    Examples:
    validate_coordinates(36.15, -95.99)
    -> "Valid"

    validate_coordinates(120, 40)
    -> "Invalid"
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Checks Latitude Range",
            "Checks Longitude Range",
            "Returns Valid or Invalid",
        ],
        "test_cases": [
            {"input": (36.15, -95.99), "expected": "Valid"},
            {"input": (-90, -180), "expected": "Valid"},
            {"input": (90, 180), "expected": "Valid"},
            {"input": (120, 40), "expected": "Invalid"},
            {"input": (-90.1, 0), "expected": "Invalid"},
            {"input": (0, 180.1), "expected": "Invalid"},
            {"input": (0, -180.1), "expected": "Invalid"},
        ],
    },

    "can_register": {
        "id": "can_register",
        "lesson_number": "LESSON 2.0",
        "title": "Can Register",
        "description": "Determine whether a student may register for a community coding workshop.",
        "function_name": "can_register",
        "starter_code": '''def can_register(age, completed_intro, permission_slip, banned):
    """
    Determine whether a student may register for a community coding workshop.

    A student may register if:
    - They are 18 or older, OR
    - They are at least 13 years old, have completed the introductory
      workshop, and have a signed permission slip.

    However, if the student is banned, they may never register.

    Return:
    "Eligible" or "Not Eligible"

    Examples:
    can_register(14, True, True, False)
    -> "Eligible"

    can_register(14, True, False, False)
    -> "Not Eligible"

    can_register(25, False, False, True)
    -> "Not Eligible"
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Combines Boolean Conditions",
            "Honors the Ban Override",
            "Returns Correct Eligibility",
        ],
        "test_cases": [
            {"input": (18, False, False, False), "expected": "Eligible"},
            {"input": (14, True, True, False), "expected": "Eligible"},
            {"input": (13, True, True, False), "expected": "Eligible"},
            {"input": (12, True, True, False), "expected": "Not Eligible"},
            {"input": (14, True, False, False), "expected": "Not Eligible"},
            {"input": (14, False, True, False), "expected": "Not Eligible"},
            {"input": (25, False, False, True), "expected": "Not Eligible"},
            {"input": (17, True, True, True), "expected": "Not Eligible"},
        ],
    },
    # =====================================================
    # LESSON 3.0
    # =====================================================

    "earthquake_summary": {
        "id": "earthquake_summary",
        "lesson_number": "LESSON 3.0",
        "title": "Earthquake Summary",
        "description": "Use tuple indexing to summarize an earthquake's magnitude and recorded time.",
        "function_name": "earthquake_summary",
        "starter_code": '''def earthquake_summary(earthquake):
    """
    Given an earthquake tuple in the form

    (
        magnitude,
        latitude,
        longitude,
        time
    )

    return the following string:

    "Magnitude [magnitude] earthquake recorded at [time]."

    Example:
    earthquake_summary((4.2, 35.47, -97.52, "2:31 PM"))
    -> "Magnitude 4.2 earthquake recorded at 2:31 PM."

    Hint:
    Access the tuple's elements using indexing.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Tuple Indexing",
            "Uses Magnitude and Time",
            "Returns Exact Summary",
        ],
        "test_cases": [
            {
                "input": ((4.2, 35.47, -97.52, "2:31 PM"),),
                "expected": "Magnitude 4.2 earthquake recorded at 2:31 PM."
            },
            {
                "input": ((3.0, 36.15, -95.99, "8:05 AM"),),
                "expected": "Magnitude 3.0 earthquake recorded at 8:05 AM."
            },
            {
                "input": ((5.75, 34.60, -98.40, "11:47 PM"),),
                "expected": "Magnitude 5.75 earthquake recorded at 11:47 PM."
            },
        ],
    },

    "tuple_information": {
        "id": "tuple_information",
        "lesson_number": "LESSON 3.0",
        "title": "Tuple Information",
        "description": "Return selected values and a slice from a tuple without modifying it.",
        "function_name": "tuple_information",
        "starter_code": '''def tuple_information(data):
    """
    Given a tuple containing at least four elements,
    return a new tuple containing:

    - the first element,
    - the last element,
    - a slice containing the first two elements.

    Examples:
    tuple_information(("Tulsa", "Norman", "Stillwater", "Lawton"))
    -> ("Tulsa", "Lawton", ("Tulsa", "Norman"))

    tuple_information((5, 10, 15, 20))
    -> (5, 20, (5, 10))

    Remember:
    Tuples are immutable, so do NOT modify the original tuple.
    Instead, create and return a new tuple.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Positive and Negative Indexing",
            "Uses Tuple Slicing",
            "Returns a New Tuple",
        ],
        "test_cases": [
            {
                "input": (("Tulsa", "Norman", "Stillwater", "Lawton"),),
                "expected": ("Tulsa", "Lawton", ("Tulsa", "Norman"))
            },
            {
                "input": ((5, 10, 15, 20),),
                "expected": (5, 20, (5, 10))
            },
            {
                "input": ((True, False, None, "done", 42),),
                "expected": (True, 42, (True, False))
            },
        ],
    },

    # =====================================================
    # LESSON 3.1
    # =====================================================

"update_inventory": {
    "id": "update_inventory",
    "lesson_number": "LESSON 3.1",
    "title": "Update Inventory",
    "description": "Use mutation to update a list without creating a new one.",
    "function_name": "update_inventory",
    "starter_code": '''def update_inventory(items, new_item):
    """
    Add a new item to the inventory list.

    Lists are mutable, meaning they can be changed
    after they are created.

    Example:

    update_inventory(["apple", "banana"], "orange")
    -> ["apple", "banana", "orange"]

    """

    # WRITE CODE HERE
    pass
''',
    "challenges": [
        "Function Exists",
        "Mutates List Correctly",
        "Returns Updated List",
        "No Extra Output",
    ],
    "test_cases": [
        {
            "input": (["apple", "banana"], "orange"),
            "expected": ["apple", "banana", "orange"]
        },
        {
            "input": ([], "Python"),
            "expected": ["Python"]
        },
        {
            "input": (["red"], "blue"),
            "expected": ["red", "blue"]
        },
    ],
},


"copy_profile": {
    "id": "copy_profile",
    "lesson_number": "LESSON 3.1",
    "title": "Copy a Profile",
    "description": "Prevent unwanted changes by creating a copy of a dictionary.",
    "function_name": "copy_profile",
    "starter_code": '''def copy_profile(profile):
    """
    Create a copy of the profile dictionary.

    The copied dictionary should have a new key:
    "verified": True

    The original dictionary should not change.

    Example:

    profile = {"name": "Alex"}

    copy_profile(profile)

    returns:
    {"name": "Alex", "verified": True}

    original stays:
    {"name": "Alex"}

    Hint:
    Use .copy()

    """

    # WRITE CODE HERE
    pass
''',
    "challenges": [
        "Function Exists",
        "Creates Independent Copy",
        "Original Dictionary Unchanged",
        "Returns Correct Dictionary",
    ],
    "test_cases": [
        {
            "input": {"name": "Alex"},
            "expected": {
                "name": "Alex",
                "verified": True
            }
        },
        {
            "input": {"name": "Jordan", "age": 16},
            "expected": {
                "name": "Jordan",
                "age": 16,
                "verified": True
            }
        },
    ],
},
    # =====================================================
    # LESSON 4
    # =====================================================

    "square_number": {
        "id": "square_number",
        "lesson_number": "LESSON 4",
        "title": "Square Number",
        "description": "Return the square of a number.",
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
        "lesson_number": "LESSON 4",
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
        "lesson_number": "LESSON 5",
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
        "lesson_number": "LESSON 5",
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
        "lesson_number": "LESSON 6",
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
        "lesson_number": "LESSON 6",
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
        "lesson_number": "LESSON 7",
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
        "lesson_number": "LESSON 7",
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


# =====================================================
# EXERCISE CURRICULUM ORDER
#
# This allowlist is the single source of truth for catalog order, lesson
# prerequisites, and the featured exercise shown at the end of each lesson.
# Problem definitions omitted here are not exposed by the app or API.
# =====================================================

EXERCISE_CURRICULUM = (
    {
        "lesson_id": "functions_preview",
        "lesson_page": 1,
        "lesson_label": "Lesson 0.5",
        "featured_problem_id": "print_greeting",
        "problem_ids": (
            "print_greeting",
            "favorite_place",
        ),
    },
    {
        "lesson_id": "variables",
        "lesson_page": 2,
        "lesson_label": "Lesson 1.1",
        "featured_problem_id": "add_one",
        "problem_ids": (
            "food_truck_total",
            "format_receipt_line",
            "clean_menu_item",
            "reverse_word",
            "first_initial",
            "last_character",
            "every_other_character",
            "repeat_chant",
            "make_order_code",
            "add_one",
            "double_number",
            "square_number",
            "rectangle_area",
        ),
    },
    {
        "lesson_id": "conditionals",
        "lesson_page": 1,
        "lesson_label": "Lesson 2.0",
        "featured_problem_id": "is_adult",
        "problem_ids": (
            "is_adult",
            "largest_number",
            "letter_grade",
            "validate_coordinates",
            "can_register",
        ),
    },
    {
        "lesson_id": "lists_dictionaries",
        "lesson_page": 1,
        "lesson_label": "Lesson 3.0",
        "featured_problem_id": "earthquake_summary",
        "problem_ids": (
            "earthquake_summary",
            "tuple_information",
        ),
    },
    {
        "lesson_id": "lists_dictionaries",
        "lesson_page": 2,
        "lesson_label": "Lesson 3.1",
        "featured_problem_id": "first_item",
        "problem_ids": (
            "update_inventory",
            "first_item",
        ),
    },
    {
        "lesson_id": "lists_dictionaries",
        "lesson_page": 3,
        "lesson_label": "Lesson 3.2",
        "featured_problem_id": "dictionary_lookup",
        "problem_ids": (
            "copy_profile",
            "dictionary_lookup",
        ),
    },
    {
        "lesson_id": "loops",
        "lesson_page": 2,
        "lesson_label": "Lesson 4.1",
        "featured_problem_id": "count_to_n",
        "problem_ids": (
            "count_to_n",
            "sum_list",
        ),
    },
    {
        "lesson_id": "recursion_capstone",
        "lesson_page": 1,
        "lesson_label": "Lesson 6.0",
        "featured_problem_id": "countdown",
        "problem_ids": (
            "countdown",
            "repeat_word",
        ),
    },
)


def _build_active_problems():
    """Return active problems in curriculum order with prerequisite data."""

    active_problems = {}

    for lesson_group in EXERCISE_CURRICULUM:
        for problem_id in lesson_group["problem_ids"]:
            problem = PROBLEMS[problem_id].copy()
            problem.update({
                "lesson_number": lesson_group["lesson_label"],
                "required_lesson_id": lesson_group["lesson_id"],
                "required_lesson_page": lesson_group["lesson_page"],
                "required_lesson_label": lesson_group["lesson_label"],
                "is_featured": (
                    problem_id == lesson_group["featured_problem_id"]
                ),
            })
            active_problems[problem_id] = problem

    return active_problems


PROBLEMS = _build_active_problems()


def get_problem(problem_id="add_one"):
    return PROBLEMS.get(problem_id)


def get_lesson_exercises(lesson_id, lesson_page):
    """Return the ordered exercises assigned to one lesson page."""

    return [
        problem
        for problem in PROBLEMS.values()
        if problem["required_lesson_id"] == lesson_id
        and problem["required_lesson_page"] == lesson_page
    ]
