import pandas

student_dict = {
    "student": ["James", "Lilly", "Rose"],
    "score": [56, 76, 98]
}

student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)

new_dict = {row.student: row.score for (index,row) in student_dataframe.iterrows()}
print(new_dict)
