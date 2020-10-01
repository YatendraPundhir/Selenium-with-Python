from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")   # website URL

print(driver.title) #title of the website

driver.get("http://freecrm.com")   # website URL

print(driver.title) #title of the website
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
driver.quit()