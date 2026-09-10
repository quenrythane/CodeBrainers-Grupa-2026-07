import logging
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger(__name__)

@pytest.fixture
def driver_options():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--incognito")
    return options


@pytest.fixture
def driver(driver_options):
    logger.info("Otwieram przeglądarkę")
    driver = webdriver.Chrome(options=driver_options)
    yield driver
    logger.info("Zamykam przeglądarkę")
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 2)