#path locator create and post module

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#get the website url
website_url="https://demoqa.com/automation-practice-form"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
#caculate the height of page
page_height=driver.execute_script("return document.body.scrollHeight")
#scroll the page
scroll_speed=200
scroll_iteration=int(page_height/scroll_speed)
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
time.sleep(0.5)
#wait for the page load
driver.implicitly_wait(10)
#fields  locator xpath
first_name=driver.find_element(By.XPATH,"//input[@id='firstName']")
last_name=driver.find_element(By.XPATH,"//input[@id='lastName']")
email_field=driver.find_element(By.XPATH,"//input[@id='userEmail']")
gender_button_female=driver.find_element(By.XPATH,"//label[normalize-space()='Female']")
mobile_number=driver.find_element(By.XPATH,"//input[@id='userNumber']")
date_of_birth=driver.find_element(By.XPATH,"//div[@id='dateOfBirth']")

#select hobbies
hobby_sport_checkbox=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//label[normalize-space()='Music']")))
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
#pass the value
first_name.send_keys("ram")
last_name.send_keys("thapa")
email_field.send_keys("test@gmail.com")
gender_button_female.click()
mobile_number.send_keys("09808")
date_of_birth.send_keys("07/14/2004")
#interact with the checkbox
driver.execute_script("arguments[0].click();",hobby_sport_checkbox)
time.sleep(5)
current_address.send_keys("Kathmandu")
print("successfully run date and check module")
#close the webdriver instance
driver.close()


