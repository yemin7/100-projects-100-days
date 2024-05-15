target = int(input("Give max range: "))

sumEven = 0
for num in range(0, target+1):
    if num % 2 == 0:
        sumEven += num

print(sumEven)
