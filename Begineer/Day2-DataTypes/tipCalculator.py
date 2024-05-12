print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tips = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

pay = (total_bill + total_bill*(tips/100)) / people
format_pay = "{:.2f}".format(pay)
#print(f"Each person should pay: ${round(pay, 2)}")
print(f"Each person should pay: ${format_pay}")

