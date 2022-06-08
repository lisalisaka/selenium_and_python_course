link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_card_button_on_the_page(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assert button !=None , f"The is no button 'Card' on the page"