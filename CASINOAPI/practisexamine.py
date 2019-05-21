from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://wikipedia.org')
#elm = browser.find_element_by_link_text('English')
elm = browser.find_element_by_xpath("/html/body/div[1]/div[1]/a/strong")
elm.click()
print(browser.current_url)
print('Done')