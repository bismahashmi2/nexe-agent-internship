from agents import Agent, ModelSettings
from my_config.gemini_config import MODEL 
from my_tool.my_tools import Plus, Multiply, Divide, Subtract

math_agent = Agent (
    name="Math Teacher", 
    instructions="""
    You are a math agent.
    Always use the tools provided to you to solve the problem. Do not solve the problem by yourself without using the tools.
    If the question is not related to math, politely refuse to answer.
    Return responses in json format only.
    After calling tools, ALWAYS return valid JSON with the following format:
    {
        "response": "the final answer to the question",
    }
    Do not return markdown.
    Do not return plain text.
    Return ONLY valid JSON.
    """,
    model=MODEL,
    tools=[Plus, Multiply, Divide, Subtract],
    model_settings=ModelSettings(tool_choice="required")
    )


