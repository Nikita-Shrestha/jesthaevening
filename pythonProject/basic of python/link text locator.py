#path locator create and post module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#set the chrome driver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#get the website url
website_url="https://merolagani.com/"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
time.sleep(2)
market=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(2)
#indices=driver.find_element(By.LINK_TEXT,"Indices")
#indices.click()
floorsheet=driver.find_element(By.LINK_TEXT,"Floorsheet")
floorsheet.click()
time.sleep(5)
print("successfully link the drop down menu")
#close the webdriver instance
driver.quit()