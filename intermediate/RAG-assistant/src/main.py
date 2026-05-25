import chromadb
from sentence_transformers import SentenceTransformer
from agents import Runner
from rag_agent import rag_agent

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="rag_collection"
)

print("RAG Assistant Ready!")
print()

while True:

    user_question = input("Ask something: ")

    if user_question.lower() == "exit":
        break

    # Convert question into embedding
    question_embedding = model.encode(
        user_question
    ).tolist()

    # Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    retrieved_chunks = results["documents"][0]

    # Combine chunks into context
    context = "\n\n".join(retrieved_chunks)

    # Final prompt
    final_prompt = f"""
Context:
{context}

Question:
{user_question}
"""

    # Run agent
    response = Runner.run_sync(
        starting_agent=rag_agent,
        input=final_prompt
    )

    print()
    print("Answer:")
    print(response.final_output)
    print()