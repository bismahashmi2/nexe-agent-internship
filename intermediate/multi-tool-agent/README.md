# 🛠️ Multi-Tool Agent

An intermediate-level Agentic AI System built using **Gemini 2.5 Flash** and **OpenAI Agents SDK** concepts and **SQLite**.


This project demonstrates how an AI agent can dynamically use multiple tools to:
- 🌐 perform web searches
- 🗄️ save search queries into a database
- 📧 send real emails using SMTP
- 🤖 route tasks through intelligent tool calling

---

## 🚀 Features 

- 🌐 Web Search Integration
- 🗄️ SQLite Database Storage
- 📧 Real Email Sending using SMTP
- 🔧 Dynamic Tool Calling
- 📦 Structured JSON responses
- ⚠️ Graceful error handling
- 🤖 Agent-based architecture
- 🧠 Tool-Oriented AI Workflow

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
- Executes the correct tool dynamically
- Returns a final response

---

### 3. Tool Execution

Depending on the request, the agent may:

- Perform a real web search
- Save data into SQLite database
- Send an actual email through SMTP

---

### 🧪 Example Usage
### 🌐 Web Search Example
#### Input
Give me latest Robotics news

#### Output
```json
{
  "tool_used": "web_search",
  "response": {
    "query": "latest robotics news",
    "results": [
      {
        "title": "Robotics News -- ScienceDaily",
        "link": "https://www.sciencedaily.com/news/computers_math/robotics/",
        "snippet": "Latest robotics research and advancements..."
      }
    ]
  }
}
```
### 📧 Email Example
#### Input
Send an email to example@gmail.com with subject "AI News"

#### Output
```json
{
  "tool_used": "send_email",
  "response": {
    "status": "success",
    "message": "Email sent successfully"
  }
}

```
--- 

### 🧰 Tools Used

- 🌐 Web Search Tool (DDGS / DuckDuckGo Search)
- 🗄️ SQLite Database Tool
- 📧 SMTP Email Sending Tool

All tasks are performed dynamically through tool calling.

---

### 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/bismahashmi2/nexe-agent-internship.git

cd intermediate
cd multi-tool-agent
```

### Install Dependencies

- uv init
- uv venv .venv
- uv add openai-agents
- uv add python-decouple
- uv add ddgs

### Run the Project
activate virtual environment by "source .venv/bin/activate". Then run:

```bash
uv run python src/main.py
```

---

### 📌 Requirements

- Python 3.10+
- OpenAI / Gemini model support via Agents SDK
- agents library
- uv package manager
- sqlite3


SQLite is included with Python by default.

---

### 🎯 Key Concepts

This project demonstrates:

- Agentic AI workflow design
- Multi-tool orchestration
- Function/tool calling through LLMs
- Web search integration
- Database persistence using SQLite
- SMTP email automation
- Structured response handling
- External API & system integration

---

### ⚠️ Notes

- The web search tool uses DuckDuckGo Search (DDGS)
- Email sending requires valid SMTP credentials
- Search queries are stored locally in SQLite database
- Some search results may contain outdated or unavailable links
- The agent uses tools dynamically depending on user requests

### ⚠️ Deterministic Behavior Note

This system is LLM-driven and therefore non-deterministic.

- Tool selection depends on model reasoning
- Web search results may vary over time
- Email and external APIs depend on runtime conditions

Because of this, identical inputs may produce slightly different outputs.
However, all outputs follow a structured tool-based workflow.

---

### 👨‍💻 Author

Built as part of an Agentic AI Internship Task.

Focused on learning:

- Tool-calling AI systems
- Agent workflows
- External integrations
- Database persistence
- SMTP automation
- Multi-tool orchestration
- Structured AI responses
---
