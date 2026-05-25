A rag assistant:
PDF → split into chunks → convert chunks to embeddings →
store in vector DB → user asks question →
find similar chunks → give chunks to LLM → answer


rag-assistant/
│
├── data/
│   └── ai_native.pdf
│
├── chroma_db/
│
├── src/
│   ├── read_pdf.py      // Extract text from PDF
│   ├── chunk_text.py    // Split long text into chunks
│   ├── embeddings.py    // Convert chunks → embeddings
│   ├── vector_store.py  // Store chunks in DB
│   ├── retrieve.py      // Ask question → retrieve relevant chunks
│   └── main.py          // User asks → AI answers using retrieved context
│
├── test_embeddings.py
├── test_chroma.py
│
├── .env
├── pyproject.toml
└── README.md

Mental Model:
PDF
↓
Chunks
↓
Embeddings
↓
Vector DB
↓
Semantic Search
↓
Relevant Context
↓
LLM Answer

Goal of vector_store.py

This file will:

1. Create embeddings
2. Create ChromaDB collection
3. Store:
   - chunks
   - embeddings

So later we can retrieve relevant knowledge.

Chroma stores:

ID
+
TEXT
+
VECTOR

Example:

{
   id: "0",
   document: "Agentic AI is...",
   embedding: [0.22, -0.91, ...]
}