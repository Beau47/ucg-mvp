import streamlit as st
from streamlit_monaco import st_monaco


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

if st.button("Run"):
    st.write("Output:")
    st.code(content)
