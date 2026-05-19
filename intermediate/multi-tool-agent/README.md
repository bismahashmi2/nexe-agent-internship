# 🛠️ Multi-Tool Agent

A intermediate-level Agentic AI System built using **Gemini 2.5 Flash** and **OpenAI Agents SDK** concepts and **SQLite database**.

This project demonstrates how an AI agent can dynamically use multiple tools to:
- perform web searches
- save data into a database
- send real emails
- return structured JSON responses

---

## 🚀 Features 

- 🌐 Web Search Integration
- 🗄️ SQLite Database Storage
- 📧 Real Email Sending using SMTP
- 🔧 Dynamic Tool Calling
- 📦 Structured JSON responses
- ⚠️ Graceful error handling
- 🤖 Agent-based architecture

---

## 🏗️ Project Structure

```text
multi-tool-agent/
│
├── src/
│   ├── main.py
│   │
│   ├── my_agent/
│   │   └── multi_tool_agent.py
│   │
│   ├── my_tools/
│   │   ├── save_db.py
│   │   ├── send_email.py
│   │   └── web_search.py
│   │
│   ├── my_config/
│   │   └── gemini_config.py
│   │
│   ├── database/
│   │   └── app.db
│   │
│   └── utils/
│       └── clean_output.py
│
├── .env
├── .gitignore
├── README.md
└── pyproject.toml
```

---

## ⚙️ How It Works

### 1. User Input
User enters a query like:

Search latest AI news and save it to database

or

Send an email to example@gmail.com with subject "AI News"

---

### 2. Agent Processing
The AI agent:
- Understands the request
- Selects the appropriate tool dynamically
- Performs the task
- Returns a structured response

---

### 3. Structured Output
The agent always responds in JSON format:

{
  "response": "Email sent successfully."
}

---

### 🧪 Example Usage
## 🌐 Web Search Tool

The agent can search the internet using the DDGS (DuckDuckGo Search) library.

## Example
Give me latest Robotics news

The tool fetches:
- titles
- links
- snippets

from real web search results.

--- 

### 🧰 Tools Used

- DuckDuckGo Library
- 

All calculations are performed via tools — not directly by the model.

---

### 📦 Installation

### Clone the Repository
git clone <your-repo-url>
cd multi-tool-agent

### Install Dependencies

- uv init
- uv add openai-agents
- uv add python-decouple

### Run the Project

uv run python src/main.py

---

### 📌 Requirements

- Python 3.10+
- OpenAI / Gemini model support via Agents SDK
- agents library
- uv package manager
- sqlite3

---

### 🎯 Key Concepts

This project demonstrates:

- Agentic AI workflow design
- Tool-calling AI agent architecture
- Function execution through LLMs
- Structured JSON output enforcement

---

### ⚠️ Notes

- The agent is designed specifically for sending emails and web search
- Responses are returned in JSON format only
- Invalid or unsupported requests are handled gracefully

---

### 👨‍💻 Author

Built as part of an Agentic AI Internship Task
Focused on learning:

- Tool-calling reasoning in AI agents
- Agent workflows
- Structured AI outputs
......





