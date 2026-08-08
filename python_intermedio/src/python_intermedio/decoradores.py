"""
Módulo: Decoradores

Los decoradores permiten envolver funciones para agregar
comportamiento extra sin modificar su código original.
"""

import time
from typing import Callable, Any


def medir_tiempo(funcion: Callable) -> Callable:
    """
    Decorador que mide cuánto tarda una función en ejecutarse.
    """
    def envoltura(*args: Any, **kwargs: Any) -> Any:
        inicio = time.perf_counter()
        resultado = funcion(*args, **kwargs)
        fin = time.perf_counter()
        print(f"⏱️  {funcion.__name__} tardó {fin - inicio:.6f} segundos")
        return resultado
    
    return envoltura


def validar_positivos(funcion: Callable) -> Callable:
    """
    Decorador que valida que TODOS los argumentos numéricos
    sean positivos antes de ejecutar la función.
    """
    def envoltura(*args: Any, **kwargs: Any) -> Any:
        # Revisar argumentos posicionales
        for valor in args:
            if isinstance(valor, (int, float)) and valor < 0:
                print(f"❌ Error: {valor} no es positivo")
                return None
        
        # Revisar argumentos nombrados
        for valor in kwargs.values():
            if isinstance(valor, (int, float)) and valor < 0:
                print(f"❌ Error: {valor} no es positivo")
                return None
        
        # Todo OK, ejecutar función original
        return funcion(*args, **kwargs)
    
    return envoltura


@validar_positivos
def calcular_area(base: int, altura: int) -> int:
    return base * altura


if __name__ == "__main__":
    print("=" * 50)
    print("DEMO: Decorador validar_positivos")
    print("=" * 50)
    
    print("\nPrueba 1: calcular_area(5, 3)")
    resultado1 = calcular_area(5, 3)
    print(f"Resultado: {resultado1}")
    
    print("\nPrueba 2: calcular_area(-5, 3)")
    resultado2 = calcular_area(-5, 3)
    print(f"Resultado: {resultado2}")