import allure
from allure_pytest.utils import allure_title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Verify Register Account")
def test_awesome_qa_register_account():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    first_name_input_tag = driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
    first_name_input_tag.send_keys("Hello")


    time.sleep(5)
    driver.quit()