from kalkulator import dodaj, odejmowanie


def test_dodaj_1():
    assert dodaj(1, 2) == 3
    assert dodaj(1, 4) == 5


def test_odejmowanie_1():
    assert odejmowanie(5, 2) == 3
    assert odejmowanie(5, 10) == -5
    assert odejmowanie(5, 5) == 0

