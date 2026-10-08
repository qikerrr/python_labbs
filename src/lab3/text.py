def  normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё","Е")

    text = text.replace("\t", " ").replace("\r"," ").replace("\n"," ")

    return " ".join(text.split())


#print( r'"ПрИвЕт\nМИр\t" - >' ,f' "{normalize("ПрИвЕт\nМИр\t")}" ', sep = ' ')
#print( '"ёжик, Ёлка" - >' ,f' "{normalize("ёжик, Ёлка" , yo2e=True)} " ',  sep = ' ')
#print( r'"Hello\r\nWorld" - >' ,f' "{normalize("Hello\r\nWorld")}" ',  sep = ' ')
#print( '"  двойные   пробелы  " - >' ,f' "{normalize("  двойные   пробелы  ")}" ' , sep = ' ')

import re

def tokenize(text: str):
    return re.findall( r'\w+(?:-\w+)*', text) #сравнивает с шаблоном и возвращает список, нересекающийся с шаблоном

#print( ' "привет мир" - > ',tokenize("привет мир"), sep ='')
#print( ' "hello,world!!!" - > ', tokenize("hello,world!!!"), sep ='')
#print( ' "по-настоящему круто" - > ', tokenize("по-настоящему круто"), sep ='')
#print( ' "2025 год" - > ', tokenize("2025 год"), sep ='')
#print( ' "emoji 😀 не слово" - > ', tokenize("emoji 😀 не слово"), sep ='')

def count_freq(tokens: list[str]):
    freq = {}

    for i in tokens:
        freq[i] = freq.get(i, 0) + 1 
        #смотрим ключ буквы, если его нет то заносим 1(если есть просто добавляем к значению 1)
    
    return freq

#print(' ["a","b","a","c","b","a"] -> ', count_freq(["a","b","a","c","b","a"]), sep = '')
#print(' ["bb","aa","bb","aa","cc"] -> ', count_freq(["bb","aa","bb","aa","cc"]), sep = '')

def top_n(dict, n): #на вход кортеж
    return sorted(dict.items(), key = lambda i : (-i[1], i[0]))[:n]
#через (items) делаем список и сортируем его по ключу -> делаем спец функцию чтобы сортировка была по убыванию

print(' {"a":3,"b":2,"c":1} -> ', top_n({"a":3,"b":2,"c":1}, n =2), sep = "")
print(' {"aa":2,"bb":2,"cc":1} -> ', top_n({"aa":2,"bb":2,"cc":1}, n =2), sep = "")