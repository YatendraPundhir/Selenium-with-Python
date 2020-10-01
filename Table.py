from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://www.seleniumeasy.com/test/table-pagination-demo.html")
len(driver.find_element_by_xpath(("//th[contains(.,'Table heading 3')]"))
#clos=len(driver.find_elements_by_xpath("(//td[contains(.,'Table cell')])[1]"))


#print(clos)