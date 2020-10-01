# INPUT BOX

# RADIO BUTTON

# CHECKBOX

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import  Select

#Chrome Browser
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
driver.maximize_window()

driver.find_element(By.CLASS_NAME,'text_field')

status = driver.find_element_by_id('RESULT_TextField-1').is_displayed()
print(status)
status = driver.find_element_by_id('RESULT_TextField-1').is_enabled()
print(status)

driver.find_element(By.ID,'RESULT_TextField-1').send_keys('Yatendra')
driver.find_element(By.ID,'RESULT_TextField-2').send_keys('Singh')
driver.find_element(By.ID,'RESULT_TextField-3').send_keys('9999999999')
driver.find_element(By.ID,'RESULT_TextField-4').send_keys('INDIA')
driver.find_element(By.ID,'RESULT_TextField-5').send_keys('Delhi')
driver.find_element(By.ID,'RESULT_TextField-6').send_keys('abcd@gmail.com')

# *******************RADIO BUTTON***********************************************************

status = driver.find_element_by_id('RESULT_RadioButton-7_0').is_selected() # MALE
print(status)

button = driver.find_element_by_xpath('//*[@id="RESULT_RadioButton-7_0"]')
driver.execute_script("arguments[0].click();", button)

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print("Gender is selected",status)

# **********************CHECK BOX************************************************************

Check1 = driver.find_element_by_xpath('//*[@id="RESULT_CheckBox-8_0"]')
driver.execute_script("arguments[0].click();", Check1)

# ***********************DROP DOWN ***********************************************************

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# Select dropdown by visible text
#drp.select_by_visible_text('Morning')

#Select dropdown by index
#drp.select_by_index(2)

#Select drop down by Value
drp.select_by_value("Radio-2")

#Count number of options
print(len(drp.options))

#Capture all options and print them '

a = drp.options
for options in a:
    print(options.text)

time.sleep(5)
driver.quit()





