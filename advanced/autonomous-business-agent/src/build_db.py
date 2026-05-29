from read_pdf import extract_text
from chunk_text import chunk_text
from embeddings import get_embeddings
from vector_store import store_in_chroma

pdf_path = "data/ai_dev.pdf"

print("📄 Reading PDF...")
text = extract_text(pdf_path)

print("✂ Chunking text...")
chunks = chunk_text(text)

print("🧠 Creating embeddings...")
embeddings = get_embeddings(chunks)

print("💾 Storing in ChromaDB...")
store_in_chroma(chunks, embeddings)

print("✅ DONE: Vector DB is ready!")