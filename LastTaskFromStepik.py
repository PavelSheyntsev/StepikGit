import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    firstname = browser.find_element(By.CSS_SELECTOR, value = "body > div > form > div > input:nth-child(2)")
    firstname.send_keys("Павел")
    lastname = browser.find_element(By.CSS_SELECTOR, value = "body > div > form > div > input:nth-child(4)")
    lastname.send_keys("Иванов")
    email = browser.find_element(By.CSS_SELECTOR, value = "body > div > form > div > input:nth-child(6)")
    email.send_keys("12345@mail.ru")

    current_dir = os.path.abspath(os.path.dirname("__file__"))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)
    element = file = browser.find_element(By.CSS_SELECTOR, value = "#file")
    element.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, value=".btn.btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
