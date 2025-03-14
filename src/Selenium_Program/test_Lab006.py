import allure
from allure_pytest.utils import allure_title
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

@pytest.mark.negative
@allure_title("Negative TestCase")
@allure.description("Verify that email and password is wrong, we will get message")
def test_negative_vwo_login():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    #Verify Email
    #<input type="email" class="text-input W(100%)" name="username" id="login-username" data-qa="hocewoqisi" data-gtm-form-interact-field-id="0">
    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    #Verify Password
   #<input type="password" class="text-input W(100%)" name="password" id="login-password" data-qa="jobodapuxe">
    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("password@1234")

    #Verify Sign In Button
    #<button type="submit" id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)" data-qa="sibequkica">
	#<span class="icon loader hidden" data-qa="zuyezasugu"></span>
	#<span data-qa="ezazsuguuy">Sign in</span>
	#</button>

    submit_btn_web_element = driver.find_element(By.ID,"js-login-btn")
    submit_btn_web_element.click()

    #Wait for some time
    time.sleep(3)

    #Verify Message
    #<div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">Your email, password,
    # IP address or location did not match
    # </div>

    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"


    time.sleep(10)
    driver.quit()