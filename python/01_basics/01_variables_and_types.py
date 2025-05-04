"""
Python Basics Review - Variables and Data Types
Este archivo contiene ejemplos y ejercicios básicos de Python
"""

def basic_variables_demo():
    # Números
    numero_entero = 42
    numero_decimal = 3.14
    
    # Strings
    texto = "Hola Mundo"
    texto_multilinea = '''
    Este es un texto
    de múltiples líneas
    '''
    
    # Booleanos
    verdadero = True
    falso = False
    
    # Listas
    lista = [1, 2, 3, 4, 5]
    
    # Tuplas (inmutables)
    tupla = (1, "dos", 3.0)
    
    # Diccionarios
    diccionario = {
        "nombre": "Python",
        "tipo": "Lenguaje de Programación",
        "año": 1991
    }
    
    # Sets
    conjunto = {1, 2, 3, 4, 5}
    
    # Imprimimos los tipos y valores
    print(f"Número entero: {numero_entero}, Tipo: {type(numero_entero)}")
    print(f"Número decimal: {numero_decimal}, Tipo: {type(numero_decimal)}")
    print(f"Texto: {texto}, Tipo: {type(texto)}")
    print(f"Lista: {lista}, Tipo: {type(lista)}")
    print(f"Tupla: {tupla}, Tipo: {type(tupla)}")
    print(f"Diccionario: {diccionario}, Tipo: {type(diccionario)}")
    print(f"Conjunto: {conjunto}, Tipo: {type(conjunto)}")

# Ejercicio 1: Crear variables de diferentes tipos
def ejercicio_1():
    """
    Ejercicio: Crea variables de diferentes tipos y realiza operaciones básicas
    """
    # 1. Crea un número entero y multiplícalo por 2
    entero = 42 * 2
    print(f"Número entero: {entero}")
    
    # 2. Crea un número decimal y súmale 5
    decimal = 2.5 + 5
    print(f"Número decimal: {decimal}")
    
    # 3. Crea una cadena y concatena " Python" al final
    cadena = 'Hola' + ' Python'
    print(f"Cadena: {cadena}")
    
    # 4. Crea una lista y agrega un elemento
    lista = [1, 2, 3]
    lista.append(4)  # Agregamos el número 4 a la lista
    print(f"Lista final: {lista}")

if __name__ == "__main__":
    print("Demostración de tipos de variables básicos en Python:")
    basic_variables_demo()
    print("\nResultados de tu ejercicio:")
    ejercicio_1()
