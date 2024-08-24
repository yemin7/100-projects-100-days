from bs4 import BeautifulSoup

with open("website.html") as f:
    soup = BeautifulSoup(f, "html.parser")

# print(soup.prettify())
all_a = soup.find_all("a")
print(all_a)

for item in all_a:
    print(item.getText())
    print(item.get("href"))

heading = soup.find("h1", id="name")
print(heading.getText())

url_in_p = soup.select_one(selector="p a")
print(url_in_p.get("href"))
