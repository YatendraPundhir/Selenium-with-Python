from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://www.freelancer.in/post-project")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,"NativeElement ng-pristine ng-invalid ng-star-inserted ng-touched").send_keys("Please subscribe  you are new to the channel")
