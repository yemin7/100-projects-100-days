import pandas

squirrel_data = pandas.read_csv("Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

total_squirrel = squirrel_data["Hectare Squirrel Number"].sum()
print(total_squirrel)

gray_squirrel_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
red_squirrel_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Red"]
black_squirrel_color = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]

print(len(gray_squirrel_color))
print(len(red_squirrel_color))
print(len(black_squirrel_color))

color_count = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [len(gray_squirrel_color), len(red_squirrel_color), len(black_squirrel_color)]
}

color_data = pandas.DataFrame(color_count)
color_data.to_csv("Squirrel_color.csv")
