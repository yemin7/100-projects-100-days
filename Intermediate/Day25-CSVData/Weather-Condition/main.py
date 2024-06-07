# with open("weather.csv") as file:
#     data = file.readlines()
#     print(data)

# import csv

# with open("weather.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "Temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather.csv")
# print(data)
# print(data["Temp"])

## Convert Series to dict
# data_dict = data.to_dict()
# print(data_dict)

## Series return list
# temp_list = data["Temp"].to_list()
# avg_temp = round(sum(temp_list) / len(temp_list),2 )

# print(f"Average Tempature: {avg_temp}")

## Average / Mean
print(data["Temp"].mean())

## Max
print(data["Temp"].max())

## Get Data in Row
# print(data[data.Day == "Monday"])

# print(data[data.Temp == data["Temp"].max()])

# monday = data[data.Day == "Monday"]
# print(monday.Condition)
# print((monday.Temp * 9/5) + 32)

## Create dataframe from scratch
student_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

student_data = pandas.DataFrame(student_dict)
print(student_data)
student_data.to_csv("student_data.csv")