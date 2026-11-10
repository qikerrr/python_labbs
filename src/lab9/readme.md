# ЛР9 — «База данных» на CSV: CRUD-функции над `students.csv` и CLI
## Содержание
**1)** [***Задание А - `group.py`***](#задание-а---grouppy)
+ [`ensure_storage(path)`](#ensure_storagepath)
+ [`load_students(path)`](#load_studentspath)
+ [`save_students(path, students)`](#save_studentspath-students)
+ [`add_student(path, student)`](#add_studentpath-student)
+ [`list_students(path, sort_by=None)`](#list_studentspath-sort_bynone)
+ [`find_students(path, substr)`](#find_studentspath-substr)

+ [`remove_student(path, fio)`](#remove_studentpath-fio)
+ [`update_student(path, fio, **fields)`](#update_studentpath-fio-fields)

**2)** [**Задание В - `cli_students.py`**](#задание-в---cli_studentspy)
+ [***Разбор кода***](#разбор-кода)



## Задание А - `group.py`
### `ensure_storage(path)`
```
def ensure_storage(path):
    p = Path(path)
    p.parent.mkdir(parents= True, exist_ok=True)

    if not p.exists():
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f , fieldnames=list(s_fields))
            writer.writeheader()
```
> Функция проверяет существует файл или нет, если нет, то создает файл с **заголовком**.
---
### `load_students(path)`
````
def load_students(path):
    ensure_storage(path)
    p = Path(path)

    students = []
    with open(path, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None:
            raise ValueError(f"В файле {p} нет заголовка!")
        if list(reader.fieldnames) != list(s_fields):
            raise ValueError("Неверный заголовок CSV!")

        for row in reader:
            if None in row:
                raise ValueError("Лишние колонки в строке!")

            student = student_from_dict(row)
            students.append({
                "fio": student.fio,
                "birthdate": student.birthdate,
                "group": student.group,
                "gpa": student.gpa,
            })

    return students
````
> *Читает сам файл, проверяет его на лишние колонки и неверный заголовок (возвращает список словарей)*
---
### `save_students(path, students)`
```
def save_students(path, students):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(s_fields))
        writer.writeheader()

        for s in students:
            writer.writerow({i: s[i] for i in s_fields})
```
> *Функция перезаписывает CSV-файл целиком*
---
### `add_student(path, student)`
```
def add_student(path, student):

    n = {i: str(student[i]) for i in s_fields}
    validated = student_from_dict(n)
    validate_student(validated)

    students = load_students(path)
    students.append({
        "fio": validated.fio,
        "birthdate": validated.birthdate,
        "group": validated.group,
        "gpa": validated.gpa,
    })
    save_students(path, students)
```
> *Валидирует запись студента и добавляет ее в конец*
---
### `list_students(path, sort_by=None)`
```
def list_students(path, sort_by=None):

    if sort_by not in (None, "fio", "gpa"):
        raise ValueError("Недопустимое значение sort_by (необходимо None, 'fio', 'gpa')")

    students = load_students(path)
    if sort_by == "fio":
        return sorted(students, key= lambda s: s["fio"])
    if sort_by == "gpa":
        return sorted(students, key=lambda s: s["gpa"])

    return students
```
> Возвращает список студентов, сортируя по `"fio"` или `"gpa"`, или вообще не сортирует при `None`
---
### `find_students(path, substr)`
```
def find_students(path, substr):
    name = substr.lower()

    return [s for s in load_students(path) if name in s["fio"].lower()]
```
> Возвращает записи студентов, у которых `substr` входит в `"fio"` *(без учета регистра)*
---
### `remove_student(path, fio)`
```
def remove_student(path, fio):
    students = load_students(path)
    remaining = [s for s in students if s["fio"] != fio]
    removed = len(students) - len(remaining)

    if removed > 0:
        save_students(path, remaining)

    return removed
```
> *Функция удаляет все записи, содержащие `"fio"`, возвращает количество удаленных записей.*
---
### `update_student(path, fio, **fields)`
```
def update_student(path, fio, **fields):

    for i in fields:
        if i not in s_fields:
            raise KeyError(f"Неизвестный ключ: {i}")

    students = load_students(path)
    for i, s in enumerate(students):
        if s["fio"] == fio:
            new = dict(s)
            new.update(fields)

            n = {e: str(new[e]) for e in s_fields}
            validated = student_from_dict(n)
            validate_student(validated)

            students[i] = {              
                "fio": validated.fio,
                "birthdate": validated.birthdate,
                "group": validated.group,
                "gpa": validated.gpa,
            }

            save_students(path, students)
            return True

    return False
```
> *Функция обновляет запись студента с заданным ФИО, валидирует результат (возвращает `True` или `False`)*
---
---
---
## Задание В - `cli_students.py`
`Код`
```
import argparse
import sys

from src.lab8.models import format_student, student_from_dict
from src.lab9 import group

DEFAULT_DB = "data/lab9/students.csv"

def build_parser():
    parser = argparse.ArgumentParser(prog="CLI_STUDENTS", description="CRUD-утилита")
    parser.add_argument("--db", default=DEFAULT_DB, help=f"Путь к CSV-файлу (по умолчанию стоит путь = {DEFAULT_DB})")

    sub = parser.add_subparsers(dest= "command", required=True)

    cm_add = sub.add_parser("add", help="Добавить студента")
    cm_add.add_argument("--fio", required=True)
    cm_add.add_argument("--birthdate", required=True)
    cm_add.add_argument("--group", required=True)
    cm_add.add_argument("--gpa", required=True)

    cm_list = sub.add_parser("list", help= "Сортировка списка студентов по fio/gpa")
    cm_list.add_argument("--sort", choices=["fio", "gpa"], default=None)

    cm_find = sub.add_parser("find", help="Поиск по подстроке ФИО")
    cm_find.add_argument("--q", required=True)

    cm_remove = sub.add_parser("remove", help="Удалить список по ФИО(выводит количество)")
    cm_remove.add_argument("--fio", required=True)

    cm_update = sub.add_parser("update", help="Обновление данных по ФИО")
    cm_update.add_argument("--fio", required=True)
    cm_update.add_argument("--birthdate", default=None)
    cm_update.add_argument("--group", default=None)
    cm_update.add_argument("--gpa", default=None)

    return parser


def main():
    args = build_parser().parse_args()

    try:
        if args.command == "add":
            student = {
                "fio": args.fio,
                "birthdate": args.birthdate,
                "group": args.group,
                "gpa": args.gpa,
            }
            group.add_student(args.db, student)
            s = student_from_dict(student)

            print(f"Добавлен: {format_student(s)}")

        elif args.command == "list":
            students = group.list_students(args.db, sort_by=args.sort)

            if not students:
                print("Пустой список")

            else:
                for s_dict in students:
                    s = student_from_dict({k: str(v) for k, v in s_dict.items()})
                    print(format_student(s))

        elif args.command == "find":
            students = group.find_students(args.db, args.q)

            if not students:
                print("Ничего не было надйено!")
            else:
                for s_dict in students:
                    s = student_from_dict({k: str(v) for k, v in s_dict.items()})
                    print(format_student(s))

        elif args.command == "remove":
            l = group.remove_student(args.db, args.fio)
            print(f"Записей удалено: {l}")

        elif args.command == "update":
            fields = {}

            if args.birthdate is not None:
                fields["birthdate"] = args.birthdate
            if args.group is not None:
                fields["group"] = args.group
            if args.gpa is not None:
                fields["gpa"] = args.gpa

            if not fields:
                print("Не указаны поля для обновления", file=sys.stderr)
                return 1

            if group.update_student(args.db, args.fio, **fields):
                print(f"Обновлена запись студента {args.fio}")
            else:
                print(f"Студент с ФИО = {args.fio} не был найден!", file=sys.stderr)
                return 1

    except (ValueError, KeyError) as e:
        print(f"Ошибка {e}", file=sys.stderr)
        return 1

    return 0

if __name__ == "__main__":
    sys.exit(main())

```
### `Разбор кода`
> Функция `build_parser()` создает парсер, делает его многоуровневым и в уровни *добавляет необходимые команды* `("add", "list", "remove",...)` и *соотсвестующие им аргументы* `("--q", "--fio", "--gpa",...)`
---
> Функция `main()` смотрит на *команду*, которую вызвали и соотвественно ей вызывает нужную функцию для преобразования со списком -> *`(удаление по фио, обновление данных, добавление данных...)`*
> + Также перехватывает ошибки вида -> `ValueError/KeyError` *(сообщение в stderr + код 1 / при успехе код 0)*