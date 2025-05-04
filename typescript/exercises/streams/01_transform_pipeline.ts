/**
 * Transform Pipeline with Backpressure
 * 
 * Dificultad: Difícil
 * 
 * Descripción:
 * Implementa un sistema de transformación de streams que maneje la contrapresión (backpressure) correctamente.
 * 
 * En procesamiento de datos, la backpressure (contrapresión) es un mecanismo que evita que un productor 
 * de datos rápido sobrecargue a un consumidor más lento, regulando el flujo de datos.
 * 
 * El sistema debe permitir:
 * 1. Añadir transformadores en un pipeline
 * 2. Procesar datos en lotes (batch) para simular backpressure
 * 3. Aplicar transformaciones de forma secuencial
 * 4. Permitir transformadores asíncronos
 * 
 * Ejemplo de uso:
 * const pipeline = new TransformPipeline<string, string>()
 *   .addTransformer(numberParser)  // string -> number
 *   .addTransformer(doubler)       // number -> number
 *   .addTransformer(formatter);    // number -> string
 * 
 * const results = await pipeline.process(inputData, 10);
 */

/**
 * Interfaz para un transformador de stream
 */
interface StreamTransformer<T, R> {
  /**
   * Transforma un elemento de entrada en uno o varios elementos de salida
   * @param chunk - Elemento de entrada
   * @returns Elemento(s) transformado(s) o Promesa de elemento(s)
   */
  transform(chunk: T): R | R[] | Promise<R | R[]>;
  
  /**
   * Método opcional para liberar elementos finales después de procesar todos los chunks
   * @returns Elementos finales o Promesa de elementos finales
   */
  flush?(): R[] | Promise<R[]>;
}

/**
 * Pipeline de transformación para procesar streams de datos con backpressure
 */
class TransformPipeline<T, R> {
  private transformers: StreamTransformer<any, any>[] = [];
  
  /**
   * Añade un transformador al pipeline
   * @param transformer - Transformador a añadir
   * @returns Pipeline modificado con tipo actualizado
   */
  addTransformer<U>(transformer: StreamTransformer<T, U>): TransformPipeline<T, U> {
    // Tu implementación aquí
    return this as any;
  }
  
  /**
   * Procesa un array simulando un stream con backpressure
   * @param input - Datos de entrada
   * @param batchSize - Tamaño de lotes para procesar
   * @returns Promise con resultados procesados
   */
  async process(input: T[], batchSize: number = 10): Promise<R[]> {
    // Tu implementación aquí
    return [];
  }
}

// Casos de prueba

// Transformador: convierte strings a números
const numberParser: StreamTransformer<string, number> = {
  transform(chunk: string): number {
    console.log(`Parsing: ${chunk}`);
    const num = parseFloat(chunk);
    return isNaN(num) ? 0 : num;
  }
};

// Transformador: duplica números
const doubler: StreamTransformer<number, number> = {
  transform(chunk: number): number {
    console.log(`Doubling: ${chunk} -> ${chunk * 2}`);
    return chunk * 2;
  }
};

// Transformador: formatea números como strings
const formatter: StreamTransformer<number, string> = {
  transform(chunk: number): string {
    const result = `Value: ${chunk.toFixed(2)}`;
    console.log(`Formatting: ${chunk} -> ${result}`);
    return result;
  }
};

// Transformador asíncrono: añade un delay para simular operación lenta
const asyncTransformer: StreamTransformer<number, number> = {
  async transform(chunk: number): Promise<number> {
    console.log(`Starting async processing of: ${chunk}`);
    // Simular procesamiento que toma tiempo
    await new Promise(resolve => setTimeout(resolve, 50));
    const result = chunk + 1;
    console.log(`Finished async processing: ${chunk} -> ${result}`);
    return result;
  }
};

// Transformador que devuelve múltiples items para un input
const splitter: StreamTransformer<string, string> = {
  transform(chunk: string): string[] {
    console.log(`Splitting: ${chunk}`);
    // Divide un string por comas y devuelve múltiples outputs
    return chunk.split(',').map(s => s.trim());
  },
  
  // Método flush para demostrar que se llama al final del procesamiento
  flush(): string[] {
    console.log('Flushing splitter...');
    return ['Final item from flush'];
  }
};

// Ejecutar pruebas
async function runTests() {
  console.log("=== Test 1: Pipeline básico ===");
  const pipeline1 = new TransformPipeline<string, string>()
    .addTransformer(numberParser)
    .addTransformer(doubler)
    .addTransformer(formatter);
  
  const inputData = ['1', '2', '3', '4', '5'];
  const results1 = await pipeline1.process(inputData, 2);
  console.log("Resultados:", results1);
  // Debería producir: ["Value: 2.00", "Value: 4.00", "Value: 6.00", "Value: 8.00", "Value: 10.00"]

  console.log("\n=== Test 2: Pipeline con transformador asíncrono ===");
  const pipeline2 = new TransformPipeline<string, string>()
    .addTransformer(numberParser)
    .addTransformer(asyncTransformer)
    .addTransformer(formatter);
  
  const results2 = await pipeline2.process(['10', '20'], 1);
  console.log("Resultados:", results2);
  // Debería producir: ["Value: 11.00", "Value: 21.00"]

  console.log("\n=== Test 3: Pipeline con transformador que produce múltiples outputs ===");
  const pipeline3 = new TransformPipeline<string, string>()
    .addTransformer(splitter)
    .addTransformer({
      transform: chunk => `Processed: ${chunk}`
    });
  
  const results3 = await pipeline3.process(['a,b,c', 'd,e'], 1);
  console.log("Resultados:", results3);
  // Debería producir algo como: ["Processed: a", "Processed: b", "Processed: c", "Processed: d", "Processed: e", "Processed: Final item from flush"]
}

runTests().catch(console.error); 