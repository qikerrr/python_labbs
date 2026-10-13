import sys

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab4.io_txt_csv import read_text, write_csv

INPUT_FILE = "data/lab4/empty.txt"
REPORT_FILE = "data/lab4/empty.csv"
FILE_ENCODING = "utf-8"  

def sorted_word_counts(freq):
    return sorted(freq.items(), key=lambda pair: (-pair[1], pair[0]))


def main():
    try:
        text = read_text(INPUT_FILE, encounding=FILE_ENCODING)
    except FileNotFoundError:
        print(f"Ошибка: файл не найден: {INPUT_FILE}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: файл не читается в кодировке {FILE_ENCODING}")
        sys.exit(1)

    words = tokenize(normalize(text))
    freq = count_freq(words)

    write_csv(sorted_word_counts(freq), REPORT_FILE, header=("word", "count"))

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top_n(freq, n=5):
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()