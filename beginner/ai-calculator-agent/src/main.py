import json
import re
from agents import Runner
from my_agent.calculator_agent import calculator_agent
from agent_memory.memory import load_memory, save_memory


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
            except:
                return {"response": data}

        return {"error": "Unexpected format", "raw": str(data)}

    except Exception as e:
        return {"error": str(e), "raw": str(data)}

user_input = input("Enter your query: ")

# Load memory
memory = load_memory()
memory_value = memory["last_result"]

memory_text = ""

if memory_value is not None:
    memory_text = f"""

MEMORY:
previous_result = {memory_value}

IMPORTANT:
If the user says:
- previous result
- last result
- it
- that number

then use previous_result ({memory_value}) as the number.
"""

# Final input to the agent
final_input = user_input + memory_text    

# RUN AGENT (ONLY STRING INPUT)
response = Runner.run_sync(
    starting_agent=calculator_agent,
    input=final_input
)

# Get output
raw_output = getattr(response, "final_output", None)

# Retry if error or empty response
if not raw_output:
    response = Runner.run_sync(
        starting_agent=calculator_agent,
        input=final_input + "\nIMPORTANT: Use previous numeric result if needed."
    )

    raw_output = getattr(response, "final_output", None)

# Clean Output
cleaned_response = clean_output(raw_output)

# Print cleaned response
print(json.dumps(cleaned_response, indent=4))

# update memory safely
memory["last_result"] = cleaned_response.get("response")
save_memory(memory)