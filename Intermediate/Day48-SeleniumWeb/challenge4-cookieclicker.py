import time
from selenium import webdriver
from selenium.webdriver.common.by import By

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
cps = driver.find_element(By.ID, "cps").text

stores = driver.find_element(By.ID, "store")
stores_div = stores.find_elements(By.TAG_NAME, "div")

stores_list = {}
store_ids = []


def get_stores():
    for item in stores_div:
        try:
            cookies = item.find_element(By.TAG_NAME, "b").text.split("-")[1]
        except IndexError:
            cookies = ''
        format_cookies = cookies.replace(',','').strip()

        store_id = item.get_attribute("id")
        store_ids.append(store_id)
        try:
            cookies = int(format_cookies)
        except ValueError:
            cookies = 0
        stores_list[store_id] = cookies

'''
def check_stores():
    stores_div_tag = stores.find_elements(By.TAG_NAME, "div")
    for item in stores_div_tag:
        check_id = item.get_attribute("id")
        is_store_grayed = True if (item.get_attribute("class")) == "grayed" else False

        if stores_list[check_id]["is_grayed"] != is_store_grayed:
            stores_list[check_id]["is_grayed"] = False
        else:
            stores_list[check_id]["is_grayed"] = True
'''

def click_store(store_id):
    driver.find_element(By.ID, value=store_id).click()


def buy_store():
    affordable_stores = {}
    money = driver.find_element(By.ID, "money").text
    if "," in money:
        money = money.replace(",", "")

    # Sort the dictionary by values in ascending order
    # available_stores = dict(sorted(available_stores.items(), key=lambda item: item[1], reverse=True))

    for store_id, amount in stores_list.items():
        if int(money) >= amount:
            affordable_stores[store_id] = amount

    highest_price = max(affordable_stores)
    click_store(highest_price)


get_stores()

while True:
    cookie.click()
    if time.time() > timeout:
        # check_stores()
        buy_store()
        timeout = time.time() + 5
    if time.time() > five_min:
        print(cps)
        break
