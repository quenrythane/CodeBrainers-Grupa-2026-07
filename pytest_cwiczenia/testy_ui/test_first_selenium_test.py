from selenium import webdriver
from selenium.webdriver.common.by import By  # Pozwala szukać elementów strony
from selenium.webdriver.common.keys import Keys  # Pozwala wpisywać klawiaturą teksty do pól
import pytest


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
    driver = webdriver.Chrome()
    driver.get(URL)

    username_input_locator = (By.ID, "username")
    username_input = driver.find_element(*username_input_locator)

    password_input_locator = (By.ID, "password")
    password_input = driver.find_element(*password_input_locator)

    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    submit_button = driver.find_element(*submit_button_locator)




    ## Act
    username_input.send_keys("admin")  # to zadziała bo ma gwiazdkę
    password_input.send_keys("admin")
    submit_button.click()
    input("Wciśnij ENTER, aby zamknąć przeglądarkę")


    ## Assert
    assert True


