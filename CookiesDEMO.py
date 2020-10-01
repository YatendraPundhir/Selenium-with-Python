from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")
driver.get("https://www.amazon.in/")

# Capture cookie details
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# ADD  A NEW COOKIE TO THE BROWSER

cookie = {'name':'yatendracookie','value':'1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

# DELETE A COOKIE

driver.delete_cookie('yatendracookie')
time.sleep(3)
cookies = driver.get_cookies()
print(cookies)
print(len(cookies))

driver.quit()
