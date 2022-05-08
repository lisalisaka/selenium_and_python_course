from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(x))))

#Открыть страницу
link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

try:
 #Считать значение для переменной x
 x = int(browser.find_element(By.ID, 'input_value').text)
 #Посчитать математическую функцию от x
 y = calc(x)
 #Проскроллить страницу вниз
 input = browser.find_element(By.ID, "answer")
 browser.execute_script("return arguments[0].scrollIntoView(true);", input)
 #Ввести ответ в текстовое поле
 input.send_keys(y)
 #Выбрать checkbox "I'm the robot"
 checkbox = browser.find_element(By.ID, 'robotCheckbox')
 checkbox.click()
 #Переключить radiobutton "Robots rule!".
 radio = browser.find_element(By.ID, 'robotsRule')
 radio.click()
 #Нажать на кнопку "Submit".
 button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
 button.click()
 time.sleep(1)
finally:
 # ожидание чтобы визуально оценить результаты прохождения скрипта
 time.sleep(10)
 # закрываем браузер после всех манипуляций
 browser.quit()