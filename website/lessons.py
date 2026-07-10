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
                "type": "paragraph",
                "text":
                "Every programmer starts with a simple program. Type the following into the editor:"
            },

            {
                "page": 1,
                "type": "code",
                "language": "python",
                "text":
"""print("Hello, Tulsa!")"""
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Or personalize it:"
            },

            {
                "page": 1,
                "type": "code",
                "language": "python",
                "text":
"""print("Hello, Little Haiti!")
print("Hello, Dine Nation!")"""
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
                "answer": "B. Displays information on the screen."
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


    "data_types": {

        "id": "data_types",

        "lesson_number": "2",

        "title": "Data Types",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "What are Data Types?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Data types describe the kind of information a variable stores. Python automatically determines the type of a value when it is assigned."
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""name = "Alex"
age = 15
height = 5.8

print(name)
print(age)
print(height)""",
                "instructions":
                "Change the values of the variables and observe how the output changes."
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "The variable name stores text (a string), age stores a whole number (an integer), and height stores a decimal number (a float)."
            },

            {
                "page": 2,
                "type": "image",
                "src": "/static/images/data_types.png",
                "caption": "Python has different types of data for storing information."
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "Use the type() function to check what type of value a variable contains."
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""x = 10

print(type(x))""",
                "instructions":
                "Change the value of x and check how Python identifies different data types."
            },

            {
                "page": 2,
                "type": "warning",
                "text":
                "Remember that strings must be surrounded by quotes."
            },

            {
                "page": 3,
                "type": "exercise",
                "problem": "create_variables"
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
    },
    "conditionals": {

    "id": "conditionals",

    "lesson_number": "2",

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
    }
}


def get_lesson(id):
    return LESSONS.get(id)
