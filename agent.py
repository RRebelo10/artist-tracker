import time
from dotenv import load_dotenv
from datetime import date
from google import genai
from google.genai import types
from watchlist import load_watchlist
from search_tool import search_web
from extract_event import Event
from seen import load_seen, save_seen, make_key
from notify import send_email, format_events

load_dotenv()
client = genai.Client()
MODEL = "gemini-3.5-flash-lite"

def find_events(artist: dict, locations: list[str]) -> str:
    prompt = (
        f"Today is {date.today()}. Find upcoming events by {artist['name']} "
        f"({artist['type']}) in: {', '.join(locations)}. "
        "Use the search tool. Only include events after today. "
        "Reply with a short plain list."
    )
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(tools=[search_web]),
    )
    return response.text

def extract_events(text: str, artist_name: str) -> list[Event]:
    response = client.models.generate_content(
        model=MODEL,
        contents=(
            f"Extract every event for {artist_name} from this text. "
            "The artist field is the performer's name; the title field is the "
            "name of the play, show or tour. "
            "If there are none, return an empty list:\n\n"
            f"{text}"
        ),
        config={
            "response_mime_type": "application/json",
            "response_schema": list[Event],
        },
    )
    return response.parsed

if __name__ == "__main__":
    data = load_watchlist()
    today = date.today().isoformat()
    seen = load_seen()
    new_events = []

    for artist in data["artists"]:
        locations = artist.get("locations", data["default_locations"])
        print(f"\n== {artist['name']} ==")
        try:
            text = find_events(artist, locations)
            events = extract_events(text, artist["name"])
        except Exception as e:
            print(f"Skipped ({type(e).__name__}): {e}")
            time.sleep(60)
            continue

        for event in events:
            if event.date is not None and event.date < today:
                continue
            key = make_key(artist["name"], event)
            if key in seen:
                continue
            seen.add(key)
            new_events.append(event)
            print("NEW:", event)
        time.sleep(10)

    if new_events:
        send_email(f"{len(new_events)} new events", format_events(new_events))
        save_seen(seen)
    print(f"\n{len(new_events)} new events")