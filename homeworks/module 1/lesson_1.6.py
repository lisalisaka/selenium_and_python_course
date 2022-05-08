import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.ID, "submit_button")
    button.click()
    time.sleep(5)

finally:
    browser.quit()