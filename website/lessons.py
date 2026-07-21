# =========================
# Lesson definitions
# =========================

LESSONS = {
    "why_python": {

        "id": "why_python",

        "lesson_number": "0",

        "title": "Why Python?",

        "description": "Lesson 0.0 - Why Python? Learn what Python is, why it matters, and how programming can help solve real community problems.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Unit 0 - Why Python?"
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

            {'page': 1,
             'type': 'quiz',
             'question': 'Which statement best describes Python?',
             'options': ['A. A programming language used to give computers instructions',
                         'B. A type of computer',
                         'C. A web browser',
                         'D. An operating system'],
             'answer': 'A. A programming language used to give computers instructions'},

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

            {'page': 1,
             'type': 'quiz',
             'question': 'Which of these is an example of using programming to help a community?',
             'options': ['A. Automatically organizing volunteer schedules',
                         'B. All of the above',
                         'C. Building a digital language dictionary',
                         'D. Analyzing public community data'],
             'answer': 'B. All of the above'},

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

            {'page': 1,
             'type': 'quiz',
             'question': 'What does Garbage In, Garbage Out mean?',
             'options': ['A. Computers sometimes become broken',
                         'B. Computers automatically fix mistakes',
                         'C. Computers only produce correct results when given correct instructions',
                         'D. Python deletes bad programs'],
             'answer': 'C. Computers only produce correct results when given correct instructions'},

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

            {'page': 1,
             'type': 'quiz',
             'question': 'What does the print() function do?',
             'options': ['A. Deletes text',
                         'B. Saves a file',
                         'C. Creates a website',
                         'D. Displays information on the screen'],
             'answer': 'D. Displays information on the screen'},

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
            },
            {
                "page": 2,
                "type": "exercise",
                "problem": "print_greeting"
            }

        ]
    },

    "functions_preview": {

        "id": "functions_preview",

        "lesson_number": "0.5",

        "title": "Read This Before Exercises",

        "description": "Preview what Python functions look like before starting coding exercises.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Lesson 0.5 - Read This Before Doing Any Exercises"
            },


            {
                "page": 1,
                "type": "heading",
                "text": "Prerequisites"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Unit 0"
                ]
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
                    "Recognize what a Python function looks like.",
                    "Identify the purpose of def and return.",
                    "Understand that every coding exercise in this course will ask you to complete a function."
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
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">def</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function name</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">parameter</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">colon</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">indentation</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">docstring</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">return</span>'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Before we begin writing Python programs, there is one important piece of syntax you will see throughout this course: functions."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Do not worry if everything in this lesson does not make sense yet. The goal is simply to become familiar with what functions look like."
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "In Lesson 5, you will learn how functions work in much greater detail. For now, think of a function as a small program that performs one specific task."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "What is a Function?"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function</span> is a reusable block of code that performs a specific task.'
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Throughout this course, nearly every coding exercise will ask you to complete a function."
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""def add_one(x):
    return x + 1
"""
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Although this may look unfamiliar, do not worry. We can break it apart."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "The Parts of a Function"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'The keyword <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">def</span> tells Python that we are defining a new function.'
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""def add_one(x):
"""
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Every function has a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">function name</span>. In this example, the function name is add_one.'
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "Good function names describe what the function does."
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Inside the parentheses is a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">parameter</span>. A parameter is information that the function receives. For now, you can think of it as the function input.'
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Every function definition ends with a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">colon</span>. The colon tells Python that an indented block of code follows.'
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Everything inside the function is indented. Python uses <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">indentation</span> to determine which lines belong to the function.'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Docstrings"
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""def add_one(x):
    \"\"\"
    Return x + 1.
    \"\"\"
"""
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'This block of text is called a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">docstring</span>, short for documentation string. A docstring explains what a function does, what information it expects, and what it returns.'
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Throughout this course, many exercises will include a docstring to describe what your function should accomplish. You do not need to write your own docstrings yet, but you should read them carefully."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Return"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'The keyword <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">return</span> sends a value back to whoever called the function.'
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""return x + 1
"""
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "In this example, the function gives back the value of x + 1. You will learn much more about return when we study functions later in the course."
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Why Are We Using Functions?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Functions help programmers organize code into small, reusable pieces. For this course, every coding exercise will already provide you with the function definition."
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""def square(x):
    \"\"\"
    Return the square of x.
    \"\"\"
    # Your code here
    pass
"""
            },

            {
                "page": 1,
                "type": "warning",
                "text":
                "Your job is not to write the function definition. Instead, you will write the code inside the function."
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'Which keyword tells Python that you are defining a function?',
             'options': ['A. def', 'B. print', 'C. return', 'D. input'],
             'answer': 'A. def'},

            {'page': 1,
             'type': 'quiz',
             'question': 'What does the return keyword do?',
             'options': ['A. Prints a message to the screen.',
                         'B. Sends a value back from the function.',
                         'C. Nothing.',
                         'D. Creates a variable.'],
             'answer': 'B. Sends a value back from the function.'},

            {
                "page": 1,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "A function is a reusable block of code.",
                    "Functions begin with the keyword def.",
                    "Parameters are inputs to a function.",
                    "The keyword return sends a result back.",
                    "For now, you only need to recognize the structure of a function.",
                    "In Lesson 5, you will learn how to write and use functions in depth."
                ]
            }

        ]
    },

    "variables": {

        "id": "variables",

        "lesson_number": "1",

        "description": "Lesson 1.0 - Variables & Data Types. Lesson 1.1 - Using Variables.",

        "title": "Variables & Data Types",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Unit 1 - Variables & Data Types"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Lesson 1.0 - Storing Information with Variables"
            },


            {
                "page": 1,
                "type": "heading",
                "text": "Prerequisites"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Unit 0"
                ]
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
                    "Explain what a variable is.",
                    "Declare variables using integers, floats, strings, and booleans.",
                    "Use the print() function.",
                    "Write comments.",
                    "Follow Python variable naming conventions."
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
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">variables</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">int</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">float</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">str</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">bool</span>'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Imagine trying to remember every customer's order at a food truck without writing anything down."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Programming has the same problem. A computer needs a place to store information so it can use it later. Those storage locations are called variables."
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'Think of <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">variables</span> as names given to values that programs use to remember information.'
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Section 1 - What is a Variable?"
            },

            {
                "page": 1,
                "type": "rich_paragraph",
                "html":
                'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">variable</span> is a named location that stores data.'
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""name = "Ariana"

# The variable is name
# The value stored is "Ariana"
"""
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Think of a variable like a labeled storage box. Instead of remembering information ourselves, we let the computer remember it."
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'What is a variable?',
             'options': ['A. A programming language',
                         'B. A computer',
                         'C. A named location that stores information',
                         'D. A keyboard'],
             'answer': 'C. A named location that stores information'},

            {
                "page": 1,
                "type": "heading",
                "text": "Section 2 - Common Data Types"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Python stores different kinds of information. Each kind has a data type."
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "int - whole numbers, like 7",
                    "float - decimal numbers, like 3.14",
                    "str - text, like \"Tulsa\"",
                    "bool - True or False values"
                ]
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""age = 16
height = 5.8
city = "Tulsa"
student = True
"""
            },

            {
                "page": 1,
                "type": "ide",
                "instructions":
                "Create one string, one integer, one float, and one boolean. Run the code to see your values print.",
                "starter_code":
"""name = "Chenise"
favorite_number = 2
bank_balance = 0.05
is_tall = True

