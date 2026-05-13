# agent.py

from pydantic import BaseModel
from typing import Optional, Literal
import requests
import os


SYSTEM_PROMPT = """
You are an intelligent AI Agent.

You operate in following steps:
1. PLAN
2. ACTION
3. OUTPUT

Rules:
- Strictly return structured output.
- Only one step at a time.
- Think step by step.
- If weather information is required, use ACTION step.
- If command execution is required, use ACTION step.

Available Functions:

1. get_weather
2. run_cmd

For ACTION step use:

{
    "step": "ACTION",
    "content": "Executing function",
    "function": "function_name",
    "input": "function_input"
}

Example:

User: What's weather in Goa?

PLAN -> User wants weather
ACTION -> get_weather Goa
OUTPUT -> Final answer


User: Create a folder named test

PLAN -> User wants system command execution
ACTION -> run_cmd mkdir test
OUTPUT -> Folder created successfully
"""


# Structured Output
class AgentResponse(BaseModel):

    step: Literal["PLAN", "ACTION", "OUTPUT"]

    content: str

    function: Optional[str] = None

    input: Optional[str] = None


# Weather Tool
def get_weather(city: str):

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong while fetching weather."


# Command Execution Tool
def run_cmd(command: str):

    try:

        result = os.popen(command).read()

        if result.strip() == "":
            return "Command executed successfully."

        return result

    except Exception as e:

        return str(e)