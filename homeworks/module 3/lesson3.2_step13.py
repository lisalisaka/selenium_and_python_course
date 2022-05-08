import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestRegistaration(unittest.TestCase):
    def test_registaration_1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        browser.find_element(By.CLASS_NAME, "first_block .first").send_keys("Ivan")
        browser.find_element(By.CLASS_NAME, "first_block .second").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "first_block .third").send_keys("Smolensk email")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element(By.TAG_NAME, value = "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"Test failed, got '{welcome_text}' instead of '{expected_text}'")
        browser.quit()
        
    def test_registaration_2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        browser.find_element(By.CLASS_NAME, "first_block .first").send_keys("Ivan")
        browser.find_element(By.CLASS_NAME, "first_block .second").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "first_block .third").send_keys("Smolensk email")
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element(By.TAG_NAME, value = "h1").text
        expected_text = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, expected_text, f"Test failed, got '{welcome_text}' instead of '{expected_text}'")
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()