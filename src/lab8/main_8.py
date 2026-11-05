from lab8.serialize import students_from_json, students_to_json

students = students_from_json("data/lab8/students_input.json")
print("прочитано:", len(students))
print(students)

students_to_json(students, "data/lab8/students_output.json")
print("записано в data/lab8/students_output.json")


students_from_json("data/lab8/students_bad.json")