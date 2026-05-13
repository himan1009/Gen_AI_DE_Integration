# main.py

import os

from openai import OpenAI
from dotenv import load_dotenv

from agent import (
    SYSTEM_PROMPT,
    AgentResponse,
    get_weather,
    run_cmd
)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


def main():

    user_query = input("> ")

    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

    while True:

        response = client.beta.chat.completions.parse(
            model="gemini-2.5-flash",
            messages=message_history,
            response_format=AgentResponse
        )

        parsed_response = response.choices[0].message.parsed

        # PLAN
        if parsed_response.step == "PLAN":

            print("\nPLAN:", parsed_response.content)

            message_history.append({
                "role": "assistant",
                "content": parsed_response.model_dump_json()
            })

            message_history.append({
                "role": "user",
                "content": "Proceed to next step."
            })

            continue

        # ACTION
        elif parsed_response.step == "ACTION":

            print(
                f"\nACTION: "
                f"{parsed_response.function}"
                f"({parsed_response.input})"
            )

            tool_result = ""

            # Weather Tool
            if parsed_response.function == "get_weather":

                tool_result = get_weather(parsed_response.input)

            # CMD Tool
            elif parsed_response.function == "run_cmd":

                tool_result = run_cmd(parsed_response.input)

            print("\nOBSERVATION:", tool_result)

            message_history.append({
                "role": "assistant",
                "content": parsed_response.model_dump_json()
            })

            message_history.append({
                "role": "user",
                "content": f"OBSERVATION: {tool_result}"
            })

            continue

        # OUTPUT
        elif parsed_response.step == "OUTPUT":

            print("\nFINAL ANSWER:")
            print(parsed_response.content)

            break

        else:

            print("Unknown step")
            break


if __name__ == "__main__":
    main()