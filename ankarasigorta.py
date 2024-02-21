from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_driver_path = "/usr/local/bin/chromedriver"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver  = webdriver.Chrome(service=service)

driver.get("https://online.ankarasigorta.com.tr/")

time.sleep(5)

image = driver.find_element(By.CLASS_NAME, 'captcha-image')
image.screenshot("images/ankarasigorta/ankarasigorta1.png")
refresh_button = driver.find_element(By.CLASS_NAME, 'btn-refresh')
refresh_button.click()
time.sleep(5)
driver.quit()

