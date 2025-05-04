# Ejercicios de Entrevistas Técnicas - TypeScript

## Arrays y Strings

### 1. Two Sum
**Dificultad:** Fácil

Dado un array de números enteros `nums` y un entero `target`, devuelve los índices de los dos números que suman `target`.

```typescript
function twoSum(nums: number[], target: number): number[] {
  // Tu implementación aquí
}

// Ejemplo:
// Input: nums = [2,7,11,15], target = 9
// Output: [0,1] (porque nums[0] + nums[1] == 9)
```

### 2. Valid Anagram
**Dificultad:** Fácil

Dadas dos strings `s` y `t`, determina si `t` es un anagrama de `s`.

```typescript
function isAnagram(s: string, t: string): boolean {
  // Tu implementación aquí
}

// Ejemplo:
// Input: s = "anagram", t = "nagaram"
// Output: true
```

### 3. Product of Array Except Self
**Dificultad:** Medio

Dado un array `nums`, devuelve un array `answer` donde `answer[i]` es igual al producto de todos los elementos de `nums` excepto `nums[i]`.

```typescript
function productExceptSelf(nums: number[]): number[] {
  // Tu implementación aquí
}

// Ejemplo:
// Input: nums = [1,2,3,4]
// Output: [24,12,8,6]
```

## Listas Enlazadas

### 4. Reverse Linked List
**Dificultad:** Fácil

Invierte una lista enlazada simple.

```typescript
class ListNode {
  val: number;
  next: ListNode | null;
  
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function reverseList(head: ListNode | null): ListNode | null {
  // Tu implementación aquí
}

// Ejemplo:
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]
```

### 5. Merge Two Sorted Lists
**Dificultad:** Fácil

Fusiona dos listas enlazadas ordenadas en una sola lista ordenada.

```typescript
function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  // Tu implementación aquí
}

// Ejemplo:
// Input: l1 = [1,2,4], l2 = [1,3,4]
// Output: [1,1,2,3,4,4]
```

## Árboles y Grafos

### 6. Maximum Depth of Binary Tree
**Dificultad:** Fácil

Encuentra la profundidad máxima de un árbol binario.

```typescript
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function maxDepth(root: TreeNode | null): number {
  // Tu implementación aquí
}

// Ejemplo:
// Input: root = [3,9,20,null,null,15,7]
// Output: 3
```

### 7. Validate Binary Search Tree
**Dificultad:** Medio

Determina si un árbol binario es un árbol de búsqueda binaria válido (BST).

```typescript
function isValidBST(root: TreeNode | null): boolean {
  // Tu implementación aquí
}

// Ejemplo:
// Input: root = [2,1,3]
// Output: true
```

## Algoritmos de Búsqueda y Ordenación

### 8. Implement Quick Sort
**Dificultad:** Medio

Implementa el algoritmo de ordenación rápida (QuickSort).

```typescript
function quickSort(arr: number[]): number[] {
  // Tu implementación aquí
}

// Ejemplo:
// Input: [5,2,3,1]
// Output: [1,2,3,5]
```

### 9. Search in Rotated Sorted Array
**Dificultad:** Medio

Busca un valor `target` en un array ordenado y rotado. Devuelve el índice si existe, de lo contrario -1.

```typescript
function search(nums: number[], target: number): number {
  // Tu implementación aquí
}

// Ejemplo:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
```

## Programación Dinámica

### 10. Climbing Stairs
**Dificultad:** Fácil

Estás subiendo una escalera que tiene n escalones. Puedes subir 1 o 2 escalones a la vez. ¿De cuántas formas distintas puedes subir hasta el escalón superior?

```typescript
function climbStairs(n: number): number {
  // Tu implementación aquí
}

// Ejemplo:
// Input: n = 3
// Output: 3 (Hay tres formas: 1+1+1, 1+2, 2+1)
```

### 11. Longest Increasing Subsequence
**Dificultad:** Medio

Encuentra la longitud de la subsecuencia creciente más larga en un array de números.

