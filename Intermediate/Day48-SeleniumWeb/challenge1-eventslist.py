# Challenge 1: Upcoming Events List
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://python.org")

events = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
find_events = events.find_elements(By.TAG_NAME, 'li')

events_list = {}


for item in range(0, len(find_events)):
    event_date = find_events[item].find_element(By.TAG_NAME, 'time').text
    event = find_events[item].find_element(By.TAG_NAME, 'a').text
    events_list[item] = {
        'time': event_date,
        'name': event,
    }

print(events_list)
driver.quit()
