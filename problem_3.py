import streamlit as st

st.set_page_config(page_title="Problem 3", page_icon="📈")

from streamlit_monaco import st_monaco
import io
from contextlib import redirect_stdout

# Hard-coded problem replaced by a Problem class for better structure and reuse
class Problem:
    def __init__(self, title, function_name, starter_code, description=None, examples=None, test_cases=None):
        self.title = title
        self.function_name = function_name
        self.starter_code = starter_code
        self.description = description or ""
        self.examples = examples or []
        self.test_cases = test_cases or []

    def add_example(self, inp, out):
        self.examples.append({"input": inp, "output": out})

    def add_test(self, inp, expected):
        self.test_cases.append({"input": inp, "expected": expected})


problem = Problem(
    title="Square",
    function_name="square",
    starter_code='''
def square(x):
    """
    Given an integer x,
    return x squared.

    Examples:
    square(5) -> 25
    square(-1) -> 1 
    """

    # Your code here
    pass
''',
    description="Write a function that returns the square of its integer input.",
    examples=[{"input": 5, "output": 25}, {"input": -1, "output": 1}],
    test_cases=[
        {"input": 1, "expected": 1},
        {"input": 6, "expected": 36},
        {"input": 0, "expected": 0},
        {"input": 11, "expected": 121},
        {"input": 30, "expected": 900},
    ],
)

st.title("Urban Coders Guild")

st.subheader(problem.title)

# Initialize the Monaco Editor component
content = st_monaco(
    value=problem.starter_code,
    height="400px",
    language="python",
    theme="vs-dark"
)

test_case = 5

# Asks student to finish a func that takes in int x, returns x squared


# Run button
if st.button("Run"):

    output = io.StringIO()
    namespace = {}

    try:
        # Run student code and capture print output
        with redirect_stdout(output):
            exec(content, namespace)

        st.subheader("Output")
        st.code(output.getvalue())

        func_name = problem.function_name

        if func_name not in namespace:
            st.error(f"Function '{func_name}' not found.")
        else:
            student_func = namespace[func_name]

            passed = 0
            total = len(problem.test_cases)

            st.subheader("Test Results")

            for test in problem.test_cases:
                try:
                    actual = student_func(test["input"])
                    expected = test["expected"]

                    if actual == expected:
                        passed += 1
                        st.success(f"Input={test['input']} | Expected={expected} | Got={actual}")
                    else:
                        st.error(f"Input={test['input']} | Expected={expected} | Got={actual}")

                except Exception as e:
                    st.error(f"Input={test['input']} | Runtime Error: {e}")

            st.subheader("Score")
            st.write(f"Passed: {passed}/{total}")

            if total > 0:
                st.write(f"Percentage: {(passed / total) * 100:.1f}%")
            else:
                st.write("Percentage: N/A")

    except Exception as e:
        st.error(f"Code Error: {e}")
