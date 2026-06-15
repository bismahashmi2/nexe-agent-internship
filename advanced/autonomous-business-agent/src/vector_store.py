from pathlib import Path
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

def store_in_chroma(chunks, embeddings):
    # Delete existing collection if it exists and create new one
    try:
        client.delete_collection(name="rag_collection")
        print("🗑️ Cleared existing collection")
    except:
        pass

    collection = client.create_collection(
        name="rag_collection"
    )

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding.tolist()]
        )

    print("✅ Data stored in ChromaDB successfully!")