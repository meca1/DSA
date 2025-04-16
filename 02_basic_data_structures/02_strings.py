"""
Basic Data Structures - Strings
Este archivo cubre los siguientes temas:
1. String methods and operations
2. Practice: String manipulation problems
"""

def string_methods():
    """Métodos y operaciones con strings"""
    print("=== 1. String Methods and Operations ===")
    
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
    print(f"\nMayúsculas (upper): '{texto.upper()}'")
    print(f"Minúsculas (lower): '{texto.lower()}'")
    print(f"Primera letra mayúscula (capitalize): '{texto.capitalize()}'")
    print(f"Palabras con mayúscula (title): '{texto.title()}'")
    
    # Métodos de búsqueda
    print(f"\nPosición de 'Mundo' (find): {texto.find('Mundo')}")
    print(f"¿Contiene 'Hola'? (in): {'Hola' in texto}")
    print(f"¿Comienza con 'Hola'? (startswith): {texto.startswith('Hola')}")
    print(f"¿Termina con 'Mundo'? (endswith): {texto.endswith('Mundo')}")
    
    # Métodos de reemplazo
    print(f"\nReemplazar 'Mundo' por 'Python' (replace): '{texto.replace('Mundo', 'Python')}'")
    
    # Métodos de división y unión
    palabras = texto.split()
    print(f"\nDividir en palabras (split): {palabras}")
    unido = '-'.join(palabras)
    print(f"Unir con guiones (join): '{unido}'")
    
    # Métodos de eliminación de espacios
    texto_espacios = "   texto con espacios   "
    print(f"\nString con espacios: '{texto_espacios}'")
    print(f"Eliminar espacios al inicio y final (strip): '{texto_espacios.strip()}'")
    print(f"Eliminar espacios al inicio (lstrip): '{texto_espacios.lstrip()}'")
    print(f"Eliminar espacios al final (rstrip): '{texto_espacios.rstrip()}'")
    
    # Métodos de verificación
    print(f"\n¿Es alfanumérico? (isalnum): {'Hola123'.isalnum()}")
    print(f"¿Es alfabético? (isalpha): {'Hola'.isalpha()}")
    print(f"¿Es numérico? (isdigit): {'123'.isdigit()}")
    print(f"¿Está en minúsculas? (islower): {'hola'.islower()}")
    print(f"¿Está en mayúsculas? (isupper): {'HOLA'.isupper()}")

def ejercicio_1(texto):
    """
    String Manipulation Problem 1:
    Contar la frecuencia de cada carácter en un string.
    Retornar un diccionario con los caracteres como claves y las frecuencias como valores.
    Ejemplo: "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    # TODO: Implementa el conteo de frecuencia de caracteres
    pass

def ejercicio_2(texto):
    """
    String Manipulation Problem 2:
    Verificar si un string es un palíndromo (se lee igual de izquierda a derecha y viceversa).
    Ignorar espacios, puntuación y diferencias entre mayúsculas y minúsculas.
    Ejemplo: "Anita lava la tina" -> True
    """
    # TODO: Implementa la verificación de palíndromo
    pass

if __name__ == "__main__":
    # Demostración de métodos de string
    string_methods()
    
    # Ejercicios de manipulación de strings
    print("\n=== 2. String Manipulation Problems ===")
    
    # Ejercicio 1: Frecuencia de caracteres
    texto = "hello world"
    print(f"\nEjercicio 1 - Frecuencia de caracteres:")
    print(f"Texto: '{texto}'")
    print("Completa ejercicio_1() para contar la frecuencia de cada carácter")
    
    # Ejercicio 2: Palíndromo
    palindromo = "Anita lava la tina"
    print(f"\nEjercicio 2 - Verificar palíndromo:")
    print(f"Texto: '{palindromo}'")
    print("Completa ejercicio_2() para verificar si es un palíndromo")
