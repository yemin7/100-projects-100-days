import colorgram

rgb_colors = []

colors = colorgram.extract('spot_painting.jpg', 30)


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colors = r,g,b
    rgb_colors.append(new_colors)

print(rgb_colors)
