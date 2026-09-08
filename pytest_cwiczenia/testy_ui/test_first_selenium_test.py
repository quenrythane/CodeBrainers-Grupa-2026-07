from selenium import webdriver
from selenium.webdriver.common.by import By  # Pozwala szukać elementów strony
from selenium.webdriver.common.keys import Keys  # Pozwala wpisywać klawiaturą teksty do pól

# id="username"
# id="password"
# type="submit"

driver = webdriver.Chrome()
URL = "http://127.0.0.1:8000"
driver.get(URL)

print(driver.title)
input("Wciśnij ENTER, aby zamknąć przeglądarkę")

# POM - Page Object Model
username_input_locator = (By.ID, "username")
username_input_element = driver.find_element(*username_input_locator)


# username_input_locator # -> (By.ID, "username")  # "zwraca worek / folder"
# *username_input_locator # -> By.ID, "username"  # "rozpakowywuje worek / folder i zwraca elementy / pliki"

# driver.find_element(username_input_locator).send_keys("admin")  # to nie zadziała
username_input_element.send_keys("admin")  # to zadziała bo ma gwiazdkę
driver.find_element(By.ID, "password").send_keys("admin")

input("2 Wciśnij ENTER, aby zamknąć przeglądarkę")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

input("3 Wciśnij ENTER, aby zamknąć przeglądarkę")

