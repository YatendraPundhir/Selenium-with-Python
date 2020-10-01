from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

driver.switch_to.frame(0)
driver.find_element_by_id("RESULT_FileUpload-10").send_keys("D:/Pic/1.png")