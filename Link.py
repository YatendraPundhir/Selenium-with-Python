from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")
links = driver.find_elements_by_tag_name("a")
print("number of links are",len(links))

for link in links:
    print(link.text)
