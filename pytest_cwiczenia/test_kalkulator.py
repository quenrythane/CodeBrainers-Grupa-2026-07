# import kalkulator
from kalkulator import dodaj

# wynik = dodaj(1, 2)
# print(wynik)

def test_dodaj_1():
    assert dodaj(1, 2) == 3

def test_dodaj_2():
    assert dodaj(1, 4) == 5

def test_dodaj_3():
    assert dodaj(1, 4) == 5