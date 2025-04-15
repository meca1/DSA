"""
Python Basics Review - Exception Handling
Este archivo contiene ejemplos y ejercicios de manejo de excepciones en Python
"""

def ejemplo_basico():
    """Ejemplo básico de try-except"""
    try:
        numero = int(input("Ingresa un número: "))
        print(f"Tu número es: {numero}")
    except ValueError:
        print("Error: Debes ingresar un número válido")

def ejemplo_multiple_except():
    """Ejemplo de múltiples except y else"""
    try:
        numero = int(input("Ingresa un número: "))
        resultado = 100 / numero
    except ValueError:
        print("Error: Debes ingresar un número válido")
    except ZeroDivisionError:
        print("Error: No puedes dividir por cero")
    else:
        print(f"100 dividido por {numero} es: {resultado}")
    finally:
        print("Esta línea siempre se ejecuta")

def ejemplo_raise():
    """Ejemplo de lanzar excepciones personalizadas"""
    edad = int(input("Ingresa tu edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad > 120:
        raise ValueError("La edad parece no ser válida")
    print(f"Tu edad es: {edad}")

def ejercicio_1():
    """
    Ejercicio: Crear una función que divida dos números
    y maneje las siguientes excepciones:
    - ValueError: si los inputs no son números
    - ZeroDivisionError: si el denominador es cero
    """
    # TODO: Implementa la función dividir aquí
    pass

def ejercicio_2():
    """
    Ejercicio: Crear una función que lea un archivo
    y maneje las siguientes excepciones:
    - FileNotFoundError: si el archivo no existe
    - PermissionError: si no hay permisos para leer el archivo
    """
    # TODO: Implementa la función leer_archivo aquí
    pass

if __name__ == "__main__":
    print("=== Ejemplo Básico de Try-Except ===")
    ejemplo_basico()
    
    print("\n=== Ejemplo de Múltiples Except ===")
    ejemplo_multiple_except()
    
    print("\n=== Ejemplo de Raise ===")
    try:
        ejemplo_raise()
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n=== Ejercicio 1: División Segura ===")
    print("Completa el ejercicio_1() para implementar una división segura")
    
    print("\n=== Ejercicio 2: Lectura de Archivo ===")
    print("Completa el ejercicio_2() para implementar una lectura segura de archivo")
