# 🤖 Multi-Agent System (Task Delegation & Agent Communication)

A simple **Multi-Agent AI System** where multiple agents collaborate to solve a task through an orchestrator.

Built using:

* 🤖 Multiple AI Agents
* 📬 Message Passing
* 🎯 Task Delegation
* ⚡ Python

---

## 🚀 Features

* 🤖 Multiple specialized agents
* 📬 Communication Layer using MessageBus
* 🎯 Task delegation through orchestrator
* 🧠 Context retrieval agent
* ✍️ Content generation agent
* ⚡ Modular architecture
* 🔄 Extensible for additional agents

---

## 🏗️ Project Structure

```text
multi-agent-system/
│
├── src/
│   ├── orchestrator.py
│   ├── message_bus.py
│   ├── main.py
│   ├── gemini_config.py
│   │
│   └── agents/
│       ├── retriever_agent.py
│       ├── writer_agent.py
│       └── __init__.py
│
├── .gitignore
├── pyproject.toml
└── README.md
```

---

## ⚙️ How It Works

### 1. User Sends Request

The user provides a task through the CLI.

### 2. Orchestrator Creates Plan

The orchestrator decides which agent should handle each part of the task.

### 3. Communication Layer

The MessageBus transfers messages between agents.

### 4. Retriever Agent Executes

The Retriever Agent processes the request and gathers relevant information.

### 5. Task Delegation

The orchestrator forwards the retrieved context to the Writer Agent.

### 6. Writer Agent Executes

The Writer Agent generates the final response.

### 7. Final Response

The orchestrator returns the completed result back to the user.

---

## 🧠 Architecture Flow

```text
User
 ↓
Orchestrator
 ↓
MessageBus
 ↓
Retriever Agent
 ↓
Retrieved Context
 ↓
MessageBus
 ↓
Writer Agent
 ↓
Final Answer
```

---

## 🧪 Example Workflow

### User Request

```text
Write a short explanation of Agentic AI.
```

### Internal Flow

```text
User
 ↓
MessageBus
 ↓
Retriever Agent
 ↓
Collect Context
 ↓
Writer Agent
 ↓
Generate Response
```

### Output

```text
Agentic AI refers to AI systems capable of planning,
reasoning, and taking actions autonomously to achieve goals.
```

---

## 🧰 Technologies Used

* ⚡ Python
* 🤖 Multi-Agent Architecture
* 📬 Message Passing
* 🎯 Task Delegation
* 🔄 Orchestration Layer
* 📬 Message Bus Pattern

---

## 📦 Installation

### Clone Repository

```bash
git clone https://github.com/bismahashmi2/nexe-agent-internship.git

cd advanced

cd multi-agent-system
```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv add openai-agents python-decouple
```

---

## ▶️ Run Project

```bash
python src/main.py
```

---

## 📌 Requirements

* Python 3.10+
* UV Package Manager
* OpenAI Agents SDK
* Gemini / OpenAI API Key

---

## 🎯 Key Concepts

This project demonstrates:

* Multi-Agent Systems
* Agent Communication
* Task Delegation
* Orchestration
* Message Passing
* Modular Agent Design
* Communication Layer
* Message Bus Pattern
---

## ⚠️ Notes

* Orchestrator controls workflow.
* Agents perform specialized tasks.
* New agents can be added easily.
* Message objects are passed between agents.

---

## 👨‍💻 Author

Built as part of an Agentic AI Internship Task.

Focused on learning:

* Multi-Agent Systems
* Agent Collaboration
* Task Delegation
* Message Passing
* Orchestration Patterns
* Agent Workflows

---


