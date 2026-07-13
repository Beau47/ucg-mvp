import streamlit as st

from models.problem import (
    Problem,
    Difficulty,
    Language,
    Category,
)

problem = Problem(
    title="Square",
    difficulty=Difficulty.EASY,
    language=Language.PYTHON,
    category=Category.FUNCTIONS,
)

problem.description = "Return the square of a number."

problem.add_example(
    input="2",
    output="4",
    explanation="2 × 2 = 4"
)

problem.add_test_case(
    input="3",
    expected_output="9"
)

st.title("Problem Blueprint")

st.subheader(problem.title)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Difficulty", problem.difficulty.value)

with col2:
    st.metric("Language", problem.language.value)

with col3:
    st.metric("Category", problem.category.value)

st.divider()

st.subheader("Description")
st.write(problem.description)

st.subheader("Examples")

for example in problem.examples:
    st.code(
        f"Input:\n{example.input}\n\nOutput:\n{example.output}",
        language="text"
    )

    if example.explanation:
        st.caption(example.explanation)

st.subheader("Hidden Test Cases")

for i, test in enumerate(problem.test_cases, start=1):
    st.write(f"Test {i}")
    st.code(
        f"Input: {test.input}\nExpected: {test.expected_output}",
        language="text"
    )