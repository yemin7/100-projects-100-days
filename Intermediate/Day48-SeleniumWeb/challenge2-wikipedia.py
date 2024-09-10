from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# num_articles = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
num_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# num_articles.click()
# print(num_articles.text)

## Find element by Link Text
content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

## Find the "Search" <input> by Name
search_python = driver.find_element(By.NAME, "search")
## Sending keyboard input to Selenium
search_python.send_keys("Python", Keys.ENTER)

# driver.quit()
