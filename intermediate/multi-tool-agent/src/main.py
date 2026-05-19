import json
import re
from agents import Runner
from my_agent.multi_tool_agent import multi_tool_agent


def clean_output(data):
    try:
        if not data:
            return {"error": "Empty response from model", "raw": data}

        if isinstance(data, dict):
            return data

        if isinstance(data, str):
            data = data.strip()

            if not data:
                return {"error": "Empty string response", "raw": data}

            data = re.sub(r"```json|```", "", data).strip()

            try:
                return json.loads(data)
            except json.JSONDecodeError:
                return {"response": data}

        return {"error": "Unexpected format", "raw": str(data)}

    except Exception as e:
        return {"error": str(e), "raw": str(data)}


user_input = input("Enter your query: ")
  

# RUN AGENT (ONLY STRING INPUT)
response = Runner.run_sync(
    starting_agent=multi_tool_agent,
    input=user_input
)

# Get output
raw_output = getattr(response, "final_output", None)

# Retry if error or empty response
if not raw_output:
    response = Runner.run_sync(
        starting_agent=multi_tool_agent,
        input=user_input + "\nIMPORTANT: Return a valid response."
    )

    raw_output = getattr(response, "final_output", None)

# Clean Output
cleaned_response = clean_output(raw_output)

# Print cleaned response
print(json.dumps(cleaned_response, indent=4))

