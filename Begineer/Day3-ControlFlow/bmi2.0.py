##############################################################################################
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. #
# It should tell them the interpretation of their BMI based on the BMI value.                #
#                                                                                            #
# Under 18.5 they are underweight                                                            #
# Equal to or over 18.5 but below 25 they have a normal weight                               #
# Equal to or over 25 but below 30 they are slightly overweight                              #
# Equal to or over 30 but below 35 they are obese                                            #
# Equal to or over 35 they are clinically obese.                                             #
##############################################################################################

# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."

height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / (height * height)
bmi_2d = "{:.2f}".format(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmi_2d}, you are underweight.")
elif 18.5 <= bmi < 25:
    print(f"Your BMI is {bmi_2d}, you have a normal weight.")
elif 25 <= bmi < 30:
    print(f"Your BMI is {bmi_2d}, you are slightly overweight.")
elif 30 <= bmi < 35:
    print(f"Your BMI is {bmi_2d}, you are obese.")
else:
    print(f"Your BMI is {bmi_2d}, you are clinically obese.")
