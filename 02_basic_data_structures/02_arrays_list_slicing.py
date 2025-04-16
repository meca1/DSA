"""
Basic Data Structures - Arrays and Lists
Tema: List slicing and operations
"""

def list_slicing():
    """Operaciones de slicing y otras operaciones de lista"""
    print("=== List Slicing and Operations ===")
    numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # Slicing básico
    print(f"\nLista completa: {numeros}")
    print(f"Primeros 3 elementos: {numeros[:3]}")
    print(f"Últimos 3 elementos: {numeros[-3:]}")
    print(f"Del índice 2 al 5: {numeros[2:6]}")
    print(f"Cada 2 elementos: {numeros[::2]}")
    print(f"Lista invertida: {numeros[::-1]}")
    
    # Operaciones de lista
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    print(f"\n--- Operaciones con listas ---")
    print(f"Lista1: {lista1}, Lista2: {lista2}")
    print(f"Concatenación (+): {lista1 + lista2}")
    print(f"Multiplicación (*3): {lista1 * 3}")
    
    # Métodos adicionales
    numeros = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\n--- Métodos de lista ---")
    print(f"Lista original: {numeros}")
    
    # Ordenar
    numeros_ordenados = sorted(numeros)  # No modifica la lista original
    print(f"sorted(): {numeros_ordenados}")
    
    numeros.sort()  # Modifica la lista original
    print(f"sort(): {numeros}")
    
    # Invertir
    numeros.reverse()
    print(f"reverse(): {numeros}")
    
    # Contar ocurrencias
    print(f"count(1): {numeros.count(1)}")
    
    # Encontrar índice
    print(f"index(5): {numeros.index(5)}")
    
    # Extender una lista
    numeros.extend([10, 11])
    print(f"extend([10, 11]): {numeros}")

def ejercicio_practico():
    """
    Ejercicio: Implementar una función que divida una lista en sublistas de tamaño n.
    Ejemplo: [1, 2, 3, 4, 5, 6, 7, 8], n=3 -> [[1, 2, 3], [4, 5, 6], [7, 8]]
    """
    # Datos de ejemplo
    lista_original = [1, 2, 3, 4, 5, 6, 7, 8]
    n = 3
    print(f"\n--- Ejercicio Práctico ---")
    print(f"Lista original: {lista_original}")
    print(f"Tamaño de sublistas (n): {n}")
    

    iterations =  len(lista_original) // n
    result = []

    inicio = 0
    fin = n
    for i in range(0, iterations):
        result.append(lista_original[inicio:fin])
        inicio += n
        fin += n

    if lista_original[n * iterations:]:
        result.append(lista_original[n * iterations:])
    
    print(f"Lista dividida en sublistas: {result}")
















    
    # Solución de ejemplo (descomenta para probar)
    # resultado = []
    # for i in range(0, len(lista_original), n):
    #     resultado.append(lista_original[i:i+n])
    # print(f"Lista dividida en sublistas: {resultado}")

if __name__ == "__main__":
    list_slicing()
    ejercicio_practico()
