import datetime as dt
import random

now = dt.datetime.now()
print(now)

date = dt.datetime.strftime(now, "%d %M, %Y")
print(date)


with open("quotes.txt") as text:
    text_list = text.readlines()
    random_text = random.choice(text_list)
    content = ''.join(random_text).replace('"', '')
    print(content)
    print(random_text)

