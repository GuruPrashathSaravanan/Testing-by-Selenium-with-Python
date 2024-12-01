from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import logging
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(5)
file_upload=driver.find_element(By.ID,"file-upload")
file_upload.send_keys(r"C:\Users\HP\OneDrive\Pictures\images.jpg")
upload_btn=driver.find_element(By.ID,"file-submit").click()

print(file_upload)
time.sleep(10)

