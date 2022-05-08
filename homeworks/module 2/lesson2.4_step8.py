from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
 WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
 browser.find_element(By.ID, 'book').click()
 x = int(browser.find_element(By.ID, 'input_value').text)
 #Посчитать математическую функцию от x
 y = calc(x)
 input = browser.find_element(By.ID, "answer")
 input.send_keys(y)
 browser.find_element(By.ID, 'solve').click()
finally:
 time.sleep(10)
 browser.quit()