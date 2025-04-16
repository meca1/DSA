"""
Basic Data Structures - Arrays and Lists
Este archivo cubre los siguientes temas:
1. Basic operations (insert, delete, traverse)
2. List slicing and operations
3. Practice: Array manipulation problems
"""

def basic_operations():
    """Operaciones básicas: insert, delete, traverse"""
    print("=== 1. Basic Operations ===")
    
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

def list_slicing():
    """Operaciones de slicing y otras operaciones de lista"""
    print("\n=== 2. List Slicing and Operations ===")
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Slicing básico
    print(f"\nLista completa: {numeros}")
    print(f"Primeros 3 elementos: {numeros[:3]}")
    print(f"Últimos 3 elementos: {numeros[-3:]}")
    print(f"Del índice 2 al 5: {numeros[2:6]}")
    print(f"Cada 2 elementos: {numeros[::2]}")
    
    # Operaciones de lista
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    print(f"\nLista1: {lista1}, Lista2: {lista2}")
    print(f"Concatenación (+): {lista1 + lista2}")
    print(f"Multiplicación (*3): {lista1 * 3}")
    
    # Métodos adicionales
    numeros = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nLista desordenada: {numeros}")
    numeros.sort()
    print(f"Después de sort(): {numeros}")
    numeros.reverse()
    print(f"Después de reverse(): {numeros}")

def ejercicio_1(lista, k):
    """
    Array Manipulation Problem 1:
    Rotar una lista k posiciones a la derecha.
    Ejemplo: 
    lista = [1,2,3,4,5], k = 2
    resultado = [4,5,1,2,3]
    """
    for i in range(0, k):
        element = lista.pop()
        lista.insert(0, element)

   # return lista[-k:] + lista[:-k]

def ejercicio_2(lista):
    """
    Array Manipulation Problem 2:
    Encontrar el rango (diferencia entre el máximo y mínimo)
    y la media de una lista de números.
    Retornar (rango, media)
    """
    if not lista:
        return (0,0)

    acum = lista[0]
    max_val = lista[0]
    min_val = lista[0]
    for i in lista[1:]:
        acum += i 
        if max_val < i:
            max_val = i
        if min_val > i: 
            min_val = i
    
    return (max_val - min_val, acum / len(lista))





if __name__ == "__main__":
    # Demostración de operaciones básicas
    basic_operations()
    
    # Demostración de slicing y operaciones
    list_slicing()
    
    # Ejercicios de manipulación de arrays
    print("\n=== 3. Array Manipulation Problems ===")
    
    # Ejercicio 1: Rotación
    numeros = [1, 2, 3, 4, 5]
    k = 2
    print(f"\nEjercicio 1 - Rotar lista:")
    print(f"Lista original: {numeros}")
    print(f"k = {k}")
    print("Completa ejercicio_1() para rotar la lista")
    
    # Ejercicio 2: Rango y Media
    datos = [4, 8, 2, 9, 5, 1, 7, 3, 6]
    print(f"\nEjercicio 2 - Rango y Media:")
    print(f"Datos: {datos}")
    print("Completa ejercicio_2() para calcular el rango y la media")
