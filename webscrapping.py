import os
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



chrome_driver_path = "/usr/local/bin/chromedriver"

service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get("https://axatek.axasigorta.com.tr/login")

# Wait for the page to load
# time.sleep(5)

def save_captcha_image(driver, refresh_xpath, save_dir_u, x, photo_xpath=None):
    try:
        # Find the captcha image    
        # wait = WebDriverWait(driver, 10)
        # image = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="f405916fb284346e1b2e84fbf51085fb8"]/div[3]/div/img')))
        image = driver.find_element(By.CLASS_NAME, 'captcha-image')
        src = image.get_attribute('src')
        image_data = base64.b64decode(src.split(',')[1])
        img = Image.open(BytesIO(image_data))
        project_dir = os.path.dirname(os.path.abspath(__file__))
        save_dir = os.path.join(project_dir, "media",f"{save_dir_u}")
        save_path = os.path.join(save_dir, f"captcha{x}.png")
        # Save the image
        img.save(save_path)
        refresh_button = driver.find_element(By.CLASS_NAME, f'{refresh_xpath}')
        refresh_button.click()
        time.sleep(2)
    except Exception as e:
        print(e)
        return False
# for x in range(10):
#     save_captcha_image(driver, '//*[@id="inspire"]/div/main/div/div/div/div/div[3]/div/form/div[4]/div/div/div[1]/div/img', '//*[@id="inspire"]/div/main/div/div/div/div/div[3]/div/form/div[4]/div/div/div[2]/button/span', "axasigorta", x)

# driver.get("https://ejento.somposigorta.com.tr/")
# driver.get("https://axatek.axasigorta.com.tr/login")
driver.get("https://online.ankarasigorta.com.tr/")

time.sleep(15)


save_captcha_image(driver,'btn-refresh btn btn-default', "ankarasigorta", 0)
driver.quit()