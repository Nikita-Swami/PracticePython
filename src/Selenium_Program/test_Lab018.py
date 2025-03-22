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
@allure.description("Verify Drag and Drop")
def test_actions_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag_element = driver.find_element(By.ID,"draggable")
    drop_element = driver.find_element(By.ID,"droppable")

    ActionChains(driver).drag_and_drop(drag_element,drop_element).perform()

    time.sleep(10)
    driver.quit()
