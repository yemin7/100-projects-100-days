weather_c = eval(input())


def c_to_f(temp):
    return round((temp * 9 / 5) + 32, 2)


weather_f = {day: c_to_f(degree) for (day, degree) in weather_c.items()}
print(weather_f)
