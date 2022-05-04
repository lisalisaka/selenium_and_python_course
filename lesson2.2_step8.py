from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#Открыть страницу
link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
 browser.find_element(By.NAME, 'firstname').send_keys("Ivan")
 browser.find_element(By.NAME, 'lastname').send_keys("Ivanov")
 browser.find_element(By.NAME, 'email').send_keys("Ivan@inan.com")
 current_dir = os.path.abspath(os.path.dirname(__file__))
 file_path = os.path.join(current_dir, '1.txt')
 send = browser.find_element(By.ID, 'file')
 send.send_keys(file_path)
 browser.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
 time.sleep(1)
  
finally:
 time.sleep(5)
 browser.quit()
 