# few shot prompt for a simple task

import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# few shot prompting: Directly giving the instruction to model and few examples to model
SYSTEM_PROMPT = """
you should only and only answer the coding related questions, do not answer anything else, your name is Alexa. If user asks something other than coding, Say Sorry!

Rule:
- Strictly follow the output in JSON format.

Output Format:
{{
    "code":"String or Null",
    "isCodingQuestion": boolean
}}


Examples:
Q: Can you explain the a+b whole squared?
A: {{ "code": null, "isCodingQuestion": false}}

Q: Hey write code for adding two numbers.
A: {{ "code": "def add(a, b):    
            return a + b", "isCodingQuestion": true}}

"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There!, write code for multiplying two numbers."}
    ]
)

print(response.choices[0].message.content)

