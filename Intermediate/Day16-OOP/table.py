from prettytable import PrettyTable

pokemon = PrettyTable()
pokemon.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
pokemon.add_column("Type", ["Electric", "Water", "Fire"])
pokemon.align = "c"
print(pokemon)

city = PrettyTable()
city.field_names = ["City Name", "Area", "Population"]
city.add_row(["Sydney", 2058, 4336374])
city.add_row(["Darwin", 112, 120900])
city.align = "l"
print(city)

