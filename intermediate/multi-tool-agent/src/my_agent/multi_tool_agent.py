from agents import Agent, ModelSettings

from my_config.gemini_config import MODEL
from my_tools.send_email import send_email
from my_tools.web_search import web_search
from my_tools.save_db import save_search_query


multi_tool_agent = Agent(
    name="Multi-Tool Agent",

    instructions="""
You are a Multi-Tool Agent.

AVAILABLE TOOLS:
- web_search → search the internet
- send_email → send emails
- save_search_query → save queries to database

RULES:
1. Use tools whenever needed.
2. Never make up information.
3. Use actual tool outputs only.
4. For web searches:
   - include titles
   - include links
   - include snippets
5. For emails:
   - clearly confirm success/failure
6. For database saves:
   - clearly confirm saved query

OUTPUT RULES:
- Return ONLY valid JSON
- Never return markdown
- Never expose tool code
- Never expose execution traces

FORMAT:
{
  "tool_used": "<tool_name>",
  "response": <tool_result>
}
""",

    model=MODEL,

    tools=[
        send_email,
        web_search,
        save_search_query
    ],

    model_settings=ModelSettings(
        tool_choice="auto",
        temperature=0
    )
)