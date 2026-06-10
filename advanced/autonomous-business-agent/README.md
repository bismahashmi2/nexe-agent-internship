# 🤖 Autonomous Business Agent (AI Execution System)

An **AI-powered autonomous agent system** that performs multi-step reasoning, task planning, and execution logging while answering user business questions using a Retrieval-Augmented Generation (RAG) pipeline.

The system simulates a real AI worker that can think, plan, retrieve knowledge, and generate structured responses using an LLM.

Built using:
- 🧠 SentenceTransformers (Embeddings)
- 🗄️ ChromaDB (Vector Database)
- 📄 PyPDF (Document Processing)
- 🤖 OpenAI Agents SDK (Response Layer)
- ⚡ Python + UV

---

## 🚀 Features

- 🧠 Multi-step reasoning (Think → Retrieve → Answer pipeline)
- 📋 Task planning system for structured execution
- 📜 Execution logs with timestamps
- 🔍 Semantic retrieval using ChromaDB
- 📄 PDF-based knowledge base (RAG integration)
- 🤖 LLM-powered response generation (Gemini / OpenAI Agents SDK)
- ⚡ CLI-based interactive agent system
- 🧩 Modular agent architecture
- 🌐 **Modern Web UI** with real-time chat interface and execution logs
- 🚀 **FastAPI Backend** for seamless frontend-agent integration

---

## 🏗️ Project Structure

```text
autonomous-business-agent/
│
├── data/
│   └── ai_dev.pdf
│
├── chroma_db/
│
├── src/
│   ├── read_pdf.py
│   ├── chunk_text.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieve.py
│   ├── rag_agent.py
│   ├── rag_tool.py   ← (optional abstraction layer)
│   ├── main.py
│   ├── autonomous_agent.py
│   └── gemini_config.py
│
├── web-ui/                    ← NEW: Web Interface
│   ├── app/
│   │   ├── page.tsx          ← Main chat interface
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── components/
│   │   ├── ChatInterface.tsx  ← Chat UI component
│   │   └── ExecutionLogs.tsx  ← Real-time logs
│   ├── api/
│   │   ├── main.py           ← FastAPI backend
│   │   └── requirements.txt
│   ├── start.sh              ← Linux/Mac startup script
│   ├── start.bat             ← Windows startup script
│   └── README.md
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

```text
"We implemented a tool abstraction layer (rag_tool.py) to decouple retrieval logic from agent reasoning, enabling modular expansion into multi-agent systems."
```

---


## ⚙️ How It Works


### 1. User Input

The user enters a business-related query in the CLI.

### 2. Agent Planning

The agent creates a structured plan:

- Understand query
- Retrieve relevant context
- Generate final answer

### 3. Retrieval (RAG System)

The query is converted into embeddings and matched with stored vectors in ChromaDB.

### 4. Context Injection

Relevant chunks from the document are retrieved and passed to the agent.

### 5. Execution (LLM Reasoning)

The agent uses an LLM to generate a final answer based on:

- user question
- retrieved context
- system instructions

### 6. Execution Logs

Every step is logged with timestamps:

- planning stage
- retrieval stage
- execution stage
- completion stage

---

### 🧪 Example Usage

#### Input:
```bash 

What is AI Native Development?
```
#### Output:
```bash

📌 FINAL ANSWER:
AI Native Development refers to systems where AI is integrated into core design...

 📜EXECUTION LOGS:
[15:25:00] Agent started
[15:25:00] Creating plan...
[15:25:00] Plan: ['Understand question', 'Retrieve relevant context from vector DB', 'Generate final answer']
[15:25:00] Retrieving from RAG system...
[15:25:00] Context retrieved
[15:25:00] Generating AI response...
[15:25:15] Answer generated
[15:25:15] Agent finished

```

--- 

### 🧰 Technologies Used

- 🧠 SentenceTransformers (Embeddings)
- 🗄️ ChromaDB (Vector Database)
- 📄 PyPDF (Document Processing)
- 🤖 OpenAI Agents SDK
- ⚡ Python
- 📦 UV Package Manager
- 🌐 Next.js 14 (Web UI)
- 🚀 FastAPI (Backend API)
- 🎨 Tailwind CSS (Styling)
- ⚛️ React 18 (Frontend Framework)


---

### 🧠 Architecture Flow

```text
User Input
↓
Agent Planning
↓
Query Embedding
↓
Vector Search (ChromaDB)
↓
Context Retrieval
↓
LLM Reasoning
↓
Final Answer
↓
Execution Logs
```
---

### 📦 Installation

### Clone the Repository

```bash

git clone https://github.com/bismahashmi2/nexe-agent-internship.git


cd advanced

cd autonomous-business-agent

```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate

```

### Install Dependencies
#### Core project dependencies (safe + lightweight)

```bash
uv add pypdf chromadb openai openai-agents python-decouple
```
#### ML / RAG dependencies (installed manually for stability)

```bash
# CPU-only PyTorch (prevents CUDA installation)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu

# Sentence transformer model
uv pip install sentence-transformers

# Required transformer ecosystem (manual control to avoid conflicts)
uv pip install transformers tokenizers safetensors huggingface-hub

# Scientific libraries
python -m pip install scikit-learn scipy numpy

```

#### Web UI Dependencies (Optional)

```bash
# Install FastAPI dependencies
pip install fastapi uvicorn pydantic python-multipart

# Install frontend dependencies
cd web-ui
npm install
cd ..
```

### Run the Project

#### Option 1: CLI Mode (Original)

```bash
python -m src.main

```

#### Option 2: Web UI Mode (New)

```bash
# Linux/Mac
cd web-ui
./start.sh

# Windows
cd web-ui
start.bat
```

The web interface will be available at:
- Frontend: `http://localhost:3002`
- Backend API: `http://localhost:8000`

---


### 📌 Requirements

- Python 3.10+

- OpenAI / Gemini model support via Agents SDK

- Openai

- uv package manager

- Torch (CPU version supported)

- ChromaDB

- SentenceTransformers 

- PyPDF

---

### 🎯 Key Concepts

This project demonstrates:

- Autonomous AI agent design
- Multi-step reasoning
- Task planning systems
- Execution logging
- Retrieval-Augmented Generation (RAG)
- Vector database search
- Context-aware LLM reasoning
- Modular AI architecture


---

### ⚠️ Notes

- PDF used: ai_dev.pdf

- ChromaDB stores data locally in chroma_db/

- Embeddings are generated using all-MiniLM-L6-v2

- Embedding model downloads once from HuggingFace

- System is fully local except LLM inference

- Designed as a lightweight autonomous agent framework


---


### 👨‍💻 Author

Built as part of an Agentic AI Internship Task.

Focused on learning:

- Autonomous agent design
- Multi-step reasoning systems
- RAG pipelines
- Execution tracking systems
- AI workflow orchestration

---

### 🏁 Final Summary

This project represents a transition from a simple RAG system to an Autonomous Business Agent capable of:

```text
| thinking → planning → retrieving → reasoning → executing → logging
```

**Two Interaction Modes:**

1. **CLI Mode**: Traditional command-line interface for direct agent interaction
2. **Web UI Mode**: Modern web interface with:
   - Real-time chat interface
   - Live execution logs
   - Beautiful gradient UI
   - FastAPI backend integration
   - Responsive design

Access the web interface at `http://localhost:3002` after running the startup script.