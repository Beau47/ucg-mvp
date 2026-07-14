import streamlit as st

st.set_page_config(page_title="Problem 3", page_icon="📈")

from streamlit_monaco import st_monaco
import io
from contextlib import redirect_stdout

# Problem is a class (not a dict) because instructors will eventually create these
# through a form or DB row — a class gives us validation and helper methods
# (add_example, add_test) instead of raw dict key-poking.
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

content = st_monaco(
    value=problem.starter_code,
    height="400px",
    language="python",
    theme="vs-dark"
)

if st.button("Run"):

    output = io.StringIO()
    namespace = {}

    try:
        with redirect_stdout(output):
            exec(content, namespace)

            func_name = problem.function_name
            if func_name not in namespace:
                raise Exception(f"Function '{func_name}' not found.")

            student_func = namespace[func_name]
            passed = 0
            total = len(problem.test_cases)
            test_results = []

            for test in problem.test_cases:
                try:
                    actual = student_func(test["input"])
                    expected = test["expected"]
                    if actual == expected:
                        passed += 1
                        test_results.append(("pass", test["input"], expected, actual))
                    else:
                        test_results.append(("fail", test["input"], expected, actual))
                except Exception as e:
                    test_results.append(("error", test["input"], None, str(e)))

        # everything below runs AFTER redirect_stdout closes — output is now complete
        st.subheader("Output")
        st.code(output.getvalue())

        st.subheader("Test Results")
        for status, inp, expected, actual in test_results:
            if status == "pass":
                st.success(f"Input={inp} | Expected={expected} | Got={actual}")
            elif status == "fail":
                st.error(f"Input={inp} | Expected={expected} | Got={actual}")
            else:
                st.error(f"Input={inp} | Runtime Error: {actual}")

        st.subheader("Score")
        st.write(f"Passed: {passed}/{total}")
        st.write(f"Percentage: {(passed/total)*100:.1f}%" if total else "Percentage: N/A")

    except Exception as e:
        st.error(f"Code Error: {e}")