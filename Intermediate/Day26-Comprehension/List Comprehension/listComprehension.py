numbers = [1, 2, 3]
word1 = "Hello World"

new_list = [i+1 for i in numbers]
print(new_list)

#String as List
str_list = [i for i in word1]
print(str_list)

#Range as List
range_list = [i for i in range(1, 5)]
print(range_list)

#Condition List Comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

