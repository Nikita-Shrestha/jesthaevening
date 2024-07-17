from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url = "https://www.mindrisers.com.np/contact-us"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
#find the form webelement by their xpath
full_name=driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
email=driver.find_element(*(By.XPATH,"//input[@placeholder='Email']"))
phone=driver.find_element(*(By.XPATH,"//input[@placeholder='Phone']"))
subject=driver.find_element(*(By.XPATH,"//input[@placeholder='Subject']"))
queries=driver.find_element(*(By.XPATH,"//textarea[@placeholder='Queries']"))
#fill the form
full_name.send_keys("Ram")
email.send_keys("ram@gmail.com")
phone.send_keys("9999")
subject.send_keys("english")
queries.send_keys("akaka")

time.sleep(2)

# finally quit the driver instance
driver.quit()



