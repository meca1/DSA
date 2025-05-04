/**
 * Reverse Linked List
 * 
 * Dificultad: Fácil
 * 
 * Descripción:
 * Invierte una lista enlazada simple.
 * 
 * Ejemplo:
 * Input: head = [1,2,3,4,5]
 * Output: [5,4,3,2,1]
 */

// Definición de la clase ListNode
class ListNode {
  val: number;
  next: ListNode | null;
  
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

// Función auxiliar para crear una lista enlazada a partir de un array
function createLinkedList(values: number[]): ListNode | null {
  if (!values.length) return null;
  
  const head = new ListNode(values[0]);
  let current = head;
  
  for (let i = 1; i < values.length; i++) {
    current.next = new ListNode(values[i]);
    current = current.next;
  }
  
  return head;
}

// Función auxiliar para convertir una lista enlazada a array (para mostrar resultados)
function linkedListToArray(head: ListNode | null): number[] {
  const result: number[] = [];
  let current = head;
  
  while (current) {
    result.push(current.val);
    current = current.next;
  }
  
  return result;
}

function reverseList(head: ListNode | null): ListNode | null {
  // Tu implementación aquí
  return null;
}

// Casos de prueba
const list1 = createLinkedList([1, 2, 3, 4, 5]);
console.log(linkedListToArray(reverseList(list1))); // Debería devolver [5, 4, 3, 2, 1]

const list2 = createLinkedList([1, 2]);
console.log(linkedListToArray(reverseList(list2))); // Debería devolver [2, 1]

const list3 = createLinkedList([]);
console.log(linkedListToArray(reverseList(list3))); // Debería devolver [] 