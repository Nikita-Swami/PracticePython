import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_webtables():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()

    #//table[contains(@id,"cust")]/tbody/tr[2]/td
    row_elements = driver.find_elements(By.XPATH,"//table[contains(@id,'cust')]/tbody/tr")
    row = len(row_elements)
    print(row)

    col_elements = driver.find_elements(By.XPATH, "//table[contains(@id,'cust')]/tbody/tr[2]/td")
    col = len(col_elements)
    print(col)

    first_part = "//table[contains(@id,'cust')]/tbody/tr["
    second_part = "]/td["
    third_part = "]"

    for i in range(2, row+1):
        for j in range(1, col + 1):
            dynamic_path = f"{first_part}{i}{second_part}{j}{third_part}"
            data = driver.find_element(dynamic_path)
            print(data.text, end=" ")