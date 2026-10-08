import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from lib.text import tokenize, count_freq, top_n


def main():
    text = sys.stdin.read()
    words = tokenize(text)
    counts = count_freq(words)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(counts)}")
    print("Топ-5:")
    for word, n in top_n(counts, 5):
        print(f"{word}:{n}")


if __name__ == "__main__":
    main()