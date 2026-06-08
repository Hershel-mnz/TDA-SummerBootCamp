# AI Study Assistant

## Overview

AI Study Assistant is a Python-based application that uses the Google Gemini API to help students learn more effectively. The application accepts user input, sends it to a Large Language Model (LLM), and displays AI-generated responses.

## Features

### 1. Explain a Concept

Provides a simple explanation of a topic along with examples.

### 2. Summarize Text

Generates a concise summary of long text.

### 3. Generate Quiz Questions

Creates quiz questions from the provided topic or text.

### 4. Chat History

Stores previous interactions during the session and allows users to review them.

### 5. Input Validation

Handles empty user input gracefully and prompts the user to enter valid text.

## Technologies Used

* Python
* Google Gemini API
* google-generativeai
* python-dotenv

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd Task-1
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project directory and add:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

## Running the Application

```bash
python app.py
```

## Example Usage

### Explain a Concept

Input:

```text
What is Recursion?
```

Output:

```text
Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.
```

### Summarize Text

Input:

```text
Artificial Intelligence is a branch of computer science...
```

Output:

```text
AI is a field of computer science focused on creating systems capable of performing tasks that require human intelligence.
```

### Generate Quiz Questions

Input:

```text
Deep Learning
```

Output:

```text
1. What is Deep Learning?
2. What are neural networks?
3. What is backpropagation?
...
```

## Project Structure

```text
Task-1/
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

Note: The `.env` file is not uploaded to GitHub because it contains the API key.

## Author

Hershel Menezes
