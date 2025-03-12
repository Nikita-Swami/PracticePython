from selenium import webdriver

def test_login_walkaroo():
    driver = webdriver.Chrome()
    driver.get("https://walkarootestv3.prowessbeat.net/")
    page_source_data = driver.page_source
    assert "Login" in page_source_data
    #assert driver.title == "Login"
    driver.quit()