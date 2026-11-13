from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Suggest three tasks for someone learning Python this week. One line each.",
)

usage = response.usage_metadata

print(response.text)
print(usage)

thoughts = usage.thoughts_token_count or 0
cost = usage.prompt_token_count * 0.30 / 1000000 + (usage.candidates_token_count + thoughts) * 2.50 / 1000000
print(f"Cost: ${cost:.6f}")
print(f"Calls to reach $1.00: {1.00 / cost:.0f}")