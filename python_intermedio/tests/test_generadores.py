"""
Tests para el módulo generadores usando pytest.
Equivalente a xUnit en C#: [Fact] se convierte en funciones que empiezan con test_
"""

from python_intermedio.generadores import contador_hasta, fibonacci_hasta


def test_contador_hasta_5():
    """Prueba que contador_hasta(5) devuelva [1, 2, 3, 4, 5]"""
    resultado = list(contador_hasta(5))
    assert resultado == [1, 2, 3, 4, 5]


def test_fibonacci_hasta_100():
    """Prueba la secuencia de Fibonacci hasta 100."""
    resultado = list(fibonacci_hasta(100))
    esperado = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert resultado == esperado


def test_contador_vacio():
    """Prueba contador_hasta(0) devuelve lista vacía."""
    resultado = list(contador_hasta(0))
    assert resultado == []