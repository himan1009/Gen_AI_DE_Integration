import os 
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only answer in maths related questions, if the query is not related to maths just say sorry, I am unable to do so, and do not answer this."},
        {"role": "user", "content": "Hey There!, can you help me to solve a squared plus b squared."}
    ]
)

print(response.choices[0].message.content)

