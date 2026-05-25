from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
vec = model.encode("Hello RAG system")

print(len(vec), "embedding OK")
print(vec[:5])