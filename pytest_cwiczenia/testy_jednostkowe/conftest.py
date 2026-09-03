import pytest


@pytest.fixture(autouse=True)
def funkcja_pomocnicza():
    print("\n Start testu")
    yield
    print("\n Koniec testu")


@pytest.fixture(scope="session", autouse=True)
def funkcja_pomocnicza_sesji():
    print("\n Start sesji testowej")



@pytest.fixture
def base_url():
    url = "http://www.google.com"
    return url

