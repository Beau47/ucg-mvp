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
                "type": "paragraph",
                "text": "Estimated Time: 10-15 minutes"
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

            {
                "page": 1,
                "type": "quiz",
                "question": "Which keyword tells Python that you are defining a function?",
                "options": [
                    "A. print",
                    "B. return",
                    "C. def",
                    "D. input"
                ],
                "answer": "C. def"
            },

            {
                "page": 1,
                "type": "quiz",
                "question": "What does the return keyword do?",
                "options": [
                    "A. Prints a message to the screen.",
                    "B. Nothing.",
                    "C. Sends a value back from the function.",
                    "D. Creates a variable."
                ],
                "answer": "C. Sends a value back from the function."
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

        "description": "Learn how Python stores information using variables, data types, print(), comments, and clear names.",

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
                "type": "paragraph",
                "text": "Estimated Time: 45-60 minutes"
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

            {
                "page": 1,
                "type": "quiz",
                "question": "What is a variable?",
                "options": [
                    "A. A programming language",
                    "B. A named location that stores information",
                    "C. A computer",
                    "D. A keyboard"
                ],
                "answer": "B. A named location that stores information"
            },

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

            {
                "page": 1,
                "type": "quiz",
                "question": "Which variable stores a float?",
                "options": [
                    "A. age = 17",
                    "B. price = 12.99",
                    "C. name = \"Jordan\"",
                    "D. student = False"
                ],
                "answer": "B. price = 12.99"
            },

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

            {
                "page": 1,
                "type": "quiz",
                "question": "What does print(age) do?",
                "options": [
                    "A. Deletes age",
                    "B. Displays the value stored inside age",
                    "C. Creates a new variable",
                    "D. Changes age"
                ],
                "answer": "B. Displays the value stored inside age"
            },

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

            {
                "page": 1,
                "type": "quiz",
                "question": "Which line is a comment?",
                "options": [
                    "A. name = \"Alex\"",
                    "B. # Store customer's name",
                    "C. print(name)",
                    "D. True"
                ],
                "answer": "B. # Store customer's name"
            },

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

            {
                "page": 1,
                "type": "quiz",
                "question": "Which is a valid variable name?",
                "options": [
                    "A. 2dogs",
                    "B. favorite food",
                    "C. favorite_food",
                    "D. class"
                ],
                "answer": "C. favorite_food"
            },

            {
                "page": 1,
                "type": "heading",
                "text": "Spotlight - Mary G. Ross"
            },

            {
                "page": 1,
                "type": "image_text",
                "src": "/static/images/mary_g_ross.png",
                "alt": "Mary G. Ross",
                "caption": "Mary G. Ross",
                "paragraphs": [
                    "Mary G. Ross was the first known Indigenous American female engineer, and she was from Oklahoma.",
                    "Working at Lockheed, she contributed to aerospace research and helped advance projects that influenced the Apollo space program.",
                    "Like engineers today, she solved complex problems by organizing information carefully - a skill that programming also requires."
                ]
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
                "type": "paragraph",
                "text": "Estimated Time: 60 minutes"
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

            {
                "page": 2,
                "type": "quiz",
                "question": "What does input() do?",
                "options": [
                    "A. Prints text",
                    "B. Deletes variables",
                    "C. Receives information from the user",
                    "D. Creates a comment"
                ],
                "answer": "C. Receives information from the user"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "What is 5 * 4?",
                "options": [
                    "A. 9",
                    "B. 20",
                    "C. 54",
                    "D. 1"
                ],
                "answer": "B. 20"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "What is string concatenation?",
                "options": [
                    "A. Deleting a string",
                    "B. Joining two or more strings together",
                    "C. Converting text into numbers",
                    "D. Printing a variable"
                ],
                "answer": "B. Joining two or more strings together"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "Which uses an f-string?",
                "options": [
                    "A. print(name)",
                    "B. print(f\"Hello {name}\")",
                    "C. print(name + age)",
                    "D. print(True)"
                ],
                "answer": "B. print(f\"Hello {name}\")"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "Given word = \"Tulsa\", what does print(word[2]) display?",
                "options": [
                    "A. T",
                    "B. u",
                    "C. l",
                    "D. s"
                ],
                "answer": "C. l"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "What is the output of word = \"Computer\" and print(word[3:6])?",
                "options": [
                    "A. put",
                    "B. pute",
                    "C. ute",
                    "D. p"
                ],
                "answer": "A. put"
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "What does the expression word[-1] return?",
                "options": [
                    "A. The first character of the string",
                    "B. The second character of the string",
                    "C. The last character of the string",
                    "D. The length of the string"
                ],
                "answer": "C. The last character of the string"
            },

            {
                "page": 2,
                "type": "quiz",
                "question": "What is the output of word = \"Urban\" and print(word[::-1])?",
                "options": [
                    "A. Urban",
                    "B. nabrU",
                    "C. U",
                    "D. abrnU"
                ],
                "answer": "B. nabrU"
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Mini Project - Tulsa Food Truck"
            },

            {
                "page": 2,
                "type": "image_text",
                "src": "/static/images/tulsa_food_truck.png",
                "alt": "Tulsa food truck menu",
                "caption": "Food truck ordering project",
                "paragraphs": [
                    "Imagine you're building software for a local food truck.",
                    "Your program should ask for the customer's name, ask which menu item they want, ask how many they want, calculate the total price, and display a receipt using f-strings."
                ]
            },

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

            {
                "page": 2,
                "type": "quiz",
                "question": "Why are f-strings useful?",
                "options": [
                    "A. They make code easier to read.",
                    "B. They automatically fix bugs.",
                    "C. They replace variables.",
                    "D. They make programs faster."
                ],
                "answer": "A. They make code easier to read."
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
     'description': 'Teach programs to make decisions using Boolean values, comparison operators, '
                    'conditional statements, and logical operators.',
     'title': 'Teaching Programs to Make Decisions',
     'blocks': [{'page': 1,
                 'type': 'heading',
                 'text': 'Lesson 2 – Teaching Programs to Make Decisions'},
                {'page': 1, 'type': 'paragraph', 'text': 'Estimated Time: 60–75 minutes'},
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
                 'options': ['A. "False"', 'B. 0', 'C. False', 'D. "No"'],
                 'answer': 'C. False'},
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
                 'question': 'What will this program print?\n'
                             'age = 15\n'
                             'if age >= 16:\n'
                             'print("Can drive")',
                 'options': ['A. Can drive', 'B. Nothing', 'C. 15', 'D. An error'],
                 'answer': 'B. Nothing'},
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
                 'options': ['A. Adult', 'B. Teen', 'C. Child', 'D. Nothing'],
                 'answer': 'C. Child'},
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
                 'question': 'if age >= 18 and has_ticket:\n'
                             'print("Enter")\n'
                             'else:\n'
                             'print("Cannot enter")',
                 'options': ['A. Enter', 'B. Cannot enter', 'C. Nothing', 'D. Error'],
                 'answer': 'B. Cannot enter'},
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
                 'items': ['✅ Compare values using comparison operators.',
                           '✅ Understand how Boolean values (True and False) control program flow.',
                           '✅ Write programs using if, elif, and else.',
                           '✅ Combine conditions using and, or, and not.',
                           '✅ Recognize common mistakes involving comparisons, indentation, and '
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
        },
        {
            "page": 11,
            "type": "exercise",
            "problem": "first_item"
        }

    ]
},
"mutation_aliasing": {

    "id": "mutation_aliasing",

    "lesson_number": "3.1",

    "title": "Mutation & Aliasing",

    "description": "Understand how Python stores data, why some values can change, and how aliasing can create unexpected behavior.",

    "blocks": [


        # =====================================================
        # PAGE 1: INTRODUCTION
        # =====================================================

        {
            "page": 1,
            "type": "heading",
            "text": "Lesson 3.1: Mutation & Aliasing — How Python Stores Data"
        },


        {
            "page": 1,
            "type": "paragraph",
            "text": """
            Before working with lists and dictionaries, it is important to
            understand how Python stores information.

            Some data types can be changed after they are created.
            Other data types cannot.

            This difference explains why changing a list can affect multiple
            variables at once, while changing a number does not.
            """
        },


        {
            "page": 1,
            "type": "tip",
            "text": """
            By the end of this lesson, you will understand:

            • The difference between mutable and immutable data
            • Why lists and dictionaries can change
            • How variables can reference the same object
            • How to avoid unexpected changes using copies
            """
        },


        # =====================================================
        # PAGE 2: VARIABLES AND OBJECTS
        # =====================================================


        {
            "page": 2,
            "type": "heading",
            "text": "Variables Store References to Data"
        },


        {
            "page": 2,
            "type": "paragraph",
            "text": """
            Many beginners think variables contain the actual value.

            In Python, variables are names that point to objects stored in
            memory.

            Think of a variable like a label attached to a box.
            The label tells Python which object you mean.
            """
        },


        {
            "page": 2,
            "type": "code",
            "text": """
age = 15

print(age)
"""
        },


        {
            "page": 2,
            "type": "paragraph",
            "text": """
            Here, the variable age points to the integer object 15.

            When we change age, Python creates a new object instead of
            changing the old one.
            """
        },


        {
            "page": 2,
            "type": "code",
            "text": """
age = 15

age = 16

print(age)

# Output:
16
"""
        },


        # =====================================================
        # PAGE 3: IMMUTABLE DATA
        # =====================================================


        {
            "page": 3,
            "type": "heading",
            "text": "Immutable Data: Values That Cannot Change"
        },


        {
            "page": 3,
            "type": "paragraph",
            "text": """
            Immutable means an object cannot be changed after it is created.

            Common immutable data types include:

            • int
            • float
            • bool
            • string
            • tuple

            When you modify these values, Python creates a new object.
            """
        },


        {
            "page": 3,
            "type": "code",
            "text": """
name = "Alex"

name = name + "!"

print(name)

# Output:
Alex!
"""
        },


        {
            "page": 3,
            "type": "paragraph",
            "text": """
            The original string was not changed.

            Python created a new string object and updated the variable to
            point to it.
            """
        },


        {
            "page": 3,
            "type": "quiz",
            "question": "Which of these is an immutable data type?",
            "options": [
                "list",
                "dictionary",
                "string",
                "set"
            ],
            "answer": "string"
        },


        # =====================================================
        # PAGE 4: MUTABLE DATA
        # =====================================================


        {
            "page": 4,
            "type": "heading",
            "text": "Mutable Data: Values That Can Change"
        },


        {
            "page": 4,
            "type": "paragraph",
            "text": """
            Mutable objects can be changed after they are created.

            Common mutable data types include:

            • list
            • dictionary
            • set

            Instead of creating a new object, Python modifies the existing
            object.
            """
        },


        {
            "page": 4,
            "type": "code",
            "text": """
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)

# Output:
[1, 2, 3, 4]
"""
        },


        {
            "page": 4,
            "type": "ide",
            "instructions": "Modify the list by adding 'Python' using mutation.",
            "starter_code": """
languages = ["Java", "C++"]

# Add Python to the list

print(languages)
"""
        },


        # =====================================================
        # PAGE 5: ALIASING
        # =====================================================


        {
            "page": 5,
            "type": "heading",
            "text": "Aliasing: Two Variables, One Object"
        },


        {
            "page": 5,
            "type": "paragraph",
            "text": """
            Aliasing happens when two variables point to the same object.

            Changing the object through one variable changes what the other
            variable sees.
            """
        },


        {
            "page": 5,
            "type": "code",
            "text": """
scores = [90, 80]

other_scores = scores

other_scores.append(100)

print(scores)

# Output:
[90, 80, 100]
"""
        },


        {
            "page": 5,
            "type": "warning",
            "text": """
            This can create unexpected bugs.

            Remember:
            If two variables reference the same list or dictionary,
            changing one changes the other.
            """
        },


        # =====================================================
        # PAGE 6: COPYING OBJECTS
        # =====================================================


        {
            "page": 6,
            "type": "heading",
            "text": "Avoiding Aliasing with Copies"
        },


        {
            "page": 6,
            "type": "paragraph",
            "text": """
            If you want a separate object, create a copy.

            Lists and dictionaries have a .copy() method that creates a new
            object with the same contents.
            """
        },


        {
            "page": 6,
            "type": "code",
            "text": """
original = [1, 2, 3]

copy = original.copy()

copy.append(4)

print(original)
print(copy)

# Output:
[1, 2, 3]
[1, 2, 3, 4]
"""
        },


        {
            "page": 6,
            "type": "ide",
            "instructions": "Fix the code so changing student_copy does not change the original student list.",
            "starter_code": """
students = ["Ana", "Luis"]

student_copy = students

student_copy.append("Maya")

print(students)
"""
        },


        # =====================================================
        # PAGE 7: SUMMARY + EXERCISE
        # =====================================================


        {
            "page": 7,
            "type": "heading",
            "text": "Mutation & Aliasing Summary"
        },


        {
            "page": 7,
            "type": "list",
            "items": [
                "Immutable objects cannot be changed after creation.",
                "Mutable objects can be changed.",
                "Lists and dictionaries are mutable.",
                "Aliasing happens when two variables reference the same object.",
                "Use .copy() to create a separate object."
            ]
        },


        {
            "page": 7,
            "type": "exercise",
            "problem": "update_inventory"
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
        },
        {
            "page": 11,
            "type": "exercise",
            "problem": "count_up"
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
                "answer": "B. It ends the function and gives a value back to the caller"
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
                "problem": "square_number"
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
