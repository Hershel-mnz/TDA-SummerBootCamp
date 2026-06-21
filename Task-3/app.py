import streamlit as st

from prompts.styles import styles
from api.image_generator import generate_image

st.title("AI Image Generator")

st.write(
    "Generate images using AI"
)

prompt = st.text_input(
    "Enter image prompt"
)

style = st.radio(
    "Choose Style",
    list(styles.keys())
)

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("Generate"):

    final_prompt = (
        prompt +
        ", " +
        styles[style]
    )

    image = generate_image(
        final_prompt
    )

    st.image(image)

    st.session_state.history.append(
        final_prompt
    )

st.subheader("Prompt History")

for item in st.session_state.history:
    st.write(item)