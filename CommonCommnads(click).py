from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")   # website URL

print(driver.title) #title of the website
print(driver.current_url) #Return URL of the page
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
time.sleep(5)

#driver.close()

driver.quit()