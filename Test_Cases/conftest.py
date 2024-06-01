from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup():
    ser_obj = Service("D:\\Sofware\\Software_file\\chromedriver_win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)
    driver.implicitly_wait(20)
    driver.maximize_window()
    return driver