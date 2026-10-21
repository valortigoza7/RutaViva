"""Tests del árbol general (TP5): jerarquía de categorías de RutaViva."""

import unittest

from servicios.arbol_general import ArbolGeneral, NodoGeneral

JERARQUIA = {
    "Naturaleza": ["Bosques y selvas", "Cataratas y ríos", "Parques naturales"],
    "Montaña": ["Cordillera", "Sierras"],
    "Playa": ["Costa atlántica", "Playas de río"],
    "Ciudad": ["Ciudades históricas", "Grandes ciudades"],
}


def armar_arbol():
    arbol = ArbolGeneral("RutaViva")
    for categoria, subcategorias in JERARQUIA.items():
        nodo = arbol.agregar_hijo(arbol.raiz, categoria)
        for sub in subcategorias:
            arbol.agregar_hijo(nodo, sub)
    return arbol


class TestArbolGeneral(unittest.TestCase):
    def setUp(self):
        self.arbol = armar_arbol()

    def test_estructura(self):
        self.assertEqual(self.arbol.raiz.nombre, "RutaViva")
        self.assertEqual(len(self.arbol.raiz.hijos), 4)
        total = len(self.arbol.recorrido_preorden())
        self.assertEqual(total, 14)

    def test_agregar_hijo_devuelve_el_nodo(self):
        nuevo = self.arbol.agregar_hijo(self.arbol.raiz, "Rural")
        self.assertIsInstance(nuevo, NodoGeneral)
        self.assertIn(nuevo, self.arbol.raiz.hijos)

    def test_agregar_hijo_padre_invalido(self):
        with self.assertRaises(TypeError):
            self.arbol.agregar_hijo("Playa", "Otra")

    def test_preorden(self):
        esperado = [
            "RutaViva",
            "Naturaleza", "Bosques y selvas", "Cataratas y ríos", "Parques naturales",
            "Montaña", "Cordillera", "Sierras",
            "Playa", "Costa atlántica", "Playas de río",
            "Ciudad", "Ciudades históricas", "Grandes ciudades",
        ]
        self.assertEqual(self.arbol.recorrido_preorden(), esperado)

    def test_postorden(self):
        resultado = self.arbol.recorrido_postorden()
        self.assertEqual(resultado[-1], "RutaViva")
        for categoria, subs in JERARQUIA.items():
            for sub in subs:
                self.assertLess(resultado.index(sub), resultado.index(categoria))

    def test_por_niveles(self):
        resultado = self.arbol.recorrido_por_niveles()
        self.assertEqual(resultado[0], "RutaViva")
        self.assertEqual(resultado[1:5], list(JERARQUIA.keys()))
        self.assertEqual(len(resultado), 14)

    def test_los_tres_recorridos_visitan_los_mismos_nodos(self):
        pre = sorted(self.arbol.recorrido_preorden())
        post = sorted(self.arbol.recorrido_postorden())
        niv = sorted(self.arbol.recorrido_por_niveles())
        self.assertEqual(pre, post)
        self.assertEqual(pre, niv)

    def test_buscar_categoria(self):
        nodo = self.arbol.buscar("Playa")
        self.assertIsNotNone(nodo)
        self.assertEqual([h.nombre for h in nodo.hijos],
                         ["Costa atlántica", "Playas de río"])

    def test_buscar_hoja(self):
        nodo = self.arbol.buscar("Cordillera")
        self.assertIsNotNone(nodo)
        self.assertEqual(nodo.hijos, [])

    def test_buscar_ignora_mayusculas(self):
        self.assertIsNotNone(self.arbol.buscar("montaña"))
        self.assertIsNotNone(self.arbol.buscar("CIUDADES HISTÓRICAS"))

    def test_buscar_inexistente(self):
        self.assertIsNone(self.arbol.buscar("Desierto"))

    def test_buscar_la_raiz(self):
        self.assertIs(self.arbol.buscar("rutaviva"), self.arbol.raiz)


if __name__ == "__main__":
    unittest.main()
