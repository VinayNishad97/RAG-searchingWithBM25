import argparse;
import json;
from pathlib import Path;
import string;
from nltk.stem import PorterStemmer;
ps = PorterStemmer();
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
    total_count = 0
    title_map = {}
    with open(file_path,"r",encoding="utf-8") as file :
        data = json.load(file)

        movies= data["movies"]

        for movie in movies:
            matching_count = 0;
            stop_word_removed_title = remove_stop_words(movie["title"].lower())
            stop_word_removed_argu = remove_stop_words(arg.lower())
            if(clean_text(stop_word_removed_title)==clean_text(arg)):
                title_map[float("inf")] = movie["title"]
                total_count+=1
                continue
           
            titlesplit  = stop_word_removed_title.split( )
            arg_split = stop_word_removed_argu.split( )
            for title in titlesplit:
                for argu in arg_split:
                 if(clean_text(title)==clean_text(argu)):
                  matching_count+=1
                  total_count+=1
            if matching_count > 0:
                title_map.setdefault(matching_count, []).append(movie["title"])

    if not title_map:
        print("No matching movies found.")
        return

    highest_matching = max(title_map)
    print("Highest matching : ", title_map[highest_matching][0])
    print("--------------Total matching------------------")
    for key, values in title_map.items():
            for value in values:
                print(value)

    print("Founded : ", total_count, " results")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("","",string.punctuation))
    return text

def remove_stop_words(text):
     stop_word_file_path = Path(__file__).resolve().parents[2] / "data" / "stopwords.txt"
     list_of_text = text.split( )
     with open(stop_word_file_path,"r",encoding="utf-8") as f:    
         stop_words = {line.strip() for line in f}
         list_of_text = [word for word in list_of_text if word not in stop_words]
         for i in range(len(list_of_text)):
             list_of_text[i] = ps.stem(list_of_text[i])
     return " ".join(list_of_text)
                 
        