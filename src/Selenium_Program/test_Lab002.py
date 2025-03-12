from selenium import webdriver
import allure
import pytest

@allure.title("Verify the title of the webpage")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://walkarootestv3.prowessbeat.net/")
    page_source_data = driver.page_source
    print(page_source_data)