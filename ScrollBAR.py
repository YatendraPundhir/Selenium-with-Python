from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import  Select

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. Scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")

# 2. Scroll down page till the element is visible
#flag = driver.find_element_by_xpath("//img[contains(@alt,'Flag of India')]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)

# 3. Scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(3)
driver.quit()