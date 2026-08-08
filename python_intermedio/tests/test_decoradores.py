from python_intermedio.decoradores import calcular_area


def test_area_valida():
    assert calcular_area(5, 3) == 15


def test_area_negativa():
    resultado = calcular_area(-5, 3)
    assert resultado is None