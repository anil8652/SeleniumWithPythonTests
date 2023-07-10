from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.com/")

driver.back()  #snapdeal
driver.forward()  #amazon
driver.refresh()

driver.quit()
