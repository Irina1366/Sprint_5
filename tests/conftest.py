import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from curl import *


@pytest.fixture(scope="function")

def driver():
    driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()