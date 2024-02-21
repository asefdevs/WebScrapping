from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = "/usr/local/bin/chromedriver"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver  = webdriver.Chrome(service=service)
driver.get("https://axatek.axasigorta.com.tr/login")

time.sleep(5)

image = driver.find_element(By.CLASS_NAME, 'char-list-img')
image.screenshot("axatek.png")
driver.quit()

