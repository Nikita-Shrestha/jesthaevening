
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
website_url="https://meroshare.cdsc.com.np/#/login"
# get the website
driver.get(website_url)
# max the window size
driver.maximize_window()
time.sleep(4)
drop_down=driver.find_element(*(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]"))
drop_down.click()
options_xpath="//li[contains(text(),'ASIAN CAPITAL LIMITED (17500)')]"
options=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,options_xpath)))
time.sleep(5)
print("successfully link the drop down menu")
#close the webdriver instance
driver.quit()