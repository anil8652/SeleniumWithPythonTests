from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()
#css selector = tag & id   #syntax = tagName#id
# driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abe@gmail.com")  #where tagName is optional

#css selector = tag & class        #syntax = tagName.className  where as tagName is optional
# driver.find_element(By.CSS_SELECTOR, ".inputtext").send_keys("abc@gmail.com")


#css selector = tag & attribute   #syntax = tagName[attribute=value]
# driver.find_element(By.CSS_SELECTOR,"[aria-label=Password]").send_keys("abc@gmail.com")

# css selector = tag, class & attribute #syntax = tagName.className[attribute=value]
driver.find_element(By.CSS_SELECTOR, "input.inputtext[aria-label=Password]").send_keys("Anil@123")