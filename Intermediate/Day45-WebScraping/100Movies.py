import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.text, "html.parser")

titles = [ title.getText() for title in soup.find_all("h3", class_="title")]

# for item in range(len(titles))[::-1]:
#     print(titles[item])
movies = titles[::-1]
# print(movies)

with open("movies.txt", "w") as movies_file:
    movies_file.write("\n".join(movies))
