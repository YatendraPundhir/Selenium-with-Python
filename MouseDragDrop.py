from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

element = driver.find_element_by_xpath("//div[contains(@id,'box7')]")
t_element = driver.find_element_by_xpath("//div[@class='dragableBoxRight'][contains(.,'Italy')]")
actions = ActionChains(driver)
actions.drag_and_drop(element,t_element).perform()

time.sleep(10)
driver.quit()
