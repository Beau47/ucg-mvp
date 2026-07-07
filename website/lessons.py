

LESSONS = {
    "variables": {
        "id": "variables",
        "title": "Variables",
        "lesson_number": "Lesson 1",

        "sections": [
            {
                "heading": "What is a Variable?",
                "content":
                "Variables are containers that store values."
            },
            {
                "heading": "Creating Variables",
                "content":
                "You create a variable using the = operator."
            },
            {
                "heading": "Example",
                "code":
"""x = 5
print(x)"""
            }
        ],

        "exercise": "add_one"
    }
}

def get_lesson(id):
    return LESSONS.get(id)
