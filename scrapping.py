from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "/usr/local/bin/chromedriver"
service = webdriver.chrome.service.Service(chrome_driver_path)
driver  = webdriver.Chrome(service=service)


def image_scrapping(url, find_method, find_photo, find_button, location, filename, loop=1):
    driver.get(url)
    for i in range(loop):
            time.sleep(5)
            if find_method == "class":
                image = driver.find_element(By.CLASS_NAME, find_photo)
                refresh_button = driver.find_element(By.CLASS_NAME, find_button)
            elif find_method == "id":
                image = driver.find_element(By.ID, find_photo)
                refresh_button = driver.find_element(By.ID, find_button)


            image.screenshot(f"images/{location}/{filename}{i}.png")
            refresh_button.click()
    driver.quit()
ankara_link = "https://online.ankarasigorta.com.tr/"
ankara_find_method = "class"
ankara_find_photo = "captcha-image"
ankara_find_button = "captcha-refresh"
ankara_location = "ankarasigorta"
ankara_filename = "ankarasigorta"


somposigorta_link = "https://ejento.somposigorta.com.tr/"
somposigorta_find_method = "id"
somposigorta_find_photo = "capthcaLogin_IMG"
sompos_find_button = "capthcaLogin_RTS"
somposigorta_location = "somposigorta"
somposigorta_filename = "somposigorta"

axatek_link = "https://axatek.axasigorta.com.tr/login"
axatek_find_method = "class"
axatek_find_photo = "char-list-img"
axatek_find_button = "v-btn__content"
axatek_location = "axatek"
axatek_filename = "axatek"

image_scrapping("https://online.ankarasigorta.com.tr/", "class", "captcha-image", "btn-refresh", "ankara", "ankarasigorta", 10)
