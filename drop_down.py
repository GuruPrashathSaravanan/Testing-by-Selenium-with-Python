from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import logging
import time

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)
dropdown =driver.find_element(By.CSS_SELECTOR,"a[href='/dropdown']").click()
time.sleep(5)
select=driver.find_element(By.ID,"dropdown").click()
time.sleep(2)
""" options=driver.find_element(By.XPATH,'//[text()="option1"]').click()
time.sleep(10)"""
option=driver.find_element(By.XPATH,"//option[@value='1']").click()
print("Selected Option 1")
time.sleep(10)