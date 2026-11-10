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
