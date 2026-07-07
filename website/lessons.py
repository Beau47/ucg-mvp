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
                "type": "heading",
                "text": "What is a Variable?"
            },

            {
                "type": "paragraph",
                "text":
                "Variables allow you to store information that can be used later."
            },

            {
                "type": "code",
                "language": "python",
                "text":
"""x = 5
print(x)"""
            },

            {
                "type": "paragraph",
                "text":
                "Notice that x now stores the value 5."
            },

            {
                "type": "image",
                "src": "/static/images/variable_box.png",
                "caption": "A variable stores a value."
            },

            {
                "type": "tip",
                "text":
                "Choose descriptive variable names."
            },

            {
                "type": "warning",
                "text":
                "Variable names cannot start with numbers."
            },

            {
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
                "type": "heading",
                "text": "What are Data Types?"
            },

            {
                "type": "paragraph",
                "text":
                "Data types describe the kind of information a variable stores. Python automatically determines the type of a value when it is assigned."
            },

            {
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
                "type": "paragraph",
                "text":
                "The variable name stores text (a string), age stores a whole number (an integer), and height stores a decimal number (a float)."
            },

            {
                "type": "image",
                "src": "/static/images/data_types.png",
                "caption": "Python has different types of data for storing information."
            },

            {
                "type": "tip",
                "text":
                "Use the type() function to check what type of value a variable contains."
            },

            {
                "type": "code",
                "language": "python",
                "text":
"""x = 10

print(type(x))"""
            },

            {
                "type": "warning",
                "text":
                "Remember that strings must be surrounded by quotes."
            },

            {
                "type": "exercise",
                "problem": "create_variables"
            }

        ]
    }
}

def get_lesson(id):
    return LESSONS.get(id)
