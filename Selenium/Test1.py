from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a new instance of the webdriver
driver = webdriver.Firefox()

driver.get("http://127.0.0.1:5501/Exercices/test.html")

input = driver.find_element(By.TAG_NAME, "input")

print(input.text)

time.sleep(2)

input.send_keys("Christopher Loisel")

time.sleep(2)

# input.send_keys(Keys.ENTER)

driver.find_element(By.TAG_NAME, "button").click()


time.sleep(2)
driver.quit()
