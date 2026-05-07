# Chain-of-thought (CoT) prompting is a technique used to improve the reasoning capabilities of language models by encouraging them to generate intermediate steps or "thoughts" before arriving at a final answer. This approach can help the model break down complex problems into smaller, more manageable parts, leading to more accurate and coherent responses.

import os 
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """
    You are an expert AI assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You needto first PLAN what needs to be done. The PLAN can be in multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.

    RULES:
    - STrictly follow the given JSON output format.
    - Only run one step at a time.
    - The squence of the steps is START (where user gives and input),
    PLAN (That can be multiple times) and OUTPUT ( which is goiing to displayed to the user).


    OUTPUT JSON FORMAT:
    {
        "step": "START" | "PLAN" | "OUTPUT", "content": "String"    
    }

    Example:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: { "step": "PLAN": "content": "Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10" }
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10  = 1.5" }
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5" }
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5" }
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans" }
    OUTPUT: { "step": "OUTPUT": "content": "3.5" }
"""

print("\n\n\n")

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query = input("what ??")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="gemini-3.1-flash-lite-preview",
        response_format={"type": "json_object"},
        messages=message_history,
    )

    raw_result = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": raw_result})
    parsed_result = json.loads(raw_result)

    if isinstance(parsed_result, list):
        parsed_result = parsed_result[0]


    if parsed_result.get("step") == "START":
        print("START: ", parsed_result.get("content"))

        message_history.append({
            "role": "user",
            "content": "Proceed to next PLAN step."
        })

        continue


    if parsed_result.get("step") == "PLAN":
        print("PLAN: ", parsed_result.get("content"))

        message_history.append({
            "role": "user",
            "content": "Proceed to next step or OUTPUT."
        })

        continue

    if parsed_result.get("step") == "OUTPUT":
        print("OUTPUT: ", parsed_result.get("content"))
        break


print("\n\n\n")