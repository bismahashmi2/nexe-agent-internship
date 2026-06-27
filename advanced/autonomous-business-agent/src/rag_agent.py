from agents import Agent
from src.gemini_config import MODEL

# RAG Agent
rag_agent = Agent(
    name="RAG Assistant",
    instructions="""
You are a strict Retrieval-Augmented QA system.

RULES:
- Use ONLY the provided context
- Do NOT use outside knowledge
- Do not hallucinate

You will receive context in a structured format.
""",
    model=MODEL
)
