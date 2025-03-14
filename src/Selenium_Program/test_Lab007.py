import allure
from allure_pytest.utils import allure_title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


@allure.description("Verify that Free Trial Button")
def test_start_free_trial():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    #Start a Free Trial
    #<a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>

    anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element.click()

    #driver.back()
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    driver.back()

    time.sleep(10)
    driver.quit()