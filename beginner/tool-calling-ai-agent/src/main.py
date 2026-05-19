import json
import re
from agents import Runner, enable_verbose_stdout_logging
from my_agent.teacher_agent import math_agent



# enable_verbose_stdout_logging()

def clean_output(data):
    try:
        if isinstance(data, str):
            data = re.sub(r"```json|```", "", data).strip()

            # remove accidental leading pipes
            data = data.lstrip("|").strip()

            # Try to extract JSON from the string
            return json.loads(data)

        elif isinstance(data, dict):
         return data

        else:
         return {"error": "Unexpected output format", "raw": str(data)} 

    except json.JSONDecodeError:
     return {
        "error": "Model did not return valid JSON",
        "raw": data if data else "Empty response"
     }     

user_input = input("Enter your query: ")

response = Runner.run_sync(starting_agent=math_agent, input=user_input)
print(json.dumps(clean_output(response.final_output), indent=4))