```typescript
function lengthOfLIS(nums: number[]): number {
  // Tu implementación aquí
}

// Ejemplo:
// Input: nums = [10,9,2,5,3,7,101,18]
// Output: 4 (La subsecuencia es [2,3,7,101])
```

## Diseño de Sistemas

### 12. Implementar una caché LRU (Least Recently Used)
**Dificultad:** Medio

Diseña e implementa una estructura de datos para un caché LRU (Least Recently Used).

```typescript
class LRUCache {
  constructor(capacity: number) {
    // Tu implementación aquí
  }

  get(key: number): number {
    // Tu implementación aquí
  }

  put(key: number, value: number): void {
    // Tu implementación aquí
  }
}

// Ejemplo:
// Input: ["LRUCache", "put", "put", "get", "put", "get", "get"]
// [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3]]
// Output: [null, null, null, 1, null, -1, 3]
```

### 13. Rate Limiter
**Dificultad:** Medio

Implementa un limitador de velocidad que restrinja el número de solicitudes que un cliente puede hacer en un período de tiempo.

```typescript
class RateLimiter {
  constructor(limit: number, timeWindowMs: number) {
    // Tu implementación aquí
  }

  canMakeRequest(clientId: string): boolean {
    // Tu implementación aquí
  }
}

// Ejemplo: Limitador que permite 3 solicitudes por minuto
// const limiter = new RateLimiter(3, 60000);
// limiter.canMakeRequest("user1"); // true
// limiter.canMakeRequest("user1"); // true
// limiter.canMakeRequest("user1"); // true
// limiter.canMakeRequest("user1"); // false (excede el límite)
```

## Node.js Específicos

### 14. Implementar un sistema de middlewares
**Dificultad:** Medio

Implementa un sistema simple de middlewares similar al de Express.

```typescript
type MiddlewareFunction = (req: any, res: any, next: () => void) => void;

class App {
  private middlewares: MiddlewareFunction[];

  constructor() {
    // Tu implementación aquí
  }

  use(middleware: MiddlewareFunction): void {
    // Tu implementación aquí
  }

  handleRequest(req: any, res: any): void {
    // Tu implementación aquí
  }
}

// Ejemplo:
// const app = new App();
// app.use((req, res, next) => {
//   req.user = { id: 1 };
//   next();
// });
// app.use((req, res, next) => {
//   res.send(`User ID: ${req.user.id}`);
// });
```

### 15. Implementar un EventEmitter
**Dificultad:** Medio

Crea una implementación simple de un EventEmitter similar al de Node.js.

```typescript
class MyEventEmitter {
  // Tu implementación aquí

  on(event: string, listener: Function): this {
    // Tu implementación aquí
    return this;
  }

  emit(event: string, ...args: any[]): boolean {
    // Tu implementación aquí
    return true;
  }

  removeListener(event: string, listener: Function): this {
    // Tu implementación aquí
    return this;
  }
}

// Ejemplo:
// const emitter = new MyEventEmitter();
// emitter.on('event', (a, b) => {
//   console.log(a, b);
// });
// emitter.emit('event', 'a', 'b');
```

## Bonus: Patrones de Diseño

### 16. Implementar Singleton
**Dificultad:** Fácil

Implementa el patrón de diseño Singleton en TypeScript.

```typescript
class Singleton {
  // Tu implementación aquí

  static getInstance(): Singleton {
    // Tu implementación aquí
  }

  someMethod(): void {
    console.log("Method called!");
  }
}

// Ejemplo:
// const instance1 = Singleton.getInstance();
// const instance2 = Singleton.getInstance();
// console.log(instance1 === instance2); // Debe ser true
```

### 17. Implementar Factory Method
**Dificultad:** Medio

Implementa el patrón de diseño Factory Method en TypeScript.

```typescript
interface Product {
  operation(): string;
}

abstract class Creator {
  abstract factoryMethod(): Product;

  someOperation(): string {
    const product = this.factoryMethod();
    return `Creator: ${product.operation()}`;
  }
}

// Implementa las clases concretas:
// class ConcreteCreator1 extends Creator { ... }
// class ConcreteProduct1 implements Product { ... }
``` 