import json

from .models import student_from_dict, student_to_dict

def students_to_json(students, path):
    data = [student_to_dict(s) for s in students]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("ОШИБКА: данные не являются списком!")

    res = []
    for i, item in enumerate(data):
        try:
            res.append(student_from_dict(item))
        except ValueError as e:
            raise ValueError(f"ОШИБКА: неправильная запись данных студента(№{i} = {e})")

    return res

