from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import  Select

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
driver.find_element_by_xpath("//button[@onclick='myFunction()'][contains(.,'Click Me')]").click()
time.sleep(5)
#driver.switch_to_alert().accept() # Close alert window using OK Button
driver.switch_to_alert().dismiss() # Close alert window using CLOSE Button


#time.sleep(10)
#driver.quit()