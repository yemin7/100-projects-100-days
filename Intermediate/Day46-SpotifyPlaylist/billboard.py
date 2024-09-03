import requests
from bs4 import BeautifulSoup

class Billboard:
    def __init__(self, date_input):
        self.billboard_url = "https://www.billboard.com/charts/hot-100"
        self.date_input = date_input
        self.data =  BeautifulSoup(self.get_billboard(self.date_input).text, "html.parser")

    def get_billboard(self, date_input):
        return requests.get(f"{self.billboard_url}/{date_input}")

    def get_songs(self):
        return self.data.select('h3.c-title.a-no-trucate')

    def get_artists(self):
        return self.data.select('span.c-label.a-no-trucate')
