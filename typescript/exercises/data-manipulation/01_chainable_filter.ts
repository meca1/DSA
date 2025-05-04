/**
 * Chainable Data Filter
 * 
 * Dificultad: Medio
 * 
 * Descripción:
 * Implementa un sistema de filtros encadenables (chainable) para manipular colecciones de datos.
 * Este patrón permite componer operaciones de filtrado, ordenación y limitación de manera fluida.
 * 
 * La implementación debe permitir:
 * - Filtrar elementos por una propiedad y valor (where)
 * - Ordenar elementos por una propiedad (sort)
 * - Limitar el número de resultados (limit)
 * - Saltar elementos (skip/offset)
 * - Ejecutar la cadena de operaciones y obtener el resultado (execute)
 * 
 * Ejemplo de uso:
 * const result = new DataFilter(users)
 *   .where('isActive', true)
 *   .sort('age')
 *   .limit(10)
 *   .execute();
 */

// Definición de la interfaz para las opciones de filtro
interface FilterOptions<T> {
  sortBy?: keyof T;
  filterKey?: keyof T;
  filterValue?: any;
  limit?: number;
  skip?: number;
}

// Implementación de la clase DataFilter
class DataFilter<T> {
  private data: T[] = [];
  
  constructor(data: T[]) {
    // Tu implementación aquí
  }
  
  where(key: keyof T, value: any): DataFilter<T> {
    // Tu implementación aquí
    return this;
  }
  
  sort(key: keyof T, ascending: boolean = true): DataFilter<T> {
    // Tu implementación aquí
    return this;
  }
  
  limit(count: number): DataFilter<T> {
    // Tu implementación aquí
    return this;
  }
  
  skip(count: number): DataFilter<T> {
    // Tu implementación aquí
    return this;
  }
  
  execute(): T[] {
    // Tu implementación aquí
    return [];
  }
}

// Casos de prueba
// Definir un tipo de datos para la prueba
interface User {
  id: number;
  name: string;
  age: number;
  isActive: boolean;
}

// Crear datos de ejemplo
const users: User[] = [
  { id: 1, name: "John", age: 25, isActive: true },
  { id: 2, name: "Jane", age: 30, isActive: false },
  { id: 3, name: "Bob", age: 20, isActive: true },
  { id: 4, name: "Alice", age: 35, isActive: true },
  { id: 5, name: "Charlie", age: 40, isActive: false },
  { id: 6, name: "Diana", age: 28, isActive: true },
  { id: 7, name: "Edward", age: 33, isActive: true },
  { id: 8, name: "Fiona", age: 22, isActive: false },
];

// Ejecutar pruebas
console.log("Usuarios activos ordenados por edad (ascendente), limitados a 3:");
const activeUsersSortedByAge = new DataFilter(users)
  .where('isActive', true)
  .sort('age')
  .limit(3)
  .execute();
console.log(activeUsersSortedByAge);
// Debería mostrar usuarios activos con ID 3, 1, 6 (Bob, John, Diana)

console.log("\nUsuarios inactivos:");
const inactiveUsers = new DataFilter(users)
  .where('isActive', false)
  .execute();
console.log(inactiveUsers);
// Debería mostrar usuarios con ID 2, 5, 8 (Jane, Charlie, Fiona)

console.log("\nUsuarios ordenados por nombre (descendente):");
const usersByNameDesc = new DataFilter(users)
  .sort('name', false)
  .execute();
console.log(usersByNameDesc);
// Debería mostrar usuarios ordenados de la Z a la A

console.log("\nUsuarios con skip 2 y limit 3:");
const paginatedUsers = new DataFilter(users)
  .skip(2)
  .limit(3)
  .execute();
console.log(paginatedUsers);
// Debería mostrar usuarios con ID 3, 4, 5 (Bob, Alice, Charlie) 