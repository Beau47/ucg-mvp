# Urban Coders Guild Learning Platform

Urban Coders Guild Learning Platform is a browser-based Python learning
environment built for beginner programmers. It combines guided curriculum,
interactive examples, quizzes, and automatically graded coding exercises in a
single Flask application.

The current repository contains an MVP with account management, persistent
course progress, student profiles, a dashboard, seven numbered curriculum
units, a prerequisite lesson, and 26 coding exercises.

## Table of Contents

1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Local Setup](#local-setup)
5. [Supabase Configuration](#supabase-configuration)
6. [Application Architecture](#application-architecture)
7. [Routes](#routes)
8. [Curriculum Content](#curriculum-content)
9. [Creating a Lesson](#creating-a-lesson)
10. [Lesson Block Types](#lesson-block-types)
11. [Creating an Exercise](#creating-an-exercise)
12. [Code Execution](#code-execution)
13. [Progress and XP](#progress-and-xp)
14. [Development Checks](#development-checks)
15. [Current Limitations](#current-limitations)
16. [Next Features](#next-features)

## Features

- Email and password authentication through Supabase Auth
- Sign-up, login, logout, email verification, and password reset flows
- Student dashboard with course progress, next lesson, and next exercise
- Editable student profiles with avatar uploads
- Multi-page Python curriculum organized into Units 0-6 and Lesson 0.5
- Rich lesson blocks for explanations, examples, vocabulary, tables, tips,
  warnings, quizzes, and embedded coding activities
- Monaco Editor instances for in-browser Python practice
- Multiple-choice questions within lessons to track learning progress
- Automatically graded coding exercises with visible test-case feedback
- Persistent lesson, task, and exercise completion records
- Browser-side restoration of completed quizzes and lesson IDE activities
- XP, levels, and progress summaries derived from completed work
- Lesson-based exercise prerequisites enforced by Flask
- Responsive lesson, dashboard, profile, and exercise interfaces

## Technology Stack

### Backend

- Python
- Flask and Jinja2
- Supabase Auth, PostgreSQL API, and Storage
- python-dotenv for local environment variables

### Frontend

- HTML and CSS
- JavaScript
- Monaco Editor for editable Python code
- Prism for syntax-highlighted code examples
- Google Fonts

Monaco, Prism, and Google Fonts are loaded from external CDNs, so an internet
connection is required for the complete local interface.

## Project Structure

```text
ucg-mvp/
|-- README.md
|-- requirements.txt
|-- website/
|   |-- app.py                 # Flask application, routes, and progress logic
|   |-- lessons.py             # Curriculum and lesson block definitions
|   |-- problems.py            # Graded exercise definitions and test cases
|   |-- runner.py              # Python execution and grading helpers
|   |-- supabase_client.py     # Supabase client
|   |-- static/
|   |   |-- css/
|   |   |   |-- dashboard.css
|   |   |   `-- style.css
|   |   |-- images/
|   |   |   `-- ucg_logo.webp
|   |   `-- js/
|   |       |-- app.js         # Graded exercise behavior
|   |       |-- lesson-progress.js # Lesson task restoration and completion
|   |       |-- lesson.js      # Monaco setup and lesson IDE behavior
|   |       `-- xp-celebration.js # XP completion animation
|   `-- templates/
|       |-- components/
|       |   |-- ide.html       # Shared Monaco IDE component
|       |   `-- navbar.html    # Shared site navigation
|       |-- dashboard.html
|       |-- edit_profile.html
|       |-- exercises.html
|       |-- forgot_password.html
|       |-- index.html         # Individual exercise workspace
|       |-- lesson.html
|       |-- lessons.html
|       |-- login.html
|       |-- profile.html
|       |-- reset_password.html
|       `-- signup.html
```

The active and tracked application source now lives entirely in `website/`.
The former root-level Streamlit prototype, prototype models and utilities, and
tracked Python cache files were removed during consolidation. Local `.next/`,
`node_modules/`, and `__pycache__/` directories are generated or obsolete
artifacts; they are ignored by Git and can be deleted without affecting Flask.

## Local Setup

### Prerequisites

- Python 3.10 or newer
- A Supabase project with the required tables and storage bucket
- Internet access for frontend CDN assets

### Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/Beau47/ucg-mvp.git
cd ucg-mvp
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install the Python dependencies:

```bash
pip install -r requirements.txt
```

Create `website/.env` and add the Supabase values described below. Then start
the development server:

```bash
python website/app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Supabase Configuration

### Environment Variables

Create a local file at `website/.env`:

```dotenv
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-project-api-key
```

Never commit `.env` or place a privileged Supabase key in frontend code. Use
the least-privileged project key supported by the configured database policies.
The repository's `.gitignore` excludes environment files.

### Required Backend Resources

The application expects the following Supabase resources:

| Resource | Purpose | Fields used by the application |
| --- | --- | --- |
| `profiles` | Student account and profile data | `id`, `username`, `xp`, `streak`, `lessons_completed`, `problems_solved`, `avatar_url` |
| `lesson_progress` | Completed curriculum units | `id`, `user_id`, `lesson_id`, `completed` |
| `lesson_tasks` | Completed quizzes, IDE tasks, and lesson pages | `id`, `user_id`, `lesson_id`, `task_id`, `completed` |
| `problem_progress` | Passed coding exercises | `id`, `user_id`, `problem_id`, `passed` |
| `avatars` bucket | Uploaded profile pictures | Public file URLs stored in `profiles.avatar_url` |

`lesson_progress` must support a unique conflict target on
`(user_id, lesson_id)` because lesson completion uses an upsert with those
columns.

Supabase Auth must have email/password authentication enabled. If email
confirmation is enabled, users must verify their email before logging in.

## Application Architecture

### Request Flow

1. Flask receives the browser request in `website/app.py`.
2. `check_session()` redirects unauthenticated users away from protected pages.
3. Jinja templates render lesson, exercise, dashboard, and profile data.
4. Shared Jinja components render navigation and embedded lesson IDEs.
5. JavaScript loads Monaco editors, restores page task state, and sends code
   or completion events to Flask JSON endpoints.
6. Flask reads lesson and problem definitions from Python dictionaries and
   enforces lesson prerequisites for exercise routes.
7. Supabase stores authentication, profile information, and completion data.

### Content Model

Curriculum content is intentionally data-driven:

- `LESSONS` in `website/lessons.py` contains unit metadata and ordered content
  blocks.
- `PROBLEMS` in `website/problems.py` contains active exercise metadata,
  starter code, required function names, and test cases.
- `EXERCISE_CURRICULUM` in `website/problems.py` defines exercise order,
  lesson prerequisites, and the featured exercise for each lesson page.
- `website/templates/lesson.html` maps each lesson block type to its rendered
  interface.
- `website/templates/components/ide.html` provides the shared interactive IDE.
- `website/templates/components/navbar.html` provides consistent navigation
  and active-page highlighting across templates.

Adding a lesson dictionary entry makes it available to the lesson listing. A
new exercise must also be placed in `EXERCISE_CURRICULUM`; a separate Flask
route is not required for either content type.

### Shared Frontend Behavior

The consolidated frontend modules have distinct responsibilities:

- `app.js` controls the graded exercise workspace and displays test results.
- `lesson.js` creates and resizes Monaco editors embedded in lessons.
- `lesson-progress.js` restores completed page activities, locks or unlocks
  lesson navigation, and synchronizes task and lesson completion with Flask.
- `xp-celebration.js` owns the reusable XP completion animation.

Templates pass page-specific values to shared scripts through `data-*`
attributes. Keep this interface synchronized when changing lesson progress or
exercise access behavior.

## Routes

### Pages

| Route | Purpose |
| --- | --- |
| `GET /` | Student dashboard |
| `GET /lessons` | Curriculum unit list |
| `GET /lesson/<lesson_id>/<page>` | One page of a lesson |
| `GET /exercises` | Exercise catalog |
| `GET /workspace/<problem_id>` | Interactive graded exercise workspace |
| `GET /profile` | Student profile and statistics |
| `GET, POST /edit-profile` | Username and avatar editing |
| `GET, POST /signup` | Account registration |
| `GET, POST /login` | Account login |
| `GET /logout` | Session logout |
| `GET, POST /forgot-password` | Password-reset email flow |
| `GET /reset-password` | Password update page |

### JSON Endpoints

| Route | Purpose |
| --- | --- |
| `GET /problems` | List exercise summaries |
| `GET /problem/<problem_id>` | Return one complete problem definition |
| `POST /run` | Execute and grade an exercise submission |
| `POST /run_snippet` | Execute an ungraded lesson snippet |
| `POST /complete_task` | Record a completed lesson task |
| `POST /lesson/<lesson_id>/complete` | Record lesson completion |

## Curriculum Content

The current curriculum is defined in `website/lessons.py`:

| Unit ID | Displayed unit | Topic | Pages |
| --- | --- | --- | --- |
| `why_python` | Unit 0 | Why Python? | 2 |
| `functions_preview` | Lesson 0.5 | Read This Before Exercises | 1 |
| `variables` | Unit 1 | Variables and Data Types | 2 |
| `conditionals` | Unit 2 | Conditionals | 1 |
| `lists_dictionaries` | Unit 3 | Collections | 3 |
| `loops` | Unit 4 | Loops | 4 |
| `functions_modularity` | Unit 5 | Functions and Modularity | 2 |
| `recursion_capstone` | Unit 6 | Recursion | 1 |

## Creating a Lesson

Add a new entry to `LESSONS` in `website/lessons.py`:

```python
"variables": {
    "id": "variables",
    "lesson_number": "1",
    "title": "Variables and Data Types",
    "description": "Lesson 1.0: Introduction to variables.\nLesson 1.1: Using variables.",
    "blocks": [
        {
            "page": 1,
            "type": "heading",
            "text": "What Is a Variable?",
        },
        {
            "page": 1,
            "type": "paragraph",
            "text": "A variable gives a value a reusable name.",
        },
    ],
}
```

Every lesson requires:

- `id`: unique URL-safe identifier matching the dictionary key
- `lesson_number`: value displayed in the lesson navigation
- `title`: unit title
- `description`: lesson-card summary; use newlines between sub-lessons
- `blocks`: ordered content blocks

Every block requires a positive `page` number and a supported `type`. Blocks
with the same page number render together in dictionary order. Keep page
numbers contiguous so Previous and Next navigation remains valid.

## Lesson Block Types

The lesson template currently supports:

| Type | Required content | Purpose |
| --- | --- | --- |
| `heading` | `text` | Section heading |
| `paragraph` | `text` | Standard prose |
| `rich_paragraph` | `html` | Trusted formatted HTML, including vocabulary highlights |
| `footnote` | `number`, `text` | Definition or citation beneath content |
| `code` | `text` | Syntax-highlighted Python example |
| `list` | `items` | Bulleted list |
| `table` | `headers`, `rows` | Responsive reference table |
| `image` | `src`, optional `caption` | Standalone image |
| `image_text` | `src`, `alt`, `paragraphs` | Image with adjacent text |
| `tip` | `text` | Highlighted instructional tip |
| `warning` | `text` | Highlighted warning |
| `quote` | `text` | Quotation or emphasized statement |
| `divider` | none | Visual section break |
| `quiz` | question data, `options`, `answer` | Required multiple-choice activity |
| `ide` | `instructions`, `starter_code` | Required interactive Python activity |
| `exercise` | `problem` | Link to a graded problem |

### Quiz Example

```python
{
    "page": 1,
    "type": "quiz",
    "question": "Which value is a Boolean?",
    "options": ["True", '"hello"', "5", "3.14"],
    "answer": "True",
}
```

The `answer` value must exactly match one item in `options`.

For questions containing Python, use `question_parts` so code is displayed in
a formatted code block instead of flattened into the heading:

```python
{
    "page": 1,
    "type": "quiz",
    "question_parts": [
        {"type": "text", "text": "What is printed?"},
        {
            "type": "code",
            "text": 'def cheer():\n    print("Go Team!")\n\ncheer()\ncheer()',
        },
    ],
    "options": ["Once", "Twice", "Nothing", "An error"],
    "answer": "Twice",
}
```

### IDE Example

```python
{
    "page": 1,
    "type": "ide",
    "instructions": "Create a variable and print it.",
    "starter_code": 'message = "Hello"\nprint(message)',
}
```

Students must run every IDE and answer every required quiz on a page before the
Next button is enabled.

### Exercise Link Example

```python
{
    "page": 2,
    "type": "exercise",
    "problem": "add_one",
}
```

The `problem` value must match a key in `PROBLEMS`.

## Creating an Exercise

Add a new entry to `PROBLEMS` in `website/problems.py`:

```python
"multiply_two": {
    "id": "multiply_two",
    "title": "Multiply Two",
    "description": "Return a number multiplied by two.",
    "function_name": "multiply_two",
    "starter_code": """def multiply_two(number):
    # WRITE CODE HERE
    pass
""",
    "challenges": [
        "Function Exists",
        "Returns Correct Value",
        "No Extra Output",
    ],
    "test_cases": [
        {"input": 5, "expected": 10},
        {"input": -3, "expected": -6},
    ],
}
```

Required fields:

- `id`: unique identifier matching the dictionary key
- `title`: displayed exercise name
- `description`: concise student-facing task
- `function_name`: function the grader retrieves after execution
- `starter_code`: initial Monaco contents
- `challenges`: visible completion checklist
- `test_cases`: inputs and expected return values

For a one-argument function, set `input` to that argument. For multiple
arguments or no arguments, use a tuple:

```python
{"input": (3, 8), "expected": 24}
{"input": (), "expected": "Hello"}
```

Add the problem ID to the appropriate `EXERCISE_CURRICULUM` group after
creating its definition. The group determines where the exercise appears,
which lesson unlocks it, and whether it is the featured lesson-end link.

## Code Execution

The application has two code-execution paths.

### Lesson IDEs

`POST /run_snippet` sends editor contents to `run_snippet()` in
`website/runner.py`. The code runs without grading, and captured standard output
or an exception message is returned to the lesson IDE.

### Graded Exercises

`POST /run` loads the selected problem and sends the submission to
`run_problem()`. The runner:

1. Executes the submitted Python code in a new namespace.
2. Finds the required function by `function_name`.
3. Calls it once for each test case.
4. Compares actual and expected return values.
5. Returns console output, per-test results, totals, percentage, and errors.
6. Records exercise progress for a logged-in user based on the returned pass
   count.

## Progress and XP

Progress is split between Supabase and browser storage:

- Supabase stores lesson completion, completed lesson task IDs, passed
  exercises, profile data, and avatars.
- `lesson_tasks` stores `page-complete-N` records used to unlock exercises at
  the end of individual lesson pages such as Lesson 1.1 or Lesson 3.2.
- `localStorage` stores per-page quiz and lesson IDE display state so completed
  controls are restored when a student navigates backward or refreshes.
- Flask checks Supabase completion records before rendering a workspace,
  returning problem details, or running submitted exercise code.

The dashboard derives XP from completion records:

- Completed lesson: 100 XP
- Completed exercise: 25 XP
- Level increase: every 500 XP

## Development Checks

There is not yet a committed automated test suite. Before merging a change,
perform at least the following checks:

1. Start the Flask server without import or configuration errors.
2. Create an account or log in with a test account.
3. Open every changed lesson page and verify block order and formatting.
4. Confirm required quizzes and IDEs unlock Next only after completion.
5. Navigate backward and verify completed page activities are restored.
6. Run one passing and one failing graded exercise.
7. Confirm dashboard and profile totals update after completion.
8. Check the browser console for JavaScript errors.
9. Test the changed interface at desktop and mobile widths.

Avoid committing `.env`, Python cache files, generated frontend files, logs, or
editor-specific settings.

## Current Limitations

- Student Python is executed with `exec()` inside the Flask process. There is
  no process isolation, resource limit, timeout, or system-call restriction.
  **Do not expose the current code runner to untrusted public traffic.** A
  production release needs an isolated execution service or sandbox.
- The Flask session secret is currently hard-coded in `website/app.py`. Move it
  to an environment variable and rotate it before deployment.
- Supabase access depends on the policies and privileges attached to
  `SUPABASE_KEY`. Review row-level security and use a least-privileged key
  before production deployment.
- Lesson activity display restoration relies on browser `localStorage`, so the
  restored button and editor state does not fully follow a student across
  browsers or devices. Exercise access itself is stored in Supabase.
- The password-reset redirect is hard-coded to the current PythonAnywhere URL
  and should become an environment-specific setting before another deployment.
- The project does not yet include automated backend, frontend, or end-to-end
  tests.
- The `/run` route currently records an exercise as completed when at least one
  test passes. It should require `passed == total` before progress is saved.
- Frontend dependencies are loaded from CDNs rather than bundled locally.

## Next Features

Future improvements planned for Urban Coders Guild include:

### Instructor View
Develop an instructor dashboard to allow teachers to:
- Monitor student progress and lesson completion
- View exercise performance and learning milestones
- Provide feedback and support

### Account Email Management
Allow users to securely change their account email through profile settings with proper verification.

### Student Achievements
Introduce achievements and badges to reward:
- Lesson completion
- Coding milestones
- XP goals
- Learning streaks

### Exercise Hint System
Add a hint feature for exercises that provides guidance without immediately revealing solutions.

### Advanced Exercise Checking
Improve challenge validation with:
- Additional test cases
- More detailed feedback
- Bonus XP and achievement rewards for completing difficult challenges

### Mobile Support
Improve usability on mobile devices through:
- Responsive layouts
- Better navigation
- Mobile-friendly coding workspace

## Credits

Urban Coders Guild Learning Platform was created as an interactive Python
education platform using Flask, Supabase, Monaco Editor, Prism, HTML, CSS, and
JavaScript.
