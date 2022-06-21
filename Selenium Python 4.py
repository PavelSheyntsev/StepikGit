from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/4/4.html")

    for checkboxes in browser.find_elements(By.XPATH, "//input[@type='checkbox']"):
        checkboxes.click()

    button = browser.find_element(By.XPATH, "//input[@type='button']")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
