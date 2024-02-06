from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the webdriver
driver = webdriver.Firefox()

driver.get("http://127.0.0.1:5500/webScrapping3/Selenium/Exercices/test.html")


## Ouvrir un nouvel onglet

driver.execute_script("window.open('');")



## creer les index des onglets

tabs = driver.window_handles


time.sleep(2)

## switcher vers le nouvel onglet

driver.switch_to.window(tabs[0])
time.sleep(2)


driver.switch_to.window(tabs[1])


driver.get("http://google.com")
time.sleep(5)

print(tabs)


driver.quit()
