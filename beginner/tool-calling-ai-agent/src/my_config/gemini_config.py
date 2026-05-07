from typing import cast
from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel, set_tracing_disabled


set_tracing_disabled(disabled=True)

gemini_api_key = cast(str, config("GEMINI_API_KEY"))
base_url: str = cast(str, config("BASE_URL"))


client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=base_url,
)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash-lite",
    openai_client=client,
)



