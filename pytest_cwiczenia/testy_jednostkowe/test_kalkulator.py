from kalkulator import dodaj, odejmowanie
import pytest

@pytest.mark.dodaj
@pytest.mark.xd
@pytest.mark.parametrize("liczba_1, liczba_2, wynik", [
    (5, 2, 7),
    (5, 10, 15),
    (5, 5, 10),
    (1, 1, 2),
    (12, 7, 19)
])
def test_dodaj_1(liczba_1, liczba_2, wynik):
    assert dodaj(liczba_1, liczba_2) == wynik


# pytest -m odejmij <- uruchamia test z mark.odejmowanie
@pytest.mark.odejmij
@pytest.mark.parametrize("liczba_1, liczba_2, wynik", [
    (5, 2, 3),
    (5, 10, -5),
    (5, 5, 0),
    (1, 1, 0),
    (12, 7, 5)
])
def test_odejmowanie_1(liczba_1, liczba_2, wynik):
    assert odejmowanie(liczba_1, liczba_2) == wynik
