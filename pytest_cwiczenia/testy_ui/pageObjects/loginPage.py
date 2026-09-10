from selenium.webdriver.common.by import By  # Pozwala szukać elementów strony
from selenium.webdriver.common.keys import Keys  # Pozwala wpisywać klawiaturą teksty do pól
import pytest
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class LoginPage:
    def __init__(self, driver, wait):
        """
        Tutaj inicjalizujemy drivera i waita które pobierane są z pliku conftest.py
        """
        self.driver = driver
        self.wait = wait
        self.logger = logging.getLogger(__name__)
        self.URL = "http://127.0.0.1:8000"


    # Lokatory strony
    """
    Tutaj są wszystkie locatory.
    Lokator to nic innego jak adres elementu na stronie internetowej po którym selenium znajduje dany element.
    """
    username_input_locator = (By.ID, "username")
    password_input_locator = (By.ID, "password")
    submit_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    form_card_locator = (By.ID, "formCard")

    # Metody
    """
    Tutaj są wszystkie metody.
    Metoda to nic innego jak funkcja która wykonuje daną operację.
    W każdej metodzie zaszywamy technikalnia potrzebne do wykonania operacji przez selenium.
    np enter_username ma wbudowanego w sobie:
        1. loggera,
        2. inteligentnego czekacza który czeka na znalezienie elementu (to o co pytał Kuba na ostanich zajęciach)
        3. Na wszelki wypadek czyści teskt w polu input
        4. Wpisuje teskt w puste pole (wiemy ze jest puste bo krok wcześniej je czyścimy)
    Czyli w skrócie - każda metoda ma mnóstwo rzeczy o których normalnie musielibyśmy pamiętać.
    A dzięki temu że są w jednym pliku odpowiedzialnym za daną stronę, to ten plik "pamięta za nas" o tych wszystkich rzeczach.
    Dzięki temu potem test może wyglądać super prosto i elegancko:
    """

    def open(self):
        self.logger.info("Otwieram strone")
        self.driver.get(self.URL)

    def enter_username(self, username):
        # logger który wypisuje informacje o danym kroku
        self.logger.info(f"Wpisuje login {username}")
        # inteligentne czekanie na element
        username_input = self.wait.until(
            EC.visibility_of_element_located(self.username_input_locator)
        )
        # czyszczenie pola input - dzięki temu przed wpisaniem treści zabezpieczamy się że to pole będzie puste
        username_input.clear()
        # wpisywanie tekstu
        username_input.send_keys(username)

    def enter_password(self, password):
        self.logger.info(f"Wpisuje haslo {password}")
        password_input = self.wait.until(
            EC.visibility_of_element_located(self.password_input_locator)
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_submit_button(self):
        self.logger.info("Klikam przycisk submit")
        submit_button = self.wait.until(
            EC.visibility_of_element_located(self.submit_button_locator)
        )
        submit_button.click()

    def is_form_card_displayed(self):
        self.logger.info("Sprawdzam czy karta jest wyswietlona")
        return self.wait.until(
            EC.visibility_of_element_located(self.form_card_locator)
        ).is_displayed()
