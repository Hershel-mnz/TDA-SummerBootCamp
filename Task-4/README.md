# 🤖 AI Project Mentor Agent

## Overview

AI Project Mentor Agent is an Agentic AI application built using **Python, Streamlit, and the Gemini API**.

Unlike a traditional chatbot that simply answers questions, this application can decide when to use different tools, remember previous conversations, and perform multiple steps before generating a response.

The goal of this project is to demonstrate the core concepts of **Agentic AI**, including planning, tool selection, memory, and autonomous decision-making.

---

## Features

* Accepts user input through a Streamlit interface
* Uses the Gemini API to generate responses
* Uses Web Search for current information
* Uses a Calculator for mathematical queries
* Maintains conversation memory across sessions
* Displays the reasoning steps used by the agent
* Allows users to download the generated response
* Simple and user-friendly interface

---

## Agent Workflow

```
User Input
      ↓
Planning
      ↓
Tool Selection
      ↓
Search / Calculator / LLM
      ↓
Tool Output
      ↓
Gemini Analysis
      ↓
Save Memory
      ↓
Final Response
```

---

## Tools Used

### 1. Web Search

Used for:

* Latest AI news
* Current events
* Recent technologies
* Information available on the web

### 2. Calculator

Used for:

* Arithmetic calculations
* Mathematical expressions

---

## Memory Implementation

The application stores conversations inside:

```
memory/memory.json
```

The most recent conversations are loaded whenever the user asks follow-up questions, allowing the agent to continue previous discussions.

---

## Technologies Used

* Python
* Streamlit
* Gemini API
* DuckDuckGo Search
* JSON (for memory)

---

## Folder Structure

```
Task-4/
│
├── app.py
├── agent.py
├── planner.py
├── tools.py
├── memory.py
├── requirements.txt
├── README.md
├── .env
│
└── memory/
    └── memory.json
```

---

## Installation

Clone the repository

```
git clone <repository-link>
```

Move into the project folder

```
cd Task-4
```

Install dependencies

```
pip install -r requirements.txt
```

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```
streamlit run app.py
```

---

## Example Queries

* Explain Prompt Engineering.
* What are the latest developments in Agentic AI?
* 3456 * 789
* I want to build an AI Resume Reviewer.
* Continue my previous project.

---

## Requirements Satisfied

* User Input
* Gemini LLM API
* Multiple Tools
* Planning
* Tool Selection
* Memory
* Multi-step Workflow
* Autonomous Decision Making
* Streamlit Frontend

---

## Future Improvements

* Function Calling
* LangGraph Integration
* RAG-based Knowledge Base
* PDF Report Generation
* Additional Custom Tools

---

## Author

Hershel Shaun Menezes


