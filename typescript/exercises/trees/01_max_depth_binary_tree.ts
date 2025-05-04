/**
 * Maximum Depth of Binary Tree
 * 
 * Dificultad: Fácil
 * 
 * Descripción:
 * Encuentra la profundidad máxima de un árbol binario.
 * La profundidad máxima es el número de nodos en el camino más largo 
 * desde el nodo raíz hasta el nodo hoja más lejano.
 * 
 * Ejemplo:
 * Input: root = [3,9,20,null,null,15,7]
 * Output: 3
 */

// Definición de la clase TreeNode
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

// Función auxiliar para crear un árbol binario a partir de un array
// El array se interpreta como un árbol binario en orden de nivel
// null representa un nodo vacío
function createBinaryTree(values: (number | null)[]): TreeNode | null {
  if (!values.length || values[0] === null) return null;
  
  const root = new TreeNode(values[0]);
  const queue: TreeNode[] = [root];
  let i = 1;
  
  while (i < values.length) {
    const node = queue.shift()!;
    
    // Crear nodo izquierdo
    if (i < values.length && values[i] !== null) {
      node.left = new TreeNode(values[i] as number);
      queue.push(node.left);
    }
    i++;
    
    // Crear nodo derecho
    if (i < values.length && values[i] !== null) {
      node.right = new TreeNode(values[i] as number);
      queue.push(node.right);
    }
    i++;
  }
  
  return root;
}

function maxDepth(root: TreeNode | null): number {
  // Tu implementación aquí
  return 0;
}

// Casos de prueba
const tree1 = createBinaryTree([3, 9, 20, null, null, 15, 7]);
console.log(maxDepth(tree1)); // Debería devolver 3

const tree2 = createBinaryTree([1, null, 2]);
console.log(maxDepth(tree2)); // Debería devolver 2

const tree3 = createBinaryTree([]);
console.log(maxDepth(tree3)); // Debería devolver 0 