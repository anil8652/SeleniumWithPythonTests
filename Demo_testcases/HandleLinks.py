import requests as requests

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
allLinks = driver.find_elements(By.TAG_NAME,"a")
num=0

for link in allLinks:
    Url=link.get_attribute("href")
    try:
        res=requests.head(Url)
    except:
        None

    if res.status_code>=400:
        print(Url,"  is broken link")
        num+= 1
    else:
        print(Url,"  is valid link")


print("Total no.of broken links",num)
