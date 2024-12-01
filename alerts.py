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
alert1=driver.find_element(By.CSS_SELECTOR,"a[href='/javascript_alerts']").click()
time.sleep(2)
driver.find_element(By.XPATH,("//button[@onclick='jsAlert()']")).click()
alert1=driver.switch_to.alert
print(alert1.text)
time.sleep(5)
alert1.accept()
time.sleep(5)