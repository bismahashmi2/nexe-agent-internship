# 🧮 AI Calculator Agent (with Memory + Tools)

An **Agentic AI Calculator** built using tool-calling architecture.  
It supports mathematical operations, remembers previous results across runs, and returns structured JSON outputs.

---

## 🚀 Features

- ➕ Addition, Subtraction, Multiplication, Division
- 🧠 Persistent memory (remembers last result across runs)
- 🔧 Tool-based computation (no direct LLM math)
- 📦 Structured JSON output only
- 🔁 Multi-step chained calculations (e.g., “add 5 to previous result”)

---

## 🏗️ Project Structure

```text
ai-calculator-agent/
│
├── src/
│   ├── main.py
│   │
│   ├── my_tools/
│   │   └── my_tools.py
│   │
│   ├── my_agent/
│   │   └── calculator_agent.py
│   │
│   ├── my_config/
│   │   └── gemini_config.py
│   │
│   └── agent_memory/
│       └── memory.py
│
├── .venv
├── .env
├── memory.json
└── README.md
```

---

## ⚙️ How It Works

### 1. User Input
User enters a math query like:

what is 5 times 8


---

### 2. Agent Processing
- Detects operation
- Calls appropriate tool (Plus / Multiply / Divide / Subtract)
- Uses memory if required

---

### 3. 🧠 Memory System
- Stores last calculation result in `memory.json`
- Loads it on every run
- Enables chained operations like:

add 2 to previous result


---

### 4. Output Format
Always returns:

```json
{
  "response": "42"
}

```

---

###  Memory System

Memory is stored in:

memory.json

Example:

{
  "last_result": "40"
}

This allows the agent to remember results between different executions.

---

### 🧪 Example Usage

### Run 1
Input: what is 5 times 8
Output: 
{
  "response": "40"
}

### Run 2
Input: add 2 to the previous result
Output: 
{
  "response": "42"
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

git clone <https://github.com/bismahashmi2/nexe-agent-internship.git>
cd beginner
cd ai-calculator-agent

---

### Install Dependencies

- uv init
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
- Tool-based mathematical reasoning
- Function execution through LLMs
- Persistent memory handling
- Structured JSON output enforcement
- Context-aware chained calculations
- Multi-step mathematical reasoning


---

### ⚠️ Notes
- Memory resets if `memory.json` is deleted
- Only mathematical queries are supported
- Non-math queries are rejected by design

---

### 👨‍💻 Author

Built as part of an Agentic AI Internship Task

Focused on learning:

- Tool-based reasoning in AI agents
- Persistent memory systems
- Structured AI outputs
- Stateful agent workflows