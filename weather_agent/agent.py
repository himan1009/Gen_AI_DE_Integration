from pydantic import BaseModel
from typing import Optional, Literal
import requests


SYSTEM_PROMPT = """
You are an intelligent AI Weather Agent.

You operate in following steps:
1. PLAN
2. ACTION
3. OUTPUT

Rules:
- Strictly return structured output.
- Only one step at a time.
- Think step by step.
- If weather information is required, use ACTION step.
- ACTION step must contain:
    - function name
    - input city

Example Flow:

PLAN -> Understand user query
ACTION -> Call get_weather
OUTPUT -> Return final answer
"""


# Structured Output Model
class AgentResponse(BaseModel):

    step: Literal["PLAN", "ACTION", "OUTPUT"]

    content: str

    function: Optional[str] = None

    input: Optional[str] = None


# Tool Function
def get_weather(city: str):

    url = f"https://wttr.in/{city.lower()}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"

    return "Something went wrong while fetching weather."