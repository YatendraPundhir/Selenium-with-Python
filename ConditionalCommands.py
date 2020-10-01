from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")   # website URL
UserName = driver.find_element_by_name("userName")
print(UserName.is_enabled())
print(UserName.is_enabled())

pwd = driver.find_element_by_name("password")
print(pwd.is_enabled())
print(pwd.is_enabled())

UserName.send_keys("mercury")
pwd.send_keys("mercury")

driver.find_element_by_name("submit").click()
print("Login Successfully,Thank you for Loggin. ")

driver.quit()