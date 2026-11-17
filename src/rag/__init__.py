import argparse
import json
import string
from pathlib import Path


def clean_text(text: str) -> str:
    return text.lower().translate(str.maketrans("", "", string.punctuation))


def words(text: str) -> set[str]:
    return {w for w in (clean_text(t) for t in text.split()) if w}


def search_movie(query: str) -> None:
    file_path = Path(__file__).resolve().parents[2] / "data" / "movies.json"
    with open(file_path, "r", encoding="utf-8") as f:
        movies = json.load(f)["movies"]

    query_words = words(query)
    results = []  # (score, title)

    for movie in movies:
        title = movie["title"]
        if clean_text(title) == clean_text(query):
            score = float("inf")  # exact match always ranks first
        else:
            score = len(query_words & words(title))
        if score > 0:
            results.append((score, title))

    if not results:
        print("No matching movies found.")
        return

    results.sort(key=lambda r: r[0], reverse=True)
    best_score, best_title = results[0]
    print("Highest matching:", best_title)

    others = results[1:]
    if others:
        print("--------------Other less matching results------------------")
        for _, title in others:
            print(title)

    print("Found:", len(results), "results")


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword search CLI")
    subparsers = parser.add_subparsers(dest="command", help="available commands")

    search_parser = subparsers.add_parser("search", help="search movies using BM25")
    search_parser.add_argument("query", type=str, help="search query")

    args = parser.parse_args()

    if args.command == "search":
        print(f"Searching for: {args.query}")
        search_movie(args.query)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()