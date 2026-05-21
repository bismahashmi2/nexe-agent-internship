# 🛠️ Tool-Calling AI Agent

A beginner-friendly AI agent project built using **Gemini 2.5 Flash** and **OpenAI Agents SDK** concepts.

This project demonstrates how an AI agent can perform mathematical reasoning through tool/function calling instead of solving calculations directly.

---

## 🚀 Features 

- 🔧 Tool / function calling
- 🧠 Multi-step mathematical reasoning
- 📦 Structured JSON responses
- ⚠️ Graceful error handling
- 🤖 Agent-based architecture

---

## 🏗️ Project Structure

```text
tool-calling-ai-agent/
│
├── src/
│   ├── main.py
│   │
│   ├── my_tools/
│   │   └── my_tools.py
│   │
│   ├── my_agent/
│   │   └── teacher_agent.py
│   │
│   └── my_config/
│       └── gemini_config.py
│
├── .env
└── README.md
```

---

## ⚙️ How It Works

### 1. User Input
User enters a math query like:

Add 6 and 6 then multiply by 2


---

### 2. Agent Processing
The AI agent:
- Understands the request
- Selects the appropriate tools
- Performs calculations step-by-step
- Returns a structured response

---

### 3. Structured Output
The agent always responds in JSON format:

{
  "response": "24"
}

---

### 🧪 Example Usage
## Input

Add 6 and 6 then multiply by 2

## Output

{
  "response": "24"
}

--- 

### 🧰 Tools Used

- Plus Tool ➕
- Subtract Tool ➖
- Multiply Tool ✖
- Divide Tool ➗

All calculations are performed via tools — not directly by the model.

---

### 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/bismahashmi2/nexe-agent-internship.git

cd beginner
cd tool-calling-ai-agent
```

### Install Dependencies

- uv init
- uv venv .venv
- uv add openai-agents
- uv add python-decouple

### Run the Project
activate virtual environment by "source .venv/bin/activate"
uv run python src/main.py

---

### 📌 Requirements

- Python 3.10+
- OpenAI / Gemini model support via Agents SDK
- agents library
- uv package manager

---

### 🎯 Key Concepts

This project demonstrates:

- Agentic AI workflow design
- Tool-calling AI agent architecture
- Function execution through LLMs
- Structured JSON output enforcement

---

### ⚠️ Notes

- The agent is designed specifically for mathematical tasks
- Responses are returned in JSON format only
- Invalid or unsupported requests are handled gracefully

---

### 👨‍💻 Author

Built as part of an Agentic AI Internship Task
Focused on learning:

- Tool-calling reasoning in AI agents
- Agent workflows
- Structured AI outputs



