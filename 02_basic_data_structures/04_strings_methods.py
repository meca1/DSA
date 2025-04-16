"""
Basic Data Structures - Strings
Tema: String methods and operations
"""

def string_methods():
    """Métodos y operaciones con strings"""
    print("=== String Methods and Operations ===")
    
    # Crear strings
    texto = "Hola Mundo"
    print(f"String original: '{texto}'")
    
    # Longitud
    print(f"\nLongitud (len): {len(texto)}")
    
    # Acceso a caracteres
    print(f"Primer carácter: '{texto[0]}'")
    print(f"Último carácter: '{texto[-1]}'")
    
    # Slicing
    print(f"Primeros 4 caracteres: '{texto[:4]}'")
    print(f"Últimos 5 caracteres: '{texto[-5:]}'")
    
    # Métodos de transformación
    print(f"\n--- Métodos de transformación ---")
    print(f"Mayúsculas (upper): '{texto.upper()}'")
    print(f"Minúsculas (lower): '{texto.lower()}'")
    print(f"Primera letra mayúscula (capitalize): '{texto.capitalize()}'")
    print(f"Palabras con mayúscula (title): '{texto.title()}'")
    
    # Métodos de búsqueda
    print(f"\n--- Métodos de búsqueda ---")
    print(f"Posición de 'Mundo' (find): {texto.find('Mundo')}")
    print(f"¿Contiene 'Hola'? (in): {'Hola' in texto}")
    print(f"¿Comienza con 'Hola'? (startswith): {texto.startswith('Hola')}")
    print(f"¿Termina con 'Mundo'? (endswith): {texto.endswith('Mundo')}")
    
    # Métodos de reemplazo
    print(f"\n--- Métodos de reemplazo ---")
    print(f"Reemplazar 'Mundo' por 'Python' (replace): '{texto.replace('Mundo', 'Python')}'")
    
    # Métodos de división y unión
    print(f"\n--- Métodos de división y unión ---")
    palabras = texto.split()
    print(f"Dividir en palabras (split): {palabras}")
    unido = '-'.join(palabras)
    print(f"Unir con guiones (join): '{unido}'")
    
    # Métodos de eliminación de espacios
    print(f"\n--- Métodos de eliminación de espacios ---")
    texto_espacios = "   texto con espacios   "
    print(f"String con espacios: '{texto_espacios}'")
    print(f"Eliminar espacios al inicio y final (strip): '{texto_espacios.strip()}'")
    print(f"Eliminar espacios al inicio (lstrip): '{texto_espacios.lstrip()}'")
    print(f"Eliminar espacios al final (rstrip): '{texto_espacios.rstrip()}'")
    
    # Métodos de verificación
    print(f"\n--- Métodos de verificación ---")
    print(f"¿Es alfanumérico? (isalnum): {'Hola123'.isalnum()}")
    print(f"¿Es alfabético? (isalpha): {'Hola'.isalpha()}")
    print(f"¿Es numérico? (isdigit): {'123'.isdigit()}")
    print(f"¿Está en minúsculas? (islower): {'hola'.islower()}")
    print(f"¿Está en mayúsculas? (isupper): {'HOLA'.isupper()}")

def ejercicio_practico():
    """
    Ejercicio: Implementar una función que cuente las vocales en un string.
    """
    # Datos de ejemplo
    texto = "Python es un lenguaje de programación"
    print(f"\n--- Ejercicio Práctico ---")
    print(f"Texto: '{texto}'")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar un bucle for y el método lower()
    
    # Solución de ejemplo (descomenta para probar)
    # vocales = "aeiou"
    # contador = 0
    # for letra in texto.lower():
    #     if letra in vocales:
    #         contador += 1
    # print(f"Número de vocales: {contador}")

if __name__ == "__main__":
    string_methods()
    ejercicio_practico()
