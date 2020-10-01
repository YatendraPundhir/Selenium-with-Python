from selenium import webdriver
from selenium.webdriver import ActionChains
import time

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()

driver.find_element_by_xpath("//input[contains(@name,'txtUsername')]").send_keys("Admin")
driver.find_element_by_xpath("//input[contains(@name,'txtPassword')]").send_keys("admin123")
driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
admin = driver.find_element_by_xpath("//b[contains(.,'Admin')]")
usermgt = driver.find_element_by_xpath("//a[contains(.,'User Management')]")
users = driver.find_element_by_xpath("//a[contains(.,'Users')]")

actions = ActionChains(driver)

actions.move_to_element(admin).move_to_element(usermgt).move_to_element(users).click().perform()

time.sleep(3)
driver.quit()
