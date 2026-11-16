import json
from pathlib import Path

SEEN_FILE = Path("seen_events.json")

def load_seen() -> set[str]:
    if not SEEN_FILE.exists() or SEEN_FILE.stat().st_size == 0:
        return set()
    with open(SEEN_FILE, encoding="utf-8") as f:
        return set(json.load(f))

def save_seen(seen: set[str]) -> None:
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(sorted(seen), f, indent=2, ensure_ascii=False)

def make_key(artist_name: str, event) -> str:
    return f"{artist_name}|{event.date}".lower()

if __name__ == "__main__":
    seen = load_seen()
    print("Loaded:", len(seen))
    seen.add("test|2099-01-01")
    save_seen(seen)
    print("Saved:", len(seen))