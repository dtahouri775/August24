from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ...
url = "https://dev06.xcl.ie/casino/lobby/slots"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 100)

wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listing-item__title')))
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'listing-item__price')))

for elm in driver.find_elements_by_css_selector(".listing-item__title,.listing-item__price"):
    print(elm.text)