"""
Test con monkeypatch: simulamos una API externa sin llamarla realmente.
"""

import pytest


# --- CÓDIGO REAL (simulado) ---
def obtener_clima(ciudad: str) -> dict:
    """En producción, esto llama a una API HTTP real."""
    import requests
    response = requests.get(f"https://api.clima.com/{ciudad}")
    return response.json()


def sugerir_ropa(ciudad: str) -> str:
    """Usa obtener_clima para decidir qué ropa ponerte."""
    clima = obtener_clima(ciudad)
    temperatura = clima["temperatura"]
    
    if temperatura > 25:
        return "Camiseta y shorts"
    elif temperatura > 15:
        return "Camiseta ligera"
    return "Chaqueta"


# --- TESTS CON MOCK ---
def test_sugerir_ropa_calor(monkeypatch):
    """Simulamos que hace 30°C. No llamamos a internet."""
    
    def clima_falso(ciudad):
        return {"temperatura": 30, "condicion": "soleado"}
    
    monkeypatch.setattr("tests.test_manager_mock.obtener_clima", clima_falso)
    
    resultado = sugerir_ropa("Madrid")
    assert resultado == "Camiseta y shorts"


def test_sugerir_ropa_frio(monkeypatch):
    """Simulamos que hace 5°C."""
    
    def clima_falso(ciudad):
        return {"temperatura": 5, "condicion": "nublado"}
    
    monkeypatch.setattr("tests.test_manager_mock.obtener_clima", clima_falso)
    
    resultado = sugerir_ropa("Oslo")
    assert resultado == "Chaqueta"


def test_sugerir_ropa_templado(monkeypatch):
    """Simulamos que hace 20°C."""
    
    def clima_falso(ciudad):
        return {"temperatura": 20, "condicion": "parcial"}
    
    monkeypatch.setattr("tests.test_manager_mock.obtener_clima", clima_falso)
    
    resultado = sugerir_ropa("Bogotá")
    assert resultado == "Camiseta ligera"