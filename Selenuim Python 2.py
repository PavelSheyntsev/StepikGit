from selenium import webdriver
from selenium.webdriver.common.by import By
import time
try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/2/2.html")

    findtext = browser.find_element(By.PARTIAL_LINK_TEXT, '16243162441624')
    findtext.click()

finally:
    time.sleep(3)
    browser.quit()