/**
 * Retry with Exponential Backoff
 * 
 * Dificultad: Medio
 * 
 * Descripción:
 * Implementa una función que reintente una operación asíncrona un número determinado 
 * de veces, con un tiempo de espera exponencial entre intentos.
 * 
 * El backoff exponencial es una estrategia de reintento que aumenta progresivamente 
 * el tiempo de espera entre reintentos para reducir la carga en el sistema y 
 * aumentar la probabilidad de éxito.
 * 
 * Fórmula de backoff: delay = baseDelay * (2 ^ retryCount)
 * 
 * Ejemplo:
 * - Intento 1: delay = 1000ms
 * - Intento 2: delay = 2000ms
 * - Intento 3: delay = 4000ms
 */

/**
 * Reintenta una operación asíncrona con backoff exponencial
 * @param operation - La función a reintentar (debe devolver una promesa)
 * @param maxRetries - Número máximo de reintentos
 * @param baseDelay - Tiempo de espera base (en ms)
 * @returns Promise que resuelve con el resultado o rechaza después de todos los reintentos
 */
function retryWithExponentialBackoff<T>(
  operation: () => Promise<T>,
  maxRetries: number,
  baseDelay: number
): Promise<T> {
  // Tu implementación aquí
  return Promise.reject("Not implemented");
}

// Función auxiliar para simular una operación que falla aleatoriamente
async function simulateUnreliableOperation(): Promise<string> {
  const random = Math.random();
  
  // Simular un 70% de probabilidad de fallo
  if (random < 0.7) {
    console.log("Operation failed, throwing error...");
    throw new Error("Simulated operation failure");
  }
  
  console.log("Operation succeeded!");
  return "Operation result data";
}

// Función auxiliar para esperar un tiempo determinado
function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}

// Casos de prueba
async function runTest() {
  console.log("Starting test with exponential backoff...");
  
  try {
    // Probar con un máximo de 5 reintentos y un retraso base de 500ms
    const result = await retryWithExponentialBackoff(
      simulateUnreliableOperation,
      5,
      500
    );
    
    console.log("Final result:", result);
  } catch (error: any) {
    console.error("All retries failed:", error.message);
  }
}

// Ejecutar prueba
runTest(); 