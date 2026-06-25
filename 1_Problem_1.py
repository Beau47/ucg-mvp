# =========================
# Imports
# =========================

import streamlit as st
from streamlit_monaco import st_monaco
import io
from contextlib import redirect_stdout

# Initializes page set up with title and page icon
st.set_page_config(page_title="Problem 1",
                   page_icon="https://images.squarespace-cdn.com/content/v1/61133a4771763d4aab457698/cc1f440b-2d12-49c1-a937-2288bccdba18/Mark+Only+%28Single+Color%29+copy.png")


# Hard-coded problem ("Add One" function)
# Problem dictionary; details the properties of each problem
problem = {
    "title": "Add One",

    "function_name": "add_one",

    "starter_code": '''
def add_one(x):
    """
    Given an integer x,
    return x + 1.

    Examples:
    add_one(5) -> 6
    add_one(-1) -> 0
    """

    # Your code here
    pass
''',

    "test_cases": [
        {"input": 1, "expected": 2},
        {"input": 5, "expected": 6},
        {"input": -1, "expected": 0},
    ]
}

# Initializes the header, subheader, and problem text, respectively
st.title("Urban Coders Guild")
st.subheader(problem["title"])
st.write("""
Create a function that adds one to a variable x.
""")

# Initialize the Monaco Editor component w/appearance
content = st_monaco(
    value=problem["starter_code"],
    height="400px",
    language="python",
    theme="vs-dark",
)

test_case = 5


# =========================
# Run button
# =========================

if st.button("Run"):
    # Capture print statements from student code
    output = io.StringIO()

    # Stores all functions/variables created by exec()
    namespace = {}

try:

    # Initialize Grading
    passed = 0
    total = len(problem["test_cases"])

    # Execute Student Code
    with redirect_stdout(output):

        # Load student code
        exec(content, namespace)

        func_name = problem["function_name"]

        if func_name not in namespace:
            raise Exception(f"Function '{func_name}' not found.")

        student_func = namespace[func_name]

        test_results = []

        # =========================
        # Run Test Cases
        # =========================

        for test in problem["test_cases"]:
            actual = student_func(test["input"])
            expected = test["expected"]

            if actual == expected:
                passed += 1
                test_results.append(
                    ("pass", test["input"], expected, actual)
                )
            else:
                test_results.append(
                    ("fail", test["input"], expected, actual)
                )

    # Display console output
    st.subheader("Console")
    st.code(output.getvalue())

    # Display test results
    st.subheader("Test Results")

    for result in test_results:
        status, inp, expected, actual = result

        if status == "pass":
            st.success(
                f"Input={inp} | Expected={expected} | Got={actual}"
            )
        else:
            st.error(
                f"Input={inp} | Expected={expected} | Got={actual}"
            )

    # =========================
    # Display Score
    # =========================

    st.subheader("Score")
    st.write(f"Passed: {passed}/{total}")

    if total > 0:
        st.write(f"Percentage: {(passed/total)*100:.1f}%")
    else:
        st.write("Percentage: N/A")

except Exception as e:
    # Display Runtime Errors
    st.error(f"Code Error: {e}")
