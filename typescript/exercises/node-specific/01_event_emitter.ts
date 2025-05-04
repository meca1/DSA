/**
 * Event Emitter Implementation
 * 
 * Dificultad: Medio
 * 
 * Descripción:
 * Implementa una versión simplificada de la clase EventEmitter de Node.js.
 * Un EventEmitter permite registrar funciones que se ejecutan cuando ocurren eventos específicos.
 * 
 * Debe implementar los siguientes métodos:
 * - on(event, listener): Registra una función para ser llamada cuando ocurre un evento
 * - emit(event, ...args): Dispara un evento, ejecutando todos los listeners registrados
 * - removeListener(event, listener): Elimina un listener específico de un evento
 * 
 * Ejemplo:
 * const emitter = new MyEventEmitter();
 * emitter.on('message', (text) => console.log(`Received: ${text}`));
 * emitter.emit('message', 'Hello world!'); // Imprime "Received: Hello world!"
 */

class MyEventEmitter {
  // Tus propiedades aquí
  
  constructor() {
    // Tu implementación aquí
  }
  
  on(event: string, listener: Function): this {
    // Tu implementación aquí
    return this;
  }
  
  emit(event: string, ...args: any[]): boolean {
    // Tu implementación aquí
    return false;
  }
  
  removeListener(event: string, listener: Function): this {
    // Tu implementación aquí
    return this;
  }
}

// Casos de prueba
const emitter = new MyEventEmitter();
let messagesReceived: string[] = [];

// Registrar listeners
const listener1 = (message: string) => messagesReceived.push(`Listener 1: ${message}`);
const listener2 = (message: string) => messagesReceived.push(`Listener 2: ${message}`);

emitter.on('message', listener1);
emitter.on('message', listener2);
emitter.on('data', (data: any) => messagesReceived.push(`Data: ${JSON.stringify(data)}`));

// Emitir eventos
emitter.emit('message', 'Hello'); // Debería llamar a listener1 y listener2
emitter.emit('data', { id: 123 }); // Debería llamar al listener de data

// Comprobar resultados
console.log(messagesReceived);
// Debería imprimir:
// ['Listener 1: Hello', 'Listener 2: Hello', 'Data: {"id":123}']

// Eliminar un listener
emitter.removeListener('message', listener1);
messagesReceived = [];

// Emitir de nuevo
emitter.emit('message', 'World'); // Ahora solo debería llamar a listener2
console.log(messagesReceived); 
// Debería imprimir:
// ['Listener 2: World'] 