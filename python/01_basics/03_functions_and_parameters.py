"""
Python Basics Review - Functions and Parameters
Este archivo contiene ejemplos y ejercicios de funciones en Python
"""

def funcion_simple():
    """Ejemplo de función sin parámetros"""
    print("¡Hola desde una función simple!")

def suma(a, b):
    """
    Función con dos parámetros que retorna su suma
    Args:
        a: primer número
        b: segundo número
    Returns:
        La suma de a y b
    """
    return a + b

def saludar(nombre, saludo="Hola"):
    """
    Función con un parámetro obligatorio y otro opcional (valor por defecto)
    Args:
        nombre: nombre de la persona a saludar
        saludo: tipo de saludo (opcional, por defecto es "Hola")
    """
    print(f"{saludo}, {nombre}!")

def calcular_promedio(*numeros):
    """
    Función con número variable de argumentos
    Args:
        *numeros: tupla con todos los números recibidos
    Returns:
        El promedio de los números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def info_persona(**datos):
    """
    Función que acepta argumentos con nombre (keywords)
    Args:
        **datos: diccionario con los datos de la persona
    """
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

# Ejemplo de función lambda (función anónima)
cuadrado = lambda x: x ** 2

def ejercicio_1(lista):
    """
    Ejercicio: Crear una función que reciba una lista de números
    y retorne una nueva lista solo con los números pares
    """            
    return list(filter(lambda x: x % 2 == 0, lista))


def ejercicio_2(number):
    """
    Ejercicio: Crear una función que calcule el factorial de un número
    usando recursión
    """
    if number < 0:
        raise ValueError("the factorial not is defined for negative numbers")
    if (number == 1 or number == 0):
        return 1
    
    return number * ejercicio_2(number - 1)
   
    

if __name__ == "__main__":
    # Ejemplos de uso de funciones
    print("=== Función Simple ===")
    funcion_simple()
    
    print("\n=== Función con Parámetros ===")
    resultado = suma(5, 3)
    print(f"5 + 3 = {resultado}")
    
    print("\n=== Función con Parámetro por Defecto ===")
    saludar("Juan")
    saludar("María", "Buenos días")
    
    print("\n=== Función con Argumentos Variables ===")
    print(f"Promedio de 1, 2, 3: {calcular_promedio(1, 2, 3)}")
    print(f"Promedio de 10, 20: {calcular_promedio(10, 20)}")
    
    print("\n=== Función con Keywords ===")
    info_persona(nombre="Ana", edad=25, ciudad="Madrid")
    
    print("\n=== Función Lambda ===\n")
    print(f"Cuadrado de 4: {cuadrado(4)}")
    
    print("\n=== Ejercicio 1: Filtrar Números Pares ===\n")
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = ejercicio_1(numeros)
    print(f"Lista original: {numeros}")
    print(f"Números pares: {pares}")
    
    print("\n=== Ejercicio 2: Factorial Recursivo ===\n")
    for n in range(6):  # Probar factorial del 0 al 5
        print(f"Factorial de {n} = {ejercicio_2(n)}")
