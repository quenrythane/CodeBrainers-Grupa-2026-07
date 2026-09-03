import pytest


@pytest.fixture
def funkcja_pomocnicza():
    print("\n Start testu")
    yield
    print("\n Koniec testu")


@pytest.fixture
def base_url():
    url = "http://www.google.com"
    return url
