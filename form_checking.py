from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import logging
import time
logging.basicConfig(filename="error_log.txt",level=logging.ERROR)
url="http://127.0.0.1:5500/main.html"
driver=webdriver.Chrome()
driver.get(url)

try:
    driver.find_element(By.ID,"usernae")
except NoSuchElementException as e:
    logging.error(f"NoSuchElementException: {e}")

username=driver.find_element(By.ID,"username")
password=driver.find_element(By.ID,"password")
username.send_keys("Arunbalaji")
password.send_keys("random79")
login_btn=driver.find_element(By.ID,"loginBtn")
login_btn.send_keys(Keys.RETURN)
cancel_btn=driver.find_element(By.NAME,"cancelBtn")
cancel_btn.send_keys(Keys.RETURN)
time.sleep(1000)