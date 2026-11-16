from dotenv import load_dotenv
from google import genai
from google.genai import types
from watchlist import load_watchlist

load_dotenv()
client = genai.Client()

def get_artists() -> list[dict]:
    """Returns the artists the user follows, with their type and optional locations."""
    print("[tool called: get_artists]")
    return load_watchlist()["artists"]

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Which comedians am I following?",
    config=types.GenerateContentConfig(tools=[get_artists]),
)
print(response.text)