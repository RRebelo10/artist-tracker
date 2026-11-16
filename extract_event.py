from dotenv import load_dotenv
from pydantic import BaseModel, Field
from google import genai

load_dotenv()
client = genai.Client()

class Event(BaseModel):
    artist: str
    date: str | None = Field(description="Format YYYY-MM-DD")
    city: str | None
    venue: str | None

def extract_event(text: str) -> Event:
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=f"Extract the event from this announcement: \n\n{text}",
        config={
            "response_mime_type": "application/json",
            "response_schema": Event,
        }
    )
    return response.parsed

if __name__ == "__main__":
    text = "OMG !! Gator is coming to Lisbon on 12 March 2027 at Coliseu dos Recreios, tickets Friday!"
    event = extract_event(text)
    print(event)
    print(event.city)