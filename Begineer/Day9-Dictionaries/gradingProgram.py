student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


def grades_calc(scores):
    student_grades = {}

    for name, score in scores.items():
        if 91 <= score <= 100:
            student_grades[name] = "Outstanding"
        elif 81 <= score <= 90:
            student_grades[name] = "Exceeds Expectations"
        elif 71 <= score <= 80:
            student_grades[name] = "Acceptable"
        else:
            student_grades[name] = "Fail"

    return student_grades


student_grades = grades_calc(student_scores)

print(student_grades)
