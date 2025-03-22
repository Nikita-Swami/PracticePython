from argparse import Action

import allure
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Action P4")
@allure.description("Verify Click and Hold")
def test_actions_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    element_to_hold = driver.find_element(By.ID,"draggable")

    time.sleep(2)

    actions = ActionChains(driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(10)
    driver.quit()