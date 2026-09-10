from selenium import webdriver
from selenium.webdriver.common.by import By  # Pozwala szukać elementów strony
from selenium.webdriver.common.keys import Keys  # Pozwala wpisywać klawiaturą teksty do pól
import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


logger = logging.getLogger(__name__)


@pytest.mark.ui_login_old
def test_ui_login_old():
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
    wait = WebDriverWait(driver, 2)
    logger.debug("Otwieram strone")
    driver.get(URL)

    logger.warning("Znajduje pole username")
    username_input_locator = (By.ID, "username")
    username_input = driver.find_element(*username_input_locator)

    logger.error("Znajduje pole password")
    password_input_locator = (By.ID, "password")
    password_input = driver.find_element(*password_input_locator)

    logger.critical("Znajduje przycisk Sign In")
    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    submit_button = driver.find_element(*submit_button_locator)

    form_card_locator = (By.ID, "formCard")


    ## Act
    logger.info("Wpisuje login admin")
    username_input.send_keys("admin")  # to zadziała bo ma gwiazdkę

    logger.info("Wpisuje haslo admin")
    password_input.send_keys("admin")

    logger.info("Klikam przycisk Sign In")
    submit_button.click()

    logger.warning("Zamykam przegladarke")

    ## Assert
    # form_card = driver.find_element(*form_card_locator)  # <- to nie zadziała, bo selenium za szybko tego szuka.
    # Przez co szuka tego elementu zanim on się załaduje - więc mówi nam że nie widzi takiego elemtnu
    # (bo w momencie gdy sprwadzał czy jest taki elelment tego elementu faktycnzie nie było)

    # Tutaj rozwiązanie: myślnik, czyli dodanie inteligentnego oczekacza, który sprawdzi, czy ten element już się załadował, i dopiero potem przepisze go do zmiennej.
    form_card = wait.until(
        EC.visibility_of_element_located(form_card_locator)
    )
    assert form_card.is_displayed()


