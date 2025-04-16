"""
Basic Data Structures - Dictionaries
Tema: Practice: Dictionary-based problems
"""

def contar_frecuencia_palabras(texto):
    """
    Problema 1: Contar la frecuencia de cada palabra en un texto.
    
    Args:
        texto: String con el texto a analizar
        
    Returns:
        Diccionario con palabras como claves y frecuencias como valores
        
    Ejemplo: 
        "hola mundo hola" -> {'hola': 2, 'mundo': 1}
    """
    # Convertir a minúsculas y dividir en palabras
    palabras = texto.lower().split()
    
    # Contar frecuencia
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

def calcular_promedios(estudiantes):
    """
    Problema 2: Calcular el promedio de calificaciones de cada estudiante.
    
    Args:
        estudiantes: Lista de diccionarios con nombre y calificaciones
        
    Returns:
        Diccionario con nombre como clave y promedio como valor
        
    Ejemplo:
        [
            {"nombre": "Ana", "calificaciones": [90, 85, 95]},
            {"nombre": "Juan", "calificaciones": [80, 75, 85]}
        ]
        ->
        {"Ana": 90.0, "Juan": 80.0}
    """
    promedios = {}
    
    for estudiante in estudiantes:
        nombre = estudiante["nombre"]
        calificaciones = estudiante["calificaciones"]
        promedio = sum(calificaciones) / len(calificaciones)
        promedios[nombre] = promedio
    
    return promedios

def ejercicio_1():
    """
    Ejercicio 1: Implementar una función que encuentre la primera palabra
    no repetida en un texto.
    
    Ejemplo:
        "hola mundo hola python mundo" -> "python"
    """
    # Datos de ejemplo
    texto = "hola mundo hola python mundo programacion"
    print(f"Texto: '{texto}'")
    
    # TODO: Implementa tu solución aquí
    # Pista: Usa un diccionario para contar la frecuencia y luego busca la primera con frecuencia 1
    
    # Solución de ejemplo (descomenta para probar)
    # palabras = texto.lower().split()
    # frecuencia = {}
    # 
    # # Contar frecuencia
    # for palabra in palabras:
    #     if palabra in frecuencia:
    #         frecuencia[palabra] += 1
    #     else:
    #         frecuencia[palabra] = 1
    # 
    # # Buscar la primera no repetida
    # for palabra in palabras:
    #     if frecuencia[palabra] == 1:
    #         print(f"Primera palabra no repetida: '{palabra}'")
    #         break
    # else:
    #     print("No hay palabras no repetidas")

def ejercicio_2():
    """
    Ejercicio 2: Implementar una función que agrupe anagramas de una lista de palabras.
    
    Ejemplo:
        ["eat", "tea", "tan", "ate", "nat", "bat"]
        ->
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    """
    # Datos de ejemplo
    palabras = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Palabras: {palabras}")
    
    # TODO: Implementa tu solución aquí
    # Pista: Usa un diccionario donde la clave sea una representación ordenada de la palabra
    
    # Solución de ejemplo (descomenta para probar)
    # anagramas = {}
    # 
    # for palabra in palabras:
    #     # Ordenar letras como clave
    #     clave = ''.join(sorted(palabra))
    #     
    #     if clave in anagramas:
    #         anagramas[clave].append(palabra)
    #     else:
    #         anagramas[clave] = [palabra]
    # 
    # # Obtener los grupos
    # grupos = list(anagramas.values())
    # print(f"Grupos de anagramas: {grupos}")

if __name__ == "__main__":
    # Demostración de problemas resueltos
    print("=== Problema 1: Frecuencia de Palabras ===")
    texto = "este es un ejemplo de texto este texto es un ejemplo"
    print(f"Texto: '{texto}'")
    print(f"Frecuencia de palabras: {contar_frecuencia_palabras(texto)}")
    
    print("\n=== Problema 2: Promedio de Calificaciones ===")
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [90, 85, 95]},
        {"nombre": "Juan", "calificaciones": [80, 75, 85]},
        {"nombre": "María", "calificaciones": [95, 90, 100]}
    ]
    print(f"Estudiantes: {estudiantes}")
    print(f"Promedios: {calcular_promedios(estudiantes)}")
    
    print("\n=== Ejercicios para Practicar ===")
    ejercicio_1()
    print()
    ejercicio_2()
