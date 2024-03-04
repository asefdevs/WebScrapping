from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

chrome_driver_path = "/usr/local/bin/chromedriver"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver  = webdriver.Chrome(service=service)


def image_scrapping(url, find_method, find_photo, find_button, location, filename, loop=1):
    driver.get(url)
    for i in range(loop):
            random_name = random.random()
            time.sleep(5)
            if find_method == "class":
                image = driver.find_element(By.CLASS_NAME, find_photo)
                refresh_button = driver.find_element(By.CLASS_NAME, find_button)
            elif find_method == "id":
                image = driver.find_element(By.ID, find_photo)
                refresh_button = driver.find_element(By.ID, find_button)


            image.screenshot(f"images/{location}/{filename}{i}{random_name}.png")
            refresh_button.click()
    driver.quit()
ankara_link = "https://online.ankarasigorta.com.tr/"
ankara_find_method = "class"
ankara_find_photo = "captcha-image"
ankara_find_button = "btn-refresh"
ankara_location = "ankara"
ankara_filename = "ankara"


somposigorta_link = "https://ejento.somposigorta.com.tr/"
somposigorta_find_method = "id"
somposigorta_find_photo = "capthcaLogin_IMG"
sompos_find_button = "capthcaLogin_RTS"
somposigorta_location = "sompos"
somposigorta_filename = "sompos"

axatek_link = "https://axatek.axasigorta.com.tr/login"
axatek_find_method = "class"
axatek_find_photo = "char-list-img"
axatek_find_button = "v-btn__content"
axatek_location = "axateks"
axatek_filename = "axatek"

# image_scrapping(ankara_link, ankara_find_method, ankara_find_photo, ankara_find_button, ankara_location, ankara_filename, 1)
# image_scrapping(somposigorta_link, somposigorta_find_method, somposigorta_find_photo, sompos_find_button, somposigorta_location, somposigorta_filename, 1)
image_scrapping(axatek_link, axatek_find_method, axatek_find_photo, axatek_find_button, axatek_location, axatek_filename, 1)

