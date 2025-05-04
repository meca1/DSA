/**
 * Singleton Pattern Implementation
 * 
 * Dificultad: Fácil
 * 
 * Descripción:
 * Implementa el patrón de diseño Singleton en TypeScript.
 * 
 * El patrón Singleton garantiza que una clase tenga una única instancia
 * y proporciona un punto de acceso global a ella.
 * 
 * Requisitos:
 * 1. Solo debe existir una instancia de la clase
 * 2. Debe proporcionar un método estático getInstance() para acceder a la instancia
 * 3. No debe ser posible crear nuevas instancias utilizando el constructor directamente
 * 4. Debe incluir al menos un método que demuestre la funcionalidad
 * 
 * Ejemplo de uso:
 * const instance1 = Singleton.getInstance();
 * const instance2 = Singleton.getInstance();
 * console.log(instance1 === instance2); // Debe ser true
 */

class Singleton {
  // Define una propiedad estática para almacenar la instancia
  
  // Constructor privado para evitar instanciación directa
  private constructor() {
    // Tu implementación aquí
  }
  
  // Método estático para obtener la instancia
  static getInstance(): Singleton {
    // Tu implementación aquí
    return null as any;
  }
  
  // Método de ejemplo
  someMethod(): void {
    console.log("Method called from Singleton instance!");
  }
  
  // Otros métodos de ejemplo que podrías agregar
  getData(): { id: number; timestamp: Date } {
    return {
      id: Math.floor(Math.random() * 1000),
      timestamp: new Date()
    };
  }
}

// Casos de prueba
function testSingleton() {
  // Obtener dos instancias
  const instance1 = Singleton.getInstance();
  const instance2 = Singleton.getInstance();
  
  // Verificar que ambas referencias apuntan al mismo objeto
  console.log("¿Las instancias son idénticas?", instance1 === instance2);
  
  // Usar los métodos de la instancia
  instance1.someMethod();
  console.log(instance1.getData());
  
  // Verificar que los cambios en un objeto afectan al otro
  // (porque en realidad es el mismo objeto)
  const data1 = instance1.getData();
  const data2 = instance2.getData();
  console.log("Data 1:", data1);
  console.log("Data 2:", data2);
}

// Ejecutar pruebas
testSingleton(); 