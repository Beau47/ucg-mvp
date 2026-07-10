# =========================
# Lesson definitions
# =========================

LESSONS = {
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


    "conditionals": {

        "id": "conditionals",

        "lesson_number": "3",

        "title": "Conditionals",

        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "What are Conditionals?"
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "Conditionals allow your program to make decisions. They let your code run different instructions depending on whether a condition is true or false."
            },

            {
                "page": 1,
                "type": "ide",
                "language": "python",
                "starter_code":
"""age = 18

if age >= 18:
    print("You can vote.")""",
                "instructions":
                "Change the value of age and test when the message appears."
            },

            {
                "page": 1,
                "type": "paragraph",
                "text":
                "In this example, Python checks whether age is greater than or equal to 18. Since the condition is true, the code inside the if statement runs."
            },

            {
                "page": 2,
                "type": "heading",
                "text": "The if-else Statement"
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "The else statement allows your program to execute a different block of code when the condition is false."
            },

            {
                "page": 2,
                "type": "ide",
                "language": "python",
                "starter_code":
"""temperature = 30

if temperature > 25:
    print("It is warm outside.")
else:
    print("It is cold outside.")""",
                "instructions":
                "Change the temperature value and see which message Python prints."
            },

            {
                "page": 2,
                "type": "paragraph",
                "text":
                "Python will only execute one of the two blocks. If the condition after if is true, the first block runs. Otherwise, the else block runs."
            },

            {
                "page": 3,
                "type": "heading",
                "text": "Using elif for Multiple Conditions"
            },

            {
                "page": 3,
                "type": "paragraph",
                "text":
                "Sometimes programs need to check more than two possibilities. The elif statement allows you to add additional conditions."
            },

            {
                "page": 3,
                "type": "code",
                "language": "python",
                "text":
"""score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep practicing!")"""
            },

            {
                "page": 3,
                "type": "tip",
                "text":
                "Remember that Python uses indentation to determine which lines belong inside an if, elif, or else block."
            },

            {
                "page": 3,
                "type": "warning",
                "text":
                "A missing colon after an if, elif, or else statement will cause a syntax error."
            }

        ]
    },
    "if_statements": {

    "id": "if_statements",

    "lesson_number": "5",

    "title": "If Statements",

    "blocks": [

        {
            "type": "heading",
            "page": 1,
            "text": "Making Decisions with if Statements"
        },

        {
            "type": "paragraph",
            "page": 1,
            "text": "Programs often need to make decisions. An if statement lets your code execute only when a condition is True."
        },

        {
            "type": "code",
            "page": 1,
            "text": "temperature = 75\n\nif temperature > 70:\n    print('It is warm outside!')"
        },

        {
            "type": "tip",
            "page": 1,
            "text": "The code inside an if statement must be indented. Python uses indentation to determine which code belongs inside the if block."
        },



        {
            "type": "heading",
            "page": 2,
            "text": "Comparison Operators"
        },

        {
            "type": "paragraph",
            "page": 2,
            "text": "Conditions are created using comparison operators."
        },

        {
            "type": "list",
            "page": 2,
            "items": [
                "==   Equal to",
                "!=   Not equal to",
                ">    Greater than",
                "<    Less than",
                ">=   Greater than or equal to",
                "<=   Less than or equal to"
            ]
        },

        {
            "type": "code",
            "page": 2,
            "text": "score = 92\n\nif score >= 90:\n    print('Excellent!')"
        },



        {
            "type": "heading",
            "page": 3,
            "text": "Quiz"
        },

        {
            "type": "quiz",
            "page": 3,
            "question": "Which condition checks whether x is equal to 10?",
            "options": [
                "x = 10",
                "x == 10",
                "x := 10",
                "x != 10"
            ],
            "answer": "x == 10"
        },



        {
            "type": "exercise",
            "page": 4,
            "problem": "if_statements_intro"
        }

    ]
}
}


def get_lesson(id):
    return LESSONS.get(id)
