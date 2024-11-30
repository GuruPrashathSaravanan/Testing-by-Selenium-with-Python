from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import logging
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(5) 
frame= driver.find_element(By.CSS_SELECTOR,"a[href='/frames']")
frame.click() 
time.sleep(5)
nestedframe=driver.find_element(By.CSS_SELECTOR,"a[href='/nested_frames']")
nestedframe.click()



"""  # Switch to frame
driver.switch_to.frame("frame1")
print("Inside Frame")
driver.switch_to.default_content()  # Switch back to main content
print("Outside Frame")
 """