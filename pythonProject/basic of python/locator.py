#path locator create and post module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url
website_url="https://demoqa.com/text-box"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
time.sleep(2)
#find the form webelement by their xpath
full_name=driver.find_element(By.XPATH,"//input[@id='userName']")
email_field=driver.find_element(By.XPATH,"//input[@id='userEmail']")
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
permanent_address=driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
submit_button=driver.find_element(By.ID,"submit")
#fill the form
full_name.send_keys("Ram")
email_field.send_keys("Ram@gmail.com")
current_address.send_keys("Kathmandu")
permanent_address.send_keys("Lalitpur")
submit_button.click()
time.sleep(4)
# extract webpage title
website_title = driver.title
print(f"Website title:{website_title}")
#close the webdriver
driver.quit()