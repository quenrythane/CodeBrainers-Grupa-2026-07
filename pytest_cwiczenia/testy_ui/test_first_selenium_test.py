from selenium import webdriver
from selenium.webdriver.common.by import By  # Pozwala szukać elementów strony
from selenium.webdriver.common.keys import Keys  # Pozwala wpisywać klawiaturą teksty do pól
import pytest
import logging

logger = logging.getLogger(__name__)


# input("Wciśnij ENTER, aby zamknąć przeglądarkę")
# pytest -m <marker> --html=reports/report.html --self-contained-html

# 1. zainstalować pytest-html -> pip install pytest-html==3.2.0
# 2. zamienić skrypt selenium na test
# 3. wykonać pytest z raportem -> pytest --html=reports/report.html --self-contained-html

@pytest.mark.ui_login
def test_ui_login():
    # POM - Page Object Model
    ## Arrange
    '''
    # username_input_locator # -> (By.ID, "username")  # "zwraca worek / folder"
    # *username_input_locator # -> By.ID, "username"  # "rozpakowywuje worek / folder i zwraca elementy / pliki"
    # driver.find_element(username_input_locator).send_keys("admin")  # to nie zadziała
    '''
    URL = "http://127.0.0.1:8000"
    logger.info("Uruchamiam przegladarke")
    driver = webdriver.Chrome()
    logger.info("Otwieram strone")
    driver.get(URL)

    logger.info("Znajduje pole username")
    username_input_locator = (By.ID, "username")
    username_input = driver.find_element(*username_input_locator)

    logger.info("Znajduje pole password")
    password_input_locator = (By.ID, "password")
    password_input = driver.find_element(*password_input_locator)

    logger.info("Znajduje przycisk Sign In")
    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    submit_button = driver.find_element(*submit_button_locator)




    ## Act
    logger.info("Wpisuje login admin")
    username_input.send_keys("admin")  # to zadziała bo ma gwiazdkę

    logger.info("Wpisuje haslo admin")
    password_input.send_keys("admin")

    logger.info("Klikam przycisk Sign In")
    submit_button.click()

    logger.info("Zamykam przeglądarkę")

    ## Assert
    assert True


