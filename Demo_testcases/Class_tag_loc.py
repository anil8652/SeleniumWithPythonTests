from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))

for lin in links:
    print(lin.text)

driver.close()
