import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2Fsearch%3Fq%3Dapple%2Bmacbook")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(10)

# close single window
driver.close()

#close multiple windows
driver.quit()