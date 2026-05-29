import chromadb

def store_in_chroma(chunks, embeddings):
    client = chromadb.PersistentClient(path="chroma_db")

    collection = client.get_or_create_collection(
        name="rag_collection"
    )

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embedding.tolist()]
        )

    print("✅ Data stored in ChromaDB successfully!")