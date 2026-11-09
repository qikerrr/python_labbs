import csv
from pathlib import Path

from src.lab8.models import student_from_dict, validate_student
s_fields = ("fio", "birthdate", "group", "gpa")

def ensure_storage(path):
    p = Path(path)
    p.parent.mkdir(parents= True, exist_ok=True)

    if not p.exists():
        with open(path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f , fieldnames=list(s_fields))
            writer.writeheader()

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

def save_students(path, students):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(s_fields))
        writer.writeheader()

        for s in students:
            writer.writerow({i: s[i] for i in s_fields})

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

def list_students(path, sort_by=None):

    if sort_by not in (None, "fio", "gpa"):
        raise ValueError("Недопустимое значение sort_by (необходимо None, 'fio', 'gpa')")

    students = load_students(path)
    if sort_by == "fio":
        return sorted(students, key= lambda s: s["fio"])
    if sort_by == "gpa":
        return sorted(students, key=lambda s: s["gpa"])

    return students

def find_students(path, substr):
    name = substr.lower()

    return [s for s in load_students(path) if name in s["fio"].lower()]

def remove_student(path, fio):
    students = load_students(path)
    remaining = [s for s in students if s["fio"] != fio]
    removed = len(students) - len(remaining)

    if removed > 0:
        save_students(path, remaining)

    return removed

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


