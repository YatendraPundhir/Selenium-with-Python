from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")

#First Frame
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(4)
driver.switch_to.default_content()

#Second Frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
time.sleep(4)
driver.switch_to.default_content()

#Third Frame
time.sleep(4)
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]/a').click()

time.sleep(3)
driver.quit()

