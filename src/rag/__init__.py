import argparse;
import json;
from pathlib import Path;
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


def SearchMovie(arg):
    file_path = Path(__file__).resolve().parents[2] / "data" / "movies.json"
    count = 0;
    lowerarg = arg.lower()
    with open(file_path,"r",encoding="utf-8") as file :
        data = json.load(file)
        
        movies= data["movies"]
       
        for movie in movies:
            if(movie["title"]==arg):
                count+=1
                print(movie["title"])
            titlesplit  = movie["title"].split( )
            for title in titlesplit:
                if(title.lower()==lowerarg):
                 count+=1
                 print(movie["title"])

            

    print("Founded : ",count," results")



