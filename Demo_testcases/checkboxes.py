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
print(len(checkboxes))
print(checkboxes)
#approach 1
# for i in range(len(checkboxes)):
#     checkboxes[i].click()

#approach 2
for checkbox in checkboxes:
    checkbox.click()

# Select Multiple checkbox by choice  (by Id)
# for checkbox in checkboxes:
#     checkName=checkbox.find_elements(By.NAME,"SELENIUM")
#     if checkName=="SELENIUM":
#         checkName.click()

# Select last two checkboxes
#totalno.of elements-2=starting index
#range(5,7)----> 6,7
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

#select first two checkboxes
# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()
time.sleep(5)
#Clearing all checkboxes or Deselcting all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

# time.sleep(10)
driver.quit()
