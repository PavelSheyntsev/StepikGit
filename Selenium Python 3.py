from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://parsinger.ru/selenium/3/3.html")

    def test1():
        #сумма каждое число
        a = [int(x.text) for x in browser.find_elements(By.TAG_NAME, "p")]
        print(sum(a))
        assert a == int("450384194300")

    def test2():
        #сумма каждое второе число
        a = [int(x.text) for x in browser.find_elements(By.XPATH, "//div[@class='text']/p[2]")]
        print(sum(a))
        assert a == int("149494128600")

    if __name__ == "__main__":
        test1()
        test2()

finally:
    time.sleep(1)
    browser.quit()
