from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
str_class_name = 'btn-add-to-basket'


def is_btn_present(driver, str_class_name):
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, str_class_name)))
    except (NoSuchElementException, TimeoutException):
        return False
    return True


def test_is_such_btn_add_to_basket(browser):
    browser.get(link)
    # time.sleep(30)
    assert is_btn_present(browser, str_class_name), "No such button add to basket"
