# zero shot prompt for a simple task

import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# zero shot prompting: Directly giving the instruction to model
SYSTEM_PROMPT = "you should only and only answer the coding related questions, do not answer anything else, your name is Alexa. If user asks something other than coding, Say Sorry"


response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": "Hey There!, write code for binary serach algorithm."}
    ]
)

print(response.choices[0].message.content)

