import json;
from pathlib import Path;
from rag.cleantext import clean_text;
from rag.cleantext import remove_stop_words;
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

