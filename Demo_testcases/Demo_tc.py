# we are using selenium version 4
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
print("logged in successfully")

act_title = driver.title
exp_title = "Swag Labs"

if act_title == exp_title:
    print("Login test is passed + Title is verified ")
else:
    print("Login test is failed")
