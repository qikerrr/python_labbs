# ЛР4 — Файлы: TXT/CSV и отчёты по текстовой статистике

## Задание A — модуль `src/lab04/io_txt_csv.py`

```
import csv
from pathlib import Path

def ensure_parent_dir(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def read_text(path, encounding: str = "utf-8"):
    return Path(path).read_text(encoding=encounding)

def write_csv(rows, path, header =None):

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

```
### **`Разбор кода`**

```
def ensure_parent_dir(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```
> Фукнция создает все недостающие родительские папки

>  `".mkdir"` -> то есть "make directory"(создание папки)
>  - `parents=True` - нужна если родительской папки нет, то создает ее
> - `exist_ok=True` -> если папка не существует не вызывать ошибку

---
```
def read_text(path, encounding: str = "utf-8"):
    return Path(path).read_text(encoding=encounding)
```
> `.read_text()` - отвечает за открытие и чтение всего файла(автоматически закрывает файл)
----
## **Функция - `write_csv`**

```
def write_csv(rows, path, header =None):

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

```
> Проходимся по списку и проверяем, чтобы длина строк и заголовка была одинакова
> `open(path, 'w', newline="", encoding="utf-8")` - открытие файла
> + `path`  - сам файл
> + `"w"`  - то есть "write" = перенаписание файла
> + `newline=""`  - необходимо, чтобы питон не редактировал файл, так как расширение csv - уже это сделало
> + `encoding="utf-8"`  - кодировка, в которой будет записан текст

> `writer = csv.writer(f)` - создание "писателя" для CSV

> `writer.writerow()` - записывает строку
-------
```
if __name__ == "__main__":
    txt = read_text("data/lab4/input.txt")
    print(txt)

    write_csv([("word", "count"), ("test", 3)], "data/lab4/proverka.csv")
```
> Читает и выводит текст из `input.txt`, а затем записывает две строки данных в файл `proverka.csv`
---
