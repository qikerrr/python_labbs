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
