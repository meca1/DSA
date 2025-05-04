# Ejercicios de Entrevista para TypeScript/Node.js

Este directorio contiene una colección de ejercicios de entrevista técnica para TypeScript y Node.js. Los ejercicios están organizados por categorías y diseñados para ayudarte a prepararte para entrevistas técnicas y mejorar tus habilidades de programación.

## Estructura de los Ejercicios

Cada ejercicio está en su propio archivo `.ts` e incluye:

- Descripción detallada del problema
- Plantilla de código para implementar
- Casos de prueba básicos
- Indicaciones de dificultad

## Organización por Categorías

### Arrays y Strings
- [Two Sum](./arrays-strings/01_two_sum.ts) - Encontrar dos números en un array que sumen un valor objetivo
- [Valid Anagram](./arrays-strings/02_valid_anagram.ts) - Verificar si dos cadenas son anagramas
- [Product Except Self](./arrays-strings/03_product_except_self.ts) - Calcular producto de todos los elementos excepto el actual

### Estructuras de Datos Lineales
- [Reverse Linked List](./linked-lists/01_reverse_linked_list.ts) - Invertir una lista enlazada

### Árboles y Grafos
- [Maximum Depth of Binary Tree](./trees/01_max_depth_binary_tree.ts) - Encontrar la profundidad máxima de un árbol binario

### Algoritmos de Búsqueda y Ordenación
- [Quick Sort](./algorithms/01_quick_sort.ts) - Implementar el algoritmo de ordenación QuickSort

### Programación Dinámica
- [Climbing Stairs](./dynamic-programming/01_climbing_stairs.ts) - Calcular distintas formas de subir escaleras

### Diseño de Sistemas
- [LRU Cache](./system-design/01_lru_cache.ts) - Implementar una caché con política de "menos recientemente usado"

### Específicos de Node.js
- [Event Emitter](./node-specific/01_event_emitter.ts) - Implementar un emisor de eventos similar al de Node.js

### Patrones de Diseño
- [Singleton](./design-patterns/01_singleton.ts) - Implementar el patrón de diseño Singleton

### Programación Asíncrona
- [Retry with Backoff](./async-programming/01_retry_with_backoff.ts) - Implementar reintentos con backoff exponencial

### Manipulación de Datos
- [Chainable Filter](./data-manipulation/01_chainable_filter.ts) - Implementar un sistema de filtros encadenables

### Procesamiento de Streams
- [Transform Pipeline](./streams/01_transform_pipeline.ts) - Implementar pipeline de transformación con backpressure

## Cómo Usar los Ejercicios

1. Selecciona un ejercicio según la categoría o nivel de dificultad que quieras practicar
2. Lee detenidamente la descripción del problema
3. Implementa tu solución en la función o clase proporcionada
4. Ejecuta el archivo para verificar tu solución con los casos de prueba incluidos:
   ```
   npx ts-node typescript/exercises/arrays-strings/01_two_sum.ts
   ```
5. Intenta resolver el problema por tu cuenta antes de buscar soluciones

## Niveles de Dificultad

- **Fácil**: Problemas fundamentales que suelen aparecer en entrevistas de primer nivel.
- **Medio**: Problemas más desafiantes que requieren un mejor entendimiento de algoritmos y estructuras de datos.
- **Difícil**: Problemas complejos que evalúan pensamiento algorítmico avanzado y optimizaciones.

## Mejores Prácticas

- Enfócate en la claridad y legibilidad del código
- Optimiza el rendimiento (tiempo y espacio)
- Prueba casos límite (arrays vacíos, valores negativos, etc.)
- Comenta tu código para explicar tu enfoque
- Practica explicando tu solución en voz alta como lo harías en una entrevista 