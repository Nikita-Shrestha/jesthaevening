# import the necessary modules for edge
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
#set the chrome driver manager
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#set the website
website_url='https://www.mindrisers.com.np/'
#get the website
driver.get(website_url)
time.sleep(3)
# max the window size
driver.maximize_window()
time.sleep(3)
#calculate the height of the web page
page_height=driver.execute_script("return document.body.scrollHeight")
#scroll down the content
scroll_speed=100
scroll_iterations=int(page_height/scroll_speed)
#loop the iteration performance
for _ in range(scroll_iterations):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(1)
#print the title
website_title=driver.title
print(f"Website title:{website_title}")
print("code run successfully")
#close the webdriver instance
driver.quit()
driver.close()

