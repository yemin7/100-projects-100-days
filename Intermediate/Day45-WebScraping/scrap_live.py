import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)

articles = soup.find_all("span", class_="titleline")
# print(articles)
article_titles = []
article_links = []

for article in articles:
    article_title = article.getText()
    article_titles.append(article_title)
    article_link = article.find("a").get("href")
    article_links.append(article_link)

article_points = [int(point.getText().split()[0]) for point in soup.find_all("span", class_="score")]

# print(article_titles)
# print(article_links)
# print(article_points)

for news in range(len(article_titles)-1):
    print(f"Title: {article_titles[news]}\t")
    print(f"Link: {article_links[news]}\t")
    print(f"Points: {article_points[news]}\n")



max_point = max(article_points)
max_point_index = article_points.index(max_point)

print(f"Top news: {article_titles[max_point_index]}\n{article_links[max_point_index]}\n{article_points[max_point_index]}")
