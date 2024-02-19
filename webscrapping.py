import os
import requests
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64

# Set the path to the chromedriver
chrome_driver_path = "/usr/local/bin/chromedriver"

# Create a new instance of the Chrome driver
service = webdriver.chrome.service.Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the website
driver.get("https://axatek.axasigorta.com.tr/login")

# Wait for the page to load
time.sleep(5)

# Find the image element
# Get the source of the image
for x in range(6000):
    try:
        image = driver.find_element(By.XPATH, '//*[@id="inspire"]/div/main/div/div/div/div/div[3]/div/form/div[4]/div/div/div[1]/div/img')
        src = image.get_attribute('src')
        image_data = base64.b64decode(src.split(',')[1])

        img = Image.open(BytesIO(image_data))
        project_dir = os.path.dirname(os.path.abspath(__file__))
        save_dir  = os.path.join(project_dir, "media","axasigorta")
        save_path = os.path.join(save_dir, f"captcha{x}.png")
        # Save the image
        img.save(save_path)

        print("Image saved", save_path)
        refresh_button = driver.find_element(By.XPATH, '//*[@id="inspire"]/div/main/div/div/div/div/div[3]/div/form/div[4]/div/div/div[2]/button/span')
        refresh_button.click()
        time.sleep(2)

    except Exception as e:
        print(e)
        break

# Close the browser
driver.quit()
