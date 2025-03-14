import allure
from allure_pytest.utils import allure_title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Verify Button Count")
def test_button_count():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    buttons = driver.find_element(By.TAG_NAME,"button")
    print(len(buttons))
    for i in buttons:
       print(i.text)

    time.sleep(10)
    driver.quit()
