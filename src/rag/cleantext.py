from pathlib import Path;
import string;
from nltk.stem import PorterStemmer;
ps = PorterStemmer();

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
                 
        