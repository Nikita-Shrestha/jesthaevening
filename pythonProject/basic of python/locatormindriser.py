#path locator create and post module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url
website_url="https://www.mindrisers.com.np/"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
time.sleep(2)
#find the form webelement by their xpath
dropdown_element = driver.find_element(By.ID, 'course')
# Create a Select object
select = Select(dropdown_element)
# Select by value attribute
select.select_by_value("2")
full_name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[6]/div/div/form/div[2]/input')
email_field=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[6]/div/div/form/div[3]/input')
phone_number=driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[6]/div/div/form/div[4]/input')
# submit_button=driver.find_element(By.ID,"submit")
#fill the form
full_name.send_keys("Ram")
email_field.send_keys("Ram@gmail.com")
phone_number.send_keys("98000")
# submit_button.click()
time.sleep(4)
# extract webpage title
website_title = driver.title
print(f"Website title:{website_title}")
#close the webdriver
driver.quit()