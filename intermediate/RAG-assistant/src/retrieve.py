import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="rag_collection"
)

# User question
query = input("Enter your query: ")

# Convert question into embedding
query_embedding = model.encode(query)

# Search in ChromaDB
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)

# Print results
print("\nTop Results:\n")

for i, doc in enumerate(results["documents"][0]):
    print(f"Result {i+1}:")
    print(doc)
    print("-" * 50)