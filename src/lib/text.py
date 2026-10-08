def  normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё","Е")

    text = text.replace("\t", " ").replace("\r"," ").replace("\n"," ")

    return " ".join(text.split())

import re

def tokenize(text: str):
    return re.findall( r'\w+(?:-\w+)*', text) 


def count_freq(tokens: list[str]):
    freq = {}

    for i in tokens:
        freq[i] = freq.get(i, 0) + 1 

    
    return freq


def top_n(dict, n):
    return sorted(dict.items(), key = lambda i : (-i[1], i[0]))[:n]


