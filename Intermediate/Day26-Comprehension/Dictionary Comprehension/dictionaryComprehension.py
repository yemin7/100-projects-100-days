import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

students_dict = {name: random.randint(1, 100) for name in names}
print(students_dict)

passed_students = {student: score for (student, score) in students_dict.items() if score >= 60}
print(passed_students)
