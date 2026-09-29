import os
from dotenv import load_dotenv
from ollama import chat

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "qwen3:4b")
TEMPERATURE = float(os.getenv("OLLAMA_TEMPERATURE", "0.6"))
# SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "").strip()
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read().strip()

conversation = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

while True:
    message = input("\nIncoming message: ")

    if message.lower() in {"exit", "quit"}:
        break

    conversation.append({
        "role": "user",
        "content": message
    })

    response = chat(
        model=MODEL,
        messages=conversation,
        options={
            "temperature": TEMPERATURE
        }
    )

    reply = response["message"]["content"].strip()

    print("\nSuggested reply:")
    print(reply)

    conversation.append({
        "role": "assistant",
        "content": reply
    })