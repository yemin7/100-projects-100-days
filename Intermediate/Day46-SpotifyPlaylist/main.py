import requests
from bs4 import BeautifulSoup

billboard_url = "https://www.billboard.com/charts/hot-100"

date_input = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
response = requests.get(f"{billboard_url}/{date_input}")

data = BeautifulSoup(response.text, "html.parser")

# top_songs = data.find_all("h3", {"class": ["c-title", "a-no-trucate"]}) # OR operator
top_songs = data.select('h3.c-title.a-no-trucate')  # AND operator
artists = data.select('span.c-label.a-no-trucate')

songs_list = []
artists_list = []


for index in range(0, len(top_songs)):
    song = " ".join(top_songs[index].getText().split())
    songs_list.append(song)
    artist = " ".join(artists[index].getText().split())
    artists_list.append(artist)
    print(f"{index}: {song} - {artist}")




