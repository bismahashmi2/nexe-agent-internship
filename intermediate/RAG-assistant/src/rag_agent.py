from agents import Agent
from gemini_config import MODEL

# RAG Agent
rag_agent = Agent(
    name="RAG Assistant",
    instructions="""
    You are a helpful AI assistant.

    Answer ONLY from the provided context.

    If the answer is not in context, say:
    "I could not find this in the provided document."
    """,
    model=MODEL
)