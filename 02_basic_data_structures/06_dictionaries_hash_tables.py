"""
Basic Data Structures - Dictionaries
Tema: Hash table concept
"""

def hash_table_concept():
    """Concepto de tabla hash y su implementación en Python como diccionarios"""
    print("=== Hash Table Concept ===")
    
    print("Una tabla hash es una estructura de datos que implementa un tipo de datos abstracto")
    print("llamado diccionario o mapa, que permite almacenar pares clave-valor.")
    print("En Python, los diccionarios son implementaciones de tablas hash.")
    
    print("\nCaracterísticas principales:")
    print("- Acceso rápido O(1) en promedio para búsqueda, inserción y eliminación")
    print("- Las claves deben ser inmutables (strings, números, tuplas)")
    print("- No hay un orden garantizado (aunque desde Python 3.7 mantienen orden de inserción)")
    print("- Cada clave aparece una sola vez en el diccionario")
    
    print("\nFuncionamiento interno:")
    print("1. Se calcula un valor hash para la clave usando una función hash")
    print("2. El valor hash se usa para determinar la posición en la tabla")
    print("3. En caso de colisiones (dos claves con el mismo hash), se usan técnicas como:")
    print("   - Encadenamiento (linked list en cada posición)")
    print("   - Direccionamiento abierto (buscar la siguiente posición disponible)")
    
    print("\nEjemplo de función hash simple:")
    print("Para la clave 'hola', podríamos sumar los valores ASCII de cada carácter:")
    print("h (104) + o (111) + l (108) + a (97) = 420")
    print("Luego, para una tabla de tamaño 10, haríamos 420 % 10 = 0")
    print("Así, 'hola' se almacenaría en la posición 0 de la tabla")

def ejercicio_practico():
    """
    Ejercicio: Implementar una función que verifique si dos strings son anagramas
    usando un diccionario para contar la frecuencia de caracteres.
    
    Ejemplo: 'listen' y 'silent' son anagramas
    """
    # Datos de ejemplo
    str1 = "listen"
    str2 = "silent"
    print(f"\n--- Ejercicio Práctico ---")
    print(f"String 1: '{str1}'")
    print(f"String 2: '{str2}'")
    
    # TODO: Implementa tu solución aquí
    # Pista: Usa un diccionario para contar la frecuencia de cada carácter
    
    # Solución de ejemplo (descomenta para probar)
    # def son_anagramas(s1, s2):
    #     if len(s1) != len(s2):
    #         return False
    #     
    #     contador = {}
    #     
    #     # Contar caracteres del primer string
    #     for char in s1:
    #         if char in contador:
    #             contador[char] += 1
    #         else:
    #             contador[char] = 1
    #     
    #     # Restar caracteres del segundo string
    #     for char in s2:
    #         if char not in contador:
    #             return False
    #         contador[char] -= 1
    #         if contador[char] == 0:
    #             del contador[char]
    #     
    #     # Si el diccionario está vacío, son anagramas
    #     return len(contador) == 0
    # 
    # print(f"¿Son anagramas? {son_anagramas(str1, str2)}")

if __name__ == "__main__":
    hash_table_concept()
    ejercicio_practico()
