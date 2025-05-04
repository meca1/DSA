/**
 * LRU Cache (Least Recently Used Cache)
 * 
 * Dificultad: Medio
 * 
 * Descripción:
 * Diseña e implementa una estructura de datos para un caché LRU (Least Recently Used).
 * Debe soportar las siguientes operaciones: get y put.
 * 
 * - get(key): Obtiene el valor asociado con la clave key si existe, o -1 si no.
 * - put(key, value): Establece o inserta el par clave-valor. Cuando el caché alcanza 
 *   su capacidad, debe eliminar el elemento menos recientemente usado antes de insertar uno nuevo.
 * 
 * Ejemplo:
 * Input: ["LRUCache", "put", "put", "get", "put", "get", "get"]
 *        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3]]
 * Output: [null, null, null, 1, null, -1, 3]
 * 
 * Explicación:
 * LRUCache lruCache = new LRUCache(2);  // Capacidad: 2
 * lruCache.put(1, 1);
 * lruCache.put(2, 2);
 * lruCache.get(1);      // returns 1
 * lruCache.put(3, 3);   // elimina el par (2,2)
 * lruCache.get(2);      // returns -1 (no encontrado)
 * lruCache.get(3);      // returns 3
 */

class LRUCache {
  // Tus propiedades aquí
  
  constructor(capacity: number) {
    // Tu implementación aquí
  }
  
  get(key: number): number {
    // Tu implementación aquí
    return -1;
  }
  
  put(key: number, value: number): void {
    // Tu implementación aquí
  }
}

// Casos de prueba
const lruCache = new LRUCache(2);
lruCache.put(1, 1);
lruCache.put(2, 2);
console.log(lruCache.get(1));    // Debería devolver 1
lruCache.put(3, 3);              // Elimina la clave 2
console.log(lruCache.get(2));    // Debería devolver -1 (no encontrado)
console.log(lruCache.get(3));    // Debería devolver 3
lruCache.put(4, 4);              // Elimina la clave 1
console.log(lruCache.get(1));    // Debería devolver -1 (no encontrado)
console.log(lruCache.get(3));    // Debería devolver 3
console.log(lruCache.get(4));    // Debería devolver 4 