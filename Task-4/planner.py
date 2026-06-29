import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def choose_tool(user_input):

    prompt = f"""
You are an AI planner.

Your job is to decide which tool should be used.

Available tools:

1. search
- Latest news
- Current information
- Web search
- Weather
- Stock prices
- Recent events

2. calculator
- Mathematical calculations
- Arithmetic
- Percentages

3. llm
- General explanations
- Coding
- AI concepts
- Project guidance
- Anything that doesn't need external tools

Return ONLY one word.

search
calculator
llm

User Request:
{user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    tool = response.text.strip().lower()

    if tool not in ["search", "calculator", "llm"]:
        tool = "llm"

    return tool