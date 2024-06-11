list_of_strings = input().split(',')

num_list = [int(num) for num in list_of_strings if int(num)%2 == 0]
print(num_list)

