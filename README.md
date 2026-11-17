# Artist Tracker

An AI agent that follows my favourite artists (bands, comedians) and emails me
when new events are announced in my locations.

## How it works
1. `artists.json` lists the artists and locations.
2. A Gemini model searches the web (`search_tool.py`) for upcoming events.
3. A second model call extracts them into structured data (`extract_event.py`).
4. `seen_events.json` remembers old events, so only new ones are emailed.
5. Windows Task Scheduler runs `run_agent.bat` every time the computer is turned on.

## Setup
1. `uv sync`
2. Create `.env` with `GEMINI_API_KEY`, `GMAIL_ADDRESS`, `GMAIL_APP_PASSWORD`
3. Edit `artists.json`
4. `uv run agent.py`