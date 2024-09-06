import requests, json
from send_message import SENDMAIL
from bs4 import BeautifulSoup

TARGET_PRICE = 100
sms = SENDMAIL()

test_url = "https://appbrewery.github.io/instant_pot"
## Live URL
# test_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

with open('header.json', 'r') as file:
    headers = json.load(file)

response = requests.get(test_url, headers=headers)
product = BeautifulSoup(response.text, "html.parser")

product_price = product.find(class_="aok-offscreen").get_text()
price = float(product_price.split('$')[1])

product_title = product.find("span", id="productTitle", class_="a-size-large product-title-word-break").get_text()
product_title = " ".join(product_title.split())

if price < TARGET_PRICE:
    sms.send_sms(product_title, price, test_url)
