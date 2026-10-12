import csv
from pathlib import Path

def ensure_parent_dir(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def read_text(path, encounding: str = "utf-8"):
    return Path(path).read_text(encoding=encounding)

def write_csv(rows, path, header):

    rows = list(rows)

    if len(rows) > 0:
        dl = len(rows[0])

        for i in rows:
            if len(i) != dl:
                raise ValueError('длина строк не совпадает')
            if header is not None and len(header) != dl:
                raise ValueError('длина заголовка не совпадает с длиной строк')

    ensure_parent_dir(path)
    with open(path, 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        for i in rows:
            writer.writerow(i)



from pathlib import Path
import sys

# Получаем папку, где лежит сам скрипт (src/lab4)
BASE_DIR = Path(__file__).resolve().parent 

# Поднимаемся на два уровня вверх (до python_labs) и идем в data/lab04
file_path = BASE_DIR.parent.parent / "data" / "lab04" / "input.txt"

text = read_text(file_path)