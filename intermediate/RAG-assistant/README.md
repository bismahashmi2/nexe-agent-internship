# 📚 RAG Assistant (AI Native PDF Q&A System)

A **Retrieval-Augmented Generation (RAG)** system that lets you ask questions from a PDF using embeddings and vector search.

Built using:

- 🧠 SentenceTransformers (Embeddings)
- 🗄️ ChromaDB (Vector Database)
- 📄 PyPDF (Document Processing)
- 🤖 OpenAI Agents SDK (Response Layer)
- ⚡ Python + UV


---


## 🚀 Features 


- 📄 Extract text from PDF
- ✂️ Chunk large documents
- 🧠 Generate embeddings using SentenceTransformer
- 🗄️ Store vectors in ChromaDB
- 🔍 Semantic search over document
- 💬 Interactive Q&A system (CLI-based)
- 🤖 Agent-based response handling (optional)


---


## 🏗️ Project Structure

```text

rag-assistant/
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
│   ├── gemini_config.py
│   └── main.py
│
├── test_embeddings.py
├── test_chroma.py
│
├── .env
├── .gitignore
├── pyproject.toml
└── README.md

```

---


## ⚙️ How It Works


### 1. Loads PDF

Extracts text from the document using PyPDF.

### 2. Chunking

Split text into smaller chunks for embedding generation.

### 3. Embeddings

Convert chunks into vector representations using SentenceTransformers.

### 4. Vector Storage

Store embeddings inside ChromaDB for fast similarity search.

### 5. Querying

User question is converted into embedding and compared with stored vectors.

### 6. Retrieval

Top matching chunks are retrieved.

### 7. Answer Generation

Chunks + question are passed to model (or agent) for final answer.

---

### 🧪 Example Usage

#### Ask:
```bash 

What is AI Native Development?
```
#### Agent Answer:
```bash

AI Native Development is an approach where AI is integrated into the core design of systems...
```

--- 


### 🧰 Technologies Used

- 🧠 SentenceTransformers
- 🗄️ ChromaDB
- 📄 PyPDF
- 🤖 OpenAI Agents SDK
- ⚡ Python
- 📦 UV Package Manager


---

### 🧠 Architecture Flow
```text
PDF
↓
Chunks
↓
Embeddings
↓
Vector Database
↓
Semantic Search
↓
Relevant Context
↓
LLM Answer
```
---

### 📦 Installation

### Clone the Repository

```bash

git clone https://github.com/bismahashmi2/nexe-agent-internship.git


cd intermediate

cd RAG-assistant

```

### Install Dependencies

- uv init
- uv venv .venv
- uv add openai
- uv add openai-agents
- uv add python-decouple

## 📦 Installation

### Clone the Repository

```bash
git clone https://github.com/bismahashmi2/nexe-agent-internship.git

cd intermediate
cd RAG-assistant
```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install torch --index-url https://download.pytorch.org/whl/cpu

uv add pypdf openai openai-agents python-decouple

uv pip install sentence-transformers --no-deps

uv add chromadb 

uv pip install transformers huggingface-hub tokenizers safetensors

python -m pip install scikit-learn scipy numpy

```

### Run the Project

```bash
python src/main.py

```

---


### 📌 Requirements

- Python 3.10+

- OpenAI / Gemini model support via Agents SDK

- Openai

- uv package manager and pip

- Torch (CPU version supported)

- ChromaDB

- SentenceTransformers 

- PyPDF

---

### 🎯 Key Concepts

This project demonstrates:

- Agentic AI workflow design

- Embeddings → numerical meaning of text

- Vector Database → stores embeddings for search

- Similarity Search → finds closest meaning chunks

- RAG → Retrieval + Generation system


---

### ⚠️ Notes

- PDF used: ai_dev.pdf

- ChromaDB stores data locally in chroma_db/

- Embeddings are generated using all-MiniLM-L6-v2

- Embedding model downloads once from HuggingFace

- After download, embeddings work locally


---


### 👨‍💻 Author

Built as part of an Agentic AI Internship Task.

Focused on learning:

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Semantic Search
- Vector Databases
- PDF Processing
- ChromaDB
- Agent Workflows
- Context Injection

---

