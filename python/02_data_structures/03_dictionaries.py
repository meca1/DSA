"""
Basic Data Structures - Dictionaries
Este archivo cubre los siguientes temas:
1. Hash table concept
2. Dictionary operations
3. Practice: Dictionary-based problems
"""

def hash_table_concept():
    """Concepto de tabla hash y su implementación en Python como diccionarios"""
    print("=== 1. Hash Table Concept ===")
    
    print("Una tabla hash es una estructura de datos que implementa un tipo de datos abstracto")
    print("llamado diccionario o mapa, que permite almacenar pares clave-valor.")
    print("En Python, los diccionarios son implementaciones de tablas hash.")
    
    print("\nCaracterísticas principales:")
    print("- Acceso rápido O(1) en promedio para búsqueda, inserción y eliminación")
    print("- Las claves deben ser inmutables (strings, números, tuplas)")
    print("- No hay un orden garantizado (aunque desde Python 3.7 mantienen orden de inserción)")
    print("- Cada clave aparece una sola vez en el diccionario")

def dictionary_operations():
    """Operaciones básicas con diccionarios"""
    print("\n=== 2. Dictionary Operations ===")
    
    # Crear diccionarios
    persona = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Madrid"
    }
    print(f"Diccionario original: {persona}")
    
    # Acceder a valores
    print(f"\nNombre: {persona['nombre']}")
    print(f"Edad: {persona.get('edad')}")
    print(f"Profesión (con valor por defecto): {persona.get('profesion', 'No especificada')}")
    
    # Modificar valores
    persona["edad"] = 26
    print(f"\nDespués de modificar edad: {persona}")
    
    # Añadir nuevos pares clave-valor
    persona["profesion"] = "Ingeniera"
    print(f"Después de añadir profesión: {persona}")
    
    # Eliminar pares clave-valor
    del persona["ciudad"]
    print(f"Después de eliminar ciudad: {persona}")
    
    # Métodos de diccionarios
    print(f"\nClaves (keys): {list(persona.keys())}")
    print(f"Valores (values): {list(persona.values())}")
    print(f"Pares clave-valor (items): {list(persona.items())}")
    
    # Verificar si una clave existe
    print(f"\n¿Existe la clave 'nombre'? {'nombre' in persona}")
    print(f"¿Existe la clave 'ciudad'? {'ciudad' in persona}")
    
    # Limpiar y copiar
    persona_copia = persona.copy()
    print(f"\nCopia del diccionario: {persona_copia}")
    
    persona.clear()
    print(f"Después de clear(): {persona}")
    
    # Combinar diccionarios
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    dict1.update(dict2)
    print(f"\nDespués de update(): {dict1}")  # La clave 'b' se sobrescribe con el valor de dict2

def ejercicio_1(texto):
    """
    Dictionary Problem 1:
    Contar la frecuencia de cada palabra en un texto.
    Retornar un diccionario con las palabras como claves y las frecuencias como valores.
    Ejemplo: "hola mundo hola" -> {'hola': 2, 'mundo': 1}
    """
    # TODO: Implementa el conteo de frecuencia de palabras
    pass

def ejercicio_2(estudiantes):
    """
    Dictionary Problem 2:
    Calcular el promedio de calificaciones de cada estudiante.
    Input: Lista de diccionarios con nombre y calificaciones.
    Output: Diccionario con nombre como clave y promedio como valor.
    
    Ejemplo:
    [
        {"nombre": "Ana", "calificaciones": [90, 85, 95]},
        {"nombre": "Juan", "calificaciones": [80, 75, 85]}
    ]
    ->
    {"Ana": 90.0, "Juan": 80.0}
    """
    # TODO: Implementa el cálculo de promedios
    pass

if __name__ == "__main__":
    # Explicación del concepto de tabla hash
    hash_table_concept()
    
    # Demostración de operaciones con diccionarios
    dictionary_operations()
    
    # Ejercicios con diccionarios
    print("\n=== 3. Dictionary-based Problems ===")
    
    # Ejercicio 1: Frecuencia de palabras
    texto = "este es un ejemplo de texto este texto es un ejemplo"
    print(f"\nEjercicio 1 - Frecuencia de palabras:")
    print(f"Texto: '{texto}'")
    print("Completa ejercicio_1() para contar la frecuencia de cada palabra")
    
    # Ejercicio 2: Promedio de calificaciones
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [90, 85, 95]},
        {"nombre": "Juan", "calificaciones": [80, 75, 85]},
        {"nombre": "María", "calificaciones": [95, 90, 100]}
    ]
    print(f"\nEjercicio 2 - Promedio de calificaciones:")
    print(f"Estudiantes: {estudiantes}")
    print("Completa ejercicio_2() para calcular el promedio de calificaciones")
