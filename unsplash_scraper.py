from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import requests

#instance of the browser
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
URL= 'https://unsplash.com/'
driver.get(URL)
#the browser will close authomaticlaly
time.sleep(10)

# automatic scroll
height=0
for i in range(15):
    height = height+500
    driver.execute_script(f"window.scrollTo(0, {height});")
    time.sleep(1)

# get URL of the image
images_tag = driver.find_elements(By.XPATH, "//img[@class='tzC2N fbGdz cnmNG']")
images_urls = [img.get_attribute('src') for img in images_tag]

# download images
for index,url in enumerate(images_urls[:10]):
    reaponse = requests.get(images_urls[0], stream=True)

    with open(f'img-{index+1}.jpg', 'wb') as f:
        for chunk in reaponse.iter_content(chunk_size=128):
            f.write(chunk)


#quit browser
driver.close()

#why use request instead of selenium?
# because requests is very fast as compared to selenium