import argparse
import sys
from pathlib import Path

from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_xlsx


def proverka(path):
    if not Path(path).is_file():
        raise FileNotFoundError(f"Файл {path} не найден")


def builder_parser():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd", required=True)

    for name, help_text in (
        ("json2csv", "Конвертировать JSON в CSV"),
        ("csv2json", "Конвертировать CSV в JSON"),
        ("csv2xlsx", "Конвертировать CSV в XLSX"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--in", dest="input", required=True, help="Входной файл")
        p.add_argument("--out", required=True, help="Выходной файл")

    return parser


def main() -> None:
    parser = builder_parser()
    args = parser.parse_args()

    expected_ext = {
        "json2csv": (".json", ".csv"),
        "csv2json": (".csv", ".json"),
        "csv2xlsx": (".csv", ".xlsx"),
    }
    in_ext, out_ext = expected_ext[args.cmd]
    if Path(args.input).suffix.lower() != in_ext:
        parser.error(f"для {args.cmd} файл должен иметь расширение {in_ext}")
    if Path(args.out).suffix.lower() != out_ext:
        parser.error(f"для {args.cmd} файл должен иметь расширение {out_ext}")

    try:
        proverka(args.input)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)

        if args.cmd == "json2csv":
            json_to_csv(args.input, args.out)
        elif args.cmd == "csv2json":
            csv_to_json(args.input, args.out)
        elif args.cmd == "csv2xlsx":
            csv_xlsx(args.input, args.out)

        print(f"Готово: {args.input} -> {args.out}")
    except FileNotFoundError:
        print(f"Файл {args.input} не найден", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()