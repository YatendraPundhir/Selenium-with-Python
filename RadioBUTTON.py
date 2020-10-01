from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.maximize_window()

status = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected() # MALE
print(status)

button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')

driver.execute_script("arguments[0].click();", button)

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Gender is selected",status)
