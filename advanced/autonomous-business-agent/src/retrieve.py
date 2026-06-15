from pathlib import Path
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_PATH = BASE_DIR / "chroma_db"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

# collection = client.get_or_create_collection(name="rag_collection")


def query_engine(query: str):

    collection = client.get_collection(name="rag_collection")

    query_embedding = model.encode(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=5
    )

    return results["documents"][0]