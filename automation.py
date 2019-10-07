from selenium import webdriver
# Loading Chrome Browser driver
chrome_browser = webdriver.Chrome('./chromedriver')
# Opening Chrome Browser to Maximum size
chrome_browser.maximize_window()
# Linking to the url for the Browser to open at
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
# Making sure that we are at the correct website
assert 'Selenium Easy Demo' in chrome_browser.title
# Grabbing Text from the button object
show_message_button = chrome_browser.find_element_by_class_name("btn-default")

# button_text = chrome_browser.find_element_by_class_name('btn-default')
# print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source
# Grabbing the message box by its ID
user_message = chrome_browser.find_element_by_id('user-message')
# Grabbing the user button by its CSS selector
user_button = chrome_browser.find_elements_by_css_selector('#get-input.btn')
print(user_button)
# Clearing all past inputs in message
user_message.clear()
# Inputing a test message
user_message.send_keys('I am extra cool')
# Clicks the button to submit the message
show_message_button.click()
# Testing to make sure that the button and message was clicked/sent
output_message = chrome_browser.find_element_by_id('display')
assert 'I am extra cool' in output_message.text

# Commands to quit the Chrome Browser instances
#chrome_browser.close()
chrome_browser.quit()