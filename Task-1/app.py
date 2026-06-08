import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

history = []

def ask_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"API Error: {e}"

while True:

    print("\n===== AI STUDY ASSISTANT =====")
    print("1. Explain a Concept")
    print("2. Summarize Text")
    print("3. Generate Quiz Questions")
    print("4. View Chat History")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "5":
        print("Goodbye!")
        break

    elif choice == "4":

        if not history:
            print("\nNo history available.")
        else:
            print("\n===== HISTORY =====")
            for item in history:
                print(item)

    elif choice in ["1", "2", "3"]:

        user_input = input("\nEnter text: ")

        if user_input.strip() == "":
            print("Input cannot be empty!")
            continue

        if choice == "1":
            prompt = f"Explain this concept simply with examples:\n{user_input}"

        elif choice == "2":
            prompt = f"Summarize the following text:\n{user_input}"

        elif choice == "3":
            prompt = f"Generate 5 quiz questions from:\n{user_input}"

        print("\nThinking...")
        result = ask_gemini(prompt)

        print("\n===== RESPONSE =====")
        print(result)

        history.append({
            "feature": choice,
            "input": user_input,
            "output": result[:100]
        })

    else:
        print("Invalid option.")