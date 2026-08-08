from typing import TypeVar, Generic

T = TypeVar('T')
Numero = TypeVar('Numero', int, float)


def primer_elemento(lista: list[T]) -> T | None:
    if len(lista) == 0:
        return None
    return lista[0]


def duplicar(valor: Numero) -> Numero:
    return valor * 2


class Pila(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    
    def push(self, item: T) -> None:
        self._items.append(item)
    
    def pop(self) -> T | None:
        if len(self._items) == 0:
            return None
        return self._items.pop()
    
    def peek(self) -> T | None:
        if len(self._items) == 0:
            return None
        return self._items[-1]
    
    def __len__(self) -> int:
        return len(self._items)


class Cola(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
    
    def encolar(self, item: T) -> None:
        self._items.append(item)
    
    def desencolar(self) -> T | None:
        if len(self._items) == 0:
            return None
        return self._items.pop(0)
    
    def frente(self) -> T | None:
        if len(self._items) == 0:
            return None
        return self._items[0]
    
    def __len__(self) -> int:
        return len(self._items)


if __name__ == "__main__":
    print("=" * 50)
    print("DEMO: TypeVar + Generic")
    print("=" * 50)
    
    print("\n1. Función genérica:")
    print(f"   primer_elemento([1, 2, 3]) = {primer_elemento([1, 2, 3])}")
    print(f"   primer_elemento(['a', 'b']) = {primer_elemento(['a', 'b'])}")
    
    print("\n2. Función genérica restringida (int/float):")
    print(f"   duplicar(5) = {duplicar(5)}")
    print(f"   duplicar(3.5) = {duplicar(3.5)}")
    
    print("\n3. Pila<int>:")
    pila_numeros: Pila[int] = Pila()
    pila_numeros.push(10)
    pila_numeros.push(20)
    print(f"   push 10, push 20, pop = {pila_numeros.pop()}")
    print(f"   peek = {pila_numeros.peek()}")
    
    print("\n4. Cola<str>:")
    cola_nombres: Cola[str] = Cola()
    cola_nombres.encolar("Ana")
    cola_nombres.encolar("Luis")
    print(f"   encolar Ana, Luis | frente = {cola_nombres.frente()}")
    print(f"   desencolar = {cola_nombres.desencolar()}")
    print(f"   desencolar = {cola_nombres.desencolar()}")