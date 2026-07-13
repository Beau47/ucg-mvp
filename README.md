# Urban Coders Guild Learning Platform

Urban Coders Guild Learning Platform is a browser-based Python learning platform built with **Flask**, **HTML/CSS**, **JavaScript**, and the **Monaco Editor**. The platform allows students to learn Python through interactive lessons, embedded code editors, quizzes, and automatically graded coding exercises.

Students progress through lessons that contain explanations, examples, interactive IDE snippets, quizzes, and coding challenges.

---

# Table of Contents

1. [Technology Stack](#technology-stack)
2. [Project Structure](#project-structure)
3. [Running the Application](#running-the-application)
4. [Creating a New Lesson](#creating-a-new-lesson)
5. [Lesson Block Types](#lesson-block-types)
6. [Creating a New Exercise](#creating-a-new-exercise)
7. [Exercise Structure](#exercise-structure)
8. [Adding a Lesson Exercise Connection](#adding-a-lesson-exercise-connection)
9. [Interactive IDE Requirements](#interactive-ide-requirements)
10. [Future Features](#future-features)

---

# Technology Stack

## Backend

### Flask

Urban Coders Guild Learning Platform uses Flask as the backend framework.

Flask handles:

* Page routing
* Loading lessons
* Loading exercises
* Running Python code
* Returning JSON responses

Documentation:

https://flask.palletsprojects.com/

---

## Frontend

The frontend uses:

* HTML templates with Jinja2
* CSS styling
* JavaScript for interactivity

Templates are stored in:

```
templates/
```

CSS:

```
static/css/
```

JavaScript:

```
static/js/
```

---

## Code Editor

The exercise workspace uses:

### Monaco Editor

Monaco is the editor that powers VS Code.

Documentation:

https://microsoft.github.io/monaco-editor/

---

# Project Structure

Current project organization:

```
Urban-Coders-Guild/

│
├── app.py
├── lessons.py
├── problems.py
├── runner.py
│
├── templates/
│   ├── dashboard.html
│   ├── lessons.html
│   ├── lesson.html
│   ├── exercises.html
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   ├── js/
│   │   └── app.js
│   │
│   └── images/
│
└── README.md
```

---

# Running the Application

Install Flask:

```bash
pip install flask
```

Start the development server:

```bash
python app.py
```

The website will run at:

```
http://127.0.0.1:5000
```

---

# Creating a New Lesson

Lessons are stored inside:

```
lessons.py
```

Lessons are stored inside the `LESSONS` dictionary.

Example:

```python
LESSONS = {

    "variables": {

        "id": "variables",

        "lesson_number": "1",

        "title": "Variables",

        "description":
        "Learn how Python stores information.",


        "blocks": [

            {
                "page": 1,
                "type": "heading",
                "text": "Introduction to Variables"
            }

        ]

    }

}
```

---

## Lesson Requirements

Every lesson needs:

```python
"id"
```

The URL identifier.

Example:

```python
"id": "variables"
```

---

```python
"lesson_number"
```

The displayed lesson number.

Example:

```python
"lesson_number": "2"
```

---

```python
"title"
```

The lesson title.

Example:

```python
"title": "Conditionals"
```

---

```python
"description"
```

Short description displayed on lesson cards.

Example:

```python
"description":
"Learn how programs make decisions."
```

---

```python
"blocks"
```

A list of lesson content.

Each block represents one piece of content.

---

# Lesson Pages

Each block requires:

```python
"page": number
```

Example:

```python
{
    "page": 2,
    "type": "paragraph",
    "text": "Variables store information."
}
```

Blocks with the same page number appear together.

---

# Lesson Block Types

The lesson system supports the following block types:

---

# Heading

Creates a section heading.

Example:

```python
{
    "page": 1,
    "type": "heading",
    "text": "What are Variables?"
}
```

---

# Paragraph

Creates normal text.

Example:

```python
{
    "page": 1,
    "type": "paragraph",
    "text":
    "Variables allow programs to store information."
}
```

---

# Rich Paragraph

Allows HTML formatting.

Example:

```python
{
    "page": 1,
    "type": "rich_paragraph",
    "html":
    """
    Python uses
    <span style="color:red">
    variables
    </span>
    """
}
```

Use carefully because HTML is rendered directly.

---

# Code

Displays formatted Python code.

Example:

```python
{
    "page": 1,
    "type": "code",
    "text":
"""
x = 5
print(x)
"""
}
```

---

# List

Creates a bullet list.

Example:

```python
{
    "page": 1,
    "type": "list",
    "items": [

        "Variables store data",

        "Python is dynamically typed"

    ]
}
```

---

# Image

Displays an image.

Example:

```python
{
    "page": 1,
    "type": "image",
    "src":
    "/static/images/example.png",

    "caption":
    "Example image"
}
```

---

# Image Text

Creates a side-by-side image and explanation.

Example:

```python
{
    "page": 1,
    "type": "image_text",

    "src":
    "/static/images/example.png",

    "alt":
    "Example",

    "paragraphs":[

        "Explanation paragraph."

    ]
}
```

---

# Tip

Creates a green tip box.

Example:

```python
{
    "page":1,
    "type":"tip",
    "text":
    "Remember that indexing starts at 0."
}
```

---

# Warning

Creates a warning box.

Example:

```python
{
    "page":1,
    "type":"warning",
    "text":
    "Do not confuse = with ==."
}
```

---

# Quote

Creates a quote section.

Example:

```python
{
    "page":1,
    "type":"quote",
    "text":
    "Programming is problem solving."
}
```

---

# Divider

Creates a horizontal divider.

Example:

```python
{
    "page":1,
    "type":"divider"
}
```

---

# Quiz

Creates an interactive multiple choice question.

Example:

```python
{
    "page":2,

    "type":"quiz",

    "question":
    "What does len() return?",

    "options":[

        "The size of a list",

        "A random number",

        "A string"

    ],

    "answer":
    "The size of a list"
}
```

Students must answer correctly before continuing.

---

# IDE

Creates an interactive code editor.

Example:

```python
{
    "page":3,

    "type":"ide",

    "instructions":
    "Create a variable called x.",

    "starter_code":
"""
x = 5
print(x)
"""
}
```

Students must click **Run** before continuing.

---

# Exercise

Links a lesson to a graded coding problem.

Example:

```python
{
    "page":4,

    "type":"exercise",

    "problem":
    "add_one"
}
```

The problem ID must exist in:

```
problems.py
```

---

# Creating a New Exercise

Exercises are stored in:

```
problems.py
```

Inside:

```python
PROBLEMS = {

}
```

Example:

```python
"multiply_two": {

    "id":
    "multiply_two",

    "lesson_number":
    "LESSON 3",

    "title":
    "Multiply Two",

    "description":
    "Return a number multiplied by two.",


    "function_name":
    "multiply_two",


    "starter_code":
'''
def multiply_two(x):

    """
    Return x multiplied by 2.
    """

    # WRITE CODE HERE

    pass
''',


    "challenges":[

        "Function Exists",

        "Returns Correct Value",

        "No Extra Output"

    ],


    "test_cases":[

        {
            "input":5,
            "expected":10
        },

        {
            "input":3,
            "expected":6
        }

    ]

}
```

---

# Exercise Fields

## id

Unique identifier.

Used when linking from lessons.

Example:

```python
"id":"multiply_two"
```

---

## title

Displayed title.

Example:

```python
"title":"Multiply Two"
```

---

## description

Displayed on exercise cards.

Example:

```python
"description":
"Return twice the value."
```

---

## function_name

Function students must create.

Example:

```python
"function_name":
"multiply_two"
```

---

## starter_code

The code shown in Monaco Editor.

Example:

```python
def multiply_two(x):

    # WRITE CODE HERE

    pass
```

---

## challenges

Checklist displayed to students.

Example:

```python
[
"Function Exists",
"Returns Correct Value"
]
```

---

## test_cases

Inputs and expected outputs.

Example:

```python
[
{
"input":5,
"expected":10
}
]
```

The runner uses these to grade submissions.

---

# Connecting a Lesson to an Exercise

Inside `lessons.py`:

```python
{
    "page":5,

    "type":"exercise",

    "problem":
    "multiply_two"
}
```

The value must match:

```python
PROBLEMS["multiply_two"]
```

---

# How Code Execution Works

There are two execution systems.

---

## Lesson IDEs

Used for practice.

Route:

```
/run_snippet
```

Features:

* Runs code
* Displays output
* Does not grade

---

## Exercises

Used for assessment.

Route:

```
/run
```

Features:

* Runs student code
* Executes test cases
* Calculates score

---

# Adding a New Lesson Workflow

1. Add lesson to:

```
lessons.py
```

2. Create lesson blocks.

3. Add exercises:

```
problems.py
```

4. Link exercises:

```python
"type":"exercise"
```

5. Add lesson card automatically appears through:

```
lessons.html
```

---

# Adding a New Exercise Workflow

1. Add dictionary entry:

```
problems.py
```

2. Define:

* id
* function name
* starter code
* tests

3. Create lesson connection:

```python
{
"type":"exercise",
"problem":"problem_id"
}
```

---

# Future Features

Potential improvements:

* User authentication
* Progress tracking
* Saved submissions
* Student profiles
* XP system
* Leaderboards
* Course completion tracking
* Database storage using PostgreSQL/Supabase

---

# Credits

Urban Coders Guild Learning Platform was built using:

* Flask
* Python
* Monaco Editor
* HTML/CSS
* JavaScript

Created as an interactive Python education platform.
