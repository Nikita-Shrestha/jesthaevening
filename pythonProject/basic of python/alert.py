from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url = "https://demoqa.com/alerts"
# get the website
driver.get(website_url)

# max the window size
driver.maximize_window()
#locate the element as
click_me=driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()
#switch to alert
alert=driver.switch_to.alert
time.sleep(2)

# finally quit the driver instance
driver.quit()



