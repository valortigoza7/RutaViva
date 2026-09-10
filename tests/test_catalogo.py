import unittest

from servicios.catalogo import Catalogo


class TestCatalogo(unittest.TestCase):
    """Pruebas para las operaciones principales del catálogo."""

    def setUp(self):
        """Prepara un catálogo cargado con los datos de prueba."""
        self.catalogo = Catalogo()
        self.catalogo.cargar_desde_json("datos/destinos.json")

    def test_buscar_por_nombre(self):
        """Verifica que se pueda buscar un destino por nombre."""
        resultado = self.catalogo.buscar("Bariloche")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Bariloche")

    def test_buscar_sin_distinguir_mayusculas(self):
        """Verifica que la búsqueda no distinga mayúsculas."""
        resultado = self.catalogo.buscar("bariloche")

        self.assertIsNotNone(resultado)
        self.assertEqual(resultado.nombre, "Bariloche")

    def test_buscar_devuelve_none_si_no_existe(self):
        """Verifica que una búsqueda inexistente devuelva None."""
        resultado = self.catalogo.buscar("Destino Inexistente")

        self.assertIsNone(resultado)

    def test_listar_devuelve_destinos(self):
        """Verifica que listar devuelva los destinos cargados."""
        resultados = self.catalogo.listar()

        self.assertTrue(len(resultados) > 0)

    def test_filtrar_por_categoria(self):
        """Verifica que se puedan filtrar destinos por categoría."""
        resultados = self.catalogo.filtrar_por_categoria("montaña")

        self.assertTrue(len(resultados) > 0)
        self.assertTrue(
            all(
                destino.categoria.lower() == "montaña"
                for destino in resultados
            )
        )


if __name__ == "__main__":
    unittest.main()