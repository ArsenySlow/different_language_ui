import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_for_adding_to_basket(browser):
    browser.get(link)
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(10)
    time.sleep(10)
    assert browser.find_elements(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket"),'Ничего не нашлось'

