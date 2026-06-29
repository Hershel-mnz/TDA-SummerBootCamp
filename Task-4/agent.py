import os
from dotenv import load_dotenv
from google import genai

from planner import choose_tool
from tools import web_search, calculator
from memory import get_recent_memory, save_chat

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def run_agent(user_input):

    previous_chats = get_recent_memory()

    memory_text = ""

    for chat in previous_chats:
        memory_text += f"""
User: {chat['user']}
Assistant: {chat['assistant']}
"""

    selected_tool = choose_tool(user_input)

    reasoning = []

    reasoning.append("Planning user request")

    if selected_tool == "search":

        reasoning.append("Selected Web Search Tool")

        tool_output = web_search(user_input)

    elif selected_tool == "calculator":

        reasoning.append("Selected Calculator Tool")

        tool_output = calculator(user_input)

    else:

        reasoning.append("No external tool required")

        tool_output = "No tool used."

    reasoning.append("Generating final response with Gemini")

    prompt = f"""
You are an AI Project Mentor.

Previous Conversation:
{memory_text}

Current User Question:
{user_input}

Tool Used:
{selected_tool}

Tool Output:
{tool_output}

Use the tool output if available.

If the user asks for a project:
- Explain the idea
- Suggest architecture
- Suggest tech stack
- Give folder structure
- Give implementation steps

Otherwise answer normally.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    final_answer = response.text

    save_chat(user_input, final_answer)

    return final_answer, selected_tool, reasoning