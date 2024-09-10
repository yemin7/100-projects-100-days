from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com")

first_name = "abcd"
last_name = "dcba"
email = "xxx@yy.zz"

f_name= driver.find_element(By.NAME, "fName")
f_name.send_keys(first_name)

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys(last_name)

email_addr = driver.find_element(By.NAME, "email")
email_addr.send_keys(email)

# signup = driver.find_element(By.CLASS_NAME, 'btn-primary')
signup = driver.find_element(By.CSS_SELECTOR, "form button")
signup.click()

