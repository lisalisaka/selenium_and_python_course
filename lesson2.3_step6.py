from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))
  
#открыть страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
 browser.find_element(By.CLASS_NAME, 'trollface.btn.btn-primary').click()
 new_window = browser.window_handles[1]
 browser.switch_to.window(new_window)
 x = int(browser.find_element(By.ID, 'input_value').text)
 #Посчитать математическую функцию от x
 y = calc(x)
 input = browser.find_element(By.ID, "answer")
 input.send_keys(y)
 button1 = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
 button1.click()
 time.sleep(1)
finally:
 time.sleep(15)
 browser.quit()
 