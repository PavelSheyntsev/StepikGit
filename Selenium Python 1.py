from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Метод стандартный
# try:
    # browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.get("https://parsinger.ru/selenium/1/1.html")
    # browser.implicitly_wait(10)
    #
    # firstname = browser.find_element(By.CSS_SELECTOR, '[name=first_name]')
    # firstname.send_keys("Сергей")
    #
    # lastname = browser.find_element(By.CSS_SELECTOR, '[name = last_name]')
    # lastname.send_keys("Петренко")
    #
    # patronymic = browser.find_element(By.CSS_SELECTOR, '[name = patronymic]')
    # patronymic.send_keys("Иванович")
    #
    # age = browser.find_element(By.CSS_SELECTOR, '[name=age]')
    # age.send_keys("30")
    #
    # city = browser.find_element(By.CSS_SELECTOR, '[name = city]')
    # city.send_keys("Санкт-Петербург")
    #
    # email = browser.find_element(By.CSS_SELECTOR, '[name=email]')
    # email.send_keys("12345@mail.ru")
    #
    # button = browser.find_element(By.CSS_SELECTOR, '[type=button]')
    # button.click()

#Метод по примеру
try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/1/1.html")
    browser.implicitly_wait(5)

    for field in browser.find_elements(By.CLASS_NAME, 'form'):
        field.send_keys('Text')
    browser.find_element(By.CSS_SELECTOR, '[type=button]').click()

finally:
    time.sleep(5)
    browser.quit()