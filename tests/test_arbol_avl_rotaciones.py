import unittest

from servicios.arbol_avl import ArbolAVL


class TestArbolAVLRotaciones(unittest.TestCase):

    def calcular_altura(self, nodo):
        if nodo is None:
            return 0

        izquierda = self.calcular_altura(nodo.izquierdo)
        derecha = self.calcular_altura(nodo.derecho)

        return 1 + max(izquierda, derecha)

    def verificar_equilibrio(self, nodo):
        if nodo is None:
            return True

        altura_izquierda = self.calcular_altura(nodo.izquierdo)
        altura_derecha = self.calcular_altura(nodo.derecho)

        if abs(altura_izquierda - altura_derecha) > 1:
            return False

        return (
            self.verificar_equilibrio(nodo.izquierdo)
            and self.verificar_equilibrio(nodo.derecho)
        )

    def probar_rotacion(self, claves, raiz_esperada):
        arbol = ArbolAVL()

        for clave in claves:
            arbol.insertar(clave, str(clave))

        self.assertEqual(arbol.raiz.clave, raiz_esperada)
        self.assertTrue(self.verificar_equilibrio(arbol.raiz))

        resultado = [
            elemento
            for elemento in arbol.inorder()
        ]

        self.assertEqual(
            resultado,
            [str(clave) for clave in sorted(claves)]
        )

    def test_rotacion_izquierda_izquierda(self):
        self.probar_rotacion([30, 20, 10], 20)

    def test_rotacion_derecha_derecha(self):
        self.probar_rotacion([10, 20, 30], 20)

    def test_rotacion_izquierda_derecha(self):
        self.probar_rotacion([30, 10, 20], 20)

    def test_rotacion_derecha_izquierda(self):
        self.probar_rotacion([10, 30, 20], 20)


if __name__ == "__main__":
    unittest.main()