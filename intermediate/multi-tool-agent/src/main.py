import json
import re
from agents import Runner
from my_agent.multi_tool_agent import multi_tool_agent


def clean_output(data):

    try:

        if not data:
            return {
                "error": "Empty response from model"
            }

        # Already JSON/dict
        if isinstance(data, dict):
            return data

        # String response
        if isinstance(data, str):

            data = data.strip()

            # Remove markdown wrappers if model adds them
            data = re.sub(r"```json|```", "", data).strip()

            try:
                return json.loads(data)

            except json.JSONDecodeError:

                # fallback safely
                return {
                    "response": data
                }

        return {
            "error": "Unexpected response format",
            "raw": str(data)
        }

    except Exception as e:

        return {
            "error": str(e)
        }


# USER INPUT
user_input = input("Enter your query: ")


# RUN AGENT
response = Runner.run_sync(
    starting_agent=multi_tool_agent,
    input=user_input
)


# GET FINAL OUTPUT
raw_output = getattr(response, "final_output", None)


# SIMPLE RETRY
if not raw_output:

    response = Runner.run_sync(
        starting_agent=multi_tool_agent,
        input=user_input + "\nIMPORTANT: Return only valid JSON."
    )

    raw_output = getattr(response, "final_output", None)


# CLEAN OUTPUT
cleaned_response = clean_output(raw_output)


# PRINT FINAL RESPONSE
print(json.dumps(cleaned_response, indent=4))


