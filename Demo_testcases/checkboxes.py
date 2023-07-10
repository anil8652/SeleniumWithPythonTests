import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://total-qa.com/checkbox-example/")
driver.maximize_window()

#selecting single checkbox
# driver.find_element(By.XPATH,'//*[@id="post-3261"]/div/p/input[1]').click()
# time.sleep(10)

# selecting all checkboxes
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and @name='chk']")
# print(len(checkboxes))
print(checkboxes)
#approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#approach 2
# for checkbox in checkboxes:
#     checkbox.click()

time.sleep(10)
driver.quit()