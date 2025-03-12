from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def test_chrome_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://walkarootestv3.prowessbeat.net/")

    time.sleep(10)
    driver.quit()