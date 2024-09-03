import os
import spotipy
from dotenv import load_dotenv
from spotipy import SpotifyOAuth

load_dotenv(dotenv_path=".env")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = os.getenv("REDIRECT_URI")
scope = os.getenv("SCOPE")
cache_path = os.getenv("CACHE_PATH")

class Spotify:
    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id = client_id,
            client_secret = client_secret,
            redirect_uri = redirect_uri,
            scope = scope,
            cache_path = cache_path,
            show_dialog=True
        ))

    def create_playlist(self, playlist_name):
        user = self.sp.current_user()['id']
        description = "Created by Python"
        playlist = self.sp.user_playlist_create(user=user, name=playlist_name,public=True, description=description)
        return playlist['id']

    def add_songs_to_playlist(self, playlist_id, songs):
        self.sp.playlist_add_items(playlist_id=playlist_id, items=songs)

    def search_song(self, artist_name, song_name):
        # sp_client = self.sp(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))
        query = f"track:{song_name}"
        # result = sp_client.search(q=query, type='track')
        result = self.sp.search(q=query, type='track')
        items = result.get('tracks', {}).get('items', [])
        if items:
            for track in items:
                artists = [artist['name'] for artist in track['artists']]
                artist_parts = artist_name.split(" ")
                for part in artist_parts:
                    if any(part.lower() in artist.lower() for artist in artists):
                        return track['external_urls']['spotify']
        else:
            return None
