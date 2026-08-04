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


    "manage_guest_list": {
        "id": "manage_guest_list",
        "lesson_number": "LESSON 3.1",
        "title": "Manage Guest List",
        "description": "Update a guest list using append(), insert(), and remove().",
        "function_name": "manage_guest_list",
        "starter_code": '''def manage_guest_list(guests):
    """
    Given a list of guest names,

    1. Add "Jordan" to the end of the list.
    2. Insert "Maria" at the beginning of the list.
    3. Remove the first occurrence of "Alex" if it exists.
    4. Return the updated list.

    Example:
    manage_guest_list(["Alex", "Chris"])
    -> ["Maria", "Chris", "Jordan"]

    Hint:
    Use append(), insert(), and remove().
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Appends Jordan",
            "Inserts Maria First",
            "Removes Only the First Alex",
        ],
        "test_cases": [
            {
                "input": ["Alex", "Chris"],
                "expected": ["Maria", "Chris", "Jordan"]
            },
            {
                "input": ["Chris"],
                "expected": ["Maria", "Chris", "Jordan"]
            },
            {
                "input": ["Alex", "Alex", "Sam"],
                "expected": ["Maria", "Alex", "Sam", "Jordan"]
            },
            {
                "input": [],
                "expected": ["Maria", "Jordan"]
            },
        ],
    },

    "sorted_reverse": {
        "id": "sorted_reverse",
        "lesson_number": "LESSON 3.1",
        "title": "Sorted Reverse",
        "description": "Sort a list in ascending order, reverse it, and return the modified list.",
        "function_name": "sorted_reverse",
        "starter_code": '''def sorted_reverse(numbers):
    """
    Given a list of numbers,

    1. Sort the list in ascending order.
    2. Reverse the list.
    3. Return the modified list.

    Example:
    sorted_reverse([4, 1, 7, 3])
    -> [7, 4, 3, 1]

    Hint:
    Use sort() and reverse().
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Sorts the List",
            "Reverses the List",
            "Returns Descending Order",
        ],
        "test_cases": [
            {"input": [4, 1, 7, 3], "expected": [7, 4, 3, 1]},
            {"input": [5, -2, 5, 0], "expected": [5, 5, 0, -2]},
            {"input": [1], "expected": [1]},
            {"input": [], "expected": []},
        ],
    },

    "copy_and_add": {
        "id": "copy_and_add",
        "lesson_number": "LESSON 3.1",
        "title": "Copy and Add",
        "description": "Copy a scores list, add 100 to the copy, and return both lists.",
        "function_name": "copy_and_add",
        "starter_code": '''def copy_and_add(scores):
    """
    Given a list of scores,

    Create a COPY of the list.

    Add 100 to the copied list.
    Return BOTH lists as a tuple:

    (original_list, copied_list)

    Example:
    copy_and_add([80, 90])
    -> ([80, 90], [80, 90, 100])

    Remember:
    Do NOT create an alias.
    The original list should remain unchanged.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Creates an Independent Copy",
            "Leaves the Original Unchanged",
            "Returns Both Lists as a Tuple",
        ],
        "test_cases": [
            {
                "input": [80, 90],
                "expected": ([80, 90], [80, 90, 100])
            },
            {
                "input": [],
                "expected": ([], [100])
            },
            {
                "input": [100, 70, 85],
                "expected": ([100, 70, 85], [100, 70, 85, 100])
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

    "update_book": {
        "id": "update_book",
        "lesson_number": "LESSON 3.2",
        "title": "Update Book",
        "description": "Add, update, and remove fields in a book dictionary.",
        "function_name": "update_book",
        "starter_code": '''def update_book(book):
    """
    Given a dictionary representing a book,

    1. Add the key "available" with the value True.
    2. Update the book's "year" to 2026.
    3. Remove the key "publisher".
    4. Return the updated dictionary.

    Example:
    update_book({
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "publisher": "Allen & Unwin"
    })

    -> {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 2026,
        "available": True
    }
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Adds and Updates Keys",
            "Removes Publisher",
            "Preserves Other Book Data",
        ],
        "test_cases": [
            {
                "input": {
                    "title": "The Hobbit",
                    "author": "J.R.R. Tolkien",
                    "year": 1937,
                    "publisher": "Allen & Unwin"
                },
                "expected": {
                    "title": "The Hobbit",
                    "author": "J.R.R. Tolkien",
                    "year": 2026,
                    "available": True
                }
            },
            {
                "input": {
                    "title": "Kindred",
                    "year": 1979,
                    "publisher": "Doubleday",
                    "genre": "Science Fiction"
                },
                "expected": {
                    "title": "Kindred",
                    "year": 2026,
                    "genre": "Science Fiction",
                    "available": True
                }
            },
            {
                "input": {
                    "title": "Python Basics",
                    "year": 2024,
                    "publisher": "UCG Press",
                    "available": False
                },
                "expected": {
                    "title": "Python Basics",
                    "year": 2026,
                    "available": True
                }
            },
        ],
    },

    "dictionary_summary": {
        "id": "dictionary_summary",
        "lesson_number": "LESSON 3.2",
        "title": "Dictionary Summary",
        "description": "Return a dictionary's keys, values, and items as lists.",
        "function_name": "dictionary_summary",
        "starter_code": '''def dictionary_summary(student):
    """
    Given a student dictionary,

    return a tuple containing:

    (
        list(student.keys()),
        list(student.values()),
        list(student.items())
    )

    Example:
    dictionary_summary({
        "name": "Jordan",
        "grade": 11
    })

    -> (
        ["name", "grade"],
        ["Jordan", 11],
        [("name", "Jordan"), ("grade", 11)]
    )

    Hint:
    Use the dictionary methods keys(), values(), and items().
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses keys(), values(), and items()",
            "Converts Views to Lists",
            "Returns the Three Lists as a Tuple",
        ],
        "test_cases": [
            {
                "input": {"name": "Jordan", "grade": 11},
                "expected": (
                    ["name", "grade"],
                    ["Jordan", 11],
                    [("name", "Jordan"), ("grade", 11)]
                )
            },
            {
                "input": {"city": "Tulsa", "active": True, "score": 95},
                "expected": (
                    ["city", "active", "score"],
                    ["Tulsa", True, 95],
                    [
                        ("city", "Tulsa"),
                        ("active", True),
                        ("score", 95)
                    ]
                )
            },
            {
                "input": {},
                "expected": ([], [], [])
            },
        ],
    },

    "emergency_contact": {
        "id": "emergency_contact",
        "lesson_number": "LESSON 3.2",
        "title": "Emergency Contact",
        "description": "Return an emergency contact or a fallback message when it is missing.",
        "function_name": "emergency_contact",
        "starter_code": '''def emergency_contact(profile):
    """
    Given a profile dictionary,

    Return the value associated with the key
    "emergency_contact".

    If the key does not exist,
    return "No emergency contact on file."

    Examples:
    emergency_contact({
        "name": "Maria",
        "emergency_contact": "Jordan"
    })
    -> "Jordan"

    emergency_contact({
        "name": "Maria"
    })
    -> "No emergency contact on file."

    Hint:
    Use the get() method.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Dictionary Lookup",
            "Handles a Missing Key",
            "Returns the Stored Value Unchanged",
        ],
        "test_cases": [
            {
                "input": {
                    "name": "Maria",
                    "emergency_contact": "Jordan"
                },
                "expected": "Jordan"
            },
            {
                "input": {"name": "Maria"},
                "expected": "No emergency contact on file."
            },
            {
                "input": {},
                "expected": "No emergency contact on file."
            },
            {
                "input": {"emergency_contact": None},
                "expected": None
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
    # LESSON 4.0
    # =====================================================

    "while_countdown": {
        "id": "while_countdown",
        "lesson_number": "LESSON 4.0",
        "title": "Countdown",
        "description": "Use a while loop to print every number from a starting value down to 1.",
        "function_name": "countdown",
        "starter_code": '''def countdown(start):
    """
    Given a positive integer start,

    print every number from start down to 1,
    one number per line.

    Example:
    countdown(5)

    Output:
    5
    4
    3
    2
    1

    Hint:
    Use a while loop and a counter.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses a Countdown",
            "Prints One Number per Line",
            "Stops After Printing 1",
        ],
        "test_cases": [
            {"input": 1, "expected": "1\n", "compare_output": True},
            {"input": 3, "expected": "3\n2\n1\n", "compare_output": True},
            {
                "input": 5,
                "expected": "5\n4\n3\n2\n1\n",
                "compare_output": True
            },
        ],
    },

    "sum_to_n": {
        "id": "sum_to_n",
        "lesson_number": "LESSON 4.0",
        "title": "Sum to N",
        "description": "Use a while loop and an accumulator to sum every integer from 1 through n.",
        "function_name": "sum_to_n",
        "starter_code": '''def sum_to_n(n):
    """
    Given a positive integer n,

    return the sum of every integer from 1 through n.

    Example:
    sum_to_n(5)
    -> 15

    because
    1 + 2 + 3 + 4 + 5 = 15

    Hint:
    Use a while loop and an accumulator.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses an Accumulator",
            "Includes Both 1 and N",
            "Returns the Correct Sum",
        ],
        "test_cases": [
            {"input": 1, "expected": 1},
            {"input": 2, "expected": 3},
            {"input": 5, "expected": 15},
            {"input": 10, "expected": 55},
            {"input": 25, "expected": 325},
        ],
    },

    "quit_menu": {
        "id": "quit_menu",
        "lesson_number": "LESSON 4.0",
        "title": "Quit Menu",
        "description": "Keep asking for commands until the user enters the sentinel value quit.",
        "function_name": "quit_menu",
        "starter_code": '''def quit_menu():
    """
    Repeatedly ask the user to enter a command.

    Continue prompting until the user types
    "quit"

    When the user enters "quit",
    print
    "Goodbye!"

    Example interaction:
    Command: help
    Command: settings
    Command: quit
    Goodbye!

    Hint:
    "quit" is the sentinel value.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Repeats Until quit",
            "Uses the Sentinel Value",
            "Prints Goodbye Exactly Once",
        ],
        "test_cases": [
            {
                "input": (),
                "stdin": ["quit"],
                "expected": "Goodbye!\n",
                "compare_output": True
            },
            {
                "input": (),
                "stdin": ["help", "settings", "quit"],
                "expected": "Goodbye!\n",
                "compare_output": True
            },
            {
                "input": (),
                "stdin": ["QUIT", "quit"],
                "expected": "Goodbye!\n",
                "compare_output": True
            },
        ],
    },

    # =====================================================
    # LESSON 4.1
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

    "count_vowels": {
        "id": "count_vowels",
        "lesson_number": "LESSON 4.1",
        "title": "Count Vowels",
        "description": "Use a for loop to count uppercase and lowercase vowels in a string.",
        "function_name": "count_vowels",
        "starter_code": '''def count_vowels(word):
    """
    Given a string,

    return the number of vowels in the string.

    Count both uppercase and lowercase vowels.

    Examples:
    count_vowels("Python")
    -> 1

    count_vowels("Education")
    -> 5

    Hint:
    Iterate through the string using a for loop.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Iterates Through the String",
            "Counts Uppercase and Lowercase Vowels",
            "Returns the Correct Count",
        ],
        "test_cases": [
            {"input": "Python", "expected": 1},
            {"input": "Education", "expected": 5},
            {"input": "AEIOUaeiou", "expected": 10},
            {"input": "rhythm", "expected": 0},
            {"input": "", "expected": 0},
        ],
    },

    "largest_coordinate": {
        "id": "largest_coordinate",
        "lesson_number": "LESSON 4.1",
        "title": "Largest Coordinate",
        "description": "Iterate through a tuple of numbers and return its largest value.",
        "function_name": "largest_coordinate",
        "starter_code": '''def largest_coordinate(coordinates):
    """
    Given a tuple of numbers,

    return the largest value.

    Examples:
    largest_coordinate((35.4, -97.5, 42.1))
    -> 42.1

    largest_coordinate((8, 3, 10, 6))
    -> 10

    Hint:
    Iterate through the tuple with a for loop.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Iterates Through the Tuple",
            "Handles Negative Values",
            "Returns the Largest Coordinate",
        ],
        "test_cases": [
            {"input": ((35.4, -97.5, 42.1),), "expected": 42.1},
            {"input": ((8, 3, 10, 6),), "expected": 10},
            {"input": ((-8, -3, -10, -6),), "expected": -3},
            {"input": ((4.5,),), "expected": 4.5},
        ],
    },

    "print_dictionary_keys": {
        "id": "print_dictionary_keys",
        "lesson_number": "LESSON 4.1",
        "title": "Print Dictionary Keys",
        "description": "Use a for loop to print every dictionary key on its own line.",
        "function_name": "print_dictionary_keys",
        "starter_code": '''def print_dictionary_keys(profile):
    """
    Given a dictionary,

    print each key on its own line.

    Example:
    print_dictionary_keys({
        "name": "Jordan",
        "grade": 11,
        "gpa": 3.8
    })

    Output:
    name
    grade
    gpa

    Hint:
    Remember what a for loop iterates through by default.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Iterates Through Dictionary Keys",
            "Preserves Key Order",
            "Prints One Key per Line",
        ],
        "test_cases": [
            {
                "input": {"name": "Jordan", "grade": 11, "gpa": 3.8},
                "expected": "name\ngrade\ngpa\n",
                "compare_output": True
            },
            {
                "input": {"city": "Tulsa", "active": True},
                "expected": "city\nactive\n",
                "compare_output": True
            },
            {
                "input": {},
                "expected": "",
                "compare_output": True
            },
        ],
    },

    "print_even_numbers": {
        "id": "print_even_numbers",
        "lesson_number": "LESSON 4.1",
        "title": "Print Even Numbers",
        "description": "Print every even number from start to stop, including the endpoints when even.",
        "function_name": "print_even_numbers",
        "starter_code": '''def print_even_numbers(start, stop):
    """
    Print every even number from start to stop (inclusive).

    Example:
    print_even_numbers(2, 10)

    Output:
    2
    4
    6
    8
    10

    Hint:
    Use range() with an appropriate step size.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Handles Even and Odd Start Values",
            "Includes an Even Stop Value",
            "Prints One Even Number per Line",
        ],
        "test_cases": [
            {
                "input": (2, 10),
                "expected": "2\n4\n6\n8\n10\n",
                "compare_output": True
            },
            {
                "input": (3, 9),
                "expected": "4\n6\n8\n",
                "compare_output": True
            },
            {
                "input": (8, 8),
                "expected": "8\n",
                "compare_output": True
            },
            {
                "input": (9, 9),
                "expected": "",
                "compare_output": True
            },
        ],
    },

    # =====================================================
    # LESSON 4.2
    # =====================================================

    "multiplication_table": {
        "id": "multiplication_table",
        "lesson_number": "LESSON 4.2",
        "title": "Multiplication Table",
        "description": "Print the 3-times multiplication table from 3 x 1 through 3 x 10 using nested loops.",
        "function_name": "multiplication_table",
        "starter_code": '''def multiplication_table():
    """
    Print the 3-times multiplication table from

    3 x 1

    through

    3 x 10

    using nested loops.

    Output:

    3 x 1 = 3
    3 x 2 = 6

    ...
    3 x 10 = 30

    Hint:
    Use one outer loop and one inner loop,
    even though the outer loop only executes once.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Prints the 3-Times Table",
            "Includes 3 x 1 Through 3 x 10",
            "Matches the Required Output",
        ],
        "test_cases": [
            {
                "input": (),
                "expected": (
                    "3 x 1 = 3\n3 x 2 = 6\n3 x 3 = 9\n"
                    "3 x 4 = 12\n3 x 5 = 15\n3 x 6 = 18\n"
                    "3 x 7 = 21\n3 x 8 = 24\n3 x 9 = 27\n"
                    "3 x 10 = 30\n"
                ),
                "compare_output": True
            },
        ],
    },

    "total_seats": {
        "id": "total_seats",
        "lesson_number": "LESSON 4.2",
        "title": "Total Seats",
        "description": "Given a classroom represented as a list of lists, return the total number of students.",
        "function_name": "total_seats",
        "starter_code": '''def total_seats(classroom):
    """
    Given a classroom represented as a list of lists,
    return the total number of students.

    Example:
    total_seats([
        ["Alex", "Maria", "Jordan"],
        ["Sophia", "Liam"],
        ["Emma"]
    ])
    -> 6

    Hint:
    Use nested for loops to visit every student.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Visits Every Classroom Row",
            "Counts Every Student",
            "Handles Empty Rows",
        ],
        "test_cases": [
            {
                "input": [
                    ["Alex", "Maria", "Jordan"],
                    ["Sophia", "Liam"],
                    ["Emma"],
                ],
                "expected": 6
            },
            {
                "input": [[], ["Alex"], [], ["Maria", "Jordan"]],
                "expected": 3
            },
            {"input": [], "expected": 0},
            {"input": [[]], "expected": 0},
            {"input": [[1], [2, 3], [4, 5, 6]], "expected": 6},
        ],
    },

    "checkerboard": {
        "id": "checkerboard",
        "lesson_number": "LESSON 4.2",
        "title": "Checkerboard",
        "description": "Print a checkerboard pattern using X and O.",
        "function_name": "checkerboard",
        "starter_code": '''def checkerboard(rows, columns):
    """
    Print a checkerboard pattern using X and O.

    Example:
    checkerboard(3, 4)

    Output:
    XOXO
    OXOX
    XOXO

    Hint:
    The character printed depends on both
    the current row and current column.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses Both Row and Column Positions",
            "Alternates X and O",
            "Prints the Requested Dimensions",
        ],
        "test_cases": [
            {
                "input": (3, 4),
                "expected": "XOXO\nOXOX\nXOXO\n",
                "compare_output": True
            },
            {
                "input": (1, 1),
                "expected": "X\n",
                "compare_output": True
            },
            {
                "input": (2, 3),
                "expected": "XOX\nOXO\n",
                "compare_output": True
            },
            {
                "input": (4, 1),
                "expected": "X\nO\nX\nO\n",
                "compare_output": True
            },
        ],
    },

    # =====================================================
    # LESSON 4.3
    # =====================================================

    "first_negative": {
        "id": "first_negative",
        "lesson_number": "LESSON 4.3",
        "title": "First Negative",
        "description": "Return the first negative number and stop searching as soon as it is found.",
        "function_name": "first_negative",
        "starter_code": '''def first_negative(numbers):
    """
    Given a list of numbers,

    return the first negative number.

    As soon as a negative number is found,
    stop searching.

    If the list contains no negative numbers,
    return None.

    Examples:

    first_negative([4, 7, -3, -8])

    -> -3

    first_negative([5, 8, 10])

    -> None

    Hint:
    Use break to stop the search early.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Finds the First Negative Number",
            "Stops Searching Early",
            "Returns None When No Negative Exists",
        ],
        "test_cases": [
            {"input": [4, 7, -3, -8], "expected": -3},
            {"input": [5, 8, 10], "expected": None},
            {"input": [-1, -2], "expected": -1},
            {"input": [0, -4, 2], "expected": -4},
            {"input": [], "expected": None},
        ],
    },

    "average_positive": {
        "id": "average_positive",
        "lesson_number": "LESSON 4.3",
        "title": "Average Positive",
        "description": "Calculate and return the average of only the positive numbers.",
        "function_name": "average_positive",
        "starter_code": '''def average_positive(numbers):
    """
    Given a list of numbers,

    calculate and return the average
    of only the positive numbers.

    Ignore all negative numbers.

    If there are no positive numbers,
    return 0.

    Examples:

    average_positive([4, -2, 6, -1])

    -> 5.0

    average_positive([-5, -8])

    -> 0

    Hint:
    Use continue to skip negative numbers.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Skips Negative Numbers",
            "Averages Only Positive Numbers",
            "Returns Zero When No Positive Exists",
        ],
        "test_cases": [
            {"input": [4, -2, 6, -1], "expected": 5.0},
            {"input": [-5, -8], "expected": 0},
            {"input": [2, 4, 6], "expected": 4.0},
            {"input": [0, 10, -5], "expected": 10.0},
            {"input": [], "expected": 0},
        ],
    },

    "placeholder_example": {
        "id": "placeholder_example",
        "lesson_number": "LESSON 4.3",
        "title": "Placeholder Example",
        "description": "Find and return the largest even number while ignoring odd numbers.",
        "function_name": "placeholder_example",
        "starter_code": '''def placeholder_example(numbers):
    """
    Given a list of numbers,

    find and return the largest even number.

    Ignore odd numbers for now by using
    the pass statement as a placeholder.

    Examples:

    placeholder_example([7, 8, 12, 3])

    -> 12

    placeholder_example([1, 3, 5])

    -> None

    Hint:
    This exercise is designed to practice
    using pass while developing a program.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Ignores Odd Numbers",
            "Finds the Largest Even Number",
            "Returns None When No Even Number Exists",
        ],
        "test_cases": [
            {"input": [7, 8, 12, 3], "expected": 12},
            {"input": [1, 3, 5], "expected": None},
            {"input": [-8, -2, -10], "expected": -2},
            {"input": [4], "expected": 4},
            {"input": [], "expected": None},
            {"input": [0, -3, -2], "expected": 0},
        ],
    },

    # =====================================================
    # LESSON 5.0
    # =====================================================

    "calculate_ticket_price": {
        "id": "calculate_ticket_price",
        "lesson_number": "LESSON 5.0",
        "title": "Calculate Ticket Price",
        "description": "Calculate a ticket price using age, student status, and weekend pricing rules.",
        "function_name": "calculate_ticket_price",
        "starter_code": '''def calculate_ticket_price(age, is_student, is_weekend):
    """
    Given a person's age, student status, and whether it is the weekend,
    calculate and return their ticket price.

    Pricing Rules:
    - Children younger than 13 pay $6.
    - Adults 65 or older pay $7.
    - Everyone else pays $12.
    - Students receive a $2 discount.
    - Weekend tickets cost an additional $3.

    The final price cannot be less than $0.

    Examples:
    calculate_ticket_price(10, False, False)
    -> 6

    calculate_ticket_price(20, True, True)
    -> 13

    calculate_ticket_price(70, False, True)
    -> 10
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Applies the Correct Base Price",
            "Applies Student and Weekend Adjustments",
            "Never Returns a Negative Price",
        ],
        "test_cases": [
            {"input": (10, False, False), "expected": 6},
            {"input": (20, True, True), "expected": 13},
            {"input": (70, False, True), "expected": 10},
            {"input": (13, False, False), "expected": 12},
            {"input": (65, False, False), "expected": 7},
            {"input": (10, True, False), "expected": 4},
            {"input": (70, True, True), "expected": 8},
        ],
    },

    "create_grade_report": {
        "id": "create_grade_report",
        "lesson_number": "LESSON 5.0",
        "title": "Create Grade Report",
        "description": "Calculate a student's average and highest score and return a grade report dictionary.",
        "function_name": "create_grade_report",
        "starter_code": '''def create_grade_report(student_name, scores):
    """
    Given a student's name and a nonempty list of scores,
    calculate the student's average and highest score.

    Return a dictionary in this form:

    {
        "name": student_name,
        "average": average_score,
        "highest": highest_score,
        "passed": True or False
    }

    The student passes if their average is at least 70.

    Example:
    create_grade_report("Maria", [80, 95, 75])
    -> {
        "name": "Maria",
        "average": 83.33333333333333,
        "highest": 95,
        "passed": True
    }

    Do not use sum() or max().
    Calculate both values using a loop.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Calculates the Average",
            "Finds the Highest Score",
            "Builds the Complete Grade Report",
        ],
        "test_cases": [
            {
                "input": ("Maria", [80, 95, 75]),
                "expected": {
                    "name": "Maria",
                    "average": 83.33333333333333,
                    "highest": 95,
                    "passed": True,
                }
            },
            {
                "input": ("Alex", [70]),
                "expected": {
                    "name": "Alex",
                    "average": 70.0,
                    "highest": 70,
                    "passed": True,
                }
            },
            {
                "input": ("Jordan", [68, 70]),
                "expected": {
                    "name": "Jordan",
                    "average": 69.0,
                    "highest": 70,
                    "passed": False,
                }
            },
            {
                "input": ("Sam", [0, 100]),
                "expected": {
                    "name": "Sam",
                    "average": 50.0,
                    "highest": 100,
                    "passed": False,
                }
            },
        ],
    },

    "update_inventory_copy": {
        "id": "update_inventory_copy",
        "lesson_number": "LESSON 5.0",
        "title": "Update Inventory Copy",
        "description": "Return an updated copy of an inventory without modifying the original dictionary.",
        "function_name": "update_inventory_copy",
        "starter_code": '''def update_inventory_copy(inventory, item, amount):
    """
    Given an inventory dictionary, an item name, and an amount,
    return an updated COPY of the inventory.

    Rules:
    - Do not modify the original dictionary.
    - If the item already exists, add amount to its current quantity.
    - If the item does not exist, add it with the given amount.
    - If the resulting quantity is 0 or less, remove the item.

    Examples:
    update_inventory_copy(
        {"Rice": 10, "Beans": 5},
        "Rice",
        3
    )
    -> {"Rice": 13, "Beans": 5}

    update_inventory_copy(
        {"Rice": 10, "Beans": 5},
        "Beans",
        -5
    )
    -> {"Rice": 10}

    The original inventory must remain unchanged.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Returns a New Dictionary",
            "Leaves the Original Unchanged",
            "Updates, Adds, and Removes Items Correctly",
        ],
        "test_cases": [
            {
                "input": ({"Rice": 10, "Beans": 5}, "Rice", 3),
                "expected": {"Rice": 13, "Beans": 5},
                "preserve_input": True,
                "require_new_result": True
            },
            {
                "input": ({"Rice": 10, "Beans": 5}, "Beans", -5),
                "expected": {"Rice": 10},
                "preserve_input": True,
                "require_new_result": True
            },
            {
                "input": ({"Rice": 10}, "Beans", 4),
                "expected": {"Rice": 10, "Beans": 4},
                "preserve_input": True,
                "require_new_result": True
            },
            {
                "input": ({"Rice": 2}, "Rice", -5),
                "expected": {},
                "preserve_input": True,
                "require_new_result": True
            },
            {
                "input": ({"Rice": 10}, "Beans", 0),
                "expected": {"Rice": 10},
                "preserve_input": True,
                "require_new_result": True
            },
        ],
    },

    "analyze_message": {
        "id": "analyze_message",
        "lesson_number": "LESSON 5.0",
        "title": "Analyze Message",
        "description": "Return a message summary with its length, vowel count, and allowed status.",
        "function_name": "analyze_message",
        "starter_code": '''def analyze_message(message, banned_words):
    """
    Given a message and a list of banned words,
    return a summary dictionary in this form:

    {
        "length": number_of_characters,
        "vowels": number_of_vowels,
        "allowed": True or False
    }

    The message is allowed only if none of the banned words
    appear inside it.

    Ignore capitalization when checking banned words.

    Examples:
    analyze_message(
        "Welcome to Python!",
        ["spam", "scam"]
    )
    -> {
        "length": 18,
        "vowels": 5,
        "allowed": True
    }

    analyze_message(
        "This looks like a SCAM",
        ["spam", "scam"]
    )
    -> {
        "length": 22,
        "vowels": 7,
        "allowed": False
    }
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Counts Characters and Vowels",
            "Checks Banned Words Inside the Message",
            "Ignores Capitalization",
        ],
        "test_cases": [
            {
                "input": ("Welcome to Python!", ["spam", "scam"]),
                "expected": {"length": 18, "vowels": 5, "allowed": True}
            },
            {
                "input": ("This looks like a SCAM", ["spam", "scam"]),
                "expected": {"length": 22, "vowels": 7, "allowed": False}
            },
            {
                "input": ("SpAmmy message", ["spam"]),
                "expected": {"length": 14, "vowels": 4, "allowed": False}
            },
            {
                "input": ("AEIOU", []),
                "expected": {"length": 5, "vowels": 5, "allowed": True}
            },
            {
                "input": ("", ["spam"]),
                "expected": {"length": 0, "vowels": 0, "allowed": True}
            },
        ],
    },

    # =====================================================
    # LESSON 5.1
    # =====================================================

    "class_statistics": {
        "id": "class_statistics",
        "lesson_number": "LESSON 5.1",
        "title": "Class Statistics",
        "description": "Return class statistics using helper functions and loop-based calculations.",
        "function_name": "class_statistics",
        "starter_code": '''def class_statistics(scores):
    """
    Given a nonempty list of quiz scores,
    return a dictionary containing:

    {
        "average": average_score,
        "highest": highest_score,
        "lowest": lowest_score,
        "passed": number_of_passing_students
    }

    A passing score is 70 or higher.

    Example:

    class_statistics([82, 95, 61, 74])

    -> {
        "average": 78.0,
        "highest": 95,
        "lowest": 61,
        "passed": 3
    }

    Requirements:
    - Create at least TWO helper functions to avoid repeating code.
      (For example, one function could count passing students,
      while another could calculate the average.)
    - Do NOT use sum(), max(), or min().
    - Use descriptive function names and write docstrings for each helper function.
    - Do not use global variables.
    """

    # WRITE CODE HERE
    pass
''',
        "challenges": [
            "Function Exists",
            "Uses at Least Two Documented Helper Functions",
            "Calculates Statistics Without sum(), max(), or min()",
            "Returns the Complete Class Report",
        ],
        "min_helper_functions": 2,
        "require_helper_docstrings": True,
        "forbidden_calls": ("sum", "max", "min"),
        "forbid_global_variables": True,
        "test_cases": [
            {
                "input": [82, 95, 61, 74],
                "expected": {
                    "average": 78.0,
                    "highest": 95,
                    "lowest": 61,
                    "passed": 3,
                }
            },
            {
                "input": [70],
                "expected": {
                    "average": 70.0,
                    "highest": 70,
                    "lowest": 70,
                    "passed": 1,
                }
            },
            {
                "input": [69, 70],
                "expected": {
                    "average": 69.5,
                    "highest": 70,
                    "lowest": 69,
                    "passed": 1,
                }
            },
            {
                "input": [100, 0, 50],
                "expected": {
                    "average": 50.0,
                    "highest": 100,
                    "lowest": 0,
                    "passed": 1,
                }
            },
            {
                "input": [-5, -10],
                "expected": {
                    "average": -7.5,
                    "highest": -5,
                    "lowest": -10,
                    "passed": 0,
                }
            },
            {
                "input": [88.5, 72.5],
                "expected": {
                    "average": 80.5,
                    "highest": 88.5,
                    "lowest": 72.5,
                    "passed": 2,
                }
            },
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
            "manage_guest_list",
            "sorted_reverse",
            "copy_and_add",
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
            "update_book",
            "dictionary_summary",
            "emergency_contact",
        ),
    },
    {
        "lesson_id": "loops",
        "lesson_page": 1,
        "lesson_label": "Lesson 4.0",
        "featured_problem_id": "while_countdown",
        "problem_ids": (
            "while_countdown",
            "sum_to_n",
            "quit_menu",
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
            "count_vowels",
            "largest_coordinate",
            "print_dictionary_keys",
            "print_even_numbers",
        ),
    },
    {
        "lesson_id": "loops",
        "lesson_page": 3,
        "lesson_label": "Lesson 4.2",
        "featured_problem_id": "multiplication_table",
        "problem_ids": (
            "multiplication_table",
            "total_seats",
            "checkerboard",
        ),
    },
    {
        "lesson_id": "loops",
        "lesson_page": 4,
        "lesson_label": "Lesson 4.3",
        "featured_problem_id": "first_negative",
        "problem_ids": (
            "first_negative",
            "average_positive",
            "placeholder_example",
        ),
    },
    {
        "lesson_id": "functions_modularity",
        "lesson_page": 1,
        "lesson_label": "Lesson 5.0",
        "featured_problem_id": "calculate_ticket_price",
        "problem_ids": (
            "calculate_ticket_price",
            "create_grade_report",
            "update_inventory_copy",
            "analyze_message",
        ),
    },
    {
        "lesson_id": "functions_modularity",
        "lesson_page": 2,
        "lesson_label": "Lesson 5.1",
        "featured_problem_id": "class_statistics",
        "problem_ids": (
            "class_statistics",
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
