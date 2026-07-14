import streamlit as st
from streamlit_monaco import st_monaco
import io
from contextlib import redirect_stdout

# Initializes page set up with title and page icon
# TODO make this default for each new problem
st.set_page_config(page_title="Problem 2",
                   page_icon="https://images.squarespace-cdn.com/content/v1/61133a4771763d4aab457698/cc1f440b-2d12-49c1-a937-2288bccdba18/Mark+Only+%28Single+Color%29+copy.png")

# Initializes the header, subheader, and problem text, respectively
st.title("Urban Coders Guild")
st.subheader("Lesson 2: Data Types")
st.write("""
Create a variable of a number, a word, a decimal, and a bool.
""")

# Initializes the sidebar appearance
st.sidebar.success("Select an exercise above.")

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

    # namespace = {}

    # exec(content, namespace)

    # if namespace.get("x") == 5:
    #     st.success("You did it!")
    # else:
    #     st.error("Try again.")
