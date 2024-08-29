import os
import spotipy

from dotenv import load_dotenv
from spotipy import SpotifyOAuth, SpotifyClientCredentials

load_dotenv(dotenv_path=".env")

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

sp = spotipy.Spotify

def get_token():
    sp_token = sp(
        auth_manager=SpotifyOAuth(
            client_id = client_id,
            client_secret=client_secret,
            redirect_uri="https://example.com",
            scope = "playlist-modify-private",
            cache_path="token.txt"
        )
    )
    result = sp_token.current_user()['id']


def search_artist(artist_name):
    sp_client = sp(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
    result = sp_client.search(q=f"artist:{artist_name}", type='artist')
    items = result.get('artists', {}).get('items', [])
    if items:
        artist = items[0]
        print(artist)

search_artist('Shaboozey')

