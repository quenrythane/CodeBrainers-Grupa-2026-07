import pytest
from pageObjects.loginPage import LoginPage



@pytest.mark.ui_login
def test_ui_login(driver, wait):
    ## Arrange
    """ Pobieramy wszystkie "technikalia" z klasy LoginPage """
    loginPage = LoginPage(driver, wait)


    ## Act
    """ Dzięki temu że wszystkie technikalia są schowane w klasie LoginPage, to test wygląda super prosto i elegancko """
    loginPage.open()
    loginPage.enter_username("admin")
    loginPage.enter_password("admin")
    loginPage.click_submit_button()

    ## Assert
    """ logika asercji jest w LoginPage (to jest dyskusyjne - jeden tester powie że tak się robi, inny że tak się nie robi)
    Sam bym powiedział że tak się NIE robi, ale w tym przypadku takie użycie zwiększało czytelnosć"""
    assert loginPage.is_form_card_displayed()




