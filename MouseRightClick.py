from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


rclickbtn = driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(rclickbtn).perform()
time.sleep(2)
cutbtn = driver.find_element(By.XPATH,"/html/body/ul/li[2]")
cutbtn.click()

time.sleep(10)
driver.quit()