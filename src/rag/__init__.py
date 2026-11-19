import argparse;
from rag.search import SearchMovie
def main() -> None:
    parser = argparse.ArgumentParser(description="keyword Search CLI")
    subparser = parser.add_subparsers(dest="command",help="available commands")

    search_parser = subparser.add_parser("search",help="search movies using BM25")
    search_parser.add_argument("query",type=str ,help="Search Query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for : {args.query}")
            SearchMovie(args.query)
            pass
        case _:
            parser.print_help()

