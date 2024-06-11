with open("file1.txt") as file1:
    num_list_1 = file1.readlines()
    num_list_1 = [int(num_list_1[i]) for i in range(len(num_list_1))]

with open("file2.txt") as file2:
    num_list_2 = file2.readlines()
    num_list_2 = [int(num_list_2[i]) for i in range(len(num_list_2))]

result = [num for num in num_list_1 if num in num_list_2]
print(result)
