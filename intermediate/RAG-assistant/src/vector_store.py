import chromadb
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read PDF
pdf_path = "data/ai_dev.pdf"

reader = PdfReader(pdf_path)

full_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        full_text += text + "\n"

# Chunking
CHUNK_SIZE = 500

chunks = []

for i in range(0, len(full_text), CHUNK_SIZE):
    chunk = full_text[i : i + CHUNK_SIZE]
    chunks.append(chunk)

print(f"Total chunks: {len(chunks)}")
print()

# Create embeddings
embeddings = model.encode(chunks)

print("Embeddings created successfully!")
print()

# Create Chroma client
client = chromadb.PersistentClient(path="chroma_db")

# Create collection
collection = client.get_or_create_collection(
    name="rag_collection"
)

# Store data
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embeddings[i].tolist()]
    )

print("Data stored in ChromaDB successfully!")

