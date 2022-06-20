from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/1/1.html")
    browser.implicitly_wait(10)

    firstname = browser.find_element(By.CSS_SELECTOR, '[name=first_name]')
    firstname.send_keys("Павел")

finally:
    time.sleep(2)
    browser.quit()