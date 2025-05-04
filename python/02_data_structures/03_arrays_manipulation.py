"""
Basic Data Structures - Arrays and Lists
Tema: Practice: Array manipulation problems
"""

def rotar_lista(lista, k):
    """
    Problema 1: Rotar una lista k posiciones a la derecha.
    
    Args:
        lista: Lista a rotar
        k: Número de posiciones a rotar
        
    Returns:
        Lista rotada
        
    Ejemplo: 
        lista = [1,2,3,4,5], k = 2
        resultado = [4,5,1,2,3]
    """
    if not lista or k == 0:
        return lista
    
    # Asegurarse de que k no sea mayor que la longitud de la lista
    k = k % len(lista)
    
    # Método 1: Usando slicing
    # return lista[-k:] + lista[:-k]
    
    # Método 2: Rotación manual (descomenta para usar)
    resultado = lista.copy()
    for _ in range(k):
        ultimo = resultado.pop()
        resultado.insert(0, ultimo)
    return resultado

def encontrar_segundo_mayor(lista):
    """
    Problema 2: Encontrar el segundo número más grande en una lista.
    
    Args:
        lista: Lista de números
        
    Returns:
        El segundo número más grande
        
    Ejemplo:
        [1, 3, 2, 5, 4, 5] -> 4
    """
    if len(lista) < 2:
        return None
    
    # Método 1: Usando sort
    # lista_ordenada = sorted(lista, reverse=True)
    # return lista_ordenada[1]
    
    # Método 2: Sin ordenar (descomenta para usar)
    maximo = segundo = float('-inf')
    for num in lista:
        if num > maximo:
            segundo = maximo
            maximo = num
        elif num > segundo and num < maximo:
            segundo = num
    
    return segundo if segundo != float('-inf') else None

def ejercicio_1():
    """
    Ejercicio 1: Implementar una función que encuentre todos los pares de números
    en una lista que sumen un valor objetivo.
    
    Ejemplo:
        lista = [1, 2, 3, 4, 5], objetivo = 6
        resultado = [(1, 5), (2, 4)]
    """
    # Datos de ejemplo
    numeros = [1, 2, 3, 4, 5, 6, 7]
    objetivo = 8
    print(f"Lista: {numeros}")
    print(f"Objetivo: {objetivo}")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar un conjunto (set) para buscar complementos
    
    # Solución de ejemplo (descomenta para probar)
    # pares = []
    # vistos = set()
    # for num in numeros:
    #     complemento = objetivo - num
    #     if complemento in vistos:
    #         pares.append((complemento, num))
    #     vistos.add(num)
    # print(f"Pares que suman {objetivo}: {pares}")

def ejercicio_2():
    """
    Ejercicio 2: Implementar una función que encuentre el subarreglo continuo
    con la suma más grande dentro de una lista.
    
    Ejemplo:
        [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> [4, -1, 2, 1] (suma = 6)
    """
    # Datos de ejemplo
    numeros = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Lista: {numeros}")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar el algoritmo de Kadane
    
    # Solución de ejemplo (descomenta para probar)
    # suma_actual = suma_maxima = numeros[0]
    # inicio = fin = 0
    # inicio_temp = 0
    # 
    # for i in range(1, len(numeros)):
    #     if suma_actual + numeros[i] > numeros[i]:
    #         suma_actual += numeros[i]
    #     else:
    #         suma_actual = numeros[i]
    #         inicio_temp = i
    #     
    #     if suma_actual > suma_maxima:
    #         suma_maxima = suma_actual
    #         inicio = inicio_temp
    #         fin = i
    # 
    # print(f"Subarreglo con suma máxima: {numeros[inicio:fin+1]} (suma = {suma_maxima})")

if __name__ == "__main__":
    # Demostración de problemas resueltos
    print("=== Problema 1: Rotación de Lista ===")
    lista_original = [1, 2, 3, 4, 5]
    k = 2
    print(f"Lista original: {lista_original}")
    print(f"Rotación de {k} posiciones: {rotar_lista(lista_original, k)}")
    
    print("\n=== Problema 2: Segundo Número Mayor ===")
    numeros = [1, 3, 2, 5, 4, 5]
    print(f"Lista: {numeros}")
    print(f"Segundo número mayor: {encontrar_segundo_mayor(numeros)}")
    
    print("\n=== Ejercicios para Practicar ===")
    ejercicio_1()
    print()
    ejercicio_2()
