import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class my_unit_class(unittest.TestCase):

    def test_case_for_me(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        form1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        form1.send_keys('John')
        form2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        form2.send_keys('Smith')
        form3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        form3.send_keys('john@smith.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_case_for_me2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля

        form1 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
        form1.send_keys('John')
        form2 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
        form2.send_keys('Smith')
        form3 = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
        form3.send_keys('john@smith.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertTrue("Congratulations! You have successfully registered!" == welcome_text)
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()