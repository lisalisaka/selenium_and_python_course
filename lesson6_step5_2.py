from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"


def logi_link():
    global browser
    try:
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        browser.get(link)
        b = str(math.ceil(math.pow(math.pi, math.e) * 10000))
        link_1 = browser.find_element_by_link_text(b)
        link_1.click()
        input1 = browser.find_element_by_tag_name("input")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_name("last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_class_name("form-control.city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element_by_id("country")
        input4.send_keys("Russia")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    # не забываем оставить пустую строку в конце файла


logi_link()