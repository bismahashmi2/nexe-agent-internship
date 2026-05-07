# Tool-Calling AI Agent

A beginner AI agent project built using Gemini and OpenAI Agents SDK concepts.


The agent can:

- perform mathematical operations using tools

- return structured JSON responses

- handle invalid or unsupported responses gracefully



---



## Features



- Function / tool calling

- JSON-based responses

- Error handling

- Multi-step mathematical reasoning



---



## Tools Used



- Python

- Gemini 2.5 Flash

- OpenAI Agents SDK

- UV package manager



## Example Query



```bash

Add 6 and 6 then multiply by 2



## Example Output



{

&#x20;   "response": "24"

}



## Project Structure



src/

│

├── main.py

├── my\_tool/

│   └── my\_tools.py

├── my\_agent/

│   └── teacher\_agent.py

├── my\_config/

│   └── gemini\_config.py





## Setup



# Install Dependencies

uv sync



# Run the Project

uv run python src/main.py



# Environment Variables



Create a .env file:



GEMINI_API_KEY=your_api_key_here

