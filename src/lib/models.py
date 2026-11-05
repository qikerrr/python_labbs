from datetime import date

s_fields = ("fio", "birthdate", "group", "gpa")

def validate_student(rec):

    if not isinstance(rec, dict):
        raise ValueError("ОШИБКА: Данные не являются словарем!")

    if set(rec) != set(s_fields):
        missing = set(s_fields) - set(rec)
        sup = set(rec) - set(s_fields)
        if missing:
            raise ValueError(f"ОШИБКА(потерянные данные): данные '{sorted(missing)}' не попали в rec, хотя были введены!")
        if sup:
            raise ValueError(f"ОШИБКА(лишние данные): данных '{sorted(sup)}' не было в вводе!")

    if not isinstance(rec["fio"], str) or not rec["fio"].strip():
        raise ValueError("ОШИБКА: ФИО пустое или имеет неверный тип данных!")

    if not isinstance(rec["group"], str) or not rec["group"].strip():
        raise ValueError("ОШИБКА: Группа пустая или имеет неверный тип данных!")

    if not isinstance(rec["birthdate"], str):
        raise ValueError("ОШИБКА: День рождения представлено не в виде строки!")
    try:
        b = date.fromisoformat(rec["birthdate"])
    except ValueError as e:
        raise ValueError(f"ОШИБКА: день рождения не является корректной ISO датой - > ({e})!")
    if b > date.today():
        raise ValueError("ОШИБКА: День рождения будет в будущем!")

    if isinstance(rec["gpa"], bool) or not isinstance(rec["gpa"], (int, float)):
        raise ValueError("ОШИБКА: GPA имеет неверный тип данных")
    if not ( 0 <= rec["gpa"] <= 5 ):
        raise ValueError("ОШИБКА: условие '0 <= GPA <= 5' не выполняется")
            

def make_student(fio, birthdate, group, gpa):

    if not isinstance(fio, str):
        raise ValueError("ОШИБКА: ФИО не является строкой!")
    if not fio.strip():
        raise ValueError("ОШИБКА: ФИО не введено!")

    if not isinstance(group, str):
        raise ValueError("ОШИБКА: Группа не является строкой!")
    if not group.strip():
        raise ValueError("ОШИБКА: Группа не введена!")

    if  not isinstance(gpa, (float, int)) or  isinstance(gpa, bool):
        raise ValueError("ОШИБКА: GPA имеет некорректный тип данных!")

    rec = {"fio" : fio.strip(), "birthdate" : birthdate, "group" : group.strip(), "gpa" : float(gpa)}

    validate_student(rec)

    return rec

def student_age(rec, today=None):

    b = date.fromisoformat(rec["birthdate"])
    if today is None:
        today = date.today()

    age = today.year - b.year
    if (today.month, today.day) < (b.month, b.day):
        age -= 1
    return age

def format_student(rec):

    fs = rec["fio"].split()
    if len(fs) >= 2:
        name = fs[0] + " " + "".join(fs[i][0] + "." for i in range(1, len(fs)))
    elif len(fs) == 1:
        name = fs[0]
    else:
        name = rec["fio"]

    age = student_age(rec)
    n = age % 100
    if 5 <= n <= 20:
        y = "лет"
    else:
        n %= 10
        y = "год" if n==1 else "года" if 2 <= n <= 4 else "лет"

    return f"{name} ({rec['group']}), {age} {y}, GPA {rec['gpa']:.2f}"

def student_to_dict(rec):
    validate_student(rec)
    return {i : rec[i] for i in s_fields}


def student_from_dict(d):

    if not isinstance(d, dict):
        raise ValueError("ОШИБКА: Неверный тип данных!")
    
    missing = [i for i in s_fields if i not in d]
    if missing:
        raise ValueError(f"ОШИБКА: не все данные были введены!({missing})")

    gpa = d["gpa"]
    if isinstance(gpa, bool):
        raise ValueError("ОШИБКА: GPA имеет недопустимый тип данных!")
    
    try:
        gpa = float(gpa)
    except (TypeError, ValueError):
        raise ValueError("ОШИБКА: GPA имеет недопустимый тип данных!")
    
    return make_student(d["fio"], d["birthdate"], d["group"], gpa)



