import sys
import os
import timeit

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import servicios.arbol_binario as mod_bst
import servicios.arbol_avl as mod_avl

def obtener_clase(modulo, posibles_nombres):
    for nombre in posibles_nombres:
        if hasattr(modulo, nombre):
            return getattr(modulo, nombre)
    return None

def medir_tiempos() -> None:
    ClaseBST = obtener_clase(mod_bst, ['ArbolBinario', 'ArbolBinarioBusqueda', 'BST', 'Arbol'])
    ClaseAVL = obtener_clase(mod_avl, ['ArbolAVL', 'AVLTree', 'AVL', 'Arbol'])

    if not ClaseBST or not ClaseAVL:
        print("Error: No se pudieron encontrar las clases de los árboles en los módulos.")
        return

    tamaños = (100, 1000, 3000)
    print("N\tBST Desbalanceado (ms)\tAVL Balanceado (ms)")

    for n in tamaños:
        datos = [f"Destino {i:05d}" for i in range(n)]

        bst = ClaseBST()
        avl = ClaseAVL()

        m_inst_bst = 'insertar' if hasattr(bst, 'insertar') else 'agregar'
        m_inst_avl = 'insertar' if hasattr(avl, 'insertar') else 'agregar'

        for d in datos:
            getattr(bst, m_inst_bst)(d, d)
            getattr(avl, m_inst_avl)(d, d)

        ultimo = datos[-1]
        m_busc_bst = 'buscar' if hasattr(bst, 'buscar') else 'obtener'
        m_busc_avl = 'buscar' if hasattr(avl, 'buscar') else 'obtener'

        t_bst = min(timeit.repeat(lambda: getattr(bst, m_busc_bst)(ultimo), number=10, repeat=3)) / 10 * 1000
        t_avl = min(timeit.repeat(lambda: getattr(avl, m_busc_avl)(ultimo), number=10, repeat=3)) / 10 * 1000

        print(f"{n}\t{t_bst:.4f}\t\t\t{t_avl:.4f}")

if __name__ == "__main__":
    medir_tiempos()