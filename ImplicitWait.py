from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")   # website URL
driver.implicitly_wait(5)
assert "Mercury Tours" in driver.title
#print(driver.title)
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("submit").click()

driver.quit()