from spotify import Spotify
from billboard import Billboard

# start = time.time()

date_input = input("Which year do you want to travel to? Type the date in YYYY-MM-DD format: ")
b_board = Billboard(date_input)
sp = Spotify()

billboard_list = []

def create_billboard_list():
    songs = b_board.get_songs()
    artists = b_board.get_artists()
    for index in range(0, len(songs)):
        song = " ".join(songs[index].getText().split())
        artist = " ".join(artists[index].getText().split())
        link = sp.search_song(artist, song)
        billboard_list.append(link)

create_billboard_list()
playlist = sp.create_playlist(f"{date_input} Billboard 100")
sp.add_songs_to_playlist(playlist, billboard_list)

# end = time.time()
# print("The time of execution of above program is :", (end-start) * 10**3, "ms")
