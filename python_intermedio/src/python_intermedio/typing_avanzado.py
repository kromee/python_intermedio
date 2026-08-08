"""
Módulo: Typing Avanzado

Python 3.10+ permite tipado expresivo similar a C#,
pero es opcional en runtime. Herramientas como mypy
lo hacen obligatorio en desarrollo.
"""

from typing import Optional, Union, Callable, Protocol
from datetime import datetime


# ============================================
# EJEMPLO 1: Optional / Union / Pipe |
# ============================================

# FORMA VIEJA (pre-3.10):
def buscar_viejo(id: int) -> Optional[str]:
    """Devuelve str o None."""
    if id <= 0:
        return None
    return f"Usuario {id}"

# FORMA MODERNA (Python 3.10+):
def buscar_nuevo(id: int) -> str | None:
    """El pipe | reemplaza a Optional y Union."""
    if id <= 0:
        return None
    return f"Usuario {id}"

# Union de múltiples tipos:
def procesar(valor: int | str | float) -> str:
    """Acepta int, str o float."""
    return str(valor)


# ============================================
# EJEMPLO 2: Callable (el Func<> de Python)
# ============================================

def filtrar_numeros(
    numeros: list[int],
    condicion: Callable[[int], bool]   # Equivalente a Func<int, bool>
) -> list[int]:
    return [n for n in numeros if condicion(n)]


def es_par(n: int) -> bool:
    return n % 2 == 0


# ============================================
# EJERCICIO: Protocol (el interface de Python)
# ============================================

class Volador(Protocol):
    """Protocol: cualquier cosa que tenga 'volar' es Volador."""
    def volar(self) -> str:
        ...


class Pato:
    def volar(self) -> str:
        return "El pato vuela bajo"


class Avion:
    def volar(self) -> str:
        return "El avión vuela alto"


def hacer_volar(cosa: Volador) -> None:
    print(cosa.volar())


# ============================================
# MAIN: Pruebas
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("DEMO: Typing Avanzado")
    print("=" * 50)
    
    print("\n1. Optional / Union:")
    print(f"   buscar_nuevo(5) = {buscar_nuevo(5)}")
    print(f"   buscar_nuevo(-1) = {buscar_nuevo(-1)}")
    
    print("\n2. Callable:")
    resultado = filtrar_numeros([1, 2, 3, 4, 5], es_par)
    print(f"   Pares: {resultado}")
    
    print("\n3. Protocol:")
    hacer_volar(Pato())
    hacer_volar(Avion())