from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element_by_xpath("//button[@ondblclick='myFunction1()'][contains(.,'Copy Text')]")

actions = ActionChains(driver)

actions.double_click(element).perform()


time.sleep(10)
driver.quit()