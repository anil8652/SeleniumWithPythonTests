from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# driver.find_element(By.ID, "user-name").send_keys("problem_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button")
# act_title = driver.title
# exp_title = "Swag Labs"
# if act_title == exp_title:
#     print("Logged in successfully")
# else:
#     print("Login test is failed")

driver.find_element(By.LINK_TEXT, "Register").click()

driver.close()
