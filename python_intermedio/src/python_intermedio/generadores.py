"""
Módulo: Generadores y yield

Los generadores permiten iterar sobre secuencias sin cargarlas
completamente en memoria. Son la base de pipelines de datos eficientes.
"""

import sys
from typing import Generator


def comparar_memoria(limite: int = 100_000) -> None:
    """
    Compara el consumo de memoria entre una lista y un generador.
    
    Args:
        limite: Cantidad de elementos a generar.
    """
    lista = [x for x in range(limite)]
    generador = (x for x in range(limite))
    
    print(f"Lista ocupa:     {sys.getsizeof(lista):,} bytes")
    print(f"Generador ocupa: {sys.getsizeof(generador):,} bytes")


def contador_hasta(maximo: int) -> Generator[int, None, None]:
    """
    Generador que produce números del 1 al maximo.
    
    Args:
        maximo: Límite superior inclusive.
        
    Yields:
        int: Siguiente número en la secuencia.
    """
    numero = 1
    while numero <= maximo:
        yield numero
        numero += 1


def fibonacci_hasta(maximo: int) -> Generator[int, None, None]:
    """
    Generador de números de Fibonacci hasta superar 'maximo'.
    
    Secuencia: 1, 1, 2, 3, 5, 8, 13...
    
    Args:
        maximo: Valor máximo permitido.
        
    Yields:
        int: Siguiente número de Fibonacci.
    """
    a, b = 1, 1
    while a <= maximo:
        yield a
        a, b = b, a + b


def leer_lineas(archivo: str) -> Generator[str, None, None]:
    """
    Lee un archivo línea por línea sin cargarlo completo en memoria.
    
    Args:
        archivo: Ruta al archivo.
        
    Yields:
        str: Línea limpia (sin saltos de línea).
    """
    with open(archivo, "r", encoding="utf-8") as f:
        for linea in f:
            yield linea.strip()