import chromadb

client = chromadb.Client()

collection = client.create_collection("test_collection")

collection.add(
    documents=["Hello world from RAG"],
    ids=["1"]
)

result = collection.query(
    query_texts=["hello"],
    n_results=1
)

print(result)