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
    "debug_add_numbers": {
    "id": "debug_add_numbers",
    "lesson_number": "LESSON 5",
    "title": "Debug Add Numbers",
    "description": "Write a function that returns the sum of two numbers.",
    "function_name": "add_numbers",
    "starter_code": '''def add_numbers(a, b):
    """
    Return the sum of a and b.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Return",
        "Returns Correct Sum",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": (3, 5), "expected": 8},
        {"input": (10, 0), "expected": 10},
        {"input": (-2, 7), "expected": 5},
        {"input": (100, 25), "expected": 125},
    ],
},

"greet_user": {
    "id": "greet_user",
    "lesson_number": "LESSON 5",
    "title": "Greet User",
    "description": "Return a greeting using the user's name.",
    "function_name": "greet_user",
    "starter_code": '''def greet_user(name):
    """
    Return "Hello, [name]!"
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Parameter",
        "Returns Greeting",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": "Alex", "expected": "Hello, Alex!"},
        {"input": "Jordan", "expected": "Hello, Jordan!"},
        {"input": "Taylor", "expected": "Hello, Taylor!"},
    ],
},

"square_number": {
    "id": "square_number",
    "lesson_number": "LESSON 5",
    "title": "Square Number",
    "description": "Return the square of a number.",
    "function_name": "square_number",
    "starter_code": '''def square_number(num):
    """
    Return the square of num.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Return",
        "Returns Correct Square",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": 4, "expected": 16},
        {"input": 0, "expected": 0},
        {"input": -3, "expected": 9},
        {"input": 10, "expected": 100},
    ],
},

"get_area_rectangle": {
    "id": "get_area_rectangle",
    "lesson_number": "LESSON 5",
    "title": "Rectangle Area",
    "description": "Return the area of a rectangle.",
    "function_name": "get_area",
    "starter_code": '''def get_area(length, width):
    """
    Return the area of a rectangle.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Parameters",
        "Returns Correct Area",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": (5, 4), "expected": 20},
        {"input": (10, 2), "expected": 20},
        {"input": (7, 3), "expected": 21},
        {"input": (1, 9), "expected": 9},
    ],
},

"validate_coordinates": {
    "id": "validate_coordinates",
    "lesson_number": "LESSON 5",
    "title": "Validate Coordinates",
    "description": "Return True if the latitude is between -90 and 90 inclusive.",
    "function_name": "validate_coordinates",
    "starter_code": '''def validate_coordinates(lat, lon):
    """
    Return True if latitude is valid.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Comparison",
        "Returns Boolean",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": (45, 120), "expected": True},
        {"input": (-90, 0), "expected": True},
        {"input": (90, -80), "expected": True},
        {"input": (95, 20), "expected": False},
        {"input": (-100, 0), "expected": False},
    ],
},

"format_name": {
    "id": "format_name",
    "lesson_number": "LESSON 5",
    "title": "Format Name",
    "description": "Return a name in 'Last, First' format.",
    "function_name": "format_name",
    "starter_code": '''def format_name(first_name, last_name):
    """
    Return the name as "Last, First".
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Parameters",
        "Returns Formatted String",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": ("Lorena", "Mesa"), "expected": "Mesa, Lorena"},
        {"input": ("Ada", "Lovelace"), "expected": "Lovelace, Ada"},
        {"input": ("Grace", "Hopper"), "expected": "Hopper, Grace"},
    ],
},

"refactor_gps_distance": {
    "id": "refactor_gps_distance",
    "lesson_number": "LESSON 5",
    "title": "GPS Distance",
    "description": "Return the distance between two coordinates using the distance formula.",
    "function_name": "calculate_distance",
    "starter_code": '''def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Return the distance between two points.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Formula",
        "Returns Float",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": (0, 0, 3, 4), "expected": 5.0},
        {"input": (1, 1, 1, 1), "expected": 0.0},
        {"input": (2, 3, 5, 7), "expected": 5.0},
    ],
},

"tech_conference_scheduler": {
    "id": "tech_conference_scheduler",
    "lesson_number": "LESSON 5",
    "title": "Assign Conference Room",
    "description": "Return 'Main Stage' if the topic is 'Keynote'; otherwise return 'Breakout 1'.",
    "function_name": "assign_room",
    "starter_code": '''def assign_room(speaker, topic):
    """
    Return the correct room assignment.
    """

    # Your code here
    pass
''',
    "challenges": [
        "Function Exists",
        "Uses Conditional",
        "Returns Correct Room",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": ("Dr. West", "Keynote"), "expected": "Main Stage"},
        {"input": ("Lorena Mesa", "Open Source"), "expected": "Breakout 1"},
        {"input": ("Alex", "Python"), "expected": "Breakout 1"},
        {"input": ("Jordan", "Keynote"), "expected": "Main Stage"},
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

def get_problem(problem_id="add_one"):
    return PROBLEMS.get(problem_id)
