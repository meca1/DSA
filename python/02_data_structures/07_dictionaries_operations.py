"""
Basic Data Structures - Dictionaries
Tema: Dictionary operations
"""

def dictionary_operations():
    """Operaciones básicas con diccionarios"""
    print("=== Dictionary Operations ===")
    
    # Crear diccionarios
    print("\n--- Creación de diccionarios ---")
    # Método 1: Usando llaves {}
    persona = {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Madrid"
    }
    print(f"Diccionario creado con llaves: {persona}")
    
    # Método 2: Usando dict()
    persona2 = dict(nombre="Carlos", edad=30, ciudad="Barcelona")
    print(f"Diccionario creado con dict(): {persona2}")
    
    # Método 3: A partir de una lista de tuplas
    items = [("nombre", "Elena"), ("edad", 28), ("ciudad", "Valencia")]
    persona3 = dict(items)
    print(f"Diccionario creado a partir de tuplas: {persona3}")
    
    # Acceder a valores
    print("\n--- Acceso a valores ---")
    print(f"Acceso con corchetes: persona['nombre'] = {persona['nombre']}")
    print(f"Acceso con get(): persona.get('edad') = {persona.get('edad')}")
    print(f"Acceso con get() y valor por defecto: persona.get('profesion', 'No especificada') = {persona.get('profesion', 'No especificada')}")
    
    # Modificar valores
    print("\n--- Modificación de valores ---")
    persona["edad"] = 26
    print(f"Después de modificar edad: {persona}")
    
    # Añadir nuevos pares clave-valor
    persona["profesion"] = "Ingeniera"
    print(f"Después de añadir profesión: {persona}")
    
    # Eliminar pares clave-valor
    print("\n--- Eliminación de elementos ---")
    # Método 1: del
    del persona["ciudad"]
    print(f"Después de del persona['ciudad']: {persona}")
    
    # Método 2: pop() - elimina y retorna el valor
    profesion = persona.pop("profesion")
    print(f"Valor eliminado con pop(): {profesion}")
    print(f"Después de pop('profesion'): {persona}")
    
    # Método 3: popitem() - elimina y retorna el último par clave-valor
    ultimo_par = persona.popitem()
    print(f"Par eliminado con popitem(): {ultimo_par}")
    print(f"Después de popitem(): {persona}")
    
    # Métodos de diccionarios
    print("\n--- Métodos de diccionarios ---")
    persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
    
    # keys(), values(), items()
    print(f"Claves (keys): {list(persona.keys())}")
    print(f"Valores (values): {list(persona.values())}")
    print(f"Pares clave-valor (items): {list(persona.items())}")
    
    # Verificar si una clave existe
    print(f"\n¿Existe la clave 'nombre'? {'nombre' in persona}")
    print(f"¿Existe la clave 'profesion'? {'profesion' in persona}")
    
    # Limpiar y copiar
    persona_copia = persona.copy()
    print(f"\nCopia del diccionario: {persona_copia}")
    
    persona.clear()
    print(f"Después de clear(): {persona}")
    
    # Combinar diccionarios
    dict1 = {"a": 1, "b": 2}
    dict2 = {"b": 3, "c": 4}
    
    # Método 1: update()
    dict1_copia = dict1.copy()
    dict1_copia.update(dict2)
    print(f"\nCombinar con update(): {dict1_copia}")  # La clave 'b' se sobrescribe
    
    # Método 2: desempaquetado (Python 3.5+)
    combinado = {**dict1, **dict2}
    print(f"Combinar con desempaquetado: {combinado}")  # La clave 'b' se sobrescribe
    
    # Método 3: | (Python 3.9+)
    # combinado = dict1 | dict2
    # print(f"Combinar con operador |: {combinado}")

def ejercicio_practico():
    """
    Ejercicio: Implementar una función que invierta un diccionario
    (intercambiando claves y valores).
    
    Nota: Asume que los valores son únicos e inmutables.
    """
    # Datos de ejemplo
    diccionario = {"a": 1, "b": 2, "c": 3}
    print(f"\n--- Ejercicio Práctico ---")
    print(f"Diccionario original: {diccionario}")
    
    # TODO: Implementa tu solución aquí
    # Pista: Crea un nuevo diccionario intercambiando claves y valores
    
    # Solución de ejemplo (descomenta para probar)
    # invertido = {valor: clave for clave, valor in diccionario.items()}
    # print(f"Diccionario invertido: {invertido}")

if __name__ == "__main__":
    dictionary_operations()
    ejercicio_practico()
