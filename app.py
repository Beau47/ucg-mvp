import streamlit as st

st.title("Urban Coders Guild")

st.subheader("Lesson 1: Variables")

st.write("""
Create a variable x and set it equal to 5.
Then print x.
""")

code = st.text_area(
    "Code Editor",
    value="print('Hello World')",
    height=300
)

if st.button("Run"):
    st.write("Output:")
    st.code(code)