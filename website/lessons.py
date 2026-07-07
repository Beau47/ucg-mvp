# =========================
# Lesson definitions
# =========================

LESSONS = {
    "why_python": {

        "id": "why_python",

        "lesson_number": "Lesson 0",

        "title": "Why Python?",

        "description": "Learn what Python is, why it matters, and how programming can help solve real community problems.",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Why Learn Python?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Python is one of the world's most popular programming languages. It is used in medicine, education, science, business, artificial intelligence, and community work."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Programming is not just about computers. It is about learning how to think logically and solve problems step by step."
            },

            {
                "page": 1,
                "type": "list",
                "items": [
                    "NASA uses Python for scientific computing.",
                    "Hospitals use Python to analyze patient data.",
                    "Researchers use Python to study climate change.",
                    "Businesses use Python to automate repetitive work.",
                    "Schools use Python to teach computer science.",
                    "Artificial intelligence companies use Python to build new tools."
                ]
            },

            {
                "page": 2,
                "type": "heading",
                "text": "Python Can Help Communities"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Communities use software to organize volunteers, manage donations, preserve culture, analyze community needs, and create educational resources."
            },

            {
                "page": 2,
                "type": "tip",
                "text":
                "As you learn Python, think about problems in your own community that technology could help solve."
            },

            {
                "page": 2,
                "type": "quote",
                "text":
                "Programming can help people turn careful instructions into useful tools."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Computers Follow Instructions"
            },

            {
                "page": 3,
                "type": "paragraph",
                "text":
                "Computers are very literal. They only perform the exact instructions they receive."
            },

            {
                "page": 3,
                "type": "warning",
                "text":
                "Garbage In, Garbage Out means a computer's output depends on the instructions it receives. Incorrect instructions can produce incorrect results."
            },

            {
                "page": 4,
                "type": "heading",
                "text": "Your First Python Program"
            },

            {
                "page": 4,
                "type": "paragraph",
                "text":
                "Every programmer starts with a simple program. In Python, print() displays information on the screen."
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""print("Hello, Tulsa!")"""
            },

            {
                "page": 4,
                "type": "code",
                "language": "python",
                "text":
"""print("Hello, Little Haiti!")
print("Hello, Dine Nation!")"""
            },

            {
                "page": 4,
                "type": "tip",
                "text":
                "You can personalize the message by replacing the place name with your own community."
            },

            {
                "page": 5,
                "type": "heading",
                "text": "Key Takeaways"
            },

            {
                "page": 5,
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

        "lesson_number": "Lesson 1",

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
                "type": "code",
                "language": "python",
                "text":
"""x = 5
print(x)"""
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

        "lesson_number": "Lesson 2",

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
                "type": "code",
                "language": "python",
                "text":
"""name = "Alex"
age = 15
height = 5.8

print(name)
print(age)
print(height)"""
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
                "type": "code",
                "language": "python",
                "text":
"""x = 10

print(type(x))"""
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
    }
}

def get_lesson(id):
    return LESSONS.get(id)
