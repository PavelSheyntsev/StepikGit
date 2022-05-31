from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://rc.credit2day.ru/registration/main-info")
browser.implicitly_wait(5)

def highlight(element):
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: null; border: 5px solid skyblue;")
    time.sleep(.1)
    apply_style("background: null; border: 5px solid red;")
    time.sleep(.1)
    apply_style("background: null; border: 5px solid lightgreen;")
    time.sleep(.1)
    apply_style(original_style)

def test1():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys(" ")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Первый символ не может быть пробелом", "Неактуальная ошибка"

def test2():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys("12345")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test3():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys("!@#$%^&*")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test4():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys("qwertyasdzxc")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test5():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys("Ааааааааааааааааааааааааааааааааааааааааа")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите не более 40 символов", "Неактуальная ошибка"
    for i in range(40):
        lastname.send_keys('\uE003')

def test6():
    lastname = browser.find_element(By.ID, 'lastName')
    lastname.send_keys("иванов") #в value отображается с маленькой буквы, фронт автоматически меняет на большую (Иванов), поэтому assert ждет "иванов"
    lastname_check = lastname.get_attribute("value")
    assert lastname_check == "иванов"
    for i in range(6):
        lastname.send_keys('\uE003')

def test7():
    lastname = browser.find_element(By.ID, 'lastName')
    highlight(lastname)
    lastname.send_keys("Петров")
    lastname_check = lastname.get_attribute("value")
    assert lastname_check == "Петров", "Если не Петров тогда все сломалось"

def test8():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys(" ")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Первый символ не может быть пробелом", "Неактуальная ошибка"

def test9():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("12345")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test10():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("!@#$%^&*")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test11():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("qwertyasdzxc")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test12():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("Ааааааааааааааааааааааааааааааааааааааааа")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите не более 35 символов", "Неактуальная ошибка"
    for i in range(40):
        firstname.send_keys('\uE003')

def test13():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("иван") #в value отображается с маленькой буквы, фронт автоматически меняет на большую (Иванов), поэтому assert ждет "иванов"
    firstname_check = firstname.get_attribute("value")
    assert firstname_check == "иван"
    for i in range(6):
        firstname.send_keys('\uE003')

def test14():
    firstname = browser.find_element(By.CSS_SELECTOR, value="#firstname.registration-first__input")
    highlight(firstname)
    firstname.send_keys("Петр")
    firstname_check = firstname.get_attribute("value")
    assert firstname_check == "Петр", "Если не Петр тогда все сломалось"

def test15():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys(" ")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Первый символ не может быть пробелом", "Неактуальная ошибка"

def test16():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("12345")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test17():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("!@#$%^&*")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test18():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("qwertyasdzxc")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите русские символы", "Неактуальная ошибка"

def test19():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("Ааааааааааааааааааааааааааааааааааааааааа")
    first_input_error = browser.find_element(By.CSS_SELECTOR, value=".registration-first__input-error")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Введите не более 35 символов", "Неактуальная ошибка"
    for i in range(40):
        middlename.send_keys('\uE003')

def test20():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("иванович") #в value отображается с маленькой буквы, фронт автоматически меняет на большую (Иванов), поэтому assert ждет "иванов"
    middlename_check = middlename.get_attribute("value")
    assert middlename_check == "иванович"
    for i in range(8):
        middlename.send_keys('\uE003')

def test21():
    middlename = browser.find_element(By.CSS_SELECTOR, value="#middleName.registration-first__input")
    highlight(middlename)
    middlename.send_keys("Петрович")
    middlename_check = middlename.get_attribute("value")
    assert middlename_check == "Петрович", "Если не Петрович тогда все сломалось"

def test22():
    checkboxfemale = browser.find_element(By.XPATH, value="//*[@id='female']/label")
    highlight(checkboxfemale)
    checkboxfemale.click()
    checkboxfemalecheck = checkboxfemale.get_attribute("class")
    assert checkboxfemalecheck == "registration-step1__form-radio-button-label checked"

def test23():
    checkboxmale = browser.find_element(By.XPATH, value="//*[@id='male']/label")
    highlight(checkboxmale)
    checkboxmale.click()
    checkboxfemalecheck = checkboxmale.get_attribute("class")
    assert checkboxfemalecheck == "registration-step1__form-radio-button-label checked"

def test24():
    button = browser.find_element(By.CSS_SELECTOR, value="#nextStep")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    highlight(button)

    birthdate = browser.find_element(By.CSS_SELECTOR, value="#birthDate")
    highlight(birthdate)
    for i in range(8):
        birthdate.send_keys('\uE003')
    birthdate.send_keys("32-13-2023")
    button.click()
    first_input_error = browser.find_element(By.XPATH, value="//*[@id='__next']/section/div[4]/div[4]/p[1]")
    first_input_error_get_text = first_input_error.text
    assert first_input_error_get_text == "Неверный формат поля «Дата Рождения»"




    time.sleep(3)
    browser.quit()

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()
    test18()
    test19()
    test20()
    test21()
    test22()
    test23()

#Pytest SecondPage_Lastname.py