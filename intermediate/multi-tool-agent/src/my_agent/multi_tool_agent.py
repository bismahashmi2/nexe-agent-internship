from agents import Agent, ModelSettings

from my_config.gemini_config import MODEL
from my_tools.send_email import send_email
from my_tools.web_search import web_search
from my_tools.save_db import save_search_query


multi_tool_agent = Agent(
    name="Multi-Tool Agent",

    instructions="""
You are a strict Multi-Tool Agent.
- Use tools whenever needed.

AVAILABLE TOOLS:
- web_search
- send_email
- save_search_query

- Return ONLY valid JSON.

- For tool responses:
return the tool output exactly.

- Do not summarize.
- Do not explain.
- Do not rewrite.

""",

    model=MODEL,

    tools=[
        web_search,
        send_email,
        save_search_query
    ],

    model_settings=ModelSettings(
        tool_choice="auto",
        temperature=0
    )
)