from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

MODEL = "gemini-3.5-flash-lite"
SYSTEM = "You are a task assistant. You help the user organise their to-do list. Keep answers under three sentences."

history = []

while True:
    user_text = input("You: ")
    if user_text == "quit":
        break

    history.append({"role": "user", "parts": [{"text": user_text}]})

    response = client.models.generate_content(
        model=MODEL,
        contents=history,
        config=types.GenerateContentConfig(system_instruction=SYSTEM),
    )

    history.append({"role": "model", "parts": [{"text": response.text}]})

    print("Assistant:", response.text)
    print("Input tokens:", response.usage_metadata.prompt_token_count)