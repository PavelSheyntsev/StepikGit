from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/3/3.html")

    p = browser.find_elements(By.TAG_NAME, 'p').text
    print(p)

finally:
    time.sleep(5)
    browser.quit()