print(name)
print(favorite_number)
print(bank_balance)
print(is_tall)
"""
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "Python variable names cannot contain spaces. Programmers often use underscores to stand in for spaces, like favorite_city."
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'Which variable stores a float?',
             'options': ['A. age = 17', 'B. name = "Jordan"', 'C. student = False', 'D. price = 12.99'],
             'answer': 'D. price = 12.99'},

            {
                "page": 1,
                "type": "heading",
                "text": "Section 3 - Printing Information"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Programs often need to display information. Python uses print() to show information on the screen."
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""name = "Jordan"
print(name)

# Output:
# Jordan
"""
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'What does print(age) do?',
             'options': ['A. Displays the value stored inside age',
                         'B. Deletes age',
                         'C. Creates a new variable',
                         'D. Changes age'],
             'answer': 'A. Displays the value stored inside age'},

            {
                "page": 1,
                "type": "heading",
                "text": "Section 4 - Comments"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Comments are notes for programmers. They help humans understand the program without needing to read every line closely."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text": "Python ignores comments when the program runs."
            },

            {
                "page": 1,
                "type": "code",
                "text":
"""# This stores the customer's name
customer = "Maria"
"""
            },

            {
                "page": 1,
                "type": "tip",
                "text":
                "Good comments explain why something is happening. They should not simply repeat what the code already says."
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'Which line is a comment?',
             'options': ['A. name = "Alex"', "B. # Store customer's name", 'C. print(name)', 'D. True'],
             'answer': "B. # Store customer's name"},

            {
                "page": 1,
                "type": "heading",
                "text": "Section 5 - Naming Variables"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Good variable names make programs easier to read."
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Good examples: customer_name, favorite_food, price, total_cost",
                    "Poor examples: x, asdf, 123name, favorite food",
                    "Use letters, numbers, and underscores.",
                    "Do not begin with a number.",
                    "Do not use spaces.",
                    "Be descriptive."
                ]
            },

            {
                "page": 1,
                "type": "warning",
                "text":
                "Some words already have special meaning in Python. Avoid using names like class, print, or True for your variables."
            },

            {'page': 1,
             'type': 'quiz',
             'question': 'Which is a valid variable name?',
             'options': ['A. 2dogs', 'B. favorite food', 'C. favorite_food', 'D. class'],
             'answer': 'C. favorite_food'},

            {
                "page": 1,
                "type": "heading",
                "text": "Spotlight - Mary G. Ross"
            },

            {'page': 1,
 'type': 'paragraph',
 'text': 'Mary G. Ross was the first known Indigenous American female engineer, and she was from '
         'Oklahoma.'},
            {'page': 1,
 'type': 'paragraph',
 'text': 'Working at Lockheed, she contributed to aerospace research and helped advance projects '
         'that influenced the Apollo space program.'},
            {'page': 1,
 'type': 'paragraph',
 'text': 'Like engineers today, she solved complex problems by organizing information carefully - '
         'a skill that programming also requires.'},

            {
                "page": 1,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "Variables store information.",
                    "Python has different data types.",
                    "print() displays information.",
                    "Comments help humans understand code.",
                    "Good variable names make programs easier to read."
                ]
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Preview"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Next you'll learn how programs can receive information from users and perform calculations."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Lesson 1.1 - Using Variables"
            },


            {
                "page": 2,
                "type": "heading",
                "text": "Learning Objectives"
            },

            {
                "page": 2,
                "type": "list",
                "items": [
                    "Gather user input using input().",
                    "Perform arithmetic.",
                    "Concatenate strings.",
                    "Use f-strings.",
                    "Use basic string methods.",
                    "Build a simple food truck ordering program."
                ]
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Word Bank"
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">input()</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">arithmetic</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">operator</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">string concatenation</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">f-string</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">string methods</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">sequence</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">index</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">zero-based indexing</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">slicing</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">step</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">negative index</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">reverse</span> &nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">immutable</span>'
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Introduction"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "In the previous lesson, you learned how to create variables and store information inside them. Programs become much more useful when the information they store can change."
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Picture this: you're opening a food ordering app, and every customer has a different name, orders different meals, and buys different quantities. It would not make sense to write a new program for every single customer."
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Instead, the program asks the user for information and stores their responses in variables. This is where <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">input()</span> comes in.'
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Section 1 - User Input"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "In the previous lesson, every value in our program was written by the programmer. This works, but it means every time someone new uses the program, we would have to edit the code ourselves."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""name = "Jordan"

name = input("What is your name? ")
"""
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "When the program reaches input(), it pauses and waits for the user to type something. Whatever the user types is stored inside the variable."
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'What does input() do?',
             'options': ['A. Prints text',
                         'B. Deletes variables',
                         'C. Creates a comment',
                         'D. Receives information from the user'],
             'answer': 'D. Receives information from the user'},

            {
                "page": 2,
                "type": "heading",
                "text": "Section 2 - Performing Calculations"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Now that our program can collect information, we often want to do something with it. Python can perform mathematical calculations just like a calculator."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""price = 8
tax = 2
total = price + tax

meal_price = 12
quantity = 3
total = meal_price * quantity
print(total)
"""
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Python uses <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">operators</span><sup>1</sup> to perform different types of calculations.'
            },

            {
                "page": 2,
                "type": "table",
                "headers": [
                    "Operator",
                    "Meaning"
                ],
                "rows": [
                    ["+", "Add"],
                    ["-", "Subtract"],
                    ["*", "Multiply"],
                    ["/", "Divide"]
                ]
            },

            {
                "page": 2,
                "type": "footnote",
                "number": "1",
                "text":
                "Operators are special symbols or keywords used with variables or values to help programs compute information."
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'What is 5 * 4?',
             'options': ['A. 20', 'B. 9', 'C. 54', 'D. 1'],
             'answer': 'A. 20'},

            {
                "page": 2,
                "type": "heading",
                "text": "Section 3 - Combining Strings"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Many programs also work with text, such as a customer's name, a city, a menu item, or a thank-you message. These are stored as strings."
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">String concatenation</span> means joining pieces of text together.'
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""first = "Urban"
second = "Coders"

print(first + " " + second)
print("Welcome, " + "Maria" + "!")
"""
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'What is string concatenation?',
             'options': ['A. Deleting a string',
                         'B. Joining two or more strings together',
                         'C. Converting text into numbers',
                         'D. Printing a variable'],
             'answer': 'B. Joining two or more strings together'},

            {
                "page": 2,
                "type": "heading",
                "text": "Section 4 - F-Strings"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "F-strings are easier to read and type because variables can be placed directly inside curly braces."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""name = "Maria"
quantity = 3
item = "Frybread Taco"

print(f"Hello {name}!")
print(f"You ordered {quantity} {item}s.")
"""
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "If a variable stores an integer and you place this variable in an f-string using curly braces, you don't need to add quotation marks to the integer to make it a string. Python will do this for you! Everything in the print function must be a string for it to work, because Python can only print strings. If you put a non-string in the print function, Python will convert it to a string. Try this by running print(5)."
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'Which uses an f-string?',
             'options': ['A. print(name)',
                         'B. print(name + age)',
                         'C. print(f"Hello {name}")',
                         'D. print(True)'],
             'answer': 'C. print(f"Hello {name}")'},

            {
                "page": 2,
                "type": "heading",
                "text": "Section 5 - String Methods"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Python provides built-in string methods. These special commands modify, format, or examine text."
            },

            {
                "page": 2,
                "type": "table",
                "headers": [
                    "Method",
                    "Description",
                    "Example Code",
                    "Output"
                ],
                "rows": [
                    [
                        "upper()",
                        "Converts all letters to uppercase.",
                        "name = \"Maria\"\nprint(name.upper())",
                        "MARIA"
                    ],
                    [
                        "lower()",
                        "Converts all letters to lowercase.",
                        "name = \"Maria\"\nprint(name.lower())",
                        "maria"
                    ],
                    [
                        "strip()",
                        "Removes extra spaces from the beginning and end of a string.",
                        "name = \"  Maria  \"\nprint(name.strip())",
                        "Maria"
                    ],
                    [
                        "title()",
                        "Capitalizes the first letter of each word.",
                        "city = \"little haiti\"\nprint(city.title())",
                        "Little Haiti"
                    ],
                    [
                        "replace()",
                        "Replaces one piece of text with another.",
                        "food = \"taco\"\nprint(food.replace(\"taco\", \"frybread\"))",
                        "frybread"
                    ]
                ]
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""name = " Maria "
city = "little haiti"
food = "taco"

print(name.strip())
print(city.title())
print(food.replace("taco", "frybread"))
"""
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "These methods are especially useful when working with information entered by users. If someone types extra spaces or uses lowercase letters, string methods can help format the text consistently before the program uses it."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Section 6 - String Operations"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "So far, we have already learned one operation that can be performed on strings: concatenation. However, concatenation is not the only operation available for strings."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Repeating Strings"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "The multiplication operator (*) has a different meaning when used with strings. Instead of performing multiplication, it repeats the string a specified number of times."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""print("Python! " * 3)

# Output:
# Python! Python! Python!
"""
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Notice how the * operator behaves differently depending on the data type. With numbers, 5 * 3 performs multiplication. With strings, \"Python\" * 3 repeats the string three times."
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "One way to remember this is the mathematical definition of multiplication: repeated addition. Just like 5 * 3 repeatedly adds 5 to itself 3 times, \"Python\" * 3 adds the string Python to itself 3 times."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Strings are Sequential Data Types"
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Python views a string as a <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">sequence</span> of characters<sup>2</sup>. A sequence is an ordered collection of items where every item has a position.'
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Python"
"""
            },

            {
                "page": 2,
                "type": "table",
                "headers": [
                    "Character",
                    "P",
                    "y",
                    "t",
                    "h",
                    "o",
                    "n"
                ],
                "rows": [
                    [
                        "Index",
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5"
                    ]
                ]
            },

            {
                "page": 2,
                "type": "footnote",
                "number": "2",
                "text":
                "Characters are letters, symbols, spaces, and more - pretty much everything on a keyboard that you can type."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Indexing"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Because strings are sequences, we can access individual characters using their index. To access a specific character, place its index inside square brackets."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Python"

print(word[0])
# Output: P

print(word[3])
# Output: h
"""
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Python begins counting at 0, not 1. This is called <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">zero-based indexing</span>.'
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'Given word = "Tulsa", what does print(word[2]) display?',
             'options': ['A. T', 'B. u', 'C. s', 'D. l'],
             'answer': 'D. l'},

            {
                "page": 2,
                "type": "heading",
                "text": "Slicing"
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Sometimes we do not want just one character. We want part of a string. This is called <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">slicing</span>. The syntax<sup>3</sup> is string[start:end:skip].'
            },

            {
                "page": 2,
                "type": "list",
                "items": [
                    "start - the index of the first character to include in the slice.",
                    "end - the index where the slice stops. This character is not included.",
                    "skip, also called the step, specifies how many characters to move forward after each selected character."
                ]
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "When you slice with string[start:end], Python interprets it as string[start:end:1] because the default step is 1."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Python"

print(word[0:3])
# Output: Pyt

print(word[2:6])
# Output: thon

print(word[0:6:2])
# Output: Pto
"""
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Python returns all characters beginning at start and ending before end. Notice that the ending index is not included. When a step is included, Python moves forward by that amount after each selected character."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Programming"
print(word[0:11:2])

# Output:
# Pormig
"""
            },

            {
                "page": 2,
                "type": "table",
                "headers": [
                    "P",
                    "r",
                    "o",
                    "g",
                    "r",
                    "a",
                    "m",
                    "m",
                    "i",
                    "n",
                    "g"
                ],
                "rows": [
                    [
                        "Yes",
                        "No",
                        "Yes",
                        "No",
                        "Yes",
                        "No",
                        "No",
                        "Yes",
                        "No",
                        "Yes",
                        "No"
                    ]
                ]
            },

            {
                "page": 2,
                "type": "rich_paragraph",
                "html":
                'Slicing allows us to extract pieces of text without changing the original string. Strings are <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">immutable</span>, meaning they cannot be changed in place<sup>4</sup>.'
            },

            {
                "page": 2,
                "type": "footnote",
                "number": "3",
                "text":
                "Syntax is the convention of a language, or the way of writing things. English has syntax too, like adding periods at the end of sentences."
            },

            {
                "page": 2,
                "type": "footnote",
                "number": "4",
                "text":
                "In place means the original object itself is modified rather than creating a new object to hold the updated value."
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'What is the output of word = "Computer" and print(word[3:6])?',
             'options': ['A. put', 'B. pute', 'C. ute', 'D. p'],
             'answer': 'A. put'},

            {
                "page": 2,
                "type": "heading",
                "text": "Working with Strings Backwards"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "So far, we have counted forward from the beginning of a string using positive indices. Python also allows us to count backward from the end of a string using negative indices."
            },

            {
                "page": 2,
                "type": "table",
                "headers": [
                    "Character",
                    "P",
                    "y",
                    "t",
                    "h",
                    "o",
                    "n"
                ],
                "rows": [
                    [
                        "Index",
                        "0",
                        "1",
                        "2",
                        "3",
                        "4",
                        "5"
                    ],
                    [
                        "Negative Index",
                        "-6",
                        "-5",
                        "-4",
                        "-3",
                        "-2",
                        "-1"
                    ]
                ]
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Python"

print(word[-1])
print(word[-2])
print(word[-3])

# Output:
# n
# o
# h
"""
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "Negative indexing is especially useful when you want to access characters near the end of a string without needing to know exactly how long the string is."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Reversing a String"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "One of the most common uses of slicing with negative indices is reversing a string. The slice [::-1] starts at the end, moves backward one character at a time, and continues until the beginning is reached."
            },

            {
                "page": 2,
                "type": "code",
                "text":
"""word = "Python"
print(word[::-1])

# Output:
# nohtyP
"""
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'What does the expression word[-1] return?',
             'options': ['A. The first character of the string',
                         'B. The last character of the string',
                         'C. The second character of the string',
                         'D. The length of the string'],
             'answer': 'B. The last character of the string'},

            {'page': 2,
             'type': 'quiz',
             'question': 'What is the output of word = "Urban" and print(word[::-1])?',
             'options': ['A. Urban', 'B. U', 'C. nabrU', 'D. abrnU'],
             'answer': 'C. nabrU'},

            {
                "page": 2,
                "type": "heading",
                "text": "Mini Project - Tulsa Food Truck"
            },

            {'page': 2, 'type': 'paragraph', 'text': "Imagine you're building software for a local food truck."},
            {'page': 2,
 'type': 'paragraph',
 'text': "Your program should ask for the customer's name, ask which menu item they want, ask how "
         'many they want, calculate the total price, and display a receipt using f-strings.'},

            {
                "page": 2,
                "type": "ide",
                "instructions":
                "Build a simple receipt. Change the customer, item, quantity, or price, then run the code.",
                "starter_code":
"""customer = "Maria"
item = "Frybread Taco"
quantity = 3
price = 8

total = quantity * price

print("Tulsa Food Truck")
print(f"Customer: {customer}")
print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Total: ${total}")
"""
            },

            {'page': 2,
             'type': 'quiz',
             'question': 'Why are f-strings useful?',
             'options': ['A. They automatically fix bugs.',
                         'B. They replace variables.',
                         'C. They make programs faster.',
                         'D. They make code easier to read.'],
             'answer': 'D. They make code easier to read.'},

            {
                "page": 2,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 2,
                "type": "list",
                "items": [
                    "input() gathers information.",
                    "Arithmetic performs calculations.",
                    "Strings can be combined.",
                    "F-strings improve readability.",
                    "String methods modify text.",
                    "Strings can be repeated, indexed, sliced, and reversed."
                ]
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Preview"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Next you'll learn how programs make decisions using conditions such as if, elif, and else."
            },

            {
                "page": 2,
                "type": "exercise",
                "problem": "food_truck_total"
            }

        ]
    },


    "conditionals": {'id': 'conditionals',
     'lesson_number': '2',
     'description': 'Lesson 2.0 - Teaching Programs to Make Decisions.',
     'title': 'Conditionals',
     'blocks': [{'page': 1,
                 'type': 'heading',
                 'text': 'Lesson 2 – Teaching Programs to Make Decisions'},
{'page': 1, 'type': 'heading', 'text': 'Prerequisites'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Lesson 1.0 – Variables & Data Types', 'Lesson 1.1 – Using Variables']},
                {'page': 1, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'By the end of this lesson, students should be able to:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Explain what Boolean values represent.',
                           'Compare values using comparison operators.',
                           'Write programs using if, elif, and else.',
                           'Combine conditions using logical operators.',
                           'Predict the output of conditional statements.']},
                {'page': 1, 'type': 'heading', 'text': 'Word Bank'},
                {'page': 1,
                 'type': 'rich_paragraph',
                 'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Boolean</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Conditional</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Expression</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Comparison Operator</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">if</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">elif</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">else</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Logical Operator</span> &nbsp; <span '
                         'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                         'border-radius:6px; font-weight:600;">Indentation</span>'},
                {'page': 1, 'type': 'heading', 'text': 'Introduction'},

                {'page': 1,
                 'type': 'paragraph',
                 'text': "Imagine you're creating a website for a community center in Tulsa."},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Before someone signs up for an event, the computer has to answer questions '
                         'like:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Is the student old enough?',
                           'Did they register before the deadline?',
                           'Have they already attended this workshop?',
                           'Are there still seats available?']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Humans answer these questions naturally without much thought.'},
                {'page': 1, 'type': 'paragraph', 'text': "Computers can't."},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'A computer only follows instructions. If we want a computer to make a '
                         'decision, we must tell it exactly how to do so (remember Garbage in, Garbage '
                         'out).'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Fortunately, Python provides a simple way to teach programs how to make '
                         'decisions.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "In this lesson, you'll learn how programs compare information, ask "
                         'questions, and choose different actions depending on the answers.'},
                {'page': 1, 'type': 'heading', 'text': 'Section 1 – Boolean Values'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'In Lesson 1, you’ve learned various data types. In this section, we talk '
                         'about Booleans (A.K.A bool)—something you’ve seen before. Booleans are the '
                         'foundation of computer decision-making, as computers must first answer a '
                         'question before they make a decision.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'While humans can answer questions with more complex answers like “How was '
                         'your day?”, computers can only answer questions with two possible answers.'},
                {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Is the light on?',
                           'Did the student pass?',
                           'Is today Friday?',
                           'Is the account logged in?']},
                {'page': 1, 'type': 'paragraph', 'text': 'The answer is either yes or no.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Programming represents these two possibilities using a special data type '
                         'called a Boolean.'},
                {'page': 1,
                 'type': 'rich_paragraph',
                 'html': 'A Boolean is a data type that can only store one of two values: '
                         '<code>True</code> or <code>False</code>.'},
                {'page': 1,
                 'type': 'tip',
                 'text': 'Notice that both begin with a capital letter. If you don’t capitalize these '
                         'keywords, Python will not know how to interpret your code.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Unlike strings, Booleans are not surrounded by quotation marks.'},
                {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
                {'page': 1, 'type': 'code', 'text': 'student = True'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'means the variable student stores the Boolean value True.'},
                {'page': 1, 'type': 'paragraph', 'text': 'However,'},
                {'page': 1, 'type': 'code', 'text': 'student = "True"'},
                {'page': 1, 'type': 'paragraph', 'text': 'stores the word "True" as a string.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Although they may look similar, these are completely different data types.'},
                {'page': 1,
                 'type': 'table',
                 'headers': ['Value', 'Data Type'],
                 'rows': [['True', 'bool'], ['"True"', 'str']]},
                {'page': 1, 'type': 'heading', 'text': 'Why Are Booleans Useful?'},
                {'page': 1, 'type': 'paragraph', 'text': 'Programs constantly ask questions.'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Is the password correct?',
                           'Is the player alive?',
                           'Does the customer have enough money?',
                           'Is the homework complete?']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Every one of these questions eventually becomes either True or False'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Without Booleans, computers would have no way of making decisions.'},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'Which of the following is a Boolean?',
                 'options': ['A. False', 'B. "False"', 'C. 0', 'D. "No"'],
                 'answer': 'A. False'},
                {'page': 1, 'type': 'heading', 'text': 'Section 2 – Comparison Operators'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Many of you have already seen comparison operators in your math classes. For '
                         'instance, the inequality 1 > 0 is a True statement as 1 is indeed greater '
                         'than 0; the comparison operator would be the > symbol, as it compares 1 and '
                         '0. Now that we know programs can store True and False, the next question '
                         'is:'},
                {'page': 1, 'type': 'paragraph', 'text': 'Where do these Boolean values come from?'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'One of the most common ways is by comparing two values, which we do with '
                         'comparison operators.'},
                {'page': 1, 'type': 'paragraph', 'text': 'Suppose you ask,'},
                {'page': 1, 'type': 'paragraph', 'text': 'Is 7 greater than 5?'},
                {'page': 1, 'type': 'paragraph', 'text': 'The answer is'},
                {'page': 1, 'type': 'code', 'text': 'True'},
                {'page': 1, 'type': 'paragraph', 'text': 'Python can answer that question for us.'},
                {'page': 1, 'type': 'code', 'text': '7 > 5\n\nOutput\nTrue'},
                {'page': 1, 'type': 'paragraph', 'text': 'Likewise,'},
                {'page': 1, 'type': 'code', 'text': '4 > 10\n\nOutput\nFalse'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'These comparisons are performed using comparison operators.'},
                {'page': 1, 'type': 'heading', 'text': 'Common Comparison Operators'},
                {'page': 1,
                 'type': 'table',
                 'headers': ['Operator', 'Meaning'],
                 'rows': [['==', 'Equal to'],
                          ['!=', 'Not equal to'],
                          ['>', 'Greater than'],
                          ['<', 'Less than'],
                          ['>=', 'Greater than or equal to'],
                          ['<=', 'Less than or equal to']]},
                {'page': 1, 'type': 'heading', 'text': 'Examples'},
                {'page': 1,
                 'type': 'code',
                 'text': '5 == 5\n'
                         'Output\n'
                         'True\n'
                         '\n'
                         '5 != 5\n'
                         'Output\n'
                         'False\n'
                         '\n'
                         '12 >= 8\n'
                         'Output\n'
                         'True\n'
                         '\n'
                         '3 < 1\n'
                         'Output\n'
                         'False'},
                {'page': 1, 'type': 'heading', 'text': 'Comparing Strings'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Comparison operators don't just work on numbers."},
                {'page': 1, 'type': 'paragraph', 'text': 'They can also compare strings.'},
                {'page': 1,
                 'type': 'code',
                 'text': 'name = "Jordan"\nname == "Jordan"\n\nOutput\nTrue'},
                {'page': 1, 'type': 'paragraph', 'text': 'However,'},
                {'page': 1, 'type': 'code', 'text': 'name == "jordan"'},
                {'page': 1, 'type': 'paragraph', 'text': 'returns'},
                {'page': 1, 'type': 'code', 'text': 'False'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Python considers uppercase and lowercase letters to be different.'},
                {'page': 1, 'type': 'heading', 'text': 'A Common Beginner Mistake'},
                {'page': 1, 'type': 'paragraph', 'text': 'Many new programmers accidentally write'},
                {'page': 1, 'type': 'code', 'text': '='},
                {'page': 1, 'type': 'paragraph', 'text': 'instead of'},
                {'page': 1, 'type': 'code', 'text': '=='},
                {'page': 1, 'type': 'paragraph', 'text': 'Remember:'},
                {'page': 1, 'type': 'code', 'text': '='},
                {'page': 1, 'type': 'paragraph', 'text': 'means'},
                {'page': 1, 'type': 'paragraph', 'text': 'Store a value.'},
                {'page': 1, 'type': 'paragraph', 'text': 'While'},
                {'page': 1, 'type': 'code', 'text': '=='},
                {'page': 1, 'type': 'paragraph', 'text': 'means'},
                {'page': 1, 'type': 'paragraph', 'text': 'Compare two values.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'These are two completely different operations.'},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'What is the output?\n12 <= 8',
                 'options': ['A. True', 'B. False', 'C. 12', 'D. An error'],
                 'answer': 'B. False'},
                {'page': 1, 'type': 'heading', 'text': 'Section 3 – The if Statement'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Now we have everything needed to make a decision.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'We can compare values and obtain either True or False.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'The next step is deciding what should happen depending on the answer.'},
                {'page': 1, 'type': 'paragraph', 'text': 'Python uses an if statement to do this.'},
                {'page': 1, 'type': 'paragraph', 'text': 'Think of an if statement as saying:'},
                {'page': 1,
                 'type': 'quote',
                 'text': 'If something is true, then perform these instructions.'},
                {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
                {'page': 1,
                 'type': 'code',
                 'text': 'age = 18\n'
                         'if age >= 18:\n'
                         '    print("You may vote.")\n'
                         '\n'
                         'Output\n'
                         'You may vote.'},
                {'page': 1, 'type': 'paragraph', 'text': "Let's examine the structure."},
                {'page': 1, 'type': 'code', 'text': 'if age >= 18:'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "The word if tells Python we're about to make a decision."},
                {'page': 1, 'type': 'paragraph', 'text': 'The expression'},
                {'page': 1, 'type': 'code', 'text': 'age >= 18'},
                {'page': 1, 'type': 'paragraph', 'text': 'evaluates to either True or False.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'If the expression is True, Python executes the indented code underneath it.'},
                {'page': 1, 'type': 'code', 'text': 'print("You may vote.")'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'If the expression is False, Python simply skips that code and continues with '
                         'the rest of the program.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Notice that, just like functions from Lesson 0.5, indentation matters. '
                         'Everything indented beneath the if statement belongs to that conditional '
                         'block.'},
                {'page': 1, 'type': 'heading', 'text': 'Example'},
                {'page': 1,
                 'type': 'code',
                 'text': 'temperature = 95\n'
                         'if temperature > 90:\n'
                         '    print("Drink plenty of water.")\n'
                         '\n'
                         'Output\n'
                         'Drink plenty of water.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Now suppose the temperature were 70 instead.'},
                {'page': 1, 'type': 'paragraph', 'text': 'The condition'},
                {'page': 1, 'type': 'code', 'text': '70 > 90'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'would evaluate to False, so Python would skip the print() statement '
                         'entirely, and nothing would be displayed.'},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'What will this program print?\nage = 15\nif age >= 16:\nprint("Can drive")',
                 'options': ['A. Can drive', 'B. 15', 'C. Nothing', 'D. An error'],
                 'answer': 'C. Nothing'},
                {'page': 1,
                 'type': 'ide',
                 'instructions': 'Create an if statement that prints "Drink plenty of water." when '
                                 'temperature is greater than 90.',
                 'starter_code': 'temperature = 95\n\n# Write your if statement below.\n'},
                {'page': 1,
                 'type': 'heading',
                 'text': 'Section 4 – Making More Than One Choice with elif and else'},
                {'page': 1, 'type': 'paragraph', 'text': "So far, we've learned how to tell Python:"},
                {'page': 1, 'type': 'quote', 'text': 'If this condition is true, do something.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'But what if we want the program to make multiple possible decisions?'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'This is an important question to consider because situations often have '
                         "multiple conditions to consider. Imagine you're still creating this website "
                         'for a community center in Tulsa. The person hiring you to make this website '
                         'tells you:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Children under 13 join group A.',
                           'Teenagers join group B.',
                           'Adults join group C.']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "An if statement by itself isn't enough—we need more choices."},
                {'page': 1, 'type': 'paragraph', 'text': 'Python gives us two additional keywords:'},
                {'page': 1, 'type': 'list', 'items': ['elif (short for else if)', 'else']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'These allow our program to choose from multiple possibilities.'},
                {'page': 1, 'type': 'heading', 'text': 'The else Statement'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'An else statement tells Python what to do if every previous condition is '
                         'false.'},
                {'page': 1, 'type': 'paragraph', 'text': 'Example:'},
                {'page': 1,
                 'type': 'code',
                 'text': 'temperature = 45\n'
                         'if temperature > 80:\n'
                         '    print("Wear shorts.")\n'
                         'else:\n'
                         '    print("Bring a jacket.")\n'
                         '\n'
                         'Output\n'
                         'Bring a jacket.'},
                {'page': 1, 'type': 'paragraph', 'text': 'Python first checks'},
                {'page': 1, 'type': 'code', 'text': 'temperature > 80'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Since the answer is False, it skips the first block and executes the code '
                         'under else.'},
                {'page': 1,
                 'type': 'tip',
                 'text': 'Think of else as saying "If nothing else matched, do this."'},
                {'page': 1, 'type': 'heading', 'text': 'The elif Statement'},
                {'page': 1, 'type': 'paragraph', 'text': "Sometimes two choices aren't enough."},
                {'page': 1, 'type': 'paragraph', 'text': "Suppose we're assigning letter grades."},
                {'page': 1,
                 'type': 'code',
                 'text': 'score = 88\n'
                         'if score >= 90:\n'
                         '    print("A")\n'
                         'elif score >= 80:\n'
                         '    print("B")\n'
                         'else:\n'
                         '    print("C")\n'
                         '\n'
                         'Output\n'
                         'B'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Python checks each condition from top to bottom.'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Is the score at least 90?',
                           'If not, is it at least 80?',
                           'If neither is true, print "C".']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'As soon as one condition is true, Python executes that block and stops '
                         'checking the remaining conditions.'},
                {'page': 1, 'type': 'heading', 'text': 'Why Order Matters'},
                {'page': 1, 'type': 'paragraph', 'text': 'Consider this program.'},
                {'page': 1,
                 'type': 'code',
                 'text': 'age = 20\n'
                         'if age >= 18:\n'
                         '    print("Adult")\n'
                         'elif age >= 65:\n'
                         '    print("Senior")\n'
                         '\n'
                         'Output\n'
                         'Adult'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Even though a 70-year-old is also greater than 65, Python would never reach '
                         'the second condition because the first one is already true.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "For this reason, it's usually best to place the most specific conditions "
                         'first.'},
                {'page': 1, 'type': 'paragraph', 'text': 'A better version would be'},
                {'page': 1,
                 'type': 'code',
                 'text': 'if age >= 65:\n'
                         '    print("Senior")\n'
                         'elif age >= 18:\n'
                         '    print("Adult")\n'
                         'else:\n'
                         '    print("Minor")'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Notice that in this program, seniors will not be wrongfully labeled as '
                         'adults because the condition age >= 65 is being checked first.'},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'What will this print?\n'
                             'age = 10\n'
                             'if age >= 18:\n'
                             'print("Adult")\n'
                             'elif age >= 13:\n'
                             'print("Teen")\n'
                             'else:\n'
                             'print("Child")',
                 'options': ['A. Adult', 'B. Teen', 'C. Nothing', 'D. Child'],
                 'answer': 'D. Child'},
                {'page': 1,
                 'type': 'heading',
                 'text': 'Section 5 – Combining Conditions with Logical Operators'},
                {'page': 1, 'type': 'paragraph', 'text': "Sometimes one condition isn't enough."},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Imagine driving for the first time. In Oklahoma,'},
                {'page': 1, 'type': 'paragraph', 'text': 'You must'},
                {'page': 1,
                 'type': 'list',
                 'items': ['be at least 15 years old', "Have a learner's permit"]},
                {'page': 1, 'type': 'paragraph', 'text': 'Both conditions must be true.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Logical operators are Python keywords that let us combine multiple '
                         'conditions.'},
                {'page': 1, 'type': 'paragraph', 'text': 'The three most common are'},
                {'page': 1,
                 'type': 'table',
                 'headers': ['Operator', 'Meaning'],
                 'rows': [['and', 'Both conditions must be true'],
                          ['or', 'At least one condition must be true'],
                          ['not', 'Reverses True and False']]},
                {'page': 1, 'type': 'heading', 'text': 'Using and'},
                {'page': 1,
                 'type': 'code',
                 'text': 'age = 15\n'
                         'has_permit = True\n'
                         'if age >= 15 and has_permit:\n'
                         '    print("You can drive!")\n'
                         'else:\n'
                         '    print("Sorry, you can’t drive.")\n'
                         '\n'
                         'Output\n'
                         'You can drive!'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'The program only prints "You can drive!" because both conditions are true.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'If either one were false, the program would skip to the else statement.'},
                {'page': 1,
                 'type': 'tip',
                 'text': 'Notice that good variable names make your program super readable. You can '
                         'almost read the if statement like plain English because the variable names '
                         'are so descriptive!'},
                {'page': 1, 'type': 'heading', 'text': 'Using or'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Sometimes only one condition needs to be true. Imagine you’re building an '
                         'identification system for your school. Students and teachers get ID cards '
                         'that identify them as students and teachers of your school, respectively. '
                         'You’d like to permit only students and teachers of your school to enter.'},
                {'page': 1,
                 'type': 'code',
                 'text': 'is_student = False\n'
                         'is_teacher = True\n'
                         'if is_student or is_teacher:\n'
                         '    print("Access granted.")\n'
                         '\n'
                         'Output\n'
                         'Access granted.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Since at least one condition is true, Python executes the code.'},
                {'page': 1, 'type': 'heading', 'text': 'Using not'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'The not operator negates1 a Boolean, meaning that it makes the value of the '
                         'Boolean the opposite of what it says.'},
                {'page': 1,
                 'type': 'code',
                 'text': 'logged_in = False\n'
                         'if not logged_in:\n'
                         '    print("Please log in.")\n'
                         '\n'
                         'Output\n'
                         'Please log in.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Since logged_in is False, the condition (not logged_in) becomes True. '
                         'Therefore, Python sees a true condition and executes the indented code.'},
                {'page': 1,
                 'type': 'footnote',
                 'number': '1',
                 'text': 'To flip the value of something or, in other words, make it the opposite of '
                         'what it originally was. For example, the opposite of 1 is -1. So, in math, '
                         'negating 1 would be to make it -1.'},
                {'page': 1,
                 'type': 'tip',
                 'text': 'When trying to figure out the value of a negated Boolean, find the original '
                         'Boolean’s value then just flip it.'},
                {'page': 1, 'type': 'heading', 'text': 'Truth Tables'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Sometimes it's helpful to see every possible outcome."},
                {'page': 1,
                 'type': 'tip',
                 'text': 'The way to read a truth table is to imagine a conditional statement. For '
                         'example, If A is True and B is True, the entire condition (A and B) is true. '
                         'Think of (A and B) as one whole condition that basically asks, are A and B '
                         'both true at the same time. If not, then (A and B) is False as a whole.'},
                {'page': 1, 'type': 'heading', 'text': 'and'},
                {'page': 1,
                 'type': 'table',
                 'headers': ['A', 'B', 'A and B'],
                 'rows': [['True', 'True', 'True'],
                          ['True', 'False', 'False'],
                          ['False', 'True', 'False'],
                          ['False', 'False', 'False']]},
                {'page': 1, 'type': 'heading', 'text': 'or'},
                {'page': 1,
                 'type': 'table',
                 'headers': ['A', 'B', 'A or B'],
                 'rows': [['True', 'True', 'True'],
                          ['True', 'False', 'True'],
                          ['False', 'True', 'True'],
                          ['False', 'False', 'False']]},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1, 'type': 'paragraph', 'text': 'Suppose'},
                {'page': 1, 'type': 'code', 'text': 'age = 17\nhas_ticket = True'},
                {'page': 1, 'type': 'paragraph', 'text': 'What will this print?'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'if age >= 18 and has_ticket:\nprint("Enter")\nelse:\nprint("Cannot enter")',
                 'options': ['A. Cannot enter', 'B. Enter', 'C. Nothing', 'D. Error'],
                 'answer': 'A. Cannot enter'},
                {'page': 1, 'type': 'heading', 'text': 'Section 6 – Common Conditional Mistakes'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Everyone makes mistakes while learning to write conditionals.'},
                {'page': 1, 'type': 'paragraph', 'text': "Let's look at a few common ones."},
                {'page': 1, 'type': 'heading', 'text': 'Mistake 1 — Using = instead of =='},
                {'page': 1, 'type': 'paragraph', 'text': 'Incorrect'},
                {'page': 1, 'type': 'code', 'text': 'if age = 18:'},
                {'page': 1, 'type': 'paragraph', 'text': 'Correct'},
                {'page': 1, 'type': 'code', 'text': 'if age == 18:'},
                {'page': 1, 'type': 'paragraph', 'text': 'Remember:'},
                {'page': 1, 'type': 'paragraph', 'text': '= stores a value.'},
                {'page': 1, 'type': 'paragraph', 'text': '== compares two values.'},
                {'page': 1, 'type': 'heading', 'text': 'Mistake 2 — Forgetting the Colon'},
                {'page': 1, 'type': 'paragraph', 'text': 'Incorrect'},
                {'page': 1, 'type': 'code', 'text': 'if age >= 18'},
                {'page': 1, 'type': 'paragraph', 'text': 'Correct'},
                {'page': 1, 'type': 'code', 'text': 'if age >= 18:'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Every if, elif, and else statement ends with a colon.'},
                {'page': 1, 'type': 'heading', 'text': 'Mistake 3 — Incorrect Indentation'},
                {'page': 1, 'type': 'paragraph', 'text': 'Incorrect'},
                {'page': 1, 'type': 'code', 'text': 'if age >= 18:\nprint("Adult")'},
                {'page': 1, 'type': 'paragraph', 'text': 'Correct'},
                {'page': 1, 'type': 'code', 'text': 'if age >= 18:\n    print("Adult")'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Python uses indentation to determine which code belongs inside the '
                         'conditional.'},
                {'page': 1, 'type': 'heading', 'text': 'Mistake 4 — Checking Impossible Conditions'},
                {'page': 1,
                 'type': 'code',
                 'text': 'age = 25\n'
                         'if age < 18:\n'
                         '    print("Minor")\n'
                         'elif age < 13:\n'
                         '    print("Child")'},
                {'page': 1, 'type': 'paragraph', 'text': 'Can the second condition ever happen?'},
                {'page': 1, 'type': 'paragraph', 'text': 'No.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Anyone younger than 13 is already younger than 18.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'This is another example of why the order of conditions matters.'},
                {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
                {'page': 1,
                 'type': 'quiz',
                 'question': 'Which line contains an error?\nage = 18\nif age = 18:\nprint("Adult")',
                 'options': ['A. Line 1', 'B. Line 2', 'C. Line 3', 'D. No errors'],
                 'answer': 'B. Line 2'},
                {'page': 1, 'type': 'heading', 'text': 'Spotlight – Predicting Oklahoma Weather'},

                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Oklahoma experiences some of the most severe weather in the United States.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'To help keep communities safe, scientists at the National Severe Storms '
                         'Laboratory (NSSL) in Norman, Oklahoma, develop software that analyzes '
                         'enormous amounts of weather data.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Although the models they use are much more advanced than the programs we've "
                         'written, they still rely on the same fundamental idea: making decisions '
                         'based on conditions.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'For example, a weather program might ask questions like:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Is the wind speed above a certain threshold?',
                           'Is the air rotating?',
                           'Is the temperature changing rapidly?',
                           'Is there enough evidence to issue a tornado warning?']},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Each of these questions can be answered with either True or False.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Using conditional statements, the software decides what to do next—whether '
                         'to continue monitoring the storm, alert meteorologists, or issue a public '
                         'warning.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "As you continue learning Python, you'll discover that the simple if "
                         "statements you're writing today are the foundation of much larger systems "
                         'used in science, medicine, engineering, and countless other fields.'},
                {'page': 1,
                 'type': 'heading',
                 'text': 'Section 7 – Mini Project: Community Event Eligibility'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Congratulations! You've learned how computers make decisions using Boolean "
                         'values, comparison operators, logical operators, and conditional '
                         'statements.'},
                {'page': 1, 'type': 'paragraph', 'text': "Now it's time to put everything together."},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Imagine you're helping organize a community coding workshop. Students must "
                         'meet certain requirements before registering.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Write a function that determines whether a student is eligible to '
                         'participate.'},
                {'page': 1, 'type': 'heading', 'text': 'Requirements'},
                {'page': 1, 'type': 'paragraph', 'text': 'A student may participate if:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['They are at least 13 years old, and',
                           'They have completed the introductory workshop.']},
                {'page': 1, 'type': 'paragraph', 'text': 'If both conditions are true, return:'},
                {'page': 1, 'type': 'code', 'text': 'Eligible'},
                {'page': 1, 'type': 'paragraph', 'text': 'Otherwise, return:'},
                {'page': 1, 'type': 'code', 'text': 'Not Eligible'},
                {'page': 1, 'type': 'heading', 'text': 'Example'},
                {'page': 1,
                 'type': 'code',
                 'text': 'def check_eligibility(age, completed_intro):\n    ...'},
                {'page': 1, 'type': 'heading', 'text': 'Example Outputs'},
                {'page': 1,
                 'type': 'code',
                 'text': 'check_eligibility(15, True)\n'
                         '\n'
                         'returns\n'
                         '\n'
                         'Eligible\n'
                         '\n'
                         'check_eligibility(12, True)\n'
                         '\n'
                         'returns\n'
                         '\n'
                         'Not Eligible'},
                {'page': 1, 'type': 'heading', 'text': 'Challenge'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Modify your function so that students who are 18 years or older are '
                         'automatically eligible, even if they have not completed the introductory '
                         'workshop.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "Think carefully about which logical operator(s) you'll need."},
                {'page': 1,
                 'type': 'ide',
                 'instructions': 'Write a function that determines whether a student is eligible to '
                                 'participate. Then try the challenge from the lesson.',
                 'starter_code': 'def check_eligibility(age, completed_intro):\n'
                                 '    # Write your code here\n'
                                 '    pass\n'
                                 '\n'
                                 'print(check_eligibility(15, True))\n'
                                 'print(check_eligibility(12, True))\n'
                                 'print(check_eligibility(18, False))\n'},
                {'page': 1, 'type': 'heading', 'text': 'Key Takeaways'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'By the end of this lesson, you should be able to:'},
                {'page': 1,
                 'type': 'list',
                 'items': ['Compare values using comparison operators.',
                           'Understand how Boolean values (True and False) control program flow.',
                           'Write programs using if, elif, and else.',
                           'Combine conditions using and, or, and not.',
                           'Recognize common mistakes involving comparisons, indentation, and '
                           'condition order.']},
                {'page': 1, 'type': 'heading', 'text': 'Looking Ahead'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'So far, our programs have made decisions based on a single piece of '
                         'information or a few variables.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'But what if we wanted to store hundreds or even thousands of pieces of '
                         'information?'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "How could we keep track of every student's name in a classroom?"},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'How might we store every score from a basketball season?'},
                {'page': 1, 'type': 'paragraph', 'text': 'Or every city in Oklahoma?'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': 'Using one variable for each item would quickly become impossible.'},
                {'page': 1,
                 'type': 'paragraph',
                 'text': "In the next lesson, you'll learn about lists—Python's first built-in "
                         'collection type—which allow you to store and work with many values at once. '
                         'Lists are one of the most important data structures in programming and form '
                         'the foundation for countless real-world applications.'}]},
    "lists_dictionaries": {
        "id": "lists_dictionaries",
        "lesson_number": "3",
        "description": "Lesson 3.0 - Tuples. Lesson 3.1 - Lists, Mutation & Aliasing. Lesson 3.2 - Dictionaries: Organizing Information with Keys.",
        "title": "Collections",
        "blocks": [
            {
                "page": 1,
                "type": "heading",
                "text": "Lesson 3.0 – Tuples"
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Prerequisites"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "Lesson 1.0 – Variables & Data Types",
                    "Lesson 1.1 – Using Variables",
                    "Lesson 2 – Teaching Programs to Make Decisions"
                ]
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Learning Objectives & Vocabulary"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "By the end of this lesson, students should be able to:"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "Explain what a collection is.",
                    "Create tuples.",
                    "Access tuple elements using indexing.",
                    "Slice tuples.",
                    "Explain why tuples are immutable.",
                    "Identify situations where tuples are preferable to lists."
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
                "html": "<span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Collection</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Tuple</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Element</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Index</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Slice</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Immutable</span>"
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Introduction"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "So far, every variable we've created has stored one piece of information."
            },
            {
                "page": 1,
                "type": "code",
                "text": "name = \"Jordan\"\nage = 16\nheight = 5.8"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "But many times, pieces of information naturally belong together. Imagine you're recording information about an earthquake in Oklahoma."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "You might need to store:"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "Magnitude",
                    "Latitude",
                    "Longitude",
                    "Time"
                ]
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Although these are four separate values, they all describe the same earthquake."
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "Instead of creating four separate variables, Python lets us group related information into one object called a <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">collection</span>."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "The first collection we'll learn is called a tuple."
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Section 1 – What is a Tuple?"
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "A <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">tuple</span> is an ordered collection of values."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Unlike variables that store one value,"
            },
            {
                "page": 1,
                "type": "code",
                "text": "age = 16"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "a tuple stores several."
            },
            {
                "page": 1,
                "type": "code",
                "text": "earthquake = (\n    4.2,\n    35.47,\n    -97.52,\n    \"2:31 PM\"\n)"
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "Each individual value inside the tuple is called an <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">element</span>."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Notice that tuples use parentheses and separate elements with commas."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Just like variables, tuples can store different data types."
            },
            {
                "page": 1,
                "type": "code",
                "text": "student = (\n    \"Jordan\",\n    16,\n    True,\n    3.8\n)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Python allows integers, floats, strings, Booleans—even other collections—to exist inside the same tuple."
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 1,
             'type': 'quiz',
             'question': 'Which of the following is a tuple?',
             'options': ['A. name = "Jordan"', 'B. 42', 'C. (1, 2, 3, (1, 2, 3))', 'D. True'],
             'answer': 'C. (1, 2, 3, (1, 2, 3))'},
            {
                "page": 1,
                "type": "heading",
                "text": "Section 2 – Indexing Tuples"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Just like strings, tuples are sequential data types."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "That means every element has an index."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Remember:"
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "Python starts counting at <strong>0</strong>."
            },
            {
                "page": 1,
                "type": "code",
                "text": "cities = (\n    \"Tulsa\",\n    \"Norman\",\n    \"Stillwater\",\n    \"Lawton\"\n)"
            },
            {
                "page": 1,
                "type": "table",
                "headers": ["Element", "“Tulsa”", "“Norman”", "“Stillwater”", "“Lawton”"],
                "rows": [["Index", "0", "1", "2", "3"]]
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Access an element exactly like a string."
            },
            {
                "page": 1,
                "type": "code",
                "text": "print(cities[0])\n\nOutput\nTulsa"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Negative indices also work."
            },
            {
                "page": 1,
                "type": "code",
                "text": "print(cities[-1])\n\nOutput\nLawton"
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 1,
             'type': 'quiz',
             'question': 'What is printed?\n'
                         '\n'
                         'animals = (\n'
                         '    "Dog",\n'
                         '    "Cat",\n'
                         '    "Bird"\n'
                         ')\n'
                         'print(animals[1])',
             'options': ['A. Dog', 'B. Bird', 'C. Error', 'D. Cat'],
             'answer': 'D. Cat'},
            {
                "page": 1,
                "type": "heading",
                "text": "Section 3 – Slicing Tuples"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Because tuples are sequential, slicing works exactly like it did with strings."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "General form:"
            },
            {
                "page": 1,
                "type": "code",
                "text": "tuple[start:end:skip]"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Python begins at start, stops before end, and selects every “skipth” element."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Example:"
            },
            {
                "page": 1,
                "type": "code",
                "text": "numbers = (\n    10,\n    20,\n    30,\n    40,\n    50\n)\n\nprint(numbers[1:4])\n\nOutput\n(20, 30, 40)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "You can also skip values."
            },
            {
                "page": 1,
                "type": "code",
                "text": "print(numbers[::2])\n\nOutput\n(10, 30, 50)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Notice that slicing returns another tuple."
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 1,
             'type': 'quiz',
             'question': 'What does this print?\n'
                         '\n'
                         'values = (\n'
                         '    5,\n'
                         '    10,\n'
                         '    15,\n'
                         '    20\n'
                         ')\n'
                         'print(values[:2])',
             'options': ['A. (5,10)', 'B. (15,20)', 'C. 5', 'D. Error'],
             'answer': 'A. (5,10)'},
            {
                "page": 1,
                "type": "heading",
                "text": "Section 4 – Tuples are Immutable"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "One feature separates tuples from many other collections."
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "Once a tuple has been created, its <strong>elements cannot be changed.</strong>"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Consider the following tuple."
            },
            {
                "page": 1,
                "type": "code",
                "text": "coordinates = (\n    35.47,\n    -97.52\n)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Suppose we try changing one value."
            },
            {
                "page": 1,
                "type": "code",
                "text": "coordinates[0] = 36"
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "Python raises a <strong>TypeError</strong><sup>1</sup>."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "This happens because tuples are immutable."
            },
            {
                "page": 1,
                "type": "rich_paragraph",
                "html": "<span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Immutable</span> means an object cannot be modified after it has been created."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Why would this be useful?"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Some information should never change."
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "birthdays",
                    "GPS coordinates",
                    "months of the year",
                    "mathematical constants"
                ]
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Using tuples helps prevent accidental changes to important information."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Don't worry too much about how Python keeps tuples immutable."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "In the next lesson, we'll learn what actually happens inside a computer's memory when objects are modified."
            },
            {
                "page": 1,
                "type": "footnote",
                "number": "1",
                "text": "A TypeError is an error that occurs when you try to perform an operation on a value of the wrong data type."
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 1,
             'type': 'quiz',
             'question': 'Which statement is true?',
             'options': ['A. Tuples can grow forever.',
                         'B. Tuples are immutable.',
                         'C. Tuples can be modified after creation.',
                         'D. Tuples only store integers.'],
             'answer': 'B. Tuples are immutable.'},
            {
                "page": 1,
                "type": "heading",
                "text": "Oklahoma STEM Spotlight – Tracking Earthquakes"
            },
            {'page': 1,
 'type': 'paragraph',
 'text': 'Oklahoma experiences thousands of small earthquakes each year.'},
            {'page': 1,
 'type': 'paragraph',
 'text': 'Scientists at the Oklahoma Geological Survey (OGS) record information about every event.'},
            {'page': 1, 'type': 'paragraph', 'text': 'A single earthquake might be represented by values like'},
            {
                "page": 1,
                "type": "code",
                "text": "earthquake = (\n    4.3,\n    35.46,\n    -97.52,\n    \"July 8, 2026\"\n)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Notice that all four values belong together and generally should not change after the event has been recorded."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Tuples are a natural way to store this kind of information because they protect important data from accidental modification."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Although professional software uses much larger and more sophisticated data structures, the same idea of grouping related information together is fundamental to scientific programming."
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Section 5 – Mini Project: Oklahoma Landmark"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Create a tuple called landmark."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "It should contain:"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "the landmark's name",
                    "the city it is located in",
                    "the year it was completed"
                ]
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "For example,"
            },
            {
                "page": 1,
                "type": "code",
                "text": "landmark = (\n    \"Golden Driller\",\n    \"Tulsa\",\n    1966\n)"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Then write code that"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "1. Prints the first element.",
                    "2. Prints the last element.",
                    "3. Prints the first two elements using slicing."
                ]
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Key Takeaways"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "By the end of this lesson, you should be able to:"
            },
            {
                "page": 1,
                "type": "list",
                "items": [
                    "Explain what a collection is.",
                    "Create tuples.",
                    "Access tuple elements using indexes.",
                    "Slice tuples.",
                    "Explain why tuples are immutable."
                ]
            },
            {
                "page": 1,
                "type": "heading",
                "text": "Looking Ahead"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Tuples introduced us to the idea of storing multiple pieces of information together."
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "But one important question remains:"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "Why are tuples immutable while some other objects can be changed?"
            },
            {
                "page": 1,
                "type": "paragraph",
                "text": "To answer that question, we'll look beneath the surface of Python itself. In the next lesson, you'll learn how Python stores objects in memory and discover two concepts that explain many beginner bugs: mutation and aliasing. You’ll also be learning about the mutable version of a Tuple—Python’s List."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Lesson 3.1 – Lists, Mutation & Aliasing"
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Prerequisites"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "Lesson 1.0 – Variables & Data Types",
                    "Lesson 1.1 – Using Variables",
                    "Lesson 2 – Teaching Programs to Make Decisions",
                    "Lesson 3.0 – Tuples"
                ]
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Learning Objectives & Vocabulary"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "By the end of this lesson, you should be able to:"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "Create and modify lists.",
                    "Explain the difference between mutable and immutable objects.",
                    "Describe what mutation means.",
                    "Explain aliasing and why it happens.",
                    "Create copies of lists.",
                    "Use common list methods."
                ]
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Word Bank"
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "<span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">List</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Mutable</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Mutability</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Mutation</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Aliasing</span>"
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Introduction"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In the previous lesson, we introduced tuples, our first collection data type."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Tuples allowed us to group multiple related pieces of information."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For instance,"
            },
            {
                "page": 2,
                "type": "code",
                "text": "earthquake = (\n    4.3,\n    35.46,\n    -97.52,\n    \"July 8, 2026\"\n)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "This worked well because the information about an earthquake should never change after it has been recorded. But not all information stays the same. Imagine you're writing software for a local food bank. At the beginning of the day, the inventory might look like this."
            },
            {
                "page": 2,
                "type": "code",
                "text": "inventory = (\n    \"Rice\",\n    \"Beans\",\n    \"Pasta\"\n)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Then someone donates canned vegetables."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Can we simply add them to the tuple?"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "No. Tuples are immutable, meaning they cannot be modified after they have been created."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Sometimes this is exactly what we want. Information like birthdays, GPS coordinates, and historical records generally shouldn't change. However, many real-world programs work with information that changes constantly. For example, a classroom gains new students, a grocery store sells products, a hospital admits new patients, and a nonprofit receives new donations."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Hence, programs need a way to store collections that can grow, shrink, and change over time."
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "For that reason, Python provides another collection called a <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">list</span>."
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "Similar to tuples, lists are ordered collections of values. However, lists are <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">mutable</span>, meaning they can be modified after they are created."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In this lesson, we'll learn not only how to use lists, but also what it actually means for an object to be mutable. Along the way, we'll explore one of the most important concepts in Python: aliasing, where multiple variables refer to the same object in memory."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Spotlight"
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Tracking Food Donations Across Oklahoma"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Organizations such as the Regional Food Bank of Oklahoma receive thousands of food donations every week. Their inventory changes constantly as new donations arrive and food is distributed to families."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Imagine representing today's inventory."
            },
            {
                "page": 2,
                "type": "code",
                "text": "inventory = (\n    \"Rice\",\n    \"Beans\",\n    \"Pasta\"\n)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Later in the day, a truck delivers canned vegetables and bottled water."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Instead of creating an entirely new collection every time something changes, the program simply updates the existing list."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Collections that frequently change are one of the primary reasons programmers use lists instead of tuples."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Perfect. Since students already understand tuples, this section shouldn't re-teach indexing from scratch. It should emphasize the similarities first, then introduce the one huge difference: lists can change."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Section 1 – What is a List?"
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "A <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">list</span> is an ordered, mutable collection of values."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Like tuples, lists allow us to store multiple related pieces of information in a single variable."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For example, suppose we're keeping track of books checked out from a local library."
            },
            {
                "page": 2,
                "type": "code",
                "text": "checked_out = [\n    \"The Hunger Games\",\n    \"Percy Jackson\",\n    \"Charlotte's Web\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Notice that lists look very similar to tuples."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Tuple:"
            },
            {
                "page": 2,
                "type": "code",
                "text": "books = (\n    \"The Hunger Games\",\n    \"Percy Jackson\",\n    \"Charlotte's Web\"\n)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "List:"
            },
            {
                "page": 2,
                "type": "code",
                "text": "books = [\n    \"The Hunger Games\",\n    \"Percy Jackson\",\n    \"Charlotte's Web\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The biggest visual difference is the type of brackets used."
            },
            {
                "page": 2,
                "type": "table",
                "headers": ["Collection", "Brackets"],
                "rows": [["Tuple", "()"], ["List", "[]"]]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Like tuples, lists"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "store multiple values,",
                    "preserve the order of those values,",
                    "allow duplicate values,",
                    "support indexing and slicing, and",
                    "can contain almost any data type."
                ]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For example,"
            },
            {
                "page": 2,
                "type": "code",
                "text": "student = [\n    \"Jordan\",\n    16,\n    True,\n    3.85\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "contains a string, an integer, a Boolean, and a float."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Although Python allows lists to contain mixed data types, most lists store similar kinds of information."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For example,"
            },
            {
                "page": 2,
                "type": "code",
                "text": "temperatures = [\n    72,\n    74,\n    69,\n    71\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "or"
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities = [\n    \"Tulsa\",\n    \"Norman\",\n    \"Stillwater\",\n    \"Lawton\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "This makes programs easier to understand and maintain."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Which of the following is a list?',
             'options': ['A. ("Tulsa", "Norman", "Lawton")',
                         'B. "Tulsa"',
                         'C. ["Tulsa", "Norman", "Lawton"]',
                         'D. 42'],
             'answer': 'C. ["Tulsa", "Norman", "Lawton"]'},
            {
                "page": 2,
                "type": "heading",
                "text": "Section 2 – Lists are Sequential Data Types"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In Lesson 1, we learned that strings are sequential data types because their characters have an order."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In Lesson 3.0, we discovered that tuples are also sequential."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Lists are no different."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Every element inside a list has an index."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Remember that Python begins counting at 0."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities = [\n    \"Tulsa\",\n    \"Norman\",\n    \"Stillwater\",\n    \"Lawton\"\n]"
            },
            {
                "page": 2,
                "type": "table",
                "headers": ["Index", "0", "1", "2", "3"],
                "rows": [["Element", "“Tulsa”", "“Norman”", "“Stillwater”", "“Lawton”"]]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "To access an element, use square brackets after the list's name."
            },
            {
                "page": 2,
                "type": "code",
                "text": "print(cities[0])\n\nOutput\nTulsa"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Negative indexes also work."
            },
            {
                "page": 2,
                "type": "code",
                "text": "print(cities[-1])\n\nOutput\nLawton"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Lists also support slicing."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "General form:"
            },
            {
                "page": 2,
                "type": "code",
                "text": "list[start:end:skip]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Python begins at start, stops before end, and selects every skipth element."
            },
            {
                "page": 2,
                "type": "code",
                "text": "print(cities[1:3])\n\nOutput\n['Norman', 'Stillwater']"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Notice that slicing a list returns another list, just as slicing a tuple returns another tuple."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "If this syntax feels familiar, that's because Python uses the same indexing and slicing rules for most sequential data types."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'What is printed?\n'
                         '\n'
                         'numbers = [\n'
                         '    10,\n'
                         '    20,\n'
                         '    30,\n'
                         '    40\n'
                         ']\n'
                         'print(numbers[-2])',
             'options': ['A. 20', 'B. 40', 'C. Error', 'D. 30'],
             'answer': 'D. 30'},
            {
                "page": 2,
                "type": "heading",
                "text": "Section 3 – Mutability: The Biggest Difference Between Tuples and Lists"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "So far, lists probably seem very similar to tuples."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Both collections:"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "store multiple values,",
                    "preserve the order of those values,",
                    "support indexing,",
                    "support slicing, and",
                    "can store almost any data type."
                ]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "This raises an important question."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Why does Python have both tuples and lists?"
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "The answer is <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">mutability</span>, which refers to whether an object is mutable."
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "A mutable object is an object whose contents can be changed <strong>in place</strong><sup>1</sup> after it has been created."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Tuples, on the other hand, are immutable, meaning their contents cannot be changed after creation."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Let's compare the two."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Suppose we create a tuple."
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades = (\n    92,\n    85,\n    78\n)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Now suppose your teacher realizes that the second grade was entered incorrectly and should actually be a 90."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "You might try to write"
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades[1] = 90"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Python returns an error because tuples are immutable."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Now let's perform the same task using a list."
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades = [\n    92,\n    85,\n    78\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Changing the second element is now perfectly valid."
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades[1] = 90"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    92,\n    90,\n    78\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Unlike tuples, lists allow individual elements to be replaced."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "This ability to modify an object after it has been created is called mutation."
            },
            {
                "page": 2,
                "type": "footnote",
                "number": "1",
                "text": "See Lesson 1.1 for a good definition of in place."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Mutating a List"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Changing a list is called mutating the list."
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "<span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Mutation</span> simply means changing the contents of a mutable object."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "One way to mutate a list is by replacing one of its elements."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For example,"
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities = [\n    \"Tulsa\",\n    \"Norman\",\n    \"Stillwater\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Suppose we want to replace \"Norman\" with \"Edmond\"."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities[1] = \"Edmond\""
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list now becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    \"Tulsa\",\n    \"Edmond\",\n    \"Stillwater\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Notice something important. We didn't create a new list. We changed the existing list. Replacing elements, however, is only one way to mutate a list. Python also provides several built-in methods that modify a list by adding, removing, or rearranging its elements."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Adding Elements"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The append() method adds a new element to the end of a list."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities.append(\"Lawton\")"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    \"Tulsa\",\n    \"Edmond\",\n    \"Stillwater\",\n    \"Lawton\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Sometimes we want to add an element somewhere other than the end. The insert() method inserts an element at a specific index."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities.insert(1, \"Norman\")"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    \"Tulsa\",\n    \"Norman\",\n    \"Edmond\",\n    \"Stillwater\",\n    \"Lawton\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Notice that the existing elements shift to make room for the new one."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Removing Elements"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The remove() method removes the first occurrence of a value."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities.remove(\"Lawton\")"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    \"Tulsa\",\n    \"Norman\",\n    \"Edmond\",\n    \"Stillwater\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "If you instead know the position of the element you want to remove, you can use the pop() method."
            },
            {
                "page": 2,
                "type": "code",
                "text": "cities.pop(2)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    \"Tulsa\",\n    \"Norman\",\n    \"Stillwater\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "If no index is provided, cities.pop() removes the last element of the list."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Rearranging Elements"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Some list methods reorganize the elements without adding or removing them."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The sort() method arranges the elements in ascending order."
            },
            {
                "page": 2,
                "type": "code",
                "text": "numbers = [\n    4,\n    2,\n    7,\n    1\n]\n\nnumbers.sort()"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    1,\n    2,\n    4,\n    7\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The reverse() method reverses the order of the elements."
            },
            {
                "page": 2,
                "type": "code",
                "text": "numbers.reverse()"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "The list becomes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[\n    7,\n    4,\n    2,\n    1\n]"
            },
            {
                "page": 2,
                "type": "heading",
                "text": "A Common Theme"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Although these operations perform different tasks, they all have one thing in common. They mutate the list. Whether you replace an element, add a new one, remove an existing one, or rearrange the elements, the original list is modified. Python does not create a brand new list for each of these operations. This idea—that an object itself changes rather than being replaced—is extremely important. In fact, it leads directly to one of Python's most commonly misunderstood concepts: aliasing, which we'll study in the next section."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Suppose we have the following list.\n'
                         '\n'
                         'numbers = [\n'
                         '    10,\n'
                         '    20,\n'
                         '    30\n'
                         ']\n'
                         '\n'
                         'After executing\n'
                         '\n'
                         'numbers[1] = 50\n'
                         '\n'
                         'what does the list become?',
             'options': ['A. [10, 50, 30]', 'B. [10, 20, 30]', 'C. [50, 20, 30]', 'D. An error occurs.'],
             'answer': 'A. [10, 50, 30]'},
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Which of the following operations mutates a list?',
             'options': ['A. numbers.append(40)',
                         'B. All of the above.',
                         'C. numbers.remove(20)',
                         'D. numbers.sort()'],
             'answer': 'B. All of the above.'},
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Which statement best describes a mutable object?',
             'options': ['A. An object that cannot be changed after it is created.',
                         'B. An object that only stores numbers.',
                         'C. An object whose contents can be changed after it is created.',
                         'D. An object that automatically creates copies of itself.'],
             'answer': 'C. An object whose contents can be changed after it is created.'},
            {
                "page": 2,
                "type": "heading",
                "text": "Section 4 – Aliasing: When Two Variables Share the Same List"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Now that we know lists are mutable, let's explore something surprising that often confuses new programmers. Suppose we create a list."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores = [\n    90,\n    85,\n    100\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Now we create another variable."
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades = scores"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "At first glance, it might seem like we've created two separate lists. Many beginners imagine Python stores the data like this."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores ───► [90, 85, 100]\ngrades ───► [90, 85, 100]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "However, this is not what Python does. Instead, Python stores one list. Both variables simply refer to that same list."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores ───────┐\n              │\n              ▼\n       [90, 85, 100]\n              ▲\n              │\ngrades ───────┘"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Because both variables refer to the same list, changing the list through one variable also changes what the other variable sees."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "An Example"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Consider the following code."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores = [\n    90,\n    85,\n    100\n]\n\ngrades = scores\n\ngrades[1] = 95\n\nprint(scores)"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "What do you think will be printed?"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Many beginners expect"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[90, 85, 100]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "However, the actual output is"
            },
            {
                "page": 2,
                "type": "code",
                "text": "[90, 95, 100]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Why?"
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "Because scores and grades are not two different lists. They are simply two different names for the same list. Changing the list through one variable changes the very same list that the other variable refers to. This relationship is called <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">aliasing</span>. Aliasing occurs when two or more variables refer to the same object in memory."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Why Does This Happen?"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Remember that variables do not actually contain objects. Instead, variables refer to objects."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "When Python executes"
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades = scores"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "it does not create a new list."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Instead, Python simply makes grades refer to the exact same list that scores already refers to. No copying takes place. This is why changing the list through either variable changes the same underlying object."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "This may be confusing, so here’s another way to think about it. Imagine you and a friend are editing the same Google Doc. You both have different links to the document. Your friend changes a sentence. When you refresh your page, you immediately see the change. Why? Because you're not editing two different documents. You're editing the same document. Aliasing works in much the same way. Different variable names correspond to the same underlying object."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Consider the following program.\n'
                         '\n'
                         'numbers = [\n'
                         '    1,\n'
                         '    2,\n'
                         '    3\n'
                         ']\n'
                         '\n'
                         'other = numbers\n'
                         'other.append(4)\n'
                         'print(numbers)\n'
                         '\n'
                         'What is printed?',
             'options': ['A. [1, 2, 3]', 'B. [4]', 'C. An error', 'D. [1, 2, 3, 4]'],
             'answer': 'D. [1, 2, 3, 4]'},
            {
                "page": 2,
                "type": "heading",
                "text": "Explanation"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "numbers and other refer to the same list. Appending through other modifies the list itself, so numbers also sees the change."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 2,
             'type': 'quiz',
             'question': 'Which statement best describes aliasing?',
             'options': ['A. Two or more variables referring to the same object.',
                         'B. Creating a copy of a list.',
                         'C. Creating two identical lists.',
                         'D. Mutating two lists at once.'],
             'answer': 'A. Two or more variables referring to the same object.'},
            {
                "page": 2,
                "type": "heading",
                "text": "Section 6 – Creating Copies of Lists"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In the previous section, we learned that assigning one list to another variable does not create a new list. Instead,"
            },
            {
                "page": 2,
                "type": "code",
                "text": "a = [1, 2, 3]\nb = a"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "creates an alias, meaning both a and b refer to the same list. But what if we actually want two separate lists? Python provides a simple solution: the copy() method."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores = [\n    90,\n    85,\n    100\n]\n\ngrades = scores.copy()"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Now there are two different lists."
            },
            {
                "page": 2,
                "type": "code",
                "text": "scores ─────► [90, 85, 100]\ngrades ─────► [90, 85, 100]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Although the lists contain the same values, they are different objects."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Suppose we modify one of them."
            },
            {
                "page": 2,
                "type": "code",
                "text": "grades.append(95)\n\nprint(scores)\nprint(grades)\n\nOutput\n[90, 85, 100]\n[90, 85, 100, 95]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Notice that changing grades did not affect scores."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Unlike aliasing, copying creates an independent list."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Whenever you want to preserve the original list while making changes to another, use the copy() method."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Section 7 – Going Further (Optional): Shallow vs. Deep Copies"
            },
            {
                "page": 2,
                "type": "rich_paragraph",
                "html": "<strong>THIS SECTION IS ENTIRELY OPTIONAL.</strong> It introduces an idea that becomes important later in Python. You do not need to master it right now. The copy() method creates what is known as a shallow copy. For most of the lists we've worked with so far, this behaves exactly as we expect. However, if a list contains other lists, a shallow copy only copies the outer list. The inner lists are still shared between the two copies."
            },
            {
                "page": 2,
                "type": "code",
                "text": "numbers = [\n    [1, 2],\n    [3, 4]\n]\n\ncopy = numbers.copy()"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "We'll revisit this idea later when we work with nested data structures."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "For now, simply remember that copy() is the correct way to create an independent copy of a one-dimensional list."
            },
            {
                "page": 2,
                "type": "tip",
                "text": "You can also copy a list with slicing. If you type copy = numbers[:], numbers[:] returns the entire list from start to finish (hence the empty slicing brackets), which is why this works the same way as copy = numbers.copy()."
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Section 8 – Mini Project: Classroom Attendance"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Your school is creating a program to manage attendance for a classroom."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Begin by creating the following list."
            },
            {
                "page": 2,
                "type": "code",
                "text": "students = [\n    \"Jordan\",\n    \"Maria\",\n    \"Alex\"\n]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Complete each of the following tasks."
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "1. Print the first student's name.",
                    "2. Print the last student's name.",
                    "3. Add a new student using append().",
                    "4. Replace one student's name using indexing.",
                    "5. Remove a student using either remove() or pop().",
                    "6. Create a second variable that is an alias of the original list.",
                    "7. Modify the alias and observe what happens to the original list.",
                    "8. Create a true copy of the original list using copy().",
                    "9. Modify the copied list and verify that the original list remains unchanged."
                ]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "As you complete each step, ask yourself:"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "Did I create a new list?",
                    "Or did I modify an existing one?"
                ]
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Understanding the answer to these questions is one of the most important goals of this lesson."
            },
            {
                "page": 2,
                "type": "ide",
                "instructions": "Complete each of the following tasks.",
                "starter_code": "students = [\n    \"Jordan\",\n    \"Maria\",\n    \"Alex\"\n]"
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Key Takeaways"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "By the end of this lesson, you should be able to:"
            },
            {
                "page": 2,
                "type": "list",
                "items": [
                    "Create and modify lists.",
                    "Explain the difference between mutable and immutable objects.",
                    "Describe what mutation means.",
                    "Explain why aliasing occurs.",
                    "Distinguish between creating an alias and creating a copy.",
                    "Use common list methods such as append(), insert(), remove(), pop(), sort(), and reverse()."
                ]
            },
            {
                "page": 2,
                "type": "heading",
                "text": "Looking Ahead"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "Lists are excellent for storing collections of information when each element can be identified by its position."
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "However, positions are not always the best way to organize data. Imagine storing information about a student. Instead of writing"
            },
            {
                "page": 2,
                "type": "code",
                "text": "student[0]\nstudent[1]\nstudent[2]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "wouldn't it be easier to write"
            },
            {
                "page": 2,
                "type": "code",
                "text": "student[\"name\"]\nstudent[\"grade\"]\nstudent[\"favorite_food\"]"
            },
            {
                "page": 2,
                "type": "paragraph",
                "text": "In the next lesson, you'll learn about dictionaries, another built-in Python collection that stores information as key–value pairs. Dictionaries make programs easier to read and allow us to organize complex information in a more meaningful way."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Lesson 3.2 - Dictionaries: Organizing Information with Keys"
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Prerequisites"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Lesson 1.0 - Variables & Data Types",
                    "Lesson 1.1 - Using Variables",
                    "Lesson 2 - Teaching Programs to Make Decisions",
                    "Lesson 3.0 - Tuples",
                    "Lesson 3.1 - Lists, Mutation & Aliasing"
                ]
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Learning Objectives & Vocabulary"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "By the end of this lesson, you should be able to:"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Explain why dictionaries are useful.",
                    "Create dictionaries.",
                    "Access values using keys.",
                    "Add and modify key-value pairs.",
                    "Remove key-value pairs.",
                    "Use common dictionary methods.",
                    "Explain the difference between lists and dictionaries."
                ]
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Word Bank"
            },
            {
                "page": 3,
                "type": "rich_paragraph",
                "html": "<span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Dictionary</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Key</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Value</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Key-Value Pair</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Lookup</span> &nbsp; <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">Mapping</span>"
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Introduction"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "So far, we've learned about two collection types. A tuple stores a fixed collection of values, while a list stores a collection that can change over time. Both collections organize information by position, which programmers refer to as indices. Although organizing information by position is often useful, there are many situations where it isn't the most natural approach."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "For example, imagine organizing folders for your classes: a math folder, a history folder, and an English folder. You could organize these folders using a sequential data type. If math is your first-period class, history is your second-period class, and English is your third-period class, you could access them by remembering their positions. However, this requires you to remember that math is folder 0, history is folder 1, English is folder 2, and so on. If your schedule changes or you simply forget the order, finding the right folder becomes more difficult."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Wouldn't it be much easier if your folders were simply labeled \"Math,\" \"History,\" and \"English\"? Instead of remembering a folder's position, you could look it up by its name. Python provides a collection that works exactly this way. Instead of organizing information by position, it organizes information using keys, which are meaningful labels chosen by the programmer."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Section 1 - What is a Dictionary?"
            },
            {
                "page": 3,
                "type": "rich_paragraph",
                "html": "A <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">dictionary</span> stores information using keys, which map to<sup>1</sup> values. These keys are similar to indices in sequential data, and the values are almost like the elements. We can access values by key, just as we can access elements by indexing."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Each piece of information consists of two parts:"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "a key, which is a unique label used to identify and access a value in a dictionary.",
                    "a value, or the piece of information associated with a key."
                ]
            },
            {
                "page": 3,
                "type": "rich_paragraph",
                "html": "Together, these form a <span style=\"background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;\">key-value pair</span>, which is a dictionary item."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Here's an example."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8,\n    \"favorite_subject\": \"Physics\"\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "The string \"name\" is a key. Its value is \"Jordan.\" The key-value pair is the item {\"name\": \"Jordan\"}."
            },
            {
                "page": 3,
                "type": "footnote",
                "number": "1",
                "text": "\"Map to\" means \"matches with.\" For example, the key \"name\" maps to the value \"Jordan\"."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Notice the syntax."
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Dictionaries use curly braces {}.",
                    "Keys appear before the colon.",
                    "Values appear after the colon.",
                    "Each key-value pair is separated by a comma."
                ]
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Unlike lists, dictionaries organize information by meaningful labels instead of numerical positions."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 3,
             'type': 'quiz',
             'question': 'Which of the following is a dictionary?',
             'options': ['A. ["Jordan", 11]',
                         'B. {"name": "Jordan", "grade": 11}',
                         'C. ("Jordan", 11)',
                         'D. "Jordan"'],
             'answer': 'B. {"name": "Jordan", "grade": 11}'},
            {
                "page": 3,
                "type": "heading",
                "text": "Section 2 - Accessing Values"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "To retrieve a value from a dictionary, use its key. This is very similar to indexing."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8\n}\n\nprint(student[\"name\"])\n\nOutput\nJordan"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Likewise,"
            },
            {
                "page": 3,
                "type": "code",
                "text": "print(student[\"gpa\"])\n\nOutput\n3.8"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Notice that dictionaries do not use indexes."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Instead of asking \"What's at position 2?\" we ask \"What's stored under the key 'gpa'?\""
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 3,
             'type': 'quiz',
             'question': 'Given car = {"make": "Toyota", "year": 2022}, what does print(car["year"]) display?',
             'options': ['A. Toyota', 'B. year', 'C. 2022', 'D. Error'],
             'answer': 'C. 2022'},
            {
                "page": 3,
                "type": "heading",
                "text": "Section 3 - Adding and Updating Information"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "One of the strengths of dictionaries is that they can grow over time."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Suppose we decide to store a student's favorite food."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student[\"favorite_food\"] = \"Pizza\""
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "The dictionary becomes"
            },
            {
                "page": 3,
                "type": "code",
                "text": "{\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8,\n    \"favorite_food\": \"Pizza\"\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "If the key already exists, Python updates its value."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student[\"grade\"] = 12\n\nstudent[\"grade\"]\n\nreturns\n12"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "The same syntax is used for both adding and updating. Python determines which operation to perform based on whether the key already exists. Notice that adding or updating doesn't cause us to make a new dictionary, meaning that dictionaries are mutable."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 3,
             'type': 'quiz',
             'question': 'Suppose student = {"name": "Jordan"} and then student["grade"] = 11. What happened?',
             'options': ['A. The dictionary became empty.',
                         'B. The key "name" was removed.',
                         'C. An error occurred.',
                         'D. A new key-value pair was added.'],
             'answer': 'D. A new key-value pair was added.'},
            {
                "page": 3,
                "type": "heading",
                "text": "Section 4 - Removing Information"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Sometimes information is no longer needed."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Python allows us to remove key-value pairs using a method you've seen before - pop(). Usually, pop expects you to specify an index, but dictionaries don't have indices; they use keys."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8\n}\n\nstudent.pop(\"gpa\")"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "The dictionary now becomes"
            },
            {
                "page": 3,
                "type": "code",
                "text": "{\n    \"name\": \"Jordan\",\n    \"grade\": 11\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Notice that pop() removes the key and its associated value. Notice that removals don't cause us to make a new dictionary, meaning that dictionaries are mutable."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 3,
             'type': 'quiz',
             'question': 'Which method removes a key-value pair?',
             'options': ['A. pop()', 'B. append()', 'C. sort()', 'D. insert()'],
             'answer': 'A. pop()'},
            {
                "page": 3,
                "type": "heading",
                "text": "Section 5 - Useful Dictionary Methods"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Dictionaries provide several useful methods."
            },
            {
                "page": 3,
                "type": "table",
                "headers": ["Method", "Purpose"],
                "rows": [
                    ["keys()", "Returns all keys."],
                    ["values()", "Returns all values."],
                    ["items()", "Returns every key-value pair."],
                    ["get(key)", "Retrieves a value safely."],
                    ["pop(key)", "Removes a key-value pair."],
                    ["clear()", "Removes all key-value pairs."]
                ]
            },
            {
                "page": 3,
                "type": "code",
                "text": "student.keys()\n\nreturns\n\ndict_keys(['name', 'grade'])"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Similarly, student.values() returns the values stored in the dictionary."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "A few corrections first:"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Keys cannot repeat.",
                    "Values can be any object.",
                    "Values can even be dictionaries.",
                    "Keys cannot be dictionaries. This is not true because dictionaries are mutable, and dictionary keys must be hashable (immutable). This is probably too advanced for your audience, so I'd simply say that keys are usually strings, numbers, or tuples. Avoid mentioning hashability."
                ]
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Here's how I'd write the section in the style of your lessons."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Section 6 - Useful Dictionary Methods"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Like every Python data type, dictionaries have a few important rules."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Rule 1 - Every Key Must Be Unique"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Within a dictionary, each key must be unique. In other words, the same key cannot appear more than once."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "For example,"
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "is perfectly valid because each key appears only once."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "However,"
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"name\": \"Maria\"\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "contains the key \"name\" twice. If duplicate keys are provided, Python keeps only the last value associated with that key."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Rule 2 - Values Can Be Any Object"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Dictionary values can store almost any type of object you've learned so far."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8,\n    \"honor_roll\": True\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "This stores a string, an integer, a float, and a Boolean."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Values can even be collections, such as lists, tuples, or other dictionaries."
            },
            {
                "page": 3,
                "type": "code",
                "text": "student = {\n    \"name\": \"Jordan\",\n    \"grades\": [92, 88, 95],\n    \"address\": {\n        \"city\": \"Tulsa\",\n        \"state\": \"Oklahoma\"\n    }\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "This allows dictionaries to represent more complex information while keeping it organized."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Rule 3 - Keys Should Be Immutable"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "While values can be almost any object, keys should be immutable. Most commonly, programmers use strings as keys because they are descriptive and easy to read."
            },
            {
                "page": 3,
                "type": "code",
                "text": "car = {\n    \"make\": \"Toyota\",\n    \"model\": \"Camry\",\n    \"year\": 2022\n}"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Numbers and tuples can also be used as keys, but strings are by far the most common choice. Although it may not seem so, this rule is very necessary. Think of the keys to a dictionary as the keys to your house. Imagine I mutate your keys by bending them; now you can't enter your house, just like how programmers can't use the same keys to access the same values."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Section 7 - Lists vs Dictionaries"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Both lists and dictionaries store collections of information. However, they organize that information differently."
            },
            {
                "page": 3,
                "type": "table",
                "headers": ["List", "Dictionary"],
                "rows": [
                    ["Uses indexes", "Uses keys"],
                    ["Ordered by position", "Organized by labels"],
                    ["Best when order matters", "Best when information has names"],
                    ["Example: class roster", "Example: student profile"]
                ]
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Ask yourself: Does each piece of information have a meaningful name? If so, a dictionary is often the better choice."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Check Your Understanding"
            },
            {'page': 3,
             'type': 'quiz',
             'question': "Which collection would you choose to store a student's name, age, GPA, and favorite "
                         'subject?',
             'options': ['A. Tuple', 'B. Dictionary', 'C. List', 'D. String'],
             'answer': 'B. Dictionary'},
            {
                "page": 3,
                "type": "heading",
                "text": "Mini Project - Student Profile"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Create a dictionary called student."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "It should store"
            },
            {
                "page": 3,
                "type": "list",
                "items": ["name", "grade", "GPA", "favorite subject"]
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "Then write code to"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "1. Print the student's name.",
                    "2. Add a favorite food.",
                    "3. Update the GPA.",
                    "4. Remove the favorite food.",
                    "5. Print all of the keys.",
                    "6. Print all of the values."
                ]
            },
            {
                "page": 3,
                "type": "ide",
                "instructions": "Create the student dictionary, then complete all six tasks.",
                "starter_code": "student = {\n    \"name\": \"Jordan\",\n    \"grade\": 11,\n    \"gpa\": 3.8,\n    \"favorite_subject\": \"Physics\"\n}\n\n# Complete the six tasks below."
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Key Takeaways"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "By the end of this lesson, you should be able to:"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Explain why dictionaries exist.",
                    "Create dictionaries.",
                    "Retrieve values using keys.",
                    "Add, update, and remove key-value pairs.",
                    "Use common dictionary methods.",
                    "Explain the difference between lists and dictionaries."
                ]
            },
            {
                "page": 3,
                "type": "heading",
                "text": "Looking Ahead"
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "You've now learned Python's three most common collection types:"
            },
            {
                "page": 3,
                "type": "list",
                "items": [
                    "Tuples, for collections that should remain unchanged.",
                    "Lists, for collections that change over time.",
                    "Dictionaries, for organizing information using meaningful keys."
                ]
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "So far, we've only worked with a few pieces of data at a time. But what if a list contains 1,000 students? Or a dictionary contains 10,000 customer records? Processing each item one at a time by hand would be impossible."
            },
            {
                "page": 3,
                "type": "paragraph",
                "text": "In the next unit, you'll learn about loops, one of the most powerful tools in programming. Loops allow programs to repeat tasks automatically, making it practical to work with large collections of data efficiently."
            }
        ]
    },
    "loops": {'id': 'loops',
 'lesson_number': '4',
 'description': 'Lesson 4.0 - While Loops. Lesson 4.1 - For Loops. Lesson 4.2 - Nested Loops. Lesson 4.3 - Advanced Loop Techniques. Build and control loops to process collections.',
 'title': 'Loops',
 'blocks': [{'page': 1, 'type': 'heading', 'text': 'Lesson 4.0 – While Loops'},
{'page': 1, 'type': 'heading', 'text': 'Prerequisites'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Before beginning this lesson, you should understand:'},
            {'page': 1,
             'type': 'list',
             'items': ['Lesson 1.0 – Variables & Data Types',
                       'Lesson 1.1 – Using Variables',
                       'Lesson 2 – Teaching Programs to Make Decisions',
                       'Lesson 3.0 – Tuples',
                       'Lesson 3.1 – Lists, Mutation & Aliasing',
                       'Lesson 3.2 – Dictionaries: Organizing Information with Keys']},
            {'page': 1, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'By the end of this lesson, you should be able to:'},
            {'page': 1,
             'type': 'list',
             'items': ['Explain why loops are useful.',
                       'Write while loops.',
                       'Explain how loop conditions work.',
                       'Use counters to control repetition.',
                       'Identify and avoid infinite loops.',
                       'Use while loops for simple input validation.']},
            {'page': 1, 'type': 'heading', 'text': 'Word Bank'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Loop</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Iteration</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">While Loop</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Condition</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Counter</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Infinite Loop</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Sentinel Value</span>'},
            {'page': 1, 'type': 'heading', 'text': 'Introduction'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Up to this point, every Python program we've written has followed the same "
                     'general pattern. Python starts at the first line of code, executes it once, '
                     'moves to the next line, executes it once, and continues until the program '
                     'reaches the end.'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'print("Welcome!")\n'
                     'print("Today we\'ll learn about loops.")\n'
                     'print("Let\'s begin!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Each print() statement executes exactly one time before the program ends. '
                     'Most real-world programs, however, need to perform the same task repeatedly. '
                     'Imagine creating a fitness app that counts your push-ups, a weather station '
                     'that records the temperature every minute, or a video game that constantly '
                     "checks whether the player has won or lost. These programs don't execute "
                     'their instructions only once—they repeat them over and over again. Without '
                     'loops, programmers would have to write the same code many times.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Suppose we wanted to print the word "Hello!" ten times.'},
            {'page': 1,
             'type': 'code',
             'text': 'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")\n'
                     'print("Hello!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': "This certainly works, but it's repetitive and annoying to type even with "
                     'copy-and-paste. Now imagine printing "Hello!" one thousand times. Clearly, '
                     'there must be a better way because you’re definitely not going to want to '
                     'copy-and-paste that many times. Fortunately, Python provides one.'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">loop</span> allows a computer to repeat '
                     'a block of code automatically. Instead of writing the same instructions over '
                     'and over, we simply tell Python what to repeat and when to stop. In this '
                     "lesson, you'll learn about the first of Python's two main looping "
                     'structures: the <span style="background:#fff1df; color:#c74716; padding:2px '
                     '7px; border-radius:6px; font-weight:600;">while loop</span>.'},
            {'page': 1, 'type': 'heading', 'text': 'Spotlight'},
            {'page': 1, 'type': 'heading', 'text': "Monitoring Oklahoma's Weather"},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Weather stations across Oklahoma continuously collect data on temperature, '
                     "humidity, rainfall, and wind speed. These measurements aren't taken just "
                     "once—they're collected over and over again throughout the day. Rather than "
                     'writing the same instructions thousands of times, programmers use loops to '
                     "repeatedly collect and process new data. The programs you'll write in this "
                     'lesson are much simpler, but they rely on the exact same idea: repeating a '
                     "task until it's time to stop."},
            {'page': 1, 'type': 'heading', 'text': 'Section 1 – Why Do We Need Loops?'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Imagine you wanted to count from 1 to 5. Without loops, you might write'},
            {'page': 1, 'type': 'code', 'text': 'print(1)\nprint(2)\nprint(3)\nprint(4)\nprint(5)'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Although this works, it quickly becomes impractical. What if you wanted to '
                     'count to 100? Or 10,000? Writing the same statement over and over again '
                     'wastes both time and space. It also makes programs harder to read and '
                     "modify. Instead, we'd like Python to repeat the same instruction "
                     "automatically. That's exactly what loops allow us to do. A loop repeatedly "
                     'executes a block of code until some condition tells it to stop.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Rather than thinking,'},
            {'page': 1, 'type': 'quote', 'text': '"Write this line 100 times,"'},
            {'page': 1, 'type': 'paragraph', 'text': 'programmers think,'},
            {'page': 1,
             'type': 'quote',
             'text': '"Write this line once, then tell Python to repeat it."'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'This simple idea is one of the most powerful concepts in computer science. '
                     'Everything from websites and mobile apps to robots and artificial '
                     'intelligence relies on loops to perform repetitive tasks efficiently.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'Which of the following problems are loops designed to solve?',
             'options': ['A. Repeating a block of code multiple times.',
                         'B. Storing multiple pieces of information.',
                         'C. Making decisions between different outcomes.',
                         'D. Creating dictionaries.'],
             'answer': 'A. Repeating a block of code multiple times.'},
            {'page': 1, 'type': 'heading', 'text': 'Section 2 – Writing Your First While Loop'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">while loop</span> repeats a block of '
                     'code while<sup>1</sup> a condition remains True.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Its general syntax is'},
            {'page': 1, 'type': 'code', 'text': 'while condition:\n    # code to repeat'},
            {'page': 1, 'type': 'paragraph', 'text': "Let's look at an example."},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n'
                     '\n'
                     'while count <= 5:\n'
                     '    print(count)\n'
                     '    count += 1\n'
                     '\n'
                     'Output\n'
                     '1\n'
                     '2\n'
                     '3\n'
                     '4\n'
                     '5'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Let's break this program down one line at a time."},
            {'page': 1, 'type': 'paragraph', 'text': 'First,'},
            {'page': 1, 'type': 'code', 'text': 'count = 1'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'creates a variable named count and gives it an initial value of 1.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Next,'},
            {'page': 1, 'type': 'code', 'text': 'while count <= 5:'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'asks Python an important question: "Is count less than or equal to 5?"'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'If the answer is True, Python executes every indented line underneath the '
                     'while statement. In this example, Python first prints the value of count.'},
            {'page': 1, 'type': 'code', 'text': 'print(count)'},
            {'page': 1, 'type': 'paragraph', 'text': 'Then,'},
            {'page': 1, 'type': 'code', 'text': 'count += 1'},
            {'page': 1, 'type': 'paragraph', 'text': 'adds one to count.'},
            {'page': 1,
             'type': 'tip',
             'text': 'count += 1 is the same as count = count + 1; you’re simply adding 1 to count '
                     'itself. There are other ways to do this using other operators like -=, *=, '
                     'or /=.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'After reaching the end of the loop, Python returns to the top and checks the '
                     'condition again. If the condition is still True, the loop repeats. If the '
                     'condition becomes False, Python exits the loop and continues executing the '
                     'rest of the program.'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'This process of repeatedly executing the loop body is called an <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">iteration</span>. Each time the loop '
                     'repeats counts as one iteration.'},
            {'page': 1,
             'type': 'footnote',
             'number': '1',
             'text': 'A Python keyword that repeatedly executes a block of code as long as a '
                     'condition remains True.'},
            {'page': 1, 'type': 'heading', 'text': 'Section 3 – Understanding the Loop Condition'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'The most important part of every while loop is its <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">condition</span>. A condition is a '
                     'Boolean expression<sup>2</sup> that evaluates to either True or False. '
                     'Python checks this condition before every iteration of the loop. If the '
                     'condition is True, the loop continues. If the condition is False, the loop '
                     'immediately stops.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Consider the following example.'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n\nwhile count <= 3:\n    print(count)\n    count += 1'},
            {'page': 1, 'type': 'paragraph', 'text': "Let's walk through what happens."},
            {'page': 1,
             'type': 'table',
             'headers': ['Value of count', 'Condition (count <= 3)', 'Loop Executes?'],
             'rows': [['1', 'True', 'Yes'],
                      ['2', 'True', 'Yes'],
                      ['3', 'True', 'Yes'],
                      ['4', 'False', 'No']]},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Notice that Python checks the condition every time before running the loop '
                     'body. Once the condition becomes False, the loop ends.'},
            {'page': 1,
             'type': 'footnote',
             'number': '2',
             'text': 'An expression that evaluates to either True or False (i.e. x > 5, age == '
                     '18).'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'Suppose the following code is executed.\n'
                         '\n'
                         'number = 4\n'
                         'while number < 7:\n'
                         '    print(number)\n'
                         '    number += 1\n'
                         '\n'
                         'How many times does the loop execute?',
             'options': ['A. 2', 'B. 3', 'C. 4', 'D. Forever'],
             'answer': 'B. 3'},
            {'page': 1, 'type': 'heading', 'text': 'Section 4 – Counters'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'In the previous examples, we repeatedly increased the variable count.'},
            {'page': 1, 'type': 'code', 'text': 'count += 1'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'Variables like count are called <span style="background:#fff1df; '
                     'color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">counters</span>. A counter is a variable whose value '
                     'changes each time a loop executes. Counters are commonly used to keep track '
                     'of how many times a loop has repeated.'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n'
                     '\n'
                     'while count <= 5:\n'
                     '    print("Iteration", count)\n'
                     '    count += 1\n'
                     '\n'
                     'Output\n'
                     'Iteration 1\n'
                     'Iteration 2\n'
                     'Iteration 3\n'
                     'Iteration 4\n'
                     'Iteration 5'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Although counters usually increase by one, they don't have to."},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 0\n'
                     '\n'
                     'while count <= 20:\n'
                     '    print(count)\n'
                     '    count += 5\n'
                     '\n'
                     'Output\n'
                     '0\n'
                     '5\n'
                     '10\n'
                     '15\n'
                     '20'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Counters can increase, decrease, or change by any amount depending on the '
                     'program.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What does this program print?\n'
                         '\n'
                         'count = 10\n'
                         'while count >= 4:\n'
                         '    print(count)\n'
                         '    count -= 2',
             'options': ['A. 10\n8\n6',
                         'B. 10\n9\n8\n7',
                         'C. 10\n8\n6\n4',
                         'D. The program never stops.'],
             'answer': 'C. 10\n8\n6\n4'},
            {'page': 1, 'type': 'heading', 'text': 'Section 5 – Infinite Loops'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'Every while loop must eventually make its condition become False. If it '
                     'never does, the program repeats forever. This is called an <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">infinite loop</span>.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Consider the following program.'},
            {'page': 1, 'type': 'code', 'text': 'count = 1\n\nwhile count <= 5:\n    print(count)'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Can you spot the problem? The variable count is never updated. It always '
                     'remains equal to 1. Since count <= 5 is always True, Python has no reason to '
                     'stop the loop.'},
            {'page': 1, 'type': 'paragraph', 'text': 'The program prints'},
            {'page': 1, 'type': 'code', 'text': '1\n1\n1\n1\n1\n...\nforever.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Infinite loops are one of the most common mistakes made by beginning '
                     "programmers. Fortunately, they're also one of the easiest to fix. Simply "
                     'make sure that something inside the loop changes the condition.'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n\nwhile count <= 5:\n    print(count)\n    count += 1'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Now the value of count changes during each iteration. Eventually, count '
                     'becomes 6, the condition becomes False, and the loop ends.'},
            {'page': 1,
             'type': 'tip',
             'text': 'Sometimes infinite loops are intentionally done with the keyword True. '
                     'Simply writing while True, Python always executes what’s within the '
                     'indentation underneath this while loop because the condition the while '
                     'keyword sees is always True.'},
            {'page': 1, 'type': 'heading', 'text': 'Common Beginner Mistakes'},
            {'page': 1, 'type': 'heading', 'text': 'Forgetting to Update the Counter'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n\nwhile count <= 5:\n    print(count)\n\n# Infinite loop'},
            {'page': 1, 'type': 'heading', 'text': 'Updating the Wrong Variable'},
            {'page': 1,
             'type': 'code',
             'text': 'count = 1\n\nwhile count <= 5:\n    print(count)\n    number += 1'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'count never changes, so the loop never ends.'},
            {'page': 1, 'type': 'heading', 'text': 'Using the Wrong Condition'},
            {'page': 1, 'type': 'code', 'text': 'count = 10\n\nwhile count < 5:\n    print(count)'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'The condition is already False. The loop never executes.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'Which of the following causes an infinite loop?',
             'options': ['A. count = 1\nwhile count <= 5:\n    count += 1',
                         'B. count = 6\nwhile count <= 5:\n    print(count)',
                         'C. count = 1\nwhile count <= 5:\n    print(count)\n    count += 1',
                         'D. count = 1\nwhile count <= 5:\n    print(count)'],
             'answer': 'D. count = 1\nwhile count <= 5:\n    print(count)'},
            {'page': 1, 'type': 'heading', 'text': 'Section 6 – Sentinel Values'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Not every loop repeats a fixed number of times. Sometimes we don't know "
                     'ahead of time when the loop should end. Instead, we allow the user to '
                     'decide.'},
            {'page': 1, 'type': 'paragraph', 'text': "Suppose we're creating a simple menu."},
            {'page': 1,
             'type': 'code',
             'text': 'choice = ""\n'
                     '\n'
                     'while choice != "quit":\n'
                     '    choice = input("Type \'quit\' to exit: ")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Here, the loop continues until the user types "quit".'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'A special value like "quit" that signals a program to stop is called a <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">sentinel value</span>.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Sentinel values are commonly used in menus, games, and interactive programs '
                     "where the number of repetitions isn't known in advance."},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'In the following program,\n'
                         '\n'
                         'command = ""\n'
                         'while command != "exit":\n'
                         '    command = input("Command: ")\n'
                         '\n'
                         'what is the sentinel value?',
             'options': ['A. "exit"', 'B. command', 'C. input', 'D. while'],
             'answer': 'A. "exit"'},
            {'page': 1, 'type': 'heading', 'text': 'Section 7 – Mini Project: Password Validator'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Let's put everything we've learned together. Many websites, applications, "
                     'and computers require users to enter the correct password before they can '
                     'continue. If the password is incorrect, the program asks the user to try '
                     'again. This is a perfect example of a situation where a while loop is useful '
                     "because we don't know how many attempts the user will need. Your goal is to "
                     'write a program that repeatedly asks the user for a password until they '
                     'enter the correct one.'},
            {'page': 1, 'type': 'heading', 'text': 'Problem'},
            {'page': 1, 'type': 'paragraph', 'text': 'The correct password is'},
            {'page': 1, 'type': 'code', 'text': 'python123'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Your program should repeatedly ask the user to enter a password.'},
            {'page': 1, 'type': 'paragraph', 'text': 'If the password is incorrect, display'},
            {'page': 1, 'type': 'code', 'text': 'Incorrect password. Try again.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'When the correct password is entered, display'},
            {'page': 1, 'type': 'code', 'text': 'Access granted!'},
            {'page': 1, 'type': 'paragraph', 'text': 'A sample interaction is shown below.'},
            {'page': 1,
             'type': 'code',
             'text': 'Enter password: hello\n'
                     'Incorrect password. Try again.\n'
                     'Enter password: password\n'
                     'Incorrect password. Try again.\n'
                     'Enter password: python123\n'
                     'Access granted!'},
            {'page': 1, 'type': 'heading', 'text': 'Before You Begin'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Before writing any code, think about the following questions.'},
            {'page': 1,
             'type': 'list',
             'items': ["1. What variable will store the user's password?",
                       '2. What Boolean expression should the while loop check?',
                       '3. What is the sentinel value?',
                       '4. Which line of code updates the password during each iteration?']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Planning your solution before programming is a habit practiced by '
                     'experienced software developers.'},
            {'page': 1, 'type': 'heading', 'text': 'Challenge'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Modify your program so that it counts how many incorrect password attempts '
                     'the user makes. After the user successfully logs in, print the total number '
                     'of incorrect attempts.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Example:'},
            {'page': 1,
             'type': 'code',
             'text': 'Enter password: hello\n'
                     'Incorrect password. Try again.\n'
                     'Enter password: abc123\n'
                     'Incorrect password. Try again.\n'
                     'Enter password: python123\n'
                     'Access granted!\n'
                     'Incorrect attempts: 2'},
            {'page': 1,
             'type': 'tip',
             'text': 'Consider using a counter that increases each time the user enters an '
                     'incorrect password.'},
            {'page': 1, 'type': 'heading', 'text': 'Vocabulary Bank'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">loop</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">iteration</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">while</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">counter</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">infinite loop</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">sentinel value</span>'},
            {'page': 1, 'type': 'heading', 'text': 'Key Takeaways'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'By the end of this lesson, you should be able to:'},
            {'page': 1,
             'type': 'list',
             'items': ['Explain why loops are useful.',
                       'Write while loops.',
                       'Explain how loop conditions control repetition.',
                       'Use counters to control a loop.',
                       'Recognize and avoid infinite loops.',
                       'Use sentinel values to repeat until a user chooses to stop.']},
            {'page': 1, 'type': 'heading', 'text': 'Looking Ahead'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'In this lesson, the computer repeated instructions while a condition '
                     'remained True. Sometimes, however, we already know exactly how many times we '
                     'want to repeat something. For example, what if we wanted to print every '
                     "student's name in a class roster or every number from 1 to 100? Rather than "
                     'managing a counter ourselves, Python provides another type of loop called '
                     'the for loop, which automatically repeats once for each item in a collection '
                     "or over a sequence of numbers. In the next lesson, you'll learn how for "
                     'loops simplify many repetitive tasks and become one of the most commonly '
                     'used tools in programming.'},
            {'page': 2, 'type': 'heading', 'text': 'Lesson 4.1 – For Loops'},
            {'page': 2, 'type': 'heading', 'text': 'Prerequisites'},
            {'page': 2,
             'type': 'list',
             'items': ['Lesson 1.0 – Variables & Data Types',
                       'Lesson 1.1 – Using Variables',
                       'Lesson 2 – Teaching Programs to Make Decisions',
                       'Lesson 3.0 – Tuples',
                       'Lesson 3.1 – Lists, Mutation & Aliasing',
                       'Lesson 3.2 – Dictionaries: Organizing Information with Keys',
                       'Lesson 4.0 – While Loops']},
            {'page': 2, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
            {'page': 2, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 2,
             'type': 'list',
             'items': ['Explain why for loops are useful.',
                       'Iterate through strings, tuples, lists, and dictionaries.',
                       'Use the range() function.',
                       'Use the loop variable.',
                       'Explain the difference between for and while loops.']},
            {'page': 2, 'type': 'heading', 'text': 'Word Bank'},
            {'page': 2,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">For Loop</span> &nbsp; <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">Loop Variable</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">Iterable</span> &nbsp; <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">range()</span>'},
            {'page': 2, 'type': 'heading', 'text': 'Introduction'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'In the previous lesson, we learned how while loops repeat a block of code while a '
                     'condition remains True. For instance,'},
            {'page': 2,
             'type': 'code',
             'text': 'count = 1\n\nwhile count <= 5:\n    print(count)\n    count += 1'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'This works well whenever we want to repeat code until something happens. However, many '
                     "programming tasks don't involve repeating until a condition changes. Instead, we want to "
                     'repeat once for every item in a collection.'},
            {'page': 2, 'type': 'paragraph', 'text': "Imagine printing every student's name in a class roster."},
            {'page': 2,
             'type': 'code',
             'text': 'students = [\n    "Jordan",\n    "Maria",\n    "Alex",\n    "Taylor"\n]'},
            {'page': 2, 'type': 'paragraph', 'text': 'Without loops, we would need to write'},
            {'page': 2,
             'type': 'code',
             'text': 'print(students[0])\nprint(students[1])\nprint(students[2])\nprint(students[3])'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'This quickly becomes impractical if the class has 30 students or if new students are '
                     "added throughout the year. Instead, we'd like Python to automatically visit each student "
                     'one at a time.'},
            {'page': 2,
             'type': 'rich_paragraph',
             'html': 'This is exactly what a <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">for loop</span> does. A for loop repeats a block of '
                     'code once for every element in a collection.'},
            {'page': 2, 'type': 'heading', 'text': 'Spotlight'},
            {'page': 2,
             'type': 'paragraph',
             'text': "Basketball isn't just played on the court—it's also analyzed with code. Teams like the "
                     'Oklahoma City Thunder collect thousands of pieces of data during every game, including '
                     'points, rebounds, assists, shot locations, passes, player speed, and defensive '
                     'positioning. Programmers and data analysts write software to process this information '
                     'and help coaches make better decisions.'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'One common programming tool for analyzing sports data is the for loop. For example, a '
                     "program might use a for loop to examine every player's statistics, calculate the team's "
                     'average shooting percentage, or count how many three-pointers were made in a game. '
                     'Rather than writing separate code for every player, a single for loop can automatically '
                     "process the entire roster. As you learn Python, you'll begin using the same type of "
                     'programming techniques that data analysts use to understand sports, improve team '
                     'performance, and turn raw numbers into meaningful insights.'},
            {'page': 2, 'type': 'heading', 'text': 'Section 1 – Writing Your First For Loop'},
            {'page': 2, 'type': 'paragraph', 'text': 'The general syntax of a for loop is'},
            {'page': 2, 'type': 'code', 'text': 'for variable in collection:\n    # code to repeat'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Unlike a while loop, a for loop does not require a Boolean condition or a counter. '
                     'Instead, Python automatically visits each element in the collection. For example,'},
            {'page': 2,
             'type': 'code',
             'text': 'students = [\n'
                     '    "Jordan",\n'
                     '    "Maria",\n'
                     '    "Alex"\n'
                     ']\n'
                     '\n'
                     'for student in students:\n'
                     '    print(student)\n'
                     '\n'
                     'Output\n'
                     'Jordan\n'
                     'Maria\n'
                     'Alex'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Notice that the variable student changes automatically during each iteration.'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'During the first iteration, student stores Jordan. During the second iteration, student '
                     'stores Maria. Finally, student stores Alex. Once every element has been processed, the '
                     'loop ends automatically.'},
            {'page': 2, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 2,
             'type': 'quiz',
             'question': 'What is printed?\n'
                         '\n'
                         'colors = [\n'
                         '    "Red",\n'
                         '    "Blue",\n'
                         '    "Green"\n'
                         ']\n'
                         '\n'
                         'for color in colors:\n'
                         '    print(color)',
             'options': ['A. 0\n1\n2', 'B. Green\nBlue\nRed', 'C. An error', 'D. Red\nBlue\nGreen'],
             'answer': 'D. Red\nBlue\nGreen'},
            {'page': 2, 'type': 'heading', 'text': 'Section 2 – The Loop Variable'},
            {'page': 2,
             'type': 'rich_paragraph',
             'html': 'The variable after the word for is called the <span style="background:#fff1df; '
                     'color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">loop '
                     'variable</span>. A loop variable stores one element from the collection during each '
                     'iteration.'},
            {'page': 2, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 2,
             'type': 'code',
             'text': 'numbers = [\n    10,\n    20,\n    30\n]\n\nfor number in numbers:\n    print(number)'},
            {'page': 2, 'type': 'paragraph', 'text': 'The loop variable changes automatically.'},
            {'page': 2,
             'type': 'table',
             'headers': ['Iteration', 'number'],
             'rows': [['1', '10'], ['2', '20'], ['3', '30']]},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Notice that we never manually update number. Python does that for us. This is one of the '
                     'biggest differences between a for loop and a while loop.'},
            {'page': 2, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 2,
             'type': 'quiz',
             'question': 'In the following code,\n'
                         '\n'
                         'animals = [\n'
                         '    "Dog",\n'
                         '    "Cat",\n'
                         '    "Bird"\n'
                         ']\n'
                         '\n'
                         'for animal in animals:\n'
                         '    print(animal)\n'
                         '\n'
                         'what is the loop variable?',
             'options': ['A. animals', 'B. animal', 'C. print', 'D. Dog'],
             'answer': 'B. animal'},
            {'page': 2, 'type': 'heading', 'text': 'Section 3 – Iterating Through Different Collections'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'One of the greatest strengths of for loops is that they work with many different '
                     'collection types.'},
            {'page': 2, 'type': 'heading', 'text': 'Strings'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Since strings are sequential data types, a for loop visits one character at a time.'},
            {'page': 2,
             'type': 'code',
             'text': 'for letter in "Python":\n    print(letter)\n\nOutput\nP\ny\nt\nh\no\nn'},
            {'page': 2, 'type': 'heading', 'text': 'Tuples'},
            {'page': 2,
             'type': 'code',
             'text': 'coordinates = (\n    35.4,\n    -97.5\n)\n\nfor value in coordinates:\n    print(value)'},
            {'page': 2, 'type': 'heading', 'text': 'Lists'},
            {'page': 2,
             'type': 'code',
             'text': 'foods = [\n'
                     '    "Pizza",\n'
                     '    "Tacos",\n'
                     '    "Pho"\n'
                     ']\n'
                     '\n'
                     'for food in foods:\n'
                     '    print(food)'},
            {'page': 2, 'type': 'heading', 'text': 'Dictionaries'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'By default, a for loop iterates over the keys of a dictionary.'},
            {'page': 2,
             'type': 'code',
             'text': 'student = {\n'
                     '    "name": "Jordan",\n'
                     '    "grade": 11,\n'
                     '    "gpa": 3.8\n'
                     '}\n'
                     '\n'
                     'for key in student:\n'
                     '    print(key)\n'
                     '\n'
                     'Output\n'
                     'name\n'
                     'grade\n'
                     'gpa'},
            {'page': 2,
             'type': 'paragraph',
             'text': "We'll learn more about looping through dictionary values in a later lesson."},
            {'page': 2, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 2,
             'type': 'quiz',
             'question': 'Which collections can be used in a for loop?',
             'options': ['A. Strings only',
                         'B. Lists only',
                         'C. Strings, tuples, lists, and dictionaries',
                         'D. Tuples and lists only'],
             'answer': 'C. Strings, tuples, lists, and dictionaries'},
            {'page': 2, 'type': 'heading', 'text': 'Section 4 – The range() Function'},
            {'page': 2,
             'type': 'paragraph',
             'text': "Sometimes we don't want to loop through a collection. Instead, we simply want to repeat "
                     'something a certain number of times. Python provides the range() function for this '
                     'purpose.'},
            {'page': 2,
             'type': 'rich_paragraph',
             'html': 'The <span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">range() function</span> creates an <span style="background:#fff1df; '
                     'color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">iterable</span>, '
                     'which is an object that can be visited one element at a time by a for loop. In fact, '
                     "every collection we've used so far—strings, tuples, lists, and dictionaries—is also an "
                     "iterable. That's why each of them can be used in a for loop."},
            {'page': 2,
             'type': 'code',
             'text': 'for number in range(5):\n    print(number)\n\nOutput\n0\n1\n2\n3\n4'},
            {'page': 2, 'type': 'paragraph', 'text': 'Notice that counting begins at 0.'},
            {'page': 2, 'type': 'paragraph', 'text': 'You can also specify a starting value.'},
            {'page': 2,
             'type': 'code',
             'text': 'for number in range(1,6):\n    print(number)\n\nOutput\n1\n2\n3\n4\n5'},
            {'page': 2, 'type': 'paragraph', 'text': 'The general form is'},
            {'page': 2, 'type': 'code', 'text': 'range(start, stop)'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Python begins at start and stops before stop. You may also include a third argument to '
                     'specify the step size.'},
            {'page': 2,
             'type': 'code',
             'text': 'for number in range(0,11,2):\n    print(number)\n\nOutput\n0\n2\n4\n6\n8\n10'},
            {'page': 2,
             'type': 'tip',
             'text': "If you remember how slicing works, you'll remember range(): start is included, stop is "
                     'excluded, and step allows you to skip numbers.'},
            {'page': 2, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 2,
             'type': 'quiz',
             'question': 'What does this print?\n\nfor i in range(2,8,2):\n    print(i)',
             'options': ['A. 2\n4\n6\n8', 'B. 0\n2\n4\n6', 'C. 2\n6\n8', 'D. 2\n4\n6'],
             'answer': 'D. 2\n4\n6'},
            {'page': 2, 'type': 'heading', 'text': 'Section 5 – Choosing Between while and for'},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Both loops repeat code, but they are designed for different situations. Use a while loop '
                     "when you don't know how many times the loop should execute."},
            {'page': 2, 'type': 'paragraph', 'text': 'Examples include:'},
            {'page': 2,
             'type': 'list',
             'items': ['Password validation', 'User menus', 'Waiting for valid input']},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Use a for loop when you want to process every element in a collection or repeat a known '
                     'number of times.'},
            {'page': 2, 'type': 'paragraph', 'text': 'Examples include:'},
            {'page': 2,
             'type': 'list',
             'items': ["Printing every student's name",
                       'Calculating the sum of a list',
                       'Counting from 1 to 100']},
            {'page': 2, 'type': 'paragraph', 'text': 'As a general rule:'},
            {'page': 2,
             'type': 'quote',
             'text': "If you already know what you're looping over, a for loop is usually the better choice."},
            {'page': 2, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 2,
             'type': 'quiz',
             'question': 'Which loop would be the better choice for repeatedly asking a user to enter the '
                         'correct password?',
             'options': ['A. for', 'B. while'],
             'answer': 'B. while'},
            {'page': 2, 'type': 'heading', 'text': 'Section 6 – Mini Project: Classroom Grades'},
            {'page': 2,
             'type': 'paragraph',
             'text': "A teacher has stored her students' quiz scores in a list."},
            {'page': 2, 'type': 'code', 'text': 'grades = [\n    92,\n    85,\n    100,\n    78,\n    95\n]'},
            {'page': 2, 'type': 'paragraph', 'text': 'Using a for loop, complete the following tasks.'},
            {'page': 2,
             'type': 'list',
             'items': ['1. Print every grade.',
                       '2. Count how many grades are greater than or equal to 90.',
                       '3. Find the highest grade.',
                       '4. Calculate the sum of all grades.',
                       '5. Calculate the class average.']},
            {'page': 2,
             'type': 'paragraph',
             'text': 'Challenge: Print only the grades that are passing (70 or higher).'},
            {'page': 2, 'type': 'heading', 'text': 'Key Takeaways'},
            {'page': 2, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 2,
             'type': 'list',
             'items': ['Write for loops.',
                       'Explain what a loop variable is.',
                       'Iterate through strings, tuples, lists, and dictionaries.',
                       'Use range() to repeat code a specific number of times.',
                       'Choose between for and while loops.']},
            {'page': 2, 'type': 'heading', 'text': 'Looking Ahead'},
            {'page': 2,
             'type': 'paragraph',
             'text': "So far, we've used loops to process one collection at a time. But what if we have a "
                     'collection inside another collection? For example, imagine a classroom seating chart, a '
                     "game board, or a multiplication table. In the next lesson, you'll learn about nested "
                     'loops, where one loop runs inside another to solve more complex problems.'},
            {'page': 3, 'type': 'heading', 'text': 'Lesson 4.2 – Nested Loops'},
            {'page': 3, 'type': 'heading', 'text': 'Prerequisites'},
            {'page': 3,
             'type': 'list',
             'items': ['Lesson 1.0 – Variables & Data Types',
                       'Lesson 1.1 – Using Variables',
                       'Lesson 2 – Teaching Programs to Make Decisions',
                       'Lesson 3.0 – Tuples',
                       'Lesson 3.1 – Lists, Mutation & Aliasing',
                       'Lesson 3.2 – Dictionaries: Organizing Information with Keys',
                       'Lesson 4.0 – While Loops',
                       'Lesson 4.1 – For Loops']},
            {'page': 3, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
            {'page': 3, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 3,
             'type': 'list',
             'items': ['Explain what a nested loop is.',
                       'Predict how many times nested loops execute.',
                       'Trace nested loops step by step.',
                       'Create simple text-based patterns.',
                       'Use nested loops to solve two-dimensional problems.']},
            {'page': 3, 'type': 'heading', 'text': 'Vocabulary'},
            {'page': 3,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">Nested Loop</span> &nbsp; <span style="background:#fff1df; '
                     'color:#c74716; padding:2px 7px; border-radius:6px; font-weight:600;">Outer Loop</span> '
                     '&nbsp; <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Inner Loop</span>'},
            {'page': 3, 'type': 'heading', 'text': 'Introduction'},
            {'page': 3,
             'type': 'paragraph',
             'text': "So far, we've used one loop at a time. Sometimes, however, a problem requires repeating "
                     'another repetition. Imagine a teacher who wants to print attendance for every student in '
                     'every classroom, or a game developer who needs to examine every square on a game board. '
                     "In these situations, one loop isn't enough. Instead, we place one loop inside another. "
                     'This is called a nested loop.'},
            {'page': 3, 'type': 'heading', 'text': 'Spotlight'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'GoldFire Studios is an independent video game studio founded in Oklahoma City in 2008. '
                     'The studio creates games for players around the world, including titles like Arctic '
                     'Awakening, Exocraft, and CasinoRPG. Their mission is to create interactive stories that '
                     'connect people through gaming.'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Many games are built using nested loops. Imagine a game map made of rows and columns. To '
                     'draw the map or check every tile for obstacles, a program uses an outer loop to move '
                     'through each row and an inner loop to visit every column within that row. Both outer and '
                     'inner loops may sound confusing now, but they will be discussed in the next section. '
                     'With just two loops, the game can process an entire world—whether it contains 100 tiles '
                     "or 100,000. As you learn nested loops, you're practicing one of the same programming "
                     'techniques that game developers use to build interactive worlds.'},
            {'page': 3, 'type': 'heading', 'text': 'Section 1 – What Is a Nested Loop?'},
            {'page': 3,
             'type': 'rich_paragraph',
             'html': 'Recall from the introduction that a <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">nested loop</span> is a loop '
                     'placed inside another loop. The outside loop is called the <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">outer loop</span>. The inside loop is called the <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">inner loop</span>.'},
            {'page': 3, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 3,
             'type': 'code',
             'text': 'for row in range(3):\n    for column in range(4):\n        print("*")'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Be careful, however, because the output of this code is NOT:'},
            {'page': 3, 'type': 'code', 'text': '****\n****\n****'},
            {'page': 3, 'type': 'paragraph', 'text': 'The output is actually,'},
            {'page': 3, 'type': 'code', 'text': '*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Notice that there are 12 stars because the outer loop runs 3 times. During each outer '
                     'loop iteration, the inner loop runs 4 times. So the total number of stars is correct, '
                     'but the format is not what we really wanted our code to output based on what we named '
                     'our loop variables.'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'The key idea to remember is this: the outer loop controls the rows, while the inner loop '
                     'controls the columns. Notice that every time the outer loop repeats, the inner loop '
                     'starts over from the beginning.'},
            {'page': 3,
             'type': 'tip',
             'text': "This example is actually useful because it shows that nested loops don't automatically "
                     'create rows and columns. Since print() moves to a new line after every call, each * '
                     'appears on its own line.'},
            {'page': 3, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 3,
             'type': 'quiz',
             'question': 'How many loops are in the following program?\n'
                         '\n'
                         'for x in range(2):\n'
                         '    for y in range(5):\n'
                         '        print(x, y)',
             'options': ['A. Two', 'B. One', 'C. Three', 'D. Five'],
             'answer': 'A. Two'},
            {'page': 3, 'type': 'heading', 'text': 'Section 2 – Tracing a Nested Loop'},
            {'page': 3, 'type': 'paragraph', 'text': "Let's examine what actually happens."},
            {'page': 3,
             'type': 'code',
             'text': 'for row in range(2):\n'
                     '    print("Row", row)\n'
                     '\n'
                     '    for column in range(3):\n'
                     '        print(column)'},
            {'page': 3, 'type': 'heading', 'text': 'Outer Loop (Iteration 1)'},
            {'page': 3, 'type': 'code', 'text': 'row = 0\n\nOutput\nRow 0'},
            {'page': 3, 'type': 'paragraph', 'text': 'Now the inner loop begins.'},
            {'page': 3, 'type': 'code', 'text': 'column = 0\ncolumn = 1\ncolumn = 2\n\nOutput\n0\n1\n2'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'The inner loop finishes. Python returns to the outer loop.'},
            {'page': 3, 'type': 'heading', 'text': 'Outer Loop (Iteration 2)'},
            {'page': 3, 'type': 'code', 'text': 'row = 1\n\nOutput\nRow 1'},
            {'page': 3, 'type': 'paragraph', 'text': 'The inner loop starts again.'},
            {'page': 3, 'type': 'code', 'text': 'column = 0\ncolumn = 1\ncolumn = 2\n\nOutput\n0\n1\n2'},
            {'page': 3, 'type': 'paragraph', 'text': 'Complete output'},
            {'page': 3, 'type': 'code', 'text': 'Row 0\n0\n1\n2\nRow 1\n0\n1\n2'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Notice that the inner loop completely finishes every time the outer loop runs once.'},
            {'page': 3, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 3,
             'type': 'quiz',
             'question': 'How many total times is the inner loop executed?\n'
                         '\n'
                         'for i in range(4):\n'
                         '    for j in range(2):\n'
                         '        print(j)',
             'options': ['A. 2', 'B. 8', 'C. 4', 'D. 6'],
             'answer': 'B. 8'},
            {'page': 3, 'type': 'heading', 'text': 'Section 3 – Creating Patterns'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Nested loops are commonly used to create patterns. Suppose we want to print four stars '
                     'on three different lines.'},
            {'page': 3,
             'type': 'code',
             'text': 'for row in range(3):\n'
                     '    for column in range(4):\n'
                     '        print("*", end="")\n'
                     '    print()\n'
                     '\n'
                     'Output\n'
                     '****\n'
                     '****\n'
                     '****'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'The inner loop prints one row. The outer loop decides how many rows to create. Changing '
                     'either loop changes the size of the pattern.'},
            {'page': 3, 'type': 'heading', 'text': 'Example'},
            {'page': 3,
             'type': 'code',
             'text': 'for row in range(5):\n'
                     '    for column in range(2):\n'
                     '        print("#", end="")\n'
                     '    print()\n'
                     '\n'
                     'Output\n'
                     '##\n'
                     '##\n'
                     '##\n'
                     '##\n'
                     '##'},
            {'page': 3, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 3,
             'type': 'quiz',
             'question': 'What does this program print?\n'
                         '\n'
                         'for row in range(2):\n'
                         '    for column in range(3):\n'
                         '        print("@", end="")\n'
                         '    print()',
             'options': ['A. @@@@@@', 'B. @\n@@\n@@@', 'C. @@@\n@@@', 'D. @@\n@@\n@@'],
             'answer': 'C. @@@\n@@@'},
            {'page': 3, 'type': 'heading', 'text': 'Section 4 – Nested Loops with Collections'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Nested loops are useful when working with collections inside other collections. For '
                     'example, imagine storing classroom seating assignments in a classroom set up in rows.'},
            {'page': 3,
             'type': 'code',
             'text': 'classroom = [\n    ["Alex", "Maria", "Jordan"],\n    ["Sophia", "Liam", "Emma"]\n]'},
            {'page': 3,
             'type': 'paragraph',
             'text': "Each inner list represents one row of students. We can print every student's name using "
                     'nested loops.'},
            {'page': 3,
             'type': 'code',
             'text': 'for row in classroom:\n'
                     '    for student in row:\n'
                     '        print(student)\n'
                     '\n'
                     'Output\n'
                     'Alex\n'
                     'Maria\n'
                     'Jordan\n'
                     'Sophia\n'
                     'Liam\n'
                     'Emma'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Nested loops allow us to process every item, even when collections contain other '
                     'collections.'},
            {'page': 3, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 3,
             'type': 'quiz',
             'question': 'Which type of data is often processed using nested loops?',
             'options': ['A. A single integer',
                         'B. A Boolean value',
                         'C. A single string',
                         'D. A list containing other lists'],
             'answer': 'D. A list containing other lists'},
            {'page': 3, 'type': 'heading', 'text': 'Section 5 – How Many Times Does a Nested Loop Run?'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'A useful way to think about nested loops is multiplication.'},
            {'page': 3, 'type': 'paragraph', 'text': 'Suppose we have'},
            {'page': 3,
             'type': 'code',
             'text': 'for row in range(5):\n    for column in range(4):\n        print("*")'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'The outer loop runs 5 times. Each time, the inner loop runs 4 times.'},
            {'page': 3, 'type': 'paragraph', 'text': 'Total executions:'},
            {'page': 3, 'type': 'code', 'text': '5 × 4 = 20'},
            {'page': 3, 'type': 'paragraph', 'text': 'In general,'},
            {'page': 3,
             'type': 'code',
             'text': 'Total inner loop iterations = (Outer Loop Iterations) × (Inner Loop Iterations)'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'This idea becomes very important when analyzing the efficiency of programs.'},
            {'page': 3, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 3,
             'type': 'quiz',
             'question': 'How many stars are printed?\n'
                         '\n'
                         'for i in range(6):\n'
                         '    for j in range(3):\n'
                         '        print("*")',
             'options': ['A. 18', 'B. 9', 'C. 12', 'D. 36'],
             'answer': 'A. 18'},
            {'page': 3, 'type': 'heading', 'text': 'Section 6 – Mini Project: Draw a Rectangle'},
            {'page': 3, 'type': 'paragraph', 'text': 'Write a program that asks the user for'},
            {'page': 3, 'type': 'list', 'items': ['the number of rows', 'the number of columns']},
            {'page': 3, 'type': 'paragraph', 'text': 'Then use nested loops to draw a rectangle of stars.'},
            {'page': 3, 'type': 'heading', 'text': 'Example'},
            {'page': 3, 'type': 'code', 'text': 'Rows: 3\nColumns: 5\n\n*****\n*****\n*****'},
            {'page': 3, 'type': 'heading', 'text': 'Challenge'},
            {'page': 3,
             'type': 'paragraph',
             'text': 'Modify your program so that it prints the row number before each row.'},
            {'page': 3, 'type': 'heading', 'text': 'Example'},
            {'page': 3, 'type': 'code', 'text': 'Row 1: *****\nRow 2: *****\nRow 3: *****'},
            {'page': 3, 'type': 'heading', 'text': 'Key Takeaways'},
            {'page': 3, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 3,
             'type': 'list',
             'items': ['Explain what a nested loop is.',
                       'Distinguish between the outer and inner loops.',
                       'Trace nested loops step by step.',
                       'Create simple text patterns.',
                       'Use nested loops to process two-dimensional collections.']},
            {'page': 3, 'type': 'heading', 'text': 'Looking Ahead'},
            {'page': 3,
             'type': 'paragraph',
             'text': "Sometimes, a loop shouldn't continue until it naturally finishes. You may want to stop a "
                     'loop early, skip certain iterations, or leave a placeholder while writing code. In the '
                     "next lesson, you'll learn how to control loop execution using the break, continue, and "
                     'pass statements.'},
            {'page': 4, 'type': 'heading', 'text': 'Lesson 4.3 – Advanced Loop Techniques'},
            {'page': 4, 'type': 'heading', 'text': 'Prerequisites'},

            {'page': 4,
 'type': 'list',
 'items': ['Lesson 1.0 – Variables & Data Types',
           'Lesson 1.1 – Using Variables',
           'Lesson 2 – Teaching Programs to Make Decisions',
           'Lesson 3.0 – Tuples',
           'Lesson 3.1 – Lists, Mutation & Aliasing',
           'Lesson 3.2 – Dictionaries: Organizing Information with Keys',
           'Lesson 4.0 – While Loops',
           'Lesson 4.1 – For Loops',
           'Lesson 4.2 – Nested Loops']},
            {'page': 4, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
            {'page': 4, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 4,
             'type': 'list',
             'items': ['Stop a loop early using break.',
                       'Skip an iteration using continue.',
                       'Explain the purpose of pass.',
                       'Solve common problems using loops.',
                       'Count, sum, search, and find maximum or minimum values in collections.']},
            {'page': 4, 'type': 'heading', 'text': 'Vocabulary'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">break</span> &nbsp; <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">continue</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">pass</span> &nbsp; <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">Accumulator</span>'},
            {'page': 4, 'type': 'heading', 'text': 'Introduction'},
            {'page': 4,
             'type': 'paragraph',
             'text': "Now that you know how to write loops, it's time to learn how to make them more powerful. "
                     "Sometimes you don't want a loop to continue until it naturally ends. Maybe you've "
                     "already found what you're looking for, or maybe you want to skip certain values. You'll "
                     'also learn several common problem-solving techniques that programmers use every day. '
                     'These patterns appear in everything from video games to scientific research and data '
                     'analysis.'},
            {'page': 4, 'type': 'heading', 'text': 'Spotlight'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'The National Weather Center in Norman, Oklahoma, collects enormous amounts of weather '
                     "data every day. Meteorologists don't examine every measurement by hand. Instead, "
                     'computer programs use loops to process thousands of readings automatically. A program '
                     'might search for the highest recorded temperature, calculate the average rainfall, count '
                     'how many counties received severe weather warnings, or stop searching as soon as it '
                     "detects dangerous conditions. These tasks rely on the same loop techniques you'll learn "
                     'in this lesson.'},
            {'page': 4, 'type': 'heading', 'text': 'Section 1 – Stopping a Loop with break'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': 'Sometimes a program finishes its job before the loop naturally ends. The <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">break statement</span> immediately exits the current loop.'},
            {'page': 4, 'type': 'heading', 'text': 'Example'},
            {'page': 4,
             'type': 'code',
             'text': 'for number in range(1, 11):\n'
                     '    if number == 6:\n'
                     '        break\n'
                     '\n'
                     '    print(number)\n'
                     '\n'
                     'Output\n'
                     '1\n'
                     '2\n'
                     '3\n'
                     '4\n'
                     '5'},
            {'page': 4, 'type': 'paragraph', 'text': 'As soon as Python reaches break, the loop ends.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What is printed?\n'
                         '\n'
                         'for letter in "python":\n'
                         '    if letter == "h":\n'
                         '        break\n'
                         '\n'
                         '    print(letter)',
             'options': ['A. py', 'B. python', 'C. pyt', 'D. thon'],
             'answer': 'A. py'},
            {'page': 4, 'type': 'heading', 'text': 'Section 2 – Skipping an Iteration with continue'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': 'Unlike break, <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">continue</span> does not stop the loop. Instead, it '
                     'skips the rest of the current iteration and moves to the next one.'},
            {'page': 4,
             'type': 'code',
             'text': 'for number in range(1, 8):\n'
                     '    if number % 2 == 0:\n'
                     '        continue\n'
                     '\n'
                     '    print(number)\n'
                     '\n'
                     'Output\n'
                     '1\n'
                     '3\n'
                     '5\n'
                     '7'},
            {'page': 4, 'type': 'paragraph', 'text': 'Even numbers are skipped.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What prints?\n\nfor i in range(5):\n    if i == 2:\n        continue\n\n    print(i)',
             'options': ['A. 0\n1\n2\n3\n4', 'B. 0\n1\n3\n4', 'C. 2\n3\n4', 'D. 0\n1'],
             'answer': 'B. 0\n1\n3\n4'},
            {'page': 4, 'type': 'heading', 'text': 'Section 3 – Placeholder Code with pass'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': "Sometimes you're still writing a program and haven't finished part of it yet. Python "
                     'requires every block of code to contain at least one statement. The <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">pass statement</span> tells Python: "Do nothing for now."'},
            {'page': 4, 'type': 'heading', 'text': 'Example'},
            {'page': 4, 'type': 'code', 'text': 'if score > 90:\n    pass'},
            {'page': 4,
             'type': 'paragraph',
             'text': "This allows the program to run even though the code isn't finished. Unlike break and "
                     "continue, pass doesn't affect how the loop runs."},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What does pass do?',
             'options': ['A. Ends the loop',
                         'B. Skips an iteration',
                         'C. Does nothing',
                         'D. Restarts the loop'],
             'answer': 'C. Does nothing'},
            {'page': 4, 'type': 'heading', 'text': 'Section 4 – Counting'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'One of the most common tasks in programming is counting. Rather than simply printing '
                     'every value in a collection, we often want to answer questions such as:'},
            {'page': 4,
             'type': 'list',
             'items': ['How many students passed the exam?',
                       'How many temperatures were above 90°F?',
                       'How many vowels appear in a word?',
                       'How many basketball players scored at least 20 points?']},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': 'Whenever you\'re trying to answer a question that begins with "How many...?", you\'ll '
                     'almost always use a <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">counter</span>. A counter is simply a variable that '
                     'keeps track of how many times something has happened. Counters usually start at 0 '
                     'because, before the loop begins, nothing has been counted yet. As the loop examines each '
                     'item, it checks whether the item meets a certain condition. If it does, the counter '
                     'increases by one.'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'For example, suppose we want to count how many even numbers appear in a list.'},
            {'page': 4,
             'type': 'code',
             'text': 'numbers = [3, 8, 5, 2, 10]\n'
                     'count = 0\n'
                     '\n'
                     'for number in numbers:\n'
                     '    if number % 2 == 0:\n'
                     '        count += 1\n'
                     '\n'
                     'print(count)\n'
                     '\n'
                     'Output\n'
                     '3'},
            {'page': 4, 'type': 'paragraph', 'text': "Let's trace the program."},
            {'page': 4,
             'type': 'table',
             'headers': ['Current Number', 'Even?', 'Count'],
             'rows': [['3', 'No', '0'],
                      ['8', 'Yes', '1'],
                      ['5', 'No', '1'],
                      ['2', 'Yes', '2'],
                      ['10', 'Yes', '3']]},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Notice that the variable count only changes when the condition is true. Numbers that are '
                     'not even simply leave the counter unchanged. This counting pattern appears throughout '
                     "computer science. Whether you're counting wins in a game, customers who made a purchase, "
                     'or words in a document, the overall structure of the algorithm stays almost exactly the '
                     'same.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What will count equal after this program finishes?\n'
                         '\n'
                         'letters = "banana"\n'
                         'count = 0\n'
                         '\n'
                         'for letter in letters:\n'
                         '    if letter == "a":\n'
                         '        count += 1',
             'options': ['A. 2', 'B. 4', 'C. 6', 'D. 3'],
             'answer': 'D. 3'},
            {'page': 4, 'type': 'heading', 'text': 'Section 5 – Summing Values'},
            {'page': 4,
             'type': 'paragraph',
             'text': "Sometimes we don't want to count items—we want to find their total. Imagine a teacher "
                     "adding together students' test scores, a cashier totaling the prices of groceries, or a "
                     'fitness app calculating the number of calories burned during the week. In each case, we '
                     'repeatedly add values together to produce one final total.'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': 'This process is called <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">accumulation</span>. An <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">accumulator</span> is a variable that stores a running total as a loop '
                     'executes. Like counters, accumulators usually begin at 0. However, instead of increasing '
                     'by 1, an accumulator increases by whatever value is currently being processed.'},
            {'page': 4, 'type': 'paragraph', 'text': 'Consider the following example.'},
            {'page': 4,
             'type': 'code',
             'text': 'numbers = [4, 8, 3]\n'
                     'total = 0\n'
                     '\n'
                     'for number in numbers:\n'
                     '    total += number\n'
                     '\n'
                     'print(total)\n'
                     '\n'
                     'Output\n'
                     '15'},
            {'page': 4, 'type': 'paragraph', 'text': "Let's trace the program."},
            {'page': 4,
             'type': 'table',
             'headers': ['Current Number', 'Running Total'],
             'rows': [['Start', '0'], ['4', '4'], ['8', '12'], ['3', '15']]},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Notice that the accumulator grows larger every iteration because each new value is added '
                     'to the previous total. This pattern is one of the most useful techniques in programming. '
                     'It can be used to calculate totals, averages, distances traveled, money earned, game '
                     'scores, and countless other quantities.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What prints after this program finishes?\n'
                         '\n'
                         'total = 0\n'
                         '\n'
                         'for n in [2, 5, 7]:\n'
                         '    total += n\n'
                         '\n'
                         'print(total)',
             'options': ['A. 7', 'B. 9', 'C. 12', 'D. 14'],
             'answer': 'D. 14'},
            {'page': 4, 'type': 'heading', 'text': 'Section 6 – Finding the Largest Value'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Another common problem in programming is finding the largest (or maximum) value in a '
                     'collection. Imagine a teacher wants to find the highest exam score in a class, a weather '
                     'station wants to determine the hottest temperature of the week, or a basketball coach '
                     'wants to know which player scored the most points in a game. Rather than comparing every '
                     'value by hand, we can write a loop that keeps track of the largest value seen so far.'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'To do this, we create a variable that stores the current largest value. A common mistake '
                     'is to initialize this variable to 0, since some collections may contain only negative '
                     'numbers. Instead, we usually begin by assuming that the first element is the largest. '
                     'Then, as the loop examines each remaining value, it compares that value to the current '
                     'largest. If the new value is larger, we update our variable. By the time the loop '
                     'finishes, the variable will contain the largest value in the collection.'},
            {'page': 4, 'type': 'paragraph', 'text': 'Consider the following example.'},
            {'page': 4,
             'type': 'code',
             'text': 'scores = [87, 92, 75, 98, 81]\n'
                     'largest = scores[0]\n'
                     '\n'
                     'for score in scores:\n'
                     '    if score > largest:\n'
                     '        largest = score\n'
                     '\n'
                     'print(largest)\n'
                     '\n'
                     'Output\n'
                     '98'},
            {'page': 4, 'type': 'paragraph', 'text': "Let's trace the program."},
            {'page': 4,
             'type': 'table',
             'headers': ['Current Score', 'Largest So Far'],
             'rows': [['Start (87)', '87'],
                      ['87', '87'],
                      ['92', '92'],
                      ['75', '92'],
                      ['98', '98'],
                      ['81', '98']]},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Notice that largest only changes when a larger value is found. Smaller values are '
                     'ignored because they cannot become the maximum. Finding the smallest value follows '
                     'exactly the same pattern. The only difference is that we use the < operator instead of '
                     '>. This algorithm is used constantly in real-world software. Search engines rank the '
                     'highest-scoring results, fitness apps record your fastest run, and weather programs '
                     'report the hottest or coldest temperatures using this same idea.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'What is printed after this program finishes?\n'
                         '\n'
                         'values = [4, 9, 2]\n'
                         'largest = values[0]\n'
                         '\n'
                         'for value in values:\n'
                         '    if value > largest:\n'
                         '        largest = value\n'
                         '\n'
                         'print(largest)',
             'options': ['A. 2', 'B. 4', 'C. 9', 'D. 15'],
             'answer': 'C. 9'},
            {'page': 4, 'type': 'heading', 'text': 'Section 7 – Searching'},
            {'page': 4,
             'type': 'rich_paragraph',
             'html': "Sometimes we aren't interested in counting values or finding the largest one. Instead, "
                     'we simply want to know whether a particular value exists. This process is called <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; border-radius:6px; '
                     'font-weight:600;">searching</span>. Searching is one of the most common tasks in '
                     "computer science. Every time you search your contacts for a friend's name, look for a "
                     'song in a playlist, or search for a product in an online store, a computer is searching '
                     'through data.'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'A simple way to search is to examine each item one at a time until the desired value is '
                     'found. Suppose we want to determine whether the name "Maria" appears in a list.'},
            {'page': 4,
             'type': 'code',
             'text': 'names = ["Alex", "Maria", "Jordan"]\n'
                     'found = False\n'
                     '\n'
                     'for name in names:\n'
                     '    if name == "Maria":\n'
                     '        found = True\n'
                     '        break\n'
                     '\n'
                     'print(found)\n'
                     '\n'
                     'Output\n'
                     'True'},
            {'page': 4, 'type': 'paragraph', 'text': "Let's trace the program."},
            {'page': 4,
             'type': 'table',
             'headers': ['Current Name', 'Found?'],
             'rows': [['Start', 'False'], ['Alex', 'False'], ['Maria', 'True'], ['Loop Ends', 'True']]},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Notice that as soon as "Maria" is found, the program executes the break statement. Since '
                     "we've already answered our question, there is no reason to continue checking the "
                     'remaining names. Using break makes programs more efficient because it prevents '
                     'unnecessary work. If a list contains thousands of items, stopping early can save a '
                     'significant amount of time. Not every search uses break. Sometimes we need to examine '
                     "every item in a collection, even after finding a match. However, when we're only "
                     'interested in whether an item exists, stopping early is often the best choice.'},
            {'page': 4, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 4,
             'type': 'quiz',
             'question': 'Why is break useful in the previous example?',
             'options': ['A. It restarts the search.',
                         'B. It skips every other item.',
                         'C. It counts the items.',
                         'D. It prevents unnecessary iterations after the item is found.'],
             'answer': 'D. It prevents unnecessary iterations after the item is found.'},
            {'page': 4, 'type': 'heading', 'text': 'Section 8 – Mini Project: Weather Data Analyzer'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'A weather station recorded the following daily high temperatures.'},
            {'page': 4, 'type': 'code', 'text': 'temperatures = [91, 85, 88, 94, 99, 86, 90]'},
            {'page': 4, 'type': 'paragraph', 'text': 'Write a program that:'},
            {'page': 4,
             'type': 'list',
             'items': ['1. Calculates the average temperature.',
                       '2. Finds the hottest temperature.',
                       '3. Counts how many days were at least 90°F.',
                       '4. Stops searching if a temperature of 100°F is found.']},
            {'page': 4, 'type': 'heading', 'text': 'Challenge'},
            {'page': 4,
             'type': 'paragraph',
             'text': 'Modify the program so the user enters temperatures until they type -1. Then display all '
                     'of the same statistics.'},
            {'page': 4, 'type': 'heading', 'text': 'Key Takeaways'},
            {'page': 4, 'type': 'paragraph', 'text': 'By the end of this lesson, you should be able to:'},
            {'page': 4,
             'type': 'list',
             'items': ['Use break to exit a loop early.',
                       'Use continue to skip an iteration.',
                       'Explain the purpose of pass.',
                       'Count values that satisfy a condition.',
                       'Calculate running totals with accumulators.',
                       'Find the largest or smallest value in a collection.',
                       'Search a collection efficiently using loops.']},
            {'page': 4, 'type': 'heading', 'text': 'Looking Ahead'},
            {'page': 4,
             'type': 'paragraph',
             'text': "So far, you've learned how to store data in variables and collections and process that "
                     "data using loops. In the next unit, you'll learn how to organize larger programs by "
                     'writing your own reusable functions, allowing you to break complex problems into '
                     'smaller, manageable pieces.'}]},
    "functions_modularity": {'id': 'functions_modularity',
 'lesson_number': '5',
 'title': 'Functions & Modularity',
 'description': 'Lesson 5.0 - Writing Your Own Functions. Define reusable functions with '
                'parameters, arguments, return values, and docstrings.',
 'blocks': [{'page': 1, 'type': 'heading', 'text': 'Lesson 5.0 – Writing Your Own Functions'},
{'page': 1, 'type': 'heading', 'text': 'Prerequisites'},
            {'page': 1,
             'type': 'list',
             'items': ['Lesson 1.0 – Variables & Data Types',
                       'Lesson 1.1 – Using Variables',
                       'Lesson 2 – Teaching Programs to Make Decisions',
                       'Lesson 3.0 – Tuples',
                       'Lesson 3.1 – Lists, Mutation & Aliasing',
                       'Lesson 3.2 – Dictionaries: Organizing Information with Keys',
                       'Lesson 4.0 – While Loops',
                       'Lesson 4.1 – For Loops',
                       'Lesson 4.2 – Nested Loops',
                       'Lesson 4.3 – Advanced Loop Techniques']},
            {'page': 1, 'type': 'heading', 'text': 'Learning Objectives & Vocabulary'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'By the end of this lesson, you should be able to:'},
            {'page': 1,
             'type': 'list',
             'items': ['Explain what a function is and why programmers use them.',
                       'Define and call your own functions using the def keyword.',
                       'Distinguish between parameters and arguments.',
                       'Return values from a function using the return statement.',
                       'Write simple functions with descriptive names and docstrings.']},
            {'page': 1, 'type': 'heading', 'text': 'Vocabulary'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': '<span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Function</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">def</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Parameter</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Argument</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">return</span> &nbsp; <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">Docstring</span>'},
            {'page': 1, 'type': 'heading', 'text': 'Introduction'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Throughout your coding journey so far, you've already used many built-in "
                     'functions without realizing it.'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example, every time you write'},
            {'page': 1, 'type': 'code', 'text': 'print("Hello!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': "you're calling¹ the built-in print() function. Likewise, when you use len() "
                     'to count the number of characters in a string or input() to ask the user for '
                     "information, you're using functions that Python provides for you."},
            {'page': 1,
             'type': 'paragraph',
             'text': "As your programs become larger, however, built-in functions aren't always "
                     "enough. You'll often find yourself writing the same block of code over and "
                     'over again. Copying and pasting code works at first, but it quickly makes '
                     'programs longer, harder to read, and more difficult to fix when something '
                     'changes. Functions solve this problem.'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">function</span> is a reusable block of '
                     'code that performs a specific task. Instead of rewriting the same '
                     'instructions multiple times, you can place them inside a function and call '
                     'that function whenever you need it. This makes programs shorter, easier to '
                     'understand, and easier to maintain.'},
            {'page': 1,
             'type': 'paragraph',
             'text': "In this lesson, you'll learn how to create your own functions, pass "
                     'information into them, and return results back to your program. By the end '
                     "of the lesson, you'll be writing programs the same way professional software "
                     'developers do—by breaking large problems into smaller, reusable pieces.'},
            {'page': 1,
             'type': 'footnote',
             'number': '1',
             'text': 'When programmers say calling, they mean executing a function by writing its '
                     'name followed by parentheses.'},
            {'page': 1, 'type': 'heading', 'text': 'Spotlight'},
            {'page': 1,
             'type': 'heading',
             'text': 'Michael Running Wolf: Preserving Indigenous Languages with AI'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Michael Running Wolf is a software engineer and a citizen of the Northern '
                     "Cheyenne Tribe. Growing up in rural Montana, he later worked on Amazon's "
                     'Alexa team before founding Indigenous in AI and the First Languages AI '
                     'Reality (FLAIR) project. His work focuses on developing artificial '
                     'intelligence tools that help preserve and revitalize Indigenous languages.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Building an AI system requires much more than writing one long program. '
                     'Instead, programmers divide their software into many small, reusable '
                     'functions, each responsible for a specific task. One function might process '
                     'speech, another might recognize words, while another converts those words '
                     'into text. By combining many small functions, developers can build powerful '
                     'applications that are easier to understand, test, and improve. As you learn '
                     "to write your own functions, you're practicing one of the same techniques "
                     'used to build large software systems like the ones Michael Running Wolf '
                     'develops.'},
            {'page': 1, 'type': 'heading', 'text': 'Section 1 – Why Do We Need Functions?'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Imagine you're writing a program for a restaurant. Every time a customer "
                     'places an order, the program needs to print a receipt.'},
            {'page': 1, 'type': 'paragraph', 'text': 'You might write something like this:'},
            {'page': 1,
             'type': 'code',
             'text': 'print("----- RECEIPT -----")\n'
                     'print("Burger: $8.99")\n'
                     'print("Tax: $0.72")\n'
                     'print("Total: $9.71")\n'
                     'print("-------------------")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Now suppose the restaurant serves one hundred customers in a day. Copying '
                     'and pasting this same block of code one hundred times would make the program '
                     'unnecessarily long. Even worse, if the restaurant changes the receipt '
                     'format, you would have to edit every copy of the code. Instead, we can place '
                     'the receipt-printing code inside a function and call it whenever we need '
                     'it.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Functions help programmers:'},
            {'page': 1,
             'type': 'list',
             'items': ['Avoid repeating code.',
                       'Break large programs into smaller, manageable pieces.',
                       'Make programs easier to read and understand.',
                       'Fix bugs in one place instead of many places.']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Professional software projects often contain thousands—or even millions—of '
                     'lines of code. Without functions, these programs would be incredibly '
                     'difficult to build and maintain. You have already been using functions '
                     'throughout this book. Every time you wrote print(), input(), or len(), you '
                     'were calling a function that someone else had written. In this lesson, '
                     "you'll learn how to create your own."},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'Which of the following is the best reason to use a function?',
             'options': ['A. It allows you to reuse code instead of writing the same instructions '
                         'multiple times.',
                         'B. It makes the computer run faster.',
                         'C. It prevents all programming errors.',
                         'D. It automatically makes every program shorter.'],
             'answer': 'A. It allows you to reuse code instead of writing the same instructions '
                       'multiple times.'},
            {'page': 1,
             'type': 'heading',
             'text': 'Section 2 – Defining and Calling Your First Function'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': "Now that we know why functions are useful, it's time to learn how to create "
                     'one. Every function definition begins with the <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">def keyword</span>, followed by the '
                     "function's name and a pair of parentheses. Just like if statements and "
                     'loops, the code inside the function must be indented.'},
            {'page': 1, 'type': 'paragraph', 'text': "Here's the simplest function you can write."},
            {'page': 1, 'type': 'code', 'text': 'def greet():\n    print("Hello!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'This code defines a function named greet, but notice that nothing is printed '
                     "when Python reaches this code. That's because defining a function is not the "
                     'same as calling one. To execute the code inside the function, you must call '
                     'it by writing its name followed by parentheses.'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet():\n    print("Hello!")\n\ngreet()\n\nOutput\nHello!'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'When Python sees the function call greet(), it temporarily jumps to the '
                     'function definition, executes the indented code, and then returns to the '
                     'line after the function call. You can call the same function as many times '
                     'as you like.'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet():\n'
                     '    print("Hello!")\n'
                     '\n'
                     'greet()\n'
                     'greet()\n'
                     'greet()\n'
                     '\n'
                     'Output\n'
                     'Hello!\n'
                     'Hello!\n'
                     'Hello!'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Notice that we only wrote the greeting once, but it was printed three times. '
                     'This is one of the biggest advantages of functions: write the code once, '
                     'reuse it whenever you need it. You can even call functions from inside '
                     'loops.'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet():\n'
                     '    print("Hello!")\n'
                     '\n'
                     'for _ in range(5):\n'
                     '    greet()\n'
                     '\n'
                     'Output\n'
                     'Hello!\n'
                     'Hello!\n'
                     'Hello!\n'
                     'Hello!\n'
                     'Hello!'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'The loop repeats the function call, not the code inside the function. Every '
                     'time greet() is called, Python executes the same reusable block of code.'},
            {'page': 1,
             'type': 'tip',
             'text': "In a for loop, the variable _ is used when you don't need to use the loop "
                     'variable. It tells readers, "This value isn\'t important—I just want the '
                     'loop to repeat a certain number of times." You could write for i in '
                     'range(5): instead, but _ makes your intention clearer.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What is printed by the following program?\n'
                         '\n'
                         'def cheer():\n'
                         '    print("Go Team!")\n'
                         '\n'
                         'cheer()\n'
                         'cheer()',
             'options': ['A. Go Team!',
                         'B. Go Team!\nGo Team!',
                         'C. Nothing is printed.',
                         'D. An error occurs.'],
             'answer': 'B. Go Team!\nGo Team!'},
            {'page': 1, 'type': 'heading', 'text': 'Section 3 – Parameters and Arguments'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'The greet() function always prints the same message.'},
            {'page': 1, 'type': 'code', 'text': 'def greet():\n    print("Hello!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'But what if we wanted to greet different people? Instead of writing a new '
                     'function for every person, we can make our function accept input.'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'The information that a function receives is called a <span '
                     'style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">parameter</span>. A parameter is a '
                     'variable listed inside the parentheses of a function definition. It acts as '
                     'a placeholder that will receive a value whenever the function is called.'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet(name):\n    print("Hello,", name + "!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Here, name is the parameter. To execute the function, we provide a value.'},
            {'page': 1,
             'type': 'code',
             'text': 'greet("Alice")\n'
                     'greet("Bob")\n'
                     'greet("Carlos")\n'
                     '\n'
                     'Output\n'
                     'Hello, Alice!\n'
                     'Hello, Bob!\n'
                     'Hello, Carlos!'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Many built-in Python functions work the same way. For example, behind the '
                     'scenes, you can imagine print() looking something like this:'},
            {'page': 1,
             'type': 'code',
             'text': 'def print(s):\n    # code that displays s on the screen'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Here, s is the parameter. When you write print("Hello!"), the string '
                     '"Hello!" is passed into the parameter s, and the function\'s code displays '
                     'it on the screen. The real print() function is much more complex, but the '
                     'idea is the same: parameters let a function work with different inputs each '
                     "time it's called."},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'Now that you know how parameters work within the definition of a function, '
                     'how do programmers use functions? They pass values into the function called '
                     '<span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">arguments</span>. An argument is the '
                     'actual value supplied when a function is called.'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet(name):\n    print("Hello,", name + "!")\n\ngreet("Alice")'},
            {'page': 1,
             'type': 'list',
             'items': ['name is the parameter.', '"Alice" is the argument.']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Every time the function is called, Python assigns the argument to the '
                     'parameter before executing the function. Functions can also have more than '
                     'one parameter.'},
            {'page': 1,
             'type': 'code',
             'text': 'def introduce(name, age):\n'
                     '    print("My name is", name)\n'
                     '    print("I am", age, "years old.")'},
            {'page': 1, 'type': 'paragraph', 'text': 'Now we must provide two arguments.'},
            {'page': 1,
             'type': 'code',
             'text': 'introduce("Emma", 16)\n\nOutput\nMy name is Emma\nI am 16 years old.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Notice that the arguments are matched to the parameters in order. The first '
                     'argument is assigned to the first parameter, the second argument is assigned '
                     'to the second parameter, and so on.'},
            {'page': 1,
             'type': 'tip',
             'text': 'Think of a function like filling out an online order form. The parameters '
                     'are the blank fields on the form (Name, Address, Phone Number), while the '
                     'arguments are the information you actually type into those fields.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'In the following code, which is the parameter?\n'
                         '\n'
                         'def multiply(a, b):\n'
                         '    return a * b\n'
                         '\n'
                         'multiply(3, 5)',
             'options': ['A. 3', 'B. 5', 'C. a and b', 'D. multiply'],
             'answer': 'C. a and b'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What is the output of this program?\n'
                         '\n'
                         'def cheer(team):\n'
                         '    print("Go", team + "!")\n'
                         '\n'
                         'cheer("Tigers")',
             'options': ['A. Go Tigers!', 'B. Go team!', 'C. Tigers', 'D. An error occurs.'],
             'answer': 'A. Go Tigers!'},
            {'page': 1, 'type': 'heading', 'text': 'Section 4 – Returning Values'},
            {'page': 1,
             'type': 'paragraph',
             'text': "So far, the functions we've written have performed an action, such as "
                     'printing a message to the screen.'},
            {'page': 1,
             'type': 'code',
             'text': 'def greet(name):\n    print("Hello,", name + "!")'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Sometimes, however, we don't want a function to print a result. Instead, we "
                     'want it to compute a value and give that value back to the rest of the '
                     'program.'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'This is the purpose of the <span style="background:#fff1df; color:#c74716; '
                     'padding:2px 7px; border-radius:6px; font-weight:600;">return '
                     'statement</span>. The return statement ends a function and sends a value '
                     'back to the place where the function was called. That returned value can '
                     'then be stored in a variable, used in an expression, or printed to the '
                     'screen.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'For example, suppose we want a function that adds two numbers together.'},
            {'page': 1, 'type': 'code', 'text': 'def add(a, b):\n    return a + b'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Notice that the function doesn't print anything. Instead, it returns the "
                     'sum. To use the returned value, we call the function.'},
            {'page': 1, 'type': 'code', 'text': 'result = add(4, 7)\nprint(result)\n\nOutput\n11'},
            {'page': 1, 'type': 'paragraph', 'text': 'Here is what happens step by step:'},
            {'page': 1,
             'type': 'list',
             'items': ['1. The function is called with the arguments 4 and 7.',
                       '2. Inside the function, Python calculates 4 + 7.',
                       '3. The return statement sends the value 11 back to the function call.',
                       '4. The variable result stores the returned value.',
                       '5. print(result) displays 11.']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Notice that the variable result is outside the function. The function '
                     "doesn't know anything about result—it simply returns a value, and the "
                     'calling code decides what to do with it.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'A function can return many different types of values.'},
            {'page': 1, 'type': 'paragraph', 'text': 'It can return a string:'},
            {'page': 1,
             'type': 'code',
             'text': 'def full_name(first, last):\n    return first + " " + last'},
            {'page': 1, 'type': 'paragraph', 'text': 'A Boolean:'},
            {'page': 1, 'type': 'code', 'text': 'def is_even(number):\n    return number % 2 == 0'},
            {'page': 1, 'type': 'paragraph', 'text': 'Or even a list:'},
            {'page': 1, 'type': 'code', 'text': 'def first_three():\n    return [1, 2, 3]'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'As long as a value can be stored in a variable, a function can return it.'},
            {'page': 1, 'type': 'heading', 'text': 'Printing vs. Returning'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Beginning programmers often confuse print() and return. Although both can '
                     'display information, they serve very different purposes.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Consider these two functions.'},
            {'page': 1,
             'type': 'code',
             'text': 'def add_print(a, b):\n'
                     '    print(a + b)\n'
                     '\n'
                     'def add_return(a, b):\n'
                     '    return a + b'},
            {'page': 1, 'type': 'paragraph', 'text': 'Suppose we call them.'},
            {'page': 1, 'type': 'code', 'text': 'add_print(2, 3)\n\nOutput\n5'},
            {'page': 1, 'type': 'paragraph', 'text': 'Now try storing the result.'},
            {'page': 1,
             'type': 'code',
             'text': 'answer = add_print(2, 3)\nprint(answer)\n\nOutput\n5\nNone'},
            {'page': 1, 'type': 'paragraph', 'text': 'Why did None appear?'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'The function printed the value 5, but it never returned anything. Since '
                     'every function returns something, Python automatically returned None, which '
                     'represents the absence of a value. Now compare it with the second function.'},
            {'page': 1,
             'type': 'code',
             'text': 'answer = add_return(2, 3)\nprint(answer)\n\nOutput\n5'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'This time, the function returned the value 5, allowing it to be stored in '
                     'the variable answer.'},
            {'page': 1,
             'type': 'tip',
             'text': 'Use print() when you want to display information to the user. Use return '
                     'when you want your function to produce a value that the rest of your program '
                     'can use.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What is printed?\n'
                         '\n'
                         'def square(number):\n'
                         '    return number * number\n'
                         '\n'
                         'print(square(5))',
             'options': ['A. 5', 'B. 10', 'C. 25', 'D. Nothing'],
             'answer': 'C. 25'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What is stored in result?\n'
                         '\n'
                         'def multiply(a, b):\n'
                         '    return a * b\n'
                         '\n'
                         'result = multiply(4, 6)',
             'options': ['A. 4', 'B. 6', 'C. 10', 'D. 24'],
             'answer': 'D. 24'},
            {'page': 1, 'type': 'heading', 'text': 'Section 5 – Writing Good Functions'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Writing a function that works is an important first step. However, '
                     'professional programmers also strive to write functions that are easy to '
                     'read, understand, and reuse. As programs grow larger, clear and organized '
                     'functions become just as important as correct ones. Other programmers—and '
                     'even your future self—should be able to understand what a function does by '
                     'reading its name and a short description. Here are three habits that will '
                     'help you write better functions.'},
            {'page': 1, 'type': 'heading', 'text': 'Give Functions Descriptive Names'},
            {'page': 1,
             'type': 'paragraph',
             'text': "A function's name should clearly describe the task it performs."},
            {'page': 1, 'type': 'paragraph', 'text': 'For example, compare these two functions.'},
            {'page': 1,
             'type': 'code',
             'text': 'def f(x):\n'
                     '    return x * 9 / 5 + 32\n'
                     '\n'
                     'def celsius_to_fahrenheit(celsius):\n'
                     '    return celsius * 9 / 5 + 32'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Both functions do exactly the same thing, but the second name immediately '
                     'tells us what the function does.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'When choosing a function name, try to use verbs because functions perform '
                     'actions. Good examples include:'},
            {'page': 1,
             'type': 'list',
             'items': ['calculate_total()', 'print_receipt()', 'find_maximum()', 'is_even()']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Names such as f(), thing(), or data() give very little information about the '
                     "function's purpose."},
            {'page': 1, 'type': 'heading', 'text': 'Write a Docstring'},
            {'page': 1,
             'type': 'rich_paragraph',
             'html': 'A <span style="background:#fff1df; color:#c74716; padding:2px 7px; '
                     'border-radius:6px; font-weight:600;">docstring</span> is a short description '
                     'written at the beginning of a function. It explains what the function does.'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Docstrings are written inside triple quotation marks (""").'},
            {'page': 1, 'type': 'paragraph', 'text': 'For example,'},
            {'page': 1,
             'type': 'code',
             'text': 'def square(number):\n'
                     '    """Returns the square of a number."""\n'
                     '    return number * number'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'A good docstring should explain what the function does, not how it does it. '
                     'As your programs become larger, docstrings make it much easier for you—and '
                     'others—to understand each function without reading every line of code.'},
            {'page': 1, 'type': 'heading', 'text': 'Keep Functions Focused'},
            {'page': 1,
             'type': 'paragraph',
             'text': "Each function should perform one specific task. Suppose you're writing a "
                     'program for a restaurant. Instead of creating one giant function that prints '
                     "the menu, calculates the bill, computes tax, and prints the receipt, it's "
                     'usually better to divide the work into several smaller functions.'},
            {'page': 1,
             'type': 'code',
             'text': 'def print_menu():\n'
                     '    ...\n'
                     '\n'
                     'def calculate_total():\n'
                     '    ...\n'
                     '\n'
                     'def print_receipt():\n'
                     '    ...'},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Small, focused functions are easier to test, easier to reuse, and easier to '
                     'modify later. If one part of the program needs to change, you only need to '
                     'update the function responsible for that task.'},
            {'page': 1,
             'type': 'tip',
             'text': 'Before writing a function, ask yourself: "Can I describe what this function '
                     'does in one simple sentence?" If the answer is no, your function may be '
                     'trying to do too many things.'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'Which function name is the most descriptive?',
             'options': ['A. def x():',
                         'B. def calculate_average():',
                         'C. def function1():',
                         'D. def stuff():'],
             'answer': 'B. def calculate_average():'},
            {'page': 1, 'type': 'heading', 'text': 'Check Your Understanding'},
            {'page': 1,
             'type': 'quiz',
             'question': 'What is the purpose of a docstring?',
             'options': ['A. To make the program run faster.',
                         'B. To store variables.',
                         'C. To explain what a function does.',
                         'D. To replace the return statement.'],
             'answer': 'C. To explain what a function does.'},
            {'page': 1, 'type': 'heading', 'text': 'Mini Project – Restaurant Bill Calculator'},
            {'page': 1,
             'type': 'paragraph',
             'text': "In this project, you'll combine everything you've learned about functions by "
                     'writing several small functions that work together to calculate a restaurant '
                     'bill.'},
            {'page': 1, 'type': 'paragraph', 'text': 'Your program should:'},
            {'page': 1,
             'type': 'list',
             'items': ['Calculate the subtotal of the meal.',
                       'Calculate the sales tax.',
                       'Calculate the final total.',
                       'Display the results neatly.']},
            {'page': 1,
             'type': 'paragraph',
             'text': 'Each task should be handled by its own function.'},
            {'page': 1, 'type': 'heading', 'text': 'Starter Code'},
            {'page': 1,
             'type': 'code',
             'text': 'def calculate_subtotal(food_cost, drink_cost):\n'
                     '    """Returns the subtotal before tax."""\n'
                     '    pass\n'
                     '\n'
                     'def calculate_tax(subtotal):\n'
                     '    """Returns the sales tax (8%)."""\n'
                     '    pass\n'
                     '\n'
                     'def calculate_total(subtotal, tax):\n'
                     '    """Returns the final bill."""\n'
                     '    pass\n'
                     '\n'
                     'food = float(input("Food cost: $"))\n'
                     'drink = float(input("Drink cost: $"))\n'
                     '\n'
                     'subtotal = calculate_subtotal(food, drink)\n'
                     'tax = calculate_tax(subtotal)\n'
                     'total = calculate_total(subtotal, tax)\n'
                     '\n'
                     'print("Subtotal: $", round(subtotal, 2))\n'
                     'print("Tax: $", round(tax, 2))\n'
                     'print("Total: $", round(total, 2))'},
            {'page': 1, 'type': 'heading', 'text': 'Example Run'},
            {'page': 1,
             'type': 'code',
             'text': 'Food cost: $15.50\n'
                     'Drink cost: $3.50\n'
                     'Subtotal: $19.00\n'
                     'Tax: $1.52\n'
                     'Total: $20.52'},
            {'page': 1, 'type': 'heading', 'text': 'Key Takeaways'},
            {'page': 1,
             'type': 'list',
             'items': ['Functions let you write code once and reuse it many times.',
                       'A function is defined using the def keyword.',
                       'A function runs only when it is called.',
                       'Parameters receive information, while arguments provide the actual values.',
                       'The return statement sends a value back to the function call.',
                       'print() displays information, while return produces a value for the rest '
                       'of the program to use.',
                       'Good functions have descriptive names, clear docstrings, and perform one '
                       'specific task.']},
            {'page': 1, 'type': 'heading', 'text': 'Looking Ahead'},
            {'page': 1,
             'type': 'paragraph',
             'text': "In the next lesson, you'll learn how Python keeps track of variables inside "
                     "and outside of functions. You'll explore scope, discover why some variables "
                     'can only be used in certain places, and learn how to organize larger '
                     'programs by importing functions from modules.'}]},
    "recursion_capstone": {

        "id": "recursion_capstone",

        "lesson_number": "6",

        "title": "Recursion & the Capstone",

        "description": "Lesson 6.0 - Recursion & the Capstone. Trace recursive functions and bring the course together in a community capstone project.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Lesson 6 - Recursion & the Capstone"
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

            {'page': 1,
             'type': 'quiz',
             'question': 'In the trace above, which call is the base case?',
             'options': ['A. factorial(0)', 'B. factorial(4)', 'C. factorial(2)', 'D. factorial(1)'],
             'answer': 'A. factorial(0)'},

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

            {'page': 2,
             'type': 'quiz',
             'question': 'Fred Begay combined Navajo tradition with physics. Which comparison best matches '
                         'recursion and iteration to two things he grew up with?',
             'options': ['A. Recursion is like a lab experiment; iteration is like oral storytelling.',
                         'B. Recursion is like oral storytelling, where each call adds a layer; iteration is '
                         'like a lab experiment, repeated step-by-step.',
                         'C. Both recursion and iteration work like oral storytelling.',
                         'D. Neither recursion nor iteration resembles either tradition.'],
             'answer': 'B. Recursion is like oral storytelling, where each call adds a layer; iteration is '
                       'like a lab experiment, repeated step-by-step.'},

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

            {'page': 2,
             'type': 'quiz',
             'question': 'What does echo("hi", 3) print?',
             'options': ['A. hi (once)',
                         'B. hi hi hi hi (four times)',
                         'C. hi hi hi (three times, one per line)',
                         'D. Nothing - it raises a RecursionError'],
             'answer': 'C. hi hi hi (three times, one per line)'},

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
            },
            {
                "page": 3,
                "type": "exericse",
                "problem": "countdown"
            }

        ]
    }
}


def get_lesson(id):
    return LESSONS.get(id)
