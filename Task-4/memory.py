import json
import os


MEMORY_FILE = "memory/memory.json"


def load_memory():
    """
    Load previous conversations from memory.json.
    If the file doesn't exist or is empty,
    return an empty list.
    """
    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_chat(user_message, assistant_message):
    """
    Save one conversation to memory.
    """

    memory = load_memory()

    memory.append({
        "user": user_message,
        "assistant": assistant_message
    })

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def clear_memory():
    """
    Delete all previous conversations.
    """

    with open(MEMORY_FILE, "w") as file:
        json.dump([], file, indent=4)


def get_recent_memory(limit=5):
    """
    Return only the most recent conversations.
    This prevents the prompt from becoming too long.
    """

    memory = load_memory()

    return memory[-limit:]