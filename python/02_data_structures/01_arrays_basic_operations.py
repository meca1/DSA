"""
Basic Data Structures - Arrays and Lists
Tema: Basic operations (insert, delete, traverse)
"""

def basic_operations():
    """Operaciones básicas: insert, delete, traverse"""
    print("=== Basic Operations ===")
    
    # Crear una lista
    numeros = [1, 2, 3, 4, 5]
    print(f"Lista original: {numeros}")
    
    # Insert (insertar)
    print("\n--- Insert Operations ---")
    numeros.insert(0, 0)  # Insertar al inicio
    print(f"Después de insert(0, 0): {numeros}")
    numeros.append(6)     # Insertar al final
    print(f"Después de append(6): {numeros}")
    numeros.insert(3, 2.5)  # Insertar en medio
    print(f"Después de insert(3, 2.5): {numeros}")
    
    # Delete (eliminar)
    print("\n--- Delete Operations ---")
    numeros.remove(2.5)   # Eliminar por valor
    print(f"Después de remove(2.5): {numeros}")
    del numeros[0]        # Eliminar por índice
    print(f"Después de del numeros[0]: {numeros}")
    ultimo = numeros.pop()  # Eliminar y retornar último elemento
    print(f"Elemento eliminado con pop(): {ultimo}")
    print(f"Después de pop(): {numeros}")
    
    # Traverse (recorrer)
    print("\n--- Traverse Operations ---")
    print("Recorrido con for:")
    for num in numeros:
        print(f"  Elemento: {num}")
    
    print("\nRecorrido con índices:")
    for i in range(len(numeros)):
        print(f"  Índice {i}: {numeros[i]}")
    
    print("\nRecorrido con enumerate:")
    for i, valor in enumerate(numeros):
        print(f"  Índice {i}: {valor}")

def ejercicio_practico():
    """
    Ejercicio: Implementar una función que elimine todos los elementos duplicados de una lista.
    Ejemplo: [1, 2, 2, 3, 4, 4, 5] -> [1, 2, 3, 4, 5]
    """
    # Datos de ejemplo
    lista_con_duplicados = [1, 2, 2, 3, 4, 4, 5, 5, 5]
    print(f"\n--- Ejercicio Práctico ---")
    print(f"Lista original con duplicados: {lista_con_duplicados}")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar un conjunto (set) para eliminar duplicados
    # numbers = list(set(lista_con_duplicados))
    numbers = {}
    for i in lista_con_duplicados:
        if i in numbers:
            continue
        else:
            numbers[i] = True

    result = list(numbers.keys())
    
    print(f"Lista sin duplicados: {result}")

if __name__ == "__main__":
    basic_operations()
    ejercicio_practico()
