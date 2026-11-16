from ddgs import DDGS

def search_web(query: str) -> list[dict]:
    """Searches the web and returns the top results (title, snippet, link). Use it to find upcoming concerts or shows."""
    print(f"[searching: {query}]")
    results = DDGS().text(query, region="pt-pt", max_results=8)
    return [
        {"title": r["title"], "snippet": r["body"], "link": r["href"]}
        for r in results
    ]

if __name__ == "__main__":
    for r in search_web("Gator concerto Lisboa 2027"):
        print(r["title"], "-", r["link"])
