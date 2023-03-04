from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest



list_of_links=['https://stepik.org/lesson/236895/step/1',
            'https://stepik.org/lesson/236896/step/1',
            'https://stepik.org/lesson/236897/step/1',
            'https://stepik.org/lesson/236898/step/1',
            'https://stepik.org/lesson/236899/step/1',
            'https://stepik.org/lesson/236903/step/1',
            'https://stepik.org/lesson/236904/step/1',
            'https://stepik.org/lesson/236905/step/1']

#list_of_links=['https://stepik.org/lesson/236895/step/1']

@pytest.mark.parametrize('link',list_of_links)
def test_login_stepik(browser, link):
    browser.implicitly_wait(5)
    browser.get(link)
    print('\nfind element to click')
    enter=browser.find_element(By.ID, 'ember33')
    enter.click()
    login=browser.find_element(By.CSS_SELECTOR, '[name="login"]')
    login.send_keys('nastya_d1199@mail.ru')
    password=browser.find_element(By.CSS_SELECTOR, '[name="password"]')
    password.send_keys('123456Ad')
    enter_button=browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    enter_button.click()
    time.sleep(10)
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.attempt textarea'))
    )
    input_field = browser.find_element(By.CSS_SELECTOR, '.attempt textarea')
    input_field.click()
    try:
        answer = math.log(int(time.time()))
        input_field.send_keys(str(answer))
    except:
        again_button = browser.find_element(By.CLASS_NAME, 'again-btn')
        again_button.click()
        WebDriverWait(browser, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.attempt textarea'))
        )
        input_field = browser.find_element(By.CSS_SELECTOR, '.attempt textarea')
        input_field.click()
        answer = math.log(int(time.time()))
        input_field.send_keys(str(answer))
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.attempt__actions button'))
    )
    answer_button = browser.find_element(By.CSS_SELECTOR, '.attempt__actions button')
    answer_button.click()
    WebDriverWait(browser, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'smart-hints__hint'))
    )
    result_file = browser.find_element(By.CLASS_NAME, 'smart-hints__hint')

    assert result_file.text == 'Correct!', f'Text in result_filed is {result_file.text}'

    time.sleep(10)


#command to run  py -m pytest -v fixture_files/test_authorization.py