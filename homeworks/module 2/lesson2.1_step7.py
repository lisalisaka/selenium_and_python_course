from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
 x1 = browser.find_element(By.ID, 'treasure')
 x = x1.get_attribute('valuex')
 y = calc(x)
 #вводим ответ в текстовое поле, предварительно находим его
 answer = browser.find_element(By.ID, 'answer')
 answer.send_keys(y)
 #ищем чек-бокс и отмечаем его
 checkbox = browser.find_element(By.ID, 'robotCheckbox')
 checkbox.click()
 #Выбрать radiobutton "Robots rule!"
 radio = browser.find_element(By.ID, 'robotsRule')
 radio.click()
 #Нажать на кнопку Submit.
 button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
 button.click()
 time.sleep(1)
finally:
 # ожидание чтобы визуально оценить результаты прохождения скрипта
 time.sleep(10)
 # закрываем браузер после всех манипуляций
 browser.quit()
