from kalkulator import dodaj, odejmowanie
import pytest

@pytest.mark.dodaj
@pytest.mark.xd
def test_dodaj_1():
    assert dodaj(1, 2) == 3
    assert dodaj(1, 4) == 5


# pytest -m odejmij <- uruchamia test z mark.odejmowanie
@pytest.mark.odejmij
@pytest.mark.parametrize("liczba_1, liczba_2, wynik", [
    (5, 2, 3),
    (5, 10, -5),
    (5, 5, 0),
    (1, 1, 0),
])
def test_odejmowanie_1(liczba_1, liczba_2, wynik):
    assert odejmowanie(liczba_1, liczba_2) == wynik
