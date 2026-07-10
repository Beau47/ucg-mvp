# =========================
# Lesson definitions
# =========================

LESSONS = {
    "why_python": {

        "id": "why_python",

        "lesson_number": "0",

        "title": "Why Python?",

        "description": "Learn what Python is, why it matters, and how programming can help solve real community problems.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Unit 0 - Why Python?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Estimated Time: 30-40 minutes"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Learning Objectives"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Explain three real-world uses of Python.",
                    "Describe how programming can help solve community problems.",
                    "Write and run your first Python program.",
                    "Understand that computers only follow instructions they are given."
                ]
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Word Bank"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">programming language</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">Garbage In, Garbage Out</span>'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Imagine if you could create a program that automatically organized donations for a nonprofit, translated endangered languages into digital dictionaries, or analyzed community data to identify where new parks or healthcare services were needed.'
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'People often think programming is only for building video games or websites. In reality, programming is used in medicine, education, science, business, and community advocacy. One of the world\'s most popular programming languages is Python, and throughout this course you will learn how to use it to solve real problems.'
            },

            {
                "page": 1,
                "type": "quote",
                "text":
                "Programming is not just about computers. It is about learning how to think logically and solve problems step by step."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 1 - What is Python?"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Python is a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">programming language</span>. A programming language is a way for humans to communicate with a computer by giving instructions that it can understand and execute.'
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Some programming languages are designed for speed, while others are designed to be easy to read and learn. Python was created with readability in mind, making it one of the best languages for beginners."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Today, Python is used by:"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "NASA for scientific computing",
                    "Hospitals to analyze patient data",
                    "Researchers studying climate change",
                    "Businesses to automate repetitive work",
                    "Schools to teach computer science",
                    "Artificial intelligence companies"
                ]
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "Which statement best describes Python?",
                "options": [
                    "A. A type of computer",
                    "B. A programming language used to give computers instructions",
                    "C. A web browser",
                    "D. An operating system"
                ],
                "answer": "B. A programming language used to give computers instructions"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 2 - Python Can Help Communities"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Programming is not only used by large technology companies. Communities use software<sup>1</sup> to organize volunteers, manage donations, preserve culture, analyze community needs, and create educational resources.'
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Organizations have used Python to analyze public datasets related to racial justice and community resources.",
                    "Language preservation projects have used software to create digital dictionaries and educational tools for Indigenous languages.",
                    "Museums and cultural organizations build websites and digital exhibits that preserve local history."
                ]
            },

            {
                "page": 1,
                "type": "footnote",
                "number": "1",
                "text": "Software means instructions, data, or code that tells a computer what to do."
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "As you learn Python, think about problems in your own community that technology could help solve."
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "Which of these is an example of using programming to help a community?",
                "options": [
                    "A. Automatically organizing volunteer schedules",
                    "B. Building a digital language dictionary",
                    "C. Analyzing public community data",
                    "D. All of the above"
                ],
                "answer": "D. All of the above"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 3 - Computers Only Follow Instructions"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Many people believe computers are smart. In reality, computers are extremely literal. They only perform the exact instructions they receive."
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Computer scientists often summarize this idea using the phrase <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">Garbage In, Garbage Out</span>. This means the computer\'s output depends entirely on how well the programmer instructs it.'
            },

            {
                "page": 1,
                "type": "warning",
                "text":
                "If the instructions are incorrect, the computer will produce incorrect results even if it follows those instructions perfectly."
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "What does Garbage In, Garbage Out mean?",
                "options": [
                    "A. Computers sometimes become broken",
                    "B. Computers only produce correct results when given correct instructions",
                    "C. Computers automatically fix mistakes",
                    "D. Python deletes bad programs"
                ],
                "answer": "B. Computers only produce correct results when given correct instructions"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 4 - Your First Python Program"
            },

            {
                "page": 1,
                "type": "ide",
                "instructions": "Run your first Python program. Try changing the message to greet your own community.",
                "starter_code": """print("Hello, Tulsa!")"""
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "What does the print() function do?",
                "options": [
                    "A. Deletes text",
                    "B. Displays information on the screen",
                    "C. Saves a file",
                    "D. Creates a website"
                ],
                "answer": "B. Displays information on the screen"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Python is a beginner-friendly programming language.",
                    "Programming can solve real community problems.",
                    "Computers only follow the instructions they are given.",
                    "Good programmers learn to think carefully and logically.",
                    "Every programmer starts with a simple first program."
                ]
            }

        ]
    },

    "variables": {

        "id": "variables",

        "lesson_number": "1",

        "description": "Learn how Python stores information using variables, strings, numbers, and basic data types.",

        "title": "Variables",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "What is a Variable?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Variables allow you to store information that can be used later."
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""x = 5
print(x)""",
                "instructions":
                "Try changing the value of x and run the code to see how the output changes."
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Notice that x now stores the value 5."
            },

            {
                "page": 2,
                "type": "image",
                "src": "/static/images/variable_box.png",
                "caption": "A variable stores a value."
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "Choose descriptive variable names."
            },

            {
                "page": 2,
                "type": "warning",
                "text":
                "Variable names cannot start with numbers."
            },

            {
                "page": 3,
                "type": "exercise",
                "problem": "add_one"
            }

        ]
    },


    "conditionals": {

    "id": "conditionals",

    "lesson_number": "2",

    "description": "Use if, elif, and else statements to help programs make decisions with logical thinking.",

    "title": "Conditionals",

    "blocks": [

        # =====================================================
        # PAGE 1: INTRODUCTION
        # =====================================================

        {
            "page": 1,
            "type": "heading",
            "text": "Unit 2: Conditionals — Teaching Python to Make Decisions"
        },

        {
            "page": 1,
            "type": "paragraph",
            "text": """
            Programs make decisions the same way people do every day.
            A concert bouncer checks: Is your ticket valid? Are you on the VIP list?
            Are you old enough to enter?

            Python uses conditional statements to follow these same yes/no
            decision paths. With if, elif, and else, programs can choose what
            happens next.
            """
        },

        {
            "page": 1,
            "type": "tip",
            "text": """
            By the end of this lesson, you will be able to:
            • Write if/elif/else statements
            • Combine conditions using and/or/not
            • Debug common conditional errors
            • Build programs that make real-world decisions
            """
        },

        {
            "page": 1,
            "type": "heading",
            "text": "Focus: Latinx in AI & Decision-Making"
        },

        {
            "page": 1,
            "type": "paragraph",
            "text": """
            Luis von Ahn, a Guatemalan-American computer scientist and
            co-founder of Duolingo, used technology and decision-making
            systems to make language learning more accessible.

            Conditional logic powers many systems people use every day,
            from learning apps to accessibility tools.
            """
        },


        # =====================================================
        # PAGE 2: BOOLEAN VALUES
        # =====================================================

        {
            "page": 2,
            "type": "heading",
            "text": "Boolean Values: True or False"
        },

        {
            "page": 2,
            "type": "paragraph",
            "text": """
            A Boolean is a value that can only be True or False.

            Think of a Boolean like a traffic light:
            True means go.
            False means stop.

            Python creates Boolean values when it compares information.
            """
        },

        {
            "page": 2,
            "type": "code",
            "text": """
print(5 > 3)

# Output:
True
"""
        },

        {
            "page": 2,
            "type": "heading",
            "text": "Comparison Operators"
        },

        {
            "page": 2,
            "type": "list",
            "items": [
                "== checks if two values are equal",
                "!= checks if two values are different",
                "> checks if one value is greater",
                "< checks if one value is smaller",
                ">= checks if one value is greater than or equal"
            ]
        },

        {
            "page": 2,
            "type": "quiz",
            "question": "What type of value can a Boolean store?",
            "options": [
                "A number",
                "A True or False value",
                "A sentence",
                "A list"
            ],
            "answer": "A True or False value"
        },


        # =====================================================
        # PAGE 3: IF STATEMENTS
        # =====================================================

        {
            "page": 3,
            "type": "heading",
            "text": "Making Decisions with if"
        },

        {
            "page": 3,
            "type": "paragraph",
            "text": """
            An if statement runs code only when a condition is True.

            Python uses indentation to show which lines belong inside
            the decision block.
            """
        },

        {
            "page": 3,
            "type": "code",
            "text": """
age = 18

if age >= 18:
    print("You can vote.")
"""
        },

        {
            "page": 3,
            "type": "ide",
            "instructions": "Create an if statement that prints VIP when a gold ticket is selected.",
            "starter_code": """
ticket_type = "gold"

# Write your condition below

"""
        },


        # =====================================================
        # PAGE 4: ELSE AND ELIF
        # =====================================================

        {
            "page": 4,
            "type": "heading",
            "text": "Adding More Paths with elif and else"
        },

        {
            "page": 4,
            "type": "paragraph",
            "text": """
            Sometimes programs need more than two choices.

            elif creates another possible path.
            else provides a default option when no conditions are true.
            """
        },

        {
            "page": 4,
            "type": "code",
            "text": """
grade = 85

if grade >= 90:
    print("A")
elif grade >= 70:
    print("C")
else:
    print("Keep practicing.")
"""
        },

        {
            "page": 4,
            "type": "quiz",
            "question": "Which keyword checks another condition after an if fails?",
            "options": [
                "then",
                "elif",
                "elseif",
                "check"
            ],
            "answer": "elif"
        },


        # =====================================================
        # PAGE 5: LOGICAL OPERATORS
        # =====================================================

        {
            "page": 5,
            "type": "heading",
            "text": "Combining Conditions with Logic"
        },

        {
            "page": 5,
            "type": "paragraph",
            "text": """
            Logical operators allow programs to combine multiple conditions.

            AND means every condition must be True.

            OR means at least one condition must be True.

            NOT reverses a Boolean value.
            """
        },

        {
            "page": 5,
            "type": "code",
            "text": """
late = False
homework_done = True

if not late and homework_done:
    print("You're on track!")
else:
    print("Check your work.")
"""
        },

        {
            "page": 5,
            "type": "ide",
            "instructions": "Modify the conditions to test different outcomes.",
            "starter_code": """
hungry = True
money = False
coupon = True

if (hungry and money) or coupon:
    print("Time to eat!")
else:
    print("Wait for another option.")
"""
        },


        # =====================================================
        # PAGE 6: DEBUGGING
        # =====================================================

        {
            "page": 6,
            "type": "heading",
            "text": "Debugging Conditional Errors"
        },

        {
            "page": 6,
            "type": "paragraph",
            "text": """
            A common mistake is using = instead of ==.

            = assigns a value.
            == compares two values.
            """
        },

        {
            "page": 6,
            "type": "code",
            "text": """
# Incorrect

snack = "Hot Cheetos"

if snack = "Hot Cheetos":
    print("Spicy choice!")


# Correct

if snack == "Hot Cheetos":
    print("Spicy choice!")
"""
        },

        {
            "page": 6,
            "type": "ide",
            "instructions": "Fix the conditional error.",
            "starter_code": """
score = 92

if score > 90
    print("A+ Student!")
"""
        },

        {
            "page": 6,
            "type": "quiz",
            "question": "What error occurs when a colon is missing after an if statement?",
            "options": [
                "SyntaxError",
                "RuntimeError",
                "LogicError",
                "No error"
            ],
            "answer": "SyntaxError"
        },


        # =====================================================
        # PAGE 7: REAL WORLD APPLICATION
        # =====================================================

        {
            "page": 7,
            "type": "heading",
            "text": "Applying Conditionals: SNAP Eligibility Checker"
        },

        {
            "page": 7,
            "type": "paragraph",
            "text": """
            Decision-making programs are used in real-world systems.

            This example checks whether someone meets requirements:
            • Income must be below 2000
            • The person must be a student or unemployed
            """
        },

        {
            "page": 7,
            "type": "code",
            "text": """
income = 1800
is_student = True
is_unemployed = False

if income < 2000 and (is_student or is_unemployed):
    print("Approved")
else:
    print("Needs Review")
"""
        },

        {
            "page": 7,
            "type": "exercise",
            "problem": "snap_checker"
        }

    ]
    },
    "lists_dictionaries": {

    "id": "lists_dictionaries",

    "lesson_number": "3",

    "description": "Organize, access, and modify collections of data using Python lists and dictionaries.",

    "title": "Lists & Dictionaries",

    "blocks": [

        {
            "page": 1,
            "type": "heading",
            "text": "Unit 3: Lists & Dictionaries"
        },

        {
            "page": 1,
            "type": "paragraph",
            "text":
            "In this lesson, you will learn how Python stores and organizes information using lists and dictionaries. "
            "You will practice accessing data, changing values, looping through collections, and loading JSON data."
        },

        {
            "page": 1,
            "type": "tip",
            "text":
            "Focus: African & Afro-Caribbean Data Science\n\n"
            "Spotlight: Anne-Marie Imafidon — STEM advocate who uses technology and education to expand access to computer science.\n\n"
            "Spotlight: Alan Emtage — Barbadian computer scientist who created Archie, one of the first internet search tools."
        },

        {
            "page": 1,
            "type": "heading",
            "text": "Vocabulary"
        },

        {
            "page": 1,
            "type": "list",
            "items": [
                "List — An ordered collection of items: ['apple', 'banana']",
                "Index — The position of an item in a list. Indexing starts at 0.",
                "Append — Adds a new item to the end of a list.",
                "Slice — Selects part of a list using a range of indexes.",
                "Dictionary — A collection of key-value pairs.",
                "Key / Value — A lookup name and the information connected to it.",
                "JSON — A text format for storing and sharing structured data."
            ]
        },


        {
            "page": 2,
            "type": "heading",
            "text": "1. Creating and Accessing Lists"
        },

        {
            "page": 2,
            "type": "paragraph",
            "text":
            "Lists store multiple values in one variable. Each item has a position called an index. "
            "Python starts counting indexes at 0."
        },

        {
            "page": 2,
            "type": "code",
            "text":
"""playlist = [
    "Kendrick Lamar",
    "SZA",
    "Bad Bunny",
    "Tems"
]

print(playlist[0])
print(playlist[-1])"""
        },

        {
            "page": 2,
            "type": "tip",
            "text":
            "Remember: playlist[0] gives the first item, while playlist[-1] gives the last item."
        },

        {
            "page": 2,
            "type": "ide",
            "instructions":
            "Create your own playlist list with four artists or creators. Print the second and last items.",

            "starter_code":
"""my_playlist = [
    "Artist 1",
    "Artist 2",
    "Artist 3",
    "Artist 4"
]

# Print the second and last artists here
"""
        },


        {
            "page": 3,
            "type": "heading",
            "text": "2. Changing Lists"
        },

        {
            "page": 3,
            "type": "paragraph",
            "text":
            "Lists can be changed after they are created. This is called mutation. "
            "You can replace values or add new items."
        },

        {
            "page": 3,
            "type": "code",
            "text":
"""playlist = [
    "Kendrick Lamar",
    "SZA",
    "Bad Bunny"
]

playlist[1] = "Beyoncé"

playlist.append("Burna Boy")

print(playlist)

print(len(playlist))"""
        },

        {
            "page": 3,
            "type": "exercise",
            "problem": "list_mutation"
        },


        {
            "page": 4,
            "type": "heading",
            "text": "3. Working With Dictionaries"
        },

        {
            "page": 4,
            "type": "paragraph",
            "text":
            "Dictionaries store information using key-value pairs. "
            "Instead of accessing data by position, you access it using a key."
        },

        {
            "page": 4,
            "type": "code",
            "text":
"""profile = {
    "name": "Zion",
    "city": "Tulsa",
    "favorite_artist": "J. Cole"
}

print(profile["city"])"""
        },

        {
            "page": 4,
            "type": "ide",
            "instructions":
            "Create a dictionary about yourself. Include name, grade, and favorite food. Print your favorite food.",

            "starter_code":
"""profile = {
    "name": "",
    "grade": "",
    "favorite_food": ""
}

# Print your favorite food
"""
        },


        {
            "page": 5,
            "type": "heading",
            "text": "4. Updating Dictionaries"
        },

        {
            "page": 5,
            "type": "code",
            "text":
"""profile = {
    "name": "Zion",
    "city": "Tulsa"
}

profile["hobby"] = "Coding"

profile["favorite_food"] = "Fried Rice"

print(profile)"""
        },

        {
            "page": 5,
            "type": "paragraph",
            "text":
            "You can add new keys or change existing values by assigning a new value."
        },


        {
            "page": 6,
            "type": "heading",
            "text": "5. Looping Through Collections"
        },

        {
            "page": 6,
            "type": "paragraph",
            "text":
            "Loops allow programs to analyze every item in a collection without writing repeated code."
        },

        {
            "page": 6,
            "type": "code",
            "text":
"""leaders = [
    "Angela Davis",
    "Malcolm X",
    "Cesar Chavez"
]

for leader in leaders:
    print(f"{leader} inspired change.")"""
        },

        {
            "page": 6,
            "type": "code",
            "text":
"""sneaker = {
    "brand": "Nike",
    "style": "Air Max",
    "year": 2023
}

for key, value in sneaker.items():
    print(key, value)"""
        },


        {
            "page": 7,
            "type": "heading",
            "text": "6. Working With JSON Data"
        },

        {
            "page": 7,
            "type": "paragraph",
            "text":
            "JSON is a common format used to transfer data between programs. "
            "Python can convert JSON text into dictionaries using json.loads()."
        },

        {
            "page": 7,
            "type": "code",
            "text":
"""import json

json_data = '{"name":"Maria","interests":["coding","music","basketball"]}'

person = json.loads(json_data)

print(person["name"])
print(person["interests"][1])"""
        },

        {
            "page": 7,
            "type": "tip",
            "text":
            "JSON looks similar to a Python dictionary because both store information using keys and values."
        },


        {
            "page": 8,
            "type": "heading",
            "text": "7. Data Structures in Real Applications"
        },

        {
            "page": 8,
            "type": "paragraph",
            "text":
            "Programs often combine lists and dictionaries to organize complex information. "
            "For example, language preservation tools can store words, translations, and audio files."
        },

        {
            "page": 8,
            "type": "code",
            "text":
"""word = {
    "original": "ᎣᏏᏲ",
    "english": "hello",
    "audio_clip": "osiyo.mp3"
}

print(word["english"])"""
        },


        {
            "page": 9,
            "type": "heading",
            "text": "Mini Debug Mission"
        },

        {
            "page": 9,
            "type": "paragraph",
            "text":
            "Find the mistake in this code:"
        },

        {
            "page": 9,
            "type": "code",
            "text":
"""fruits = [
    "apple",
    "orange",
    "banana"
]

print(fruits[3])"""
        },

        {
            "page": 9,
            "type": "tip",
            "text":
            "Lists start at index 0. A list with three items has indexes 0, 1, and 2."
        },

        {
            "page": 9,
            "type": "ide",
            "instructions":
            "Fix the indexing error so the program prints the last item in the list.",

            "starter_code":
"""fruits = [
    "apple",
    "orange",
    "banana"
]

print(fruits[3])
"""
        },


        {
            "page": 10,
            "type": "heading",
            "text": "Key Takeaways"
        },

        {
            "page": 10,
            "type": "list",
            "items": [
                "Lists store ordered collections and use indexes starting at 0.",
                "append() adds new items to lists.",
                "Dictionaries store information using key-value pairs.",
                "Loops help process every item in a collection.",
                "json.loads() converts JSON text into Python dictionaries."
            ]
        }

    ]
},
    "loops": {

    "id": "loops",

    "lesson_number": "4",

    "description": "Repeat tasks efficiently using for and while loops, ranges, and data processing techniques.",

    "title": "Loops",

    "blocks": [

        {
            "page": 1,
            "type": "heading",
            "text": "Unit 4: Loops"
        },

        {
            "page": 1,
            "type": "paragraph",
            "text":
            "By the end of this lesson, students will be able to use for and while loops, "
            "control loops with break and continue, understand range(), and process data "
            "from CSV files. Students will learn how computers repeat tasks efficiently "
            "and how loops are used in real-world data systems."
        },


        {
            "page": 1,
            "type": "heading",
            "text": "Vocabulary"
        },

        {
            "page": 1,
            "type": "list",
            "items": [
                "Loop - Code that repeats until a condition is met",
                "range() - A Python function that generates a sequence of numbers",
                "CSV - A spreadsheet-like file where values are separated by commas",
                "Iteration - One repetition of a loop",
                "break - A keyword that immediately exits a loop",
                "continue - A keyword that skips the current iteration"
            ]
        },


        {
            "page": 1,
            "type": "tip",
            "text":
            "Women of Color Spotlight: Lorena Mesa is a Latina Python Software Foundation "
            "chair who has helped improve Python communities. Dr. Gladys West is a Black "
            "mathematician whose work helped create modern GPS technology."
        },


        {
            "page": 2,
            "type": "heading",
            "text": "Why Do We Use Loops?"
        },


        {
            "page": 2,
            "type": "paragraph",
            "text":
            "Imagine you had to send the same message to 1,000 people. Instead of writing "
            "the same code 1,000 times, a loop lets the computer repeat instructions "
            "automatically."
        },


        {
            "page": 2,
            "type": "heading",
            "text": "For Loops"
        },


        {
            "page": 2,
            "type": "paragraph",
            "text":
            "A for loop is used when you know what you want to loop through. "
            "This can be a list, string, or range of numbers."
        },


        {
            "page": 2,
            "type": "code",
            "text":
"""artists = [
    "Rhapsody",
    "Peso Pluma",
    "Usher",
    "Jhené Aiko"
]

for artist in artists:
    print(f"{artist} stays on repeat!")
"""
        },


        {
            "page": 2,
            "type": "paragraph",
            "text":
            "Your Turn: Create a list of your favorite artists or songs. "
            "Use a for loop to print a message for each item."
        },


        {
            "page": 3,
            "type": "heading",
            "text": "Using range()"
        },


        {
            "page": 3,
            "type": "paragraph",
            "text":
            "The range() function creates a sequence of numbers. "
            "It is commonly used with for loops."
        },


        {
            "page": 3,
            "type": "code",
            "text":
"""for i in range(1, 6):
    print(f"Verse {i}")
"""
        },


        {
            "page": 3,
            "type": "paragraph",
            "text":
            "range(start, stop, step) allows you to control where counting begins, "
            "where it ends, and how much it changes each time."
        },


        {
            "page": 3,
            "type": "code",
            "text":
"""for number in range(10, 0, -1):
    print(number)

print("Let's go!")
"""
        },


        {
            "page": 4,
            "type": "heading",
            "text": "Break and Continue"
        },


        {
            "page": 4,
            "type": "paragraph",
            "text":
            "break stops a loop completely. continue skips the current iteration "
            "and moves to the next one."
        },


        {
            "page": 4,
            "type": "code",
            "text":
"""foods = [
    "Wings",
    "Tofu",
    "Pork",
    "Mac & Cheese"
]

for food in foods:

    if food == "Pork":
        continue

    print(food)
"""
        },


        {
            "page": 4,
            "type": "paragraph",
            "text":
            "Your Turn: Create a list and use continue to skip something. "
            "Then use break to stop when a certain item appears."
        },


        {
            "page": 5,
            "type": "heading",
            "text": "While Loops"
        },


        {
            "page": 5,
            "type": "paragraph",
            "text":
            "A while loop repeats while a condition remains True. "
            "Use while loops when you do not know exactly how many repetitions you need."
        },


        {
            "page": 5,
            "type": "code",
            "text":
"""energy = 5

while energy > 0:
    print("Still working!")
    energy -= 1

print("Break time!")
"""
        },


        {
            "page": 5,
            "type": "warning",
            "text":
            "Be careful! If the condition never becomes False, the loop will run forever."
        },


        {
            "page": 6,
            "type": "heading",
            "text": "Working With CSV Files"
        },


        {
            "page": 6,
            "type": "paragraph",
            "text":
            "CSV files store information in rows and columns. Python can read these files "
            "using the csv module."
        },


        {
            "page": 6,
            "type": "code",
            "text":
"""import csv

with open("students.csv") as file:

    reader = csv.DictReader(file)

    for row in reader:

        print(
            f"{row['name']} lives in {row['city']}"
        )
"""
        },


        {
            "page": 6,
            "type": "tip",
            "text":
            "Loops are powerful because they allow programmers to analyze thousands "
            "of rows of information quickly."
        },


        {
            "page": 7,
            "type": "heading",
            "text": "Nested Loops"
        },


        {
            "page": 7,
            "type": "paragraph",
            "text":
            "A nested loop is a loop inside another loop. They are useful for searching "
            "through groups of data, such as folders inside folders."
        },


        {
            "page": 7,
            "type": "code",
            "text":
"""domains = [
    ".edu",
    ".gov",
    ".africa"
]

pages = [
    "/home",
    "/research",
    "/team"
]


for domain in domains:

    for page in pages:

        print(
            f"https://www{domain}{page}"
        )
"""
        },


        {
            "page": 8,
            "type": "heading",
            "text": "Searching With Loops"
        },


        {
            "page": 8,
            "type": "paragraph",
            "text":
            "Linear search checks each item one by one. Binary search is faster because "
            "it repeatedly cuts a sorted list in half."
        },


        {
            "page": 8,
            "type": "code",
            "text":
"""left = 0
right = len(arr) - 1

while left <= right:

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

return -1
"""
        },


        {
            "page": 9,
            "type": "heading",
            "text": "Debug Challenge"
        },


        {
            "page": 9,
            "type": "paragraph",
            "text":
            "Find the error in this code:"
        },


        {
            "page": 9,
            "type": "code",
            "text":
"""for i in range(5)

    print(i)
"""
        },


        {
            "page": 9,
            "type": "paragraph",
            "text":
            "Hint: Python requires punctuation after certain statements."
        },


        {
            "page": 9,
            "type": "code",
            "text":
"""# Fixed version

for i in range(5):

    print(i)
"""
        },


        {
            "page": 10,
            "type": "heading",
            "text": "Practice Challenge"
        },


        {
            "page": 10,
            "type": "paragraph",
            "text":
            "Create a program that searches through a list of names and prints only "
            "names that start with the letter A."
        },


        {
            "page": 10,
            "type": "code",
            "text":
"""names = [
    "Ali",
    "Beth",
    "Andrew",
    "Zane",
    "Angela"
]

# Write your loop here
"""
        }

    ]
},
    "functions_modularity": {

        "id": "functions_modularity",

        "lesson_number": "5",

        "title": "Functions & Modularity",

        "description": "Write reusable functions with parameters and returns, document them with docstrings, import helper modules, and refactor repeated code.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Lesson 5 - Functions & Modularity"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Estimated Time: 2 weeks"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Learning Objectives"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Write reusable functions using def and return.",
                    "Explain the difference between a parameter and an argument.",
                    "Draw a scope diagram showing where a variable is visible.",
                    "Write a clear one-line docstring for a function.",
                    "Import and use functions from a separate module.",
                    "Refactor repeated code into a function."
                ]
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Word Bank"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">def</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">parameter / argument</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">scope</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">module / import</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">docstring</span>'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function</span> is a reusable block of code you can call by name. You start a function definition with the <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">def</span> keyword, and you decide what value it hands back using return.'
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">parameter</span> is the input a function expects when you define it; the <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">argument</span> is the actual value you pass in when you call it. In def add(a, b), a and b are parameters. In add(5, 7), 5 and 7 are arguments.'
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">Scope</span> is where a variable is visible in your code. A variable created inside a function only exists while that function is running - it disappears once the function returns.'
            },

            {
                "page": 1,
                "type": "code",
                "language": "python",
                "text":
"""def add(a, b):
    total = a + b   # total only exists inside add()
    return total

print(add(2, 3))
print(total)   # this line crashes - total is out of scope here"""
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "A scope diagram is just a box drawn around each function call. Any variable created inside the box only lives there - once the box closes, the variable is gone."
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">module</span> is a separate file of functions you can bring into your program with <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">import</span>, and a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">docstring</span> is a short description written in triple quotes at the top of a function, explaining what it does.'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Focus: Indigenous Data Sovereignty"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "This unit's focus is Indigenous data sovereignty - the idea that a community should control the data collected about its own people, lands, and culture. A Python dictionary is just a lookup table: each key belongs to whoever controls it, and it only gives up its value to someone with the right access. A tribal database works the same way - the nation that holds the keys decides who gets to see the values."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Spotlight: Stephanie Russo Carroll"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Stephanie Russo Carroll, Ahtna and a citizen of the Native Village of Kluti-Kaah in Alaska, is a scholar of Indigenous data governance at the University of Arizona. She co-founded the US Indigenous Data Sovereignty Network and helped write the CARE Principles for Indigenous Data Governance, which hold that Indigenous nations - not outside researchers or companies - should decide how data about their own communities gets collected, stored, and used."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Spotlight: Michael Running Wolf"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Michael Running Wolf, a citizen of the Northern Cheyenne Tribe, grew up in Birney, Montana, without consistent electricity. He later worked as a software engineer on Amazon\'s Alexa team before founding Indigenous in AI and the FLAIR project, building automatic speech recognition tools so endangered Indigenous languages can be spoken to - and understood by - AI.<sup>1</sup>'
            },

            {
                "page": 1,
                "type": "footnote",
                "number": "1",
                "text": "Read more: Walking in two worlds - how an Indigenous computer scientist is using AI to preserve threatened languages, Nature (2025). https://www.nature.com/articles/d41586-025-01354-y"
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Guided Practice 1 - Make It a Function"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text": "Every function starts with def, a name, parentheses, and a colon."
            },

            {
                "page": 2,
                "type": "code",
                "language": "python",
                "text":
"""def greet():
    print("Peace and power to you.")

greet()"""
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""def morning_motivation():
    # print your favorite affirmation or quote here
    pass

morning_motivation()""",
                "instructions":
                "Write a function called morning_motivation() that prints your favorite affirmation or quote. Bonus: call it at the very start of your script to kick things off with good energy."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Guided Practice 2 - Build Your Own Calculator"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text": "A function can also hand a value back to whoever called it, using return."
            },

            {
                "page": 2,
                "type": "code",
                "language": "python",
                "text":
"""def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)"""
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""def multiply(a, b):
    # return the product of a and b
    pass

print(multiply(3, 8))
print(multiply(10, 0))""",
                "instructions":
                "Write a function called multiply that takes two numbers and returns the product. Try calling it with different values, like multiply(3, 8) and multiply(10, 0)."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Guided Practice 3 - Customize the Message"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text": "Functions can take more than one parameter at a time."
            },

            {
                "page": 2,
                "type": "code",
                "language": "python",
                "text":
"""def shoutout(name, talent):
    return f"Shoutout to {name} for their skills in {talent}!"

print(shoutout("Jordan", "design"))"""
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""def shoutout_admire(name, why_you_admire):
    # return a shoutout string using both parameters
    pass

print(shoutout_admire("", ""))""",
                "instructions":
                "Write your own version that gives a shoutout to someone you admire in your community or friend group. Use two parameters: name and why_you_admire."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Guided Practice 4 - Say It Clearly"
            },

            {
                "page": 3,
                "type": "paragraph",
                "text": "A docstring is a short description in triple quotes, right under the def line, explaining what the function does."
            },

            {
                "page": 3,
                "type": "code",
                "language": "python",
                "text":
'''def calculate_average(score1, score2):
    """
    Calculates the average of two scores.
    """
    return (score1 + score2) / 2

print(calculate_average(85, 90))'''
            },

            {
                "page": 3,
                "type": "ide",
                "language": "python",
                "starter_code":
'''def my_full_name():
    """
    # write a one-line docstring here
    """
    # return your full name
    pass

print(my_full_name())''',
                "instructions":
                "Write a function that returns your full name. Add a docstring that explains what the function does."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Guided Practice 5 - Call Me Back"
            },

            {
                "page": 3,
                "type": "code",
                "language": "python",
                "text":
"""def favorite_song():
    return "Alright by Kendrick Lamar"

print(favorite_song())"""
            },

            {
                "page": 3,
                "type": "ide",
                "language": "python",
                "starter_code":
"""def favorite_show():
    # return the title of a show or YouTube series you love
    pass

print(favorite_show())""",
                "instructions":
                "Create a function called favorite_show() that returns the title of a show or YouTube series you love. Test it with print() and make sure it works as expected."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Guided Practice 6 - Mini Debug Mission"
            },

            {
                "page": 3,
                "type": "paragraph",
                "text": "Can you fix this broken function?"
            },

            {
                "page": 3,
                "type": "code",
                "language": "python",
                "text":
"""def hype(name)
    print("Let's go", name + "!")"""
            },

            {
                "page": 3,
                "type": "tip",
                "text": "Check your function definition carefully - what's missing?"
            },

            {
                "page": 3,
                "type": "ide",
                "language": "python",
                "starter_code":
"""def hype(name):
    print("Let's go", name + "!")

hype("your friend's name here")""",
                "instructions":
                "Fix the code so it runs correctly and hypes up a friend of yours."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Reflection Prompts"
            },

            {
                "page": 3,
                "type": "list",
                "items": [
                    "How does breaking your code into functions make it easier to work with - like breaking a big task into smaller ones in life?",
                    "If you could write a function that describes who you are, what would it return?",
                    "Why is it important to test and document your functions, especially if someone else will use your code later?",
                    "Think of a community need, like helping someone find a resource or plan an event. How could functions help automate or simplify that task?"
                ]
            },

            {
                "page": 4,
                "type": "heading",
                "text": "Importing Helper Modules"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text":
                "Once you have functions you use often, you can move them into their own file - a module - and import them wherever you need them. This is how programmers avoid repeating themselves across projects."
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""# utils.py
def square(n):
    \"\"\"Returns n squared.\"\"\"
    return n * n"""
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""# main.py
from utils import square

print(square(4))"""
            },

            {
                "page": 4,
                "type": "warning",
                "text":
                "utils.py and main.py must be saved in the same folder, or the import will fail with a ModuleNotFoundError."
            },

            {
                "page": 4,
                "type": "heading",
                "text": "Unit 5 Quiz - Functions & Modularity"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "Read each question carefully, then choose the correct answer, write your own code, or explain the concept."
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "1. Fill in the Blank (2 points): A function helps programmers to __________ complex problems and encourages code reuse."
            },

            {
                "page": 4,
                "type": "tip",
                "text": "Answer: break down"
            },

            {
                "page": 4,
                "type": "quiz",
                "question": "2. Multiple Choice (2 points): What does the return keyword do in a Python function?",
                "options": [
                    "A. It prints the result to the console",
                    "B. It ends the function and gives a value back to the caller",
                    "C. It stores data in a list",
                    "D. It asks the user for input"
                ],
                "answer": "B. It ends the function and gives a value back to the caller."
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "3. Debug This Code (5 points): Find and fix the errors in the function below, which is supposed to add two numbers and return the result."
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""def add_numbers(a, b)
    sum = a + b
    return sum

print(add_numbers(3 5))"""
            },

            {
                "page": 4,
                "type": "exercise",
                "problem": "debug_add_numbers"
            },

            {
                "page": 4,
                "type": "tip",
                "text":
                "Answer: def add_numbers(a, b):  (missing colon) ... print(add_numbers(3, 5))  (missing comma between arguments)"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text":
                "4. Code the Function (5 points): Write a function called greet_user that takes one parameter, name, and returns the string \"Hello, [name]!\" Example: greet_user(\"Alex\") returns \"Hello, Alex!\""
            },

            {
                "page": 4,
                "type": "exercise",
                "problem": "greet_user"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "5. Short Answer (2 points): What is a parameter in a function? Why are parameters important?"
            },

            {
                "page": 4,
                "type": "tip",
                "text":
                "Answer: A parameter is a variable listed in a function's definition that receives data when the function is called. Parameters matter because they let a function accept input, making it flexible and reusable for different values."
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "6. Code Completion (4 points): Complete the function below to return the square of a number. Example: square_number(4) returns 16."
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""def square_number(num):
    # your code here
    pass"""
            },

            {
                "page": 4,
                "type": "exercise",
                "problem": "square_number"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text":
                "7. Write a Function with a Docstring (5 points): Write a function get_area that calculates the area of a rectangle. It should take two parameters, length and width, return the area, and include a docstring describing what the function does and its parameters."
            },

            {
                "page": 4,
                "type": "exercise",
                "problem": "get_area_rectangle"
            },

            {
                "page": 4,
                "type": "quiz",
                "question": "8. Multiple Choice (2 points): Which of the following is the correct way to call a function named calculate_tax with one argument, 100?",
                "options": [
                    "A. def calculate_tax(100)",
                    "B. calculate_tax = 100",
                    "C. calculate_tax(100)",
                    "D. return calculate_tax(100)"
                ],
                "answer": "C. calculate_tax(100)"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text": "9. Fill in the Blank (2 points): The opposite of calling a function is __________ a function, where you define what it does and how it works."
            },

            {
                "page": 4,
                "type": "tip",
                "text": "Answer: defining"
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Extension: The GPS Toolkit"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text":
                "Dr. Gladys West's work on satellite geodesy helped make GPS possible, by breaking an enormous problem into smaller functions, like calculate_distance() and adjust_for_relativity(). Lorena Mesa, an open-source Python community leader, builds tools that often take direct user input, like formatting a speaker's name."
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Part 1 - Functions as Building Blocks"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text":
                "Why is breaking a large program into small functions, the way Dr. West's team broke GPS into pieces, better than writing one giant program?"
            },

            {
                "page": 5,
                "type": "tip",
                "text":
                "Answer: it's easier to debug and test individual pieces, the code becomes reusable, multiple developers can work on different functions at once, and it's simpler to maintain and update over time."
            },

            {
                "page": 5,
                "type": "paragraph",
                "text": "Write a function validate_coordinates(lat, long) that returns True if the latitude is between -90 and 90."
            },

            {
                "page": 5,
                "type": "exercise",
                "problem": "validate_coordinates"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text": "Debug this function - calling it raises a TypeError."
            },

            {
                "page": 5,
                "type": "code",
                "language": "python",
                "text":
"""def gps_accuracy(error_margin):
    print("Accuracy: " + error_margin + " meters")"""
            },

            {
                "page": 5,
                "type": "tip",
                "text":
                "Answer: error_margin is probably a number, and you can't concatenate a string with a number using +. Wrap it with str(): print(\"Accuracy: \" + str(error_margin) + \" meters\")"
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Part 2 - Parameters, Arguments, and Returns"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text": "Write a function that returns a speaker's name in the format \"Mesa, Lorena\" - last name, then first name."
            },

            {
                "page": 5,
                "type": "exercise",
                "problem": "format_name"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text":
                "If a function like calculate_satellite_position() needs Earth's curvature to do its math, should it (A) calculate that value internally, or (B) accept it as a parameter? Justify your answer."
            },

            {
                "page": 5,
                "type": "tip",
                "text":
                "Answer: (B) accept it as a parameter. This keeps the function flexible for different scenarios, follows the single-responsibility principle, and makes it far easier to test with different input values."
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Part 3 - Designing in Modules"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text": "Split the code below into three functions: get_user_coordinates(), calculate_distance(), and display_result()."
            },

            {
                "page": 5,
                "type": "code",
                "language": "python",
                "text":
"""lat1, long1 = 40.7, -74.0
lat2, long2 = 34.0, -118.2
distance = ((lat2 - lat1)**2 + (long2 - long1)**2)**0.5
print(f"Distance: {distance}")"""
            },

            {
                "page": 5,
                "type": "exercise",
                "problem": "refactor_gps_distance"
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Part 4 - Lab: Tech Conference Scheduler"
            },

            {
                "page": 5,
                "type": "paragraph",
                "text":
                "Objective: use functions to manage speaker logistics. Fill in the functions below based on their docstrings, and feel free to write more functions if you think they're useful. This project is exploratory, not strictly technical."
            },

            {
                "page": 5,
                "type": "code",
                "language": "python",
                "text":
'''def assign_room(speaker, topic):
    """Returns "Main Stage" for keynotes, else "Breakout 1"."""
    pass

def send_reminder(email):
    """Mock email sender (print a confirmation)."""
    pass

speakers = [
    {"name": "Lorena Mesa", "topic": "Open-Source Leadership"},
    {"name": "Dr. West", "topic": "GPS History"}
]'''
            },

            {
                "page": 5,
                "type": "exercise",
                "problem": "tech_conference_scheduler"
            },

            {
                "page": 6,
                "type": "heading",
                "text": "Explore More: Hangman, Part 1"
            },

            {
                "page": 6,
                "type": "paragraph",
                "text":
                "Here's a complete mini-project that leans entirely on functions: a word-guessing game. Notice how pick_word(), display_word(), and play_hangman() each have one clear job, and how play_hangman() calls the other two to get its work done."
            },

            {
                "page": 6,
                "type": "code",
                "language": "python",
                "text":
'''import random

def pick_word():
    """Returns a random word from a predefined list."""
    words = ["apple", "banana", "python", "hangman", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """Shows the word with underscores for unguessed letters."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    """Main game function."""
    word = pick_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print("\\n" + display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print(f"\\nYou won! The word was: {word}")
            return

    print(f"\\nGame over! The word was: {word}")

play_hangman()'''
            },

            {
                "page": 6,
                "type": "tip",
                "text":
                "Try it yourself: add a function that tracks a high score, or one that lets a player choose a difficulty level by picking from a longer or shorter word list."
            },

            {
                "page": 6,
                "type": "exercise",
                "problem": "hangman_part_2"
            }

        ]
    },
    "recursion_capstone": {

        "id": "recursion_capstone",

        "lesson_number": "6",

        "title": "Recursion & the Capstone",

        "description": "Trace and implement recursive functions, understand the call stack, and bring every skill from this course together into a community capstone project.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Lesson 6 - Recursion & the Capstone"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Estimated Time: 30-40 minutes"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Learning Objectives"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Trace and implement a simple recursive function.",
                    "Identify the base case and the recursive call in a function.",
                    "Sketch the call stack for factorial(4).",
                    "Convert an iterative family-tree printer into a recursive one.",
                    "Plan a capstone project using a checklist of required constructs.",
                    "Refactor code for clarity by adding docstrings and comments.",
                    "Deliver a 2-minute capstone demo and capture peer feedback."
                ]
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Word Bank"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">recursion</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">base case</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">call stack</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">capstone project</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">refactor</span>'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Imagine asking a grandparent to tell you a family story. They tell you their part, then say, "for the rest, ask your great-aunt - she knows what came before me." Your great-aunt does the same thing, pointing further back, until someone finally says, "that\'s the beginning - there\'s no one before me." That is exactly how a recursive function works: each step solves a small piece and hands the rest down, until someone finally stops the chain.'
            },

            {
                "page": 1,
                "type": "quote",
                "text":
                "Recursion = passing down knowledge. - inspired by Roy Clay Sr., known as the \"Godfather of Silicon Valley\""
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 1 - What Is Recursion?"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">Recursion</span> is a function calling itself to solve a smaller piece of the same problem. Every recursive function needs a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">base case</span> - the simple situation where the function stops calling itself. Without one, the function would call itself forever.'
            },

            {
                "page": 1,
                "type": "code",
                "language": "python",
                "text":
"""def factorial(n):
    # base case: the "no one before me" moment
    if n == 0:
        return 1
    # recursive call: hand off a smaller version of the problem
    return n * factorial(n - 1)"""
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "Every recursive function needs two things: a base case that stops it, and a recursive call that hands off a smaller version of the same problem."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 2 - Tracing the Call Stack"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'The <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">call stack</span> is the list of function calls the computer is managing at any moment.<sup>1</sup> Each call waits, paused, for the next one to finish. Here is the full trace for factorial(4) - the stack grows downward as calls are made, then collapses back upward as each call returns its answer:'
            },

            {
                "page": 1,
                "type": "code",
                "language": "text",
                "text":
"""factorial(4)
  factorial(3)
    factorial(2)
      factorial(1)
        factorial(0) -> base case hit, returns 1
      returns 1 * 1 = 1
    returns 2 * 1 = 2
  returns 3 * 2 = 6
returns 4 * 6 = 24"""
            },

            {
                "page": 1,
                "type": "footnote",
                "number": "1",
                "text": "The call stack is managed automatically by the Python interpreter - you never have to build it yourself."
            },

            {
                "page": 1,
                "type": "warning",
                "text":
                "If a recursive function never reaches its base case, the call stack keeps growing until Python runs out of room and raises a RecursionError. Always double-check that every recursive call moves toward the base case."
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "In the trace above, which call is the base case?",
                "options": [
                    "A. factorial(4)",
                    "B. factorial(2)",
                    "C. factorial(0)",
                    "D. factorial(1)"
                ],
                "answer": "C. factorial(0)"
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Section 3 - From Loops to Lineage: The Family-Tree Printer"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "An iterative printer walks a family tree with a loop and its own manual stack. A recursive printer lets the call stack do that bookkeeping for you - each generation just prints itself and hands the next generation down."
            },

            {
                "page": 2,
                "type": "code",
                "language": "python",
                "text":
"""# Iterative
def print_tree(root):
    stack = [(root, 0)]
    while stack:
        person, depth = stack.pop()
        print("  " * depth + person.name)
        for child in person.children:
            stack.append((child, depth + 1))

# Recursive
def print_tree(person, depth=0):
    # base case: a person with no children simply prints and stops
    print("  " * depth + person.name)
    for child in person.children:
        print_tree(child, depth + 1)"""
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "Notice the recursive version has no explicit stack list - the call stack is doing that job invisibly. Your task: rewrite one iterative function from an earlier unit into recursive form, and label its base case in a comment."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Section 4 - Planning Your Capstone"
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Your <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">capstone project</span> is a final project that showcases everything you\'ve learned this course. Before writing a line of code, plan against this checklist, then <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">refactor</span> - improve the code without changing what it does - and deliver a 2-minute demo.'
            },

            {
                "page": 2,
                "type": "list",
                "items": [
                    "At least one recursive function with a clearly labeled base case.",
                    "A data structure from this unit - a list, tree, or heap - used meaningfully.",
                    "Clear docstrings and comments explaining each function.",
                    "A 2-minute demo, plus one piece of peer feedback you collect afterward."
                ]
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Section 5 - Passing It Down"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Recursion works because each generation trusts the next one to finish the job. Roy Clay Sr., the \"Black Godfather of Silicon Valley,\" led the team that built HP's first computer and spent his career mentoring the next generation of Black engineers. Fred Begay, the first Native American to earn a Ph.D. in physics, researched nuclear fusion at Los Alamos while mentoring Indigenous students in STEM - drawing on the Navajo stories his own parents passed down to him."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Recap Questions"
            },

            {
                "page": 2,
                "type": "quiz",
                "question": "Fred Begay combined Navajo tradition with physics. Which comparison best matches recursion and iteration to two things he grew up with?",
                "options": [
                    "A. Recursion is like oral storytelling, where each call adds a layer; iteration is like a lab experiment, repeated step-by-step.",
                    "B. Recursion is like a lab experiment; iteration is like oral storytelling.",
                    "C. Both recursion and iteration work like oral storytelling.",
                    "D. Neither recursion nor iteration resembles either tradition."
                ],
                "answer": "A. Recursion is like oral storytelling, where each call adds a layer; iteration is like a lab experiment, repeated step-by-step."
            },

            {
                "page": 2,
                "type": "code",
                "language": "python",
                "text":
"""def echo(word, times):
    if times > 0:
        print(word)
        echo(word, times - 1)"""
            },

            {
                "page": 2,
                "type": "quiz",
                "question": "What does echo(\"hi\", 3) print?",
                "options": [
                    "A. hi (once)",
                    "B. hi hi hi (three times, one per line)",
                    "C. hi hi hi hi (four times)",
                    "D. Nothing - it raises a RecursionError"
                ],
                "answer": "B. hi hi hi (three times, one per line)"
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 2,
                "type": "list",
                "items": [
                    "A recursive function needs a base case and a recursive call.",
                    "The call stack tracks every waiting call until the base case is hit, then unwinds those calls one by one.",
                    "Recursion can replace a loop plus a manual stack - the call stack does that bookkeeping for you.",
                    "Passing down knowledge - from Roy Clay Sr. to Fred Begay to your own capstone - is what keeps a field like computer science moving forward."
                ]
            }

        ]
    }
}


def get_lesson(id):
    return LESSONS.get(id)
