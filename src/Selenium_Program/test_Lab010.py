import allure
from allure_pytest.utils import allure_title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Print titles on ebay")
def test_ebay_title():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")

    search_box_input = driver.find_element(By.XPATH,"//input[@placeholder='Search for anything']")
    search_box_input.send_keys("macmini")


    #class ="gh-search-button__label" > Search < / span >
    search_box_button = driver.find_element(By.CLASS_NAME,"gh-search-button__label")
    search_box_button.click()

    list_of_items = driver.find_elements(By.XPATH,"//input[@class='.s-item__title']")
    for i in list_of_items:
       print(i.text)
       #print(list_of_items)

    #assert len(list_of_items) == 62

    time.sleep(5)
    driver.quit()