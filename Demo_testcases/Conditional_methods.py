from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register/")
driver.maximize_window()

#is_displayed  & is_enabled Methods
SearchBox = driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print("Display status:",SearchBox.is_displayed())
print("Display status:",SearchBox.is_enabled())


#is_selected method
male_rd = driver.find_element(By.XPATH,'//*[@id="gender-male"]')
female_rd = driver.find_element(By.XPATH, '//*[@id="gender-female"]')

print("male radio button status:",male_rd.is_selected())
print("femal radio button status:",female_rd.is_selected())


print("After selecting male radio button....")
male_rd.click()
print("male radio button status:",male_rd.is_selected())
print("femal radio button status:",female_rd.is_selected())


print("After selecting fe-male radio button....")
female_rd.click()
print("male radio button status:",male_rd.is_selected())
print("female radio button status:",female_rd.is_selected())