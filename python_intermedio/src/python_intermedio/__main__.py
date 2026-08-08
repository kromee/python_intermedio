from python_intermedio.generadores import comparar_memoria, contador_hasta, fibonacci_hasta

if __name__ == "__main__":
    print("=" * 50)
    print("DEMO: Generadores en Python")
    print("=" * 50)
    
    print("\n1. Comparación de memoria:")
    comparar_memoria(100_000)
    
    print("\n2. Contador hasta 5:")
    for n in contador_hasta(5):
        print(f"   {n}")
    
    print("\n3. Fibonacci hasta 100:")
    for n in fibonacci_hasta(100):
        print(f"   {n}")