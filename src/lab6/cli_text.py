import argparse
import sys
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n

def proverka(path):
    p = Path(path)

    if not p.is_file():
        raise FileNotFoundError(f"Файл {p} не найден")
    return p

def cmd_cat(input_file, n):
    p = proverka(input_file)

    with p.open("r", encoding='utf-8') as f:
        for i, line in enumerate(f, start = 1):
            line = line.rstrip("\n")
            print(f"{i:>4} {line}" if n else line)

def cmd_states(input_file, n):
    p = proverka(input_file)
    text = p.read_text(encoding='utf-8')

    token = tokenize(normalize(text))
    freq = count_freq(token)

    for word, count in top_n(freq, n):
        print(f"{word:<15} {count}")

def builder_parser():
    parser = argparse.ArgumentParser(description="CLI-утилиты")
    sub = parser.add_subparsers(dest="command", required=True)

    p_cat = sub.add_parser("cat", help= "Вывод содержимого файла")
    p_cat.add_argument("--input", required=True, help="Путь файла")
    p_cat.add_argument("-n", action="store_true", help="Нумерация строк")

    p_stats = sub.add_parser("stats", help = "Частоты слов в тексте")
    p_stats.add_argument("--input", required=True, help="Путь файла")
    p_stats.add_argument("--top", type=int, default=5, help="Сколько слов показать")

    return parser

def main():
    parser = builder_parser()
    args = parser.parse_args()

    if args.command == "stats" and args.top <= 0:
        parser.error("--top не является положительным числом")

    try:
        if args.command == "cat":
            cmd_cat(args.input, args.n)
        elif args.command == "stats":
            cmd_states(args.input, args.top)

    except FileNotFoundError:
        print(f"Ошибка: файл {args.input} не найден", file=sys.stderr)
        sys.exit(1)

    except UnicodeDecodeError:
        print(f"Ошибка: неверная кодировка", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()