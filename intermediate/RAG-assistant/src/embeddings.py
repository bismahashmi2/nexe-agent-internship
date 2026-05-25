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

print("Shape of embeddings:")
print(embeddings.shape)

print()

print("First embedding:")
print(embeddings[0][:10])