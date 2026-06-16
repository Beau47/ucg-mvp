import streamlit as st

st.set_page_config(page_title="Problem 1", page_icon="📈")

from streamlit_monaco import st_monaco
import io
from contextlib import redirect_stdout


st.title("Urban Coders Guild")

st.subheader("Lesson 1: Variables")

st.write("""
Create a variable x and set it equal to 5.
Then print x.
""")

# Initialize the Monaco Editor component
content = st_monaco(
    value="# Type your Python code here\nprint('Hello from Monaco!')",
    height="400px",
    language="python",
    theme="vs-dark"
)

test_case = 5


#Hard-coded problem (add one function)
problem = {
    "title": "Add One",
    "function_name": "add_one",
    "starter_code": """
def add_one(x):
    pass
""",
    "test_cases": [
        {"input": 1, "expected": 2},
        {"input": 5, "expected": 6},
        {"input": -1, "expected": 0},
    ]
}
# Asks student to finish a func that takes in int x, returns x + 1


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

        func_name = problem["function_name"]

        if func_name not in namespace:
            st.error(f"Function '{func_name}' not found.")

        else:
            student_func = namespace[func_name]

            passed = 0
            total = len(problem["test_cases"])

            st.subheader("Test Results")

            for test in problem["test_cases"]:

                try:
                    actual = student_func(test["input"])
                    expected = test["expected"]

                    if actual == expected:
                        passed += 1
                        st.success(
                            f"Input={test['input']} | Expected={expected} | Got={actual}"
                        )

                    else:
                        st.error(
                            f"Input={test['input']} | Expected={expected} | Got={actual}"
                        )

                except Exception as e:
                    st.error(
                        f"Input={test['input']} | Runtime Error: {e}"
                    )

            st.subheader("Score")

            st.write(f"Passed: {passed}/{total}")

            if total > 0:
                st.write(
                    f"Percentage: {(passed / total) * 100:.1f}%"
                )
            else:
                st.write("Percentage: N/A")

    except Exception as e:
        st.error(f"Code Error: {e}")
