from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

knowledge = [
    {
        "role": "system",
        "content": "You are an standup comedy that uses black humour",
    },
]

message = {"role": "user", "content": "make a joke about evo morales and coca"}
knowledge.append(message)
response = client.chat.completions.create(model="gpt-3.5-turbo", messages=knowledge)
chat_message= response.choices[0].message.content
print(f"Standup comedian: {chat_message}")
