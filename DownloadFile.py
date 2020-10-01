from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

#Download TEXT File
driver.find_element_by_id("textbox").send_keys("testing download text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

#Download PDF File
driver.find_element_by_id("pdftbox").send_keys("testing download pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()