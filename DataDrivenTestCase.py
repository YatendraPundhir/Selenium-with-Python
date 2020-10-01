import xlutils
import openpyxl
from selenium import webdriver
from openpyxl import load_workbook

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path = "D:\Pic\Login1.xlsx"

rows = xlutils.getrowcount(path,'Sheet1')

for r in range(2,rows+1):
    username = xlutils.readData(path,"Sheet1",r,1)
    password = xlutils.readData(path,"Sheet1",r,2)

driver.find_element_by_name("userName").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_name("Submit").click()



