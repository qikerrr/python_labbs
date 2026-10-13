import csv
from pathlib import Path

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def read_text(path, encounding: str = "utf-8") -> str:
    return Path(path).read_text(encoding=encounding)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:

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


if __name__ == "__main__":
    txt = read_text("data/lab4/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab4/proverka.csv")

