from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://www.facebook.com/")   # website URL

print(driver.title) #title of the website

# driver.close()






