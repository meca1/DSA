"""
Python Basics Review - Control Structures
Este archivo contiene ejemplos y ejercicios de estructuras de control en Python
"""

def ejemplos_if_else():
    """Ejemplos de estructuras if/else"""
    # If simple
    edad = 18
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    
    # If con elif
    nota = 85
    if nota >= 90:
        print("A - Excelente")
    elif nota >= 80:
        print("B - Muy bien")
    elif nota >= 70:
        print("C - Bien")
    else:
        print("D - Necesitas mejorar")

def ejemplos_for_loops():
    """Ejemplos de bucles for"""
    # Iterar sobre una lista
    frutas = ["manzana", "banana", "naranja"]
    for fruta in frutas:
        print(f"Me gusta la {fruta}")
    
    # Iterar con range
    print("\nContando del 1 al 5:")
    for i in range(1, 6):  # range(1, 6) genera números del 1 al 5
        print(i)
    
    # Iterar sobre un diccionario
    estudiante = {
        "nombre": "Ana",
        "edad": 20,
        "carrera": "Informática"
    }
    for clave, valor in estudiante.items():
        print(f"{clave}: {valor}")

def ejemplos_while():
    """Ejemplos de bucles while"""
    # While con contador
    contador = 5
    while contador > 0:
        print(f"Contador: {contador}")
        contador -= 1
    
    # While con break
    print("\nEjemplo de break:")
    numero = 1
    while True:
        if numero > 3:
            break
        print(f"Número: {numero}")
        numero += 1

def ejercicio_1():
    """
    Ejercicio: FizzBuzz
    - Para números del 1 al 15:
    - Si el número es divisible por 3, imprime 'Fizz'
    - Si es divisible por 5, imprime 'Buzz'
    - Si es divisible por ambos, imprime 'FizzBuzz'
    - Si no es divisible por ninguno, imprime el número
    """
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0: 
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz') 
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

    
   

def ejercicio_2():
    """
    Ejercicio: Suma de números pares
    Usa un bucle para sumar todos los números pares del 1 al 10
    """
    acum = 0
    for i  in range(1, 11):
        if i % 2 == 0:
            acum += i
    print(acum)


if __name__ == "__main__":
    print("=== Ejemplos de IF/ELSE ===")
    ejemplos_if_else()
    
    print("\n=== Ejemplos de FOR LOOPS ===")
    ejemplos_for_loops()
    
    print("\n=== Ejemplos de WHILE ===")
    ejemplos_while()
    
    print("\n=== Ejercicio 1: FizzBuzz ===")
    print("Completa el ejercicio_1() para resolver el FizzBuzz")
    
    print("\n=== Ejercicio 2: Suma de pares ===")
    print("Completa el ejercicio_2() para sumar números pares")
