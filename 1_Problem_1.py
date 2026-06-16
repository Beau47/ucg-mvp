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

# Run button
if st.button("Run"):
    output = io.StringIO()

    try:
        with redirect_stdout(output):
            exec(content)

        st.write("Output:")
        st.code(output.getvalue())

    except Exception as e:
        st.error(str(e))

    namespace = {}

    exec(content, namespace)

    if namespace.get("x") == 5:
        st.success("You did it!")
    else:
        st.error("Try again.")



st.sidebar.success("Select an exercise above.")
