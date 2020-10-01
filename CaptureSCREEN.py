from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.get("https://www.amazon.in/")
driver.save_screenshot("D:\Pic\homepage.png")