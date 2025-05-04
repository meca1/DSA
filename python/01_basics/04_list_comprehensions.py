"""
Python Basics Review - List Comprehensions
Este archivo contiene ejemplos y ejercicios de list comprehensions en Python
"""

def ejemplos_basicos():
    """Ejemplos básicos de list comprehensions"""
    
    # Lista tradicional vs List comprehension
    print("=== Crear lista de números cuadrados ===")
    # Método tradicional con for
    cuadrados_tradicional = []
    for i in range(5):
        cuadrados_tradicional.append(i ** 2)
    print(f"Método tradicional: {cuadrados_tradicional}")
    
    # Con list comprehension
    cuadrados_comprehension = [i ** 2 for i in range(5)]
    print(f"List comprehension: {cuadrados_comprehension}")
    
    # List comprehension con condición (filtrado)
    print("\n=== Filtrar números pares ===")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = [x for x in numeros if x % 2 == 0]
    print(f"Números originales: {numeros}")
    print(f"Números pares: {pares}")
    
    # List comprehension con operador ternario
    print("\n=== Operador ternario en list comprehension ===")
    resultado = ["par" if x % 2 == 0 else "impar" for x in range(5)]
    print(f"Clasificación par/impar: {resultado}")

def ejercicio_1():
    """
    Ejercicio: Crear una list comprehension que genere una lista de 
    temperaturas en Fahrenheit a partir de una lista de temperaturas en Celsius
    Fórmula: F = C * 9/5 + 32
    """
    celsius = [0, 10, 20, 30, 40]
    # TODO: Crear la list comprehension para convertir a Fahrenheit
    return [i * 9/5 + 32 for i in celsius ]

def ejercicio_2():
    """
    Ejercicio: Crear una list comprehension que filtre las palabras
    que tienen más de 3 letras y las convierta a mayúsculas
    """
    palabras = ["el", "la", "perro", "gato", "casa", "y", "en", "parque"]
    # TODO: Crear la list comprehension para filtrar y convertir a mayúsculas

    return [ palabra.upper() for palabra in palabras if len(palabra) > 3]


if __name__ == "__main__":
    print("=== Ejemplos Básicos de List Comprehensions ===")
    ejemplos_basicos()
    
    print("\n=== Ejercicio 1: Conversión de Temperaturas ===")
    print("Completa el ejercicio_1() para convertir temperaturas")
    
    print("\n=== Ejercicio 2: Filtrado y Transformación de Palabras ===")
    print("Completa el ejercicio_2() para filtrar y transformar palabras")
