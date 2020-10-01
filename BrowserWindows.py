from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("(//button[@class='btn btn-info'][contains(.,'click')])[1]").click()
print(driver.current_window_handle)

handles = driver.window_handles

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames & windows":
        driver.close()

driver.quit()
