/**
 * Implement Quick Sort
 * 
 * Dificultad: Medio
 * 
 * Descripción:
 * Implementa el algoritmo de ordenación rápida (QuickSort).
 * QuickSort es un algoritmo de ordenación eficiente que utiliza 
 * la estrategia "divide y vencerás".
 * 
 * Pasos del algoritmo:
 * 1. Elegir un elemento pivote del array.
 * 2. Particionar: reorganizar el array de modo que todos los elementos menores que 
 *    el pivote estén a la izquierda, y todos los mayores a la derecha.
 * 3. Aplicar recursivamente los pasos anteriores a los sub-arrays izquierdo y derecho.
 * 
 * Ejemplo:
 * Input: [5,2,3,1]
 * Output: [1,2,3,5]
 */

function quickSort(arr: number[]): number[] {
  // Tu implementación aquí
  return [];
}

// Función auxiliar para particionar el array (puedes utilizarla en tu implementación)
function partition(arr: number[], low: number, high: number): number {
  // Tu implementación aquí
  return 0;
}

// Casos de prueba
console.log(quickSort([5, 2, 3, 1]));          // Debería devolver [1, 2, 3, 5]
console.log(quickSort([5, 1, 1, 2, 0, 0]));    // Debería devolver [0, 0, 1, 1, 2, 5]
console.log(quickSort([]));                    // Debería devolver []
console.log(quickSort([1]));                   // Debería devolver [1] 