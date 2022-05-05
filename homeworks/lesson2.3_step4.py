from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

try: 
 #открыть страницу
 link = "http://suninjuly.github.io/alert_accept.html"
 browser = webdriver.Chrome()
 browser.get(link)
 #нажать на кнопку
 browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
 #Принять confirm
 browser.switch_to.alert.accept()
 #На новой странице решить капчу для роботов, чтобы получить число с ответом
 x = int(browser.find_element(By.ID, 'input_value').text)
 #Посчитать математическую функцию от x
 y = calc(x)
 input = browser.find_element(By.ID, "answer")
 input.send_keys(y)
 button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
 button.click()
 time.sleep(1)
finally: 
 time.sleep(5)
 browser.quit()