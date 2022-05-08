from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

link = "http://suninjuly.github.io/find_link_text"

try:
 browser = webdriver.Chrome()
 browser.get(link)
 value = str(math.ceil(math.pow(math.pi, math.e)*10000))
 link = browser.find_element(By.PARTIAL_LINK_TEXT, value)
 link.click()
 input1 = browser.find_element(By.TAG_NAME, "input")
 input1.send_keys("Ivan")
 input2 = browser.find_element(By.NAME, "last_name")
 input2.send_keys("Petrov")
 input3 = browser.find_element(By.CLASS_NAME, "city")
 input3.send_keys("Smolensk")
 input4 = browser.find_element(By.ID, "country")
 input4.send_keys("Russia")
 button = browser.find_element(By.CSS_SELECTOR, "button.btn")
 button.click()
 
finally:
    time.sleep(15)
    browser.quit()