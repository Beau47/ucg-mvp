# =========================
# Lesson definitions
# =========================

LESSONS = {
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
