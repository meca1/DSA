"""
Basic Data Structures - Strings
Tema: Practice: String manipulation problems
"""

def contar_frecuencia_caracteres(texto):
    """
    Problema 1: Contar la frecuencia de cada carácter en un string.
    
    Args:
        texto: String a analizar
        
    Returns:
        Diccionario con caracteres como claves y frecuencias como valores
        
    Ejemplo: 
        "hello" -> {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    frecuencia = {}
    for caracter in texto:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

def es_palindromo(texto):
    """
    Problema 2: Verificar si un string es un palíndromo.
    
    Args:
        texto: String a verificar
        
    Returns:
        True si es palíndromo, False en caso contrario
        
    Ejemplo:
        "anita lava la tina" -> True (ignorando espacios)
    """
    # Eliminar espacios y convertir a minúsculas
    texto = texto.lower()
    texto = ''.join(caracter for caracter in texto if caracter.isalnum())
    
    # Verificar si es igual al revés
    return texto == texto[::-1]

def ejercicio_1():
    """
    Ejercicio 1: Implementar una función que invierta las palabras en una frase,
    manteniendo el orden de las palabras.
    
    Ejemplo:
        "Hola mundo Python" -> "aloH odnum nohtyP"
    """
    # Datos de ejemplo
    frase = "Hola mundo Python"
    print(f"Frase original: '{frase}'")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar split, un bucle y join
    
    # Solución de ejemplo (descomenta para probar)
    # palabras = frase.split()
    # palabras_invertidas = [palabra[::-1] for palabra in palabras]
    # resultado = ' '.join(palabras_invertidas)
    # print(f"Frase con palabras invertidas: '{resultado}'")

def ejercicio_2():
    """
    Ejercicio 2: Implementar una función que encuentre la subcadena más larga
    sin caracteres repetidos.
    
    Ejemplo:
        "abcabcbb" -> "abc" (longitud 3)
    """
    # Datos de ejemplo
    texto = "abcabcbb"
    print(f"Texto original: '{texto}'")
    
    # TODO: Implementa tu solución aquí
    # Pista: Puedes usar un conjunto (set) y una ventana deslizante
    
    # Solución de ejemplo (descomenta para probar)
    # inicio = 0
    # max_longitud = 0
    # subcadena_actual = ""
    # caracteres = {}
    # 
    # for i, caracter in enumerate(texto):
    #     if caracter in caracteres and caracteres[caracter] >= inicio:
    #         inicio = caracteres[caracter] + 1
    #     else:
    #         longitud_actual = i - inicio + 1
    #         if longitud_actual > max_longitud:
    #             max_longitud = longitud_actual
    #             subcadena_actual = texto[inicio:i+1]
    #     
    #     caracteres[caracter] = i
    # 
    # print(f"Subcadena más larga sin repeticiones: '{subcadena_actual}' (longitud {max_longitud})")

if __name__ == "__main__":
    # Demostración de problemas resueltos
    print("=== Problema 1: Frecuencia de Caracteres ===")
    texto = "hello world"
    print(f"Texto: '{texto}'")
    print(f"Frecuencia de caracteres: {contar_frecuencia_caracteres(texto)}")
    
    print("\n=== Problema 2: Verificación de Palíndromo ===")
    palindromo = "Anita lava la tina"
    print(f"Texto: '{palindromo}'")
    print(f"¿Es palíndromo? {es_palindromo(palindromo)}")
    
    print("\n=== Ejercicios para Practicar ===")
    ejercicio_1()
    print()
    ejercicio_2()
