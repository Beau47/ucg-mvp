

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
    }
}

def get_lesson(id):
    return LESSONS.get(id)
