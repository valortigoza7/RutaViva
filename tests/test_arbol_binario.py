import unittest

from servicios.arbol_binario import ArbolBinarioBusqueda


class TestArbolBinarioBusqueda(unittest.TestCase):

    def setUp(self):
        self.arbol = ArbolBinarioBusqueda()

        self.arbol.insertar("madrid", "Madrid")
        self.arbol.insertar("barcelona", "Barcelona")
        self.arbol.insertar("paris", "París")
        self.arbol.insertar("londres", "Londres")
        self.arbol.insertar("roma", "Roma")

    def test_buscar_elemento_existente(self):
        resultado = self.arbol.buscar("paris")

        self.assertEqual(resultado, "París")

    def test_buscar_elemento_inexistente(self):
        resultado = self.arbol.buscar("tokio")

        self.assertIsNone(resultado)

    def test_recorrido_inorder(self):
        resultado = self.arbol.inorder()

        esperado = [
            "Barcelona",
            "Londres",
            "Madrid",
            "París",
            "Roma"
        ]

        self.assertEqual(resultado, esperado)

    def test_recorrido_preorder(self):
        resultado = self.arbol.preorder()

        esperado = [
            "Madrid",
            "Barcelona",
            "Londres",
            "París",
            "Roma"
        ]

        self.assertEqual(resultado, esperado)

    def test_recorrido_postorder(self):
        resultado = self.arbol.postorder()

        esperado = [
            "Londres",
            "Barcelona",
            "Roma",
            "París",
            "Madrid"
        ]

        self.assertEqual(resultado, esperado)


if __name__ == "__main__":
    unittest.main()