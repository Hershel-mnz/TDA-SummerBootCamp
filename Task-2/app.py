import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)

st.title("Prompt Engineering Playground")

st.write(
    "Explore different prompting techniques using Gemini AI"
)

user_input = st.text_area(
    "Enter your text:"
)

mode = st.selectbox(
    "Choose Prompt Mode",
    [
        "Explain Like I'm 5",
        "Professional Rewrite",
        "Summarize",
        "Quiz Generator",
        "Mentor Mode"
    ]
)

generate = st.button("Generate")

if generate:

    if user_input.strip() == "":

        st.warning(
            "Please enter some text."
        )

    else:

        if mode == "Explain Like I'm 5":

            prompt = f"""
            Explain the following concept
            to a 5 year old child:

            {user_input}
            """

        elif mode == "Professional Rewrite":

            prompt = f"""
            Rewrite the following text
            in a professional tone:

            {user_input}
            """

        elif mode == "Summarize":

            prompt = f"""
            Summarize the following text
            into key points:

            {user_input}
            """

        elif mode == "Quiz Generator":

            prompt = f"""
            Generate 5 quiz questions
            from the following topic:

            {user_input}
            """

        elif mode == "Mentor Mode":

            prompt = f"""
            Act as a mentor.

            Explain:

            {user_input}

            Include:
            - Simple explanation
            - Real world example
            - Practical advice
            """

        with st.spinner("Generating response..."):

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.subheader("Response")

        st.write(response.text)