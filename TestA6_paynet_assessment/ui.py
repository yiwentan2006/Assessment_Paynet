import os
import time
import pytest
from selenium import webdriver

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.facebook.com/")
time.sleep(10)

# init()

@pytest.mark.parametrize(
    "username,password",
    [("user@gmail.com", "123456")])

def test_login(username,password):
    print("start test")
    driver.find_element_by_id("email").send_keys(username)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("u_0_b").click()




