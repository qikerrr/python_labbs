import csv
import json
from pathlib import Path

JSON_PATH = "data/samples/people.json"
CSV_PATH = "data/samples/people.csv"

CSV_TO = 'data/out/people_from_csv_to_json.json'
JSON_TO = 'data/out/people_from_json_to_csv.csv'

def proverka(path, EXT):
    p = Path(path)

    if p.suffix.lower() != EXT:
        raise ValueError(f"Неверный тип файла")
    if not p.exists():
        raise FileNotFoundError(path)
    return p

def json_to_csv(json_path, csv_path):

    with proverka(json_path, ".json").open(encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, list) or not data or not all(isinstance(r, dict) for r in data):
        raise ValueError('Нет данных или неподдерживаемый тип данных')
    fields = list(dict.fromkeys(i for r in data for i in r))
    Path(csv_path).parent.mkdir(parents=True, exist_ok=True)

    with open(csv_path, "w", newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, restval="")
        w.writeheader()
        w.writerows(data)

def csv_to_json(csv_path, json_path):

    with proverka(csv_path, '.csv').open(newline="", encoding='utf-8') as f:
        read = csv.DictReader(f)
        if not read.fieldnames:
            raise ValueError('CSV без заголовка')
        rows = list(read)

    if not rows:
        raise ValueError('CSV пустой')

    Path(json_path).parent.mkdir(parents=True, exist_ok=True)

    with open(json_path, "w", encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent = 2)

if __name__ == "__main__":
    json_to_csv(JSON_PATH, JSON_TO)
    csv_to_json(CSV_PATH, CSV_TO)
