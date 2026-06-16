import streamlit as st
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
