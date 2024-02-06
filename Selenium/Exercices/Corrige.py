from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

driver = webdriver.Firefox()
driver.get("https://www.lesechos.fr/")
driver.maximize_window()

try:

    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, 'button[id="didomi-notice-agree-button"]'))
    )
    button.click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "[aria-label='Recherche']")
        )
    )
    search_box.click()

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input")
        )
    )
    # Recuperer les attributs d'un élément
    # print(search_box.get_attribute("aria-label"))
    search_box.get_attribute("aria-label")
    search_box.send_keys("intelligence artificielle")

    search_box.send_keys(Keys.RETURN)

    result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
    )
    articles = driver.find_elements(By.CSS_SELECTOR, "article")

    print(len(articles))

    for article in articles[:10]:  # Limite à 10 articles
        lien = article.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        print(lien)

    time.sleep(50)


finally:
    driver.quit()

print("Extraction terminée. Les données sont enregistrées dans 'les_echos_articles.csv'")
