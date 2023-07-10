from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
#Absolute xpath
# driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/form/input")
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button" )

#Relative xpath
driver.find_element(By.XPATH,'//*[@id="small-searchterms"]').send_keys("Apple Macbook")
driver.find_element(By.XPATH,'//*[@id="small-search-box-form"]/button').click()