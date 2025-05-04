/**
 * TypeScript Basics - Variables and Data Types
 */

// Basic Types
const numberVariable: number = 42;
const stringVariable: string = "Hello, TypeScript!";
const booleanVariable: boolean = true;
const undefinedVariable: undefined = undefined;
const nullVariable: null = null;

// Arrays
const numberArray: number[] = [1, 2, 3, 4, 5];
const stringArray: Array<string> = ["a", "b", "c"];

// Tuples
const tuple: [string, number] = ["age", 30];

// Object Types
interface Person {
  name: string;
  age: number;
  isActive?: boolean; // Optional property
}

const person: Person = {
  name: "John",
  age: 30,
  isActive: true
};

// Union Types
let id: string | number = 123;
id = "ABC-123"; // Also valid

// Type Assertions
const someValue: any = "This is a string";
const strLength: number = (someValue as string).length;

// Enums
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT"
}
const playerDirection: Direction = Direction.Up;

// Function with type annotations
function add(a: number, b: number): number {
  return a + b;
}

// Usage examples
console.log(`Number: ${numberVariable}`);
console.log(`String: ${stringVariable}`);
console.log(`Person: ${person.name}, ${person.age} years old`);
console.log(`Direction: ${playerDirection}`);
console.log(`2 + 3 = ${add(2, 3)}`); 