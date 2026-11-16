import json

def load_watchlist(path="artists.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    data = load_watchlist()
    print("Default locations:", data["default_locations"])
    for artist in data["artists"]:
        locations = artist.get("locations", data["default_locations"])
        print("-", artist["name"], f"({artist['type']})", "->", locations)