########################################################################################################################
#You are going to write a program that calculates the average student height from a List of heights.
#
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#
#e.g.
#
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#
#There are a total of 7 heights in student_heights
#
#1146 ÷ 7 = 163.71428571428572
#
#Average height rounded to the nearest whole number = 164
########################################################################################################################

student_heights = input().split()
sum = 0
for n in student_heights:
    sum += int(n)

average = sum / len(student_heights)
print(f"total height = {sum}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {int(round(average))}")
