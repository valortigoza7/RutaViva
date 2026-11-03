"""Tests del grafo de destinos y sus consultas (TP7, puntos 3 y 4)."""

import json
import tempfile
import unittest
from pathlib import Path

from servicios import consultas_grafo as q
from servicios.catalogo import Catalogo

DATOS = [
    # nombre, categoria, region, rating
    ("Bariloche", "montaña", "Patagonia", 9.0),
    ("El Chaltén", "montaña", "Patagonia", 8.9),
    ("Ushuaia", "naturaleza", "Patagonia", 9.0),
    ("Iguazú", "naturaleza", "Litoral", 9.6),
    ("Mar del Plata", "playa", "Buenos Aires", 7.8),  # no comparte nada
    ("Isla Perdida", "isla", "Mar Austral", 5.0),     # no comparte nada
]


def catalogo():
    datos = [
        {"nombre": n, "categoria": c, "region": r, "rating": rt}
        for n, c, r, rt in DATOS
    ]
    with tempfile.TemporaryDirectory() as tmp:
        ruta = Path(tmp) / "d.json"
        ruta.write_text(json.dumps(datos), encoding="utf-8")
        cat = Catalogo()
        cat.cargar_desde_json(ruta)
    cat.construir_grafo()
    return cat


class TestGrafoCatalogo(unittest.TestCase):
    def setUp(self):
        self.cat = catalogo()

    def test_un_vertice_por_destino(self):
        self.assertEqual(len(self.cat.grafo.adyacencia), len(DATOS))

    def test_arista_por_misma_region_o_categoria(self):
        g = self.cat.grafo
        self.assertIn("Ushuaia", g.obtener_vecinos("Bariloche"))   # región
        self.assertIn("Ushuaia", g.obtener_vecinos("Iguazú"))      # categoría
        self.assertNotIn("Iguazú", g.obtener_vecinos("Bariloche"))

    def test_grafo_no_dirigido(self):
        g = self.cat.grafo
        for a, vecinos in g.adyacencia.items():
            for b in vecinos:
                self.assertIn(a, g.obtener_vecinos(b))

    def test_sin_aristas_repetidas_ni_lazos(self):
        for a, vecinos in self.cat.grafo.adyacencia.items():
            self.assertEqual(len(vecinos), len(set(vecinos)))
            self.assertNotIn(a, vecinos)

    def test_relacionados_ordenados_por_rating(self):
        nombres = [d.nombre for d in self.cat.relacionados("Ushuaia")]
        self.assertEqual(nombres, ["Iguazú", "Bariloche", "El Chaltén"])

    def test_relacionados_ignora_mayusculas(self):
        self.assertEqual(
            [d.nombre for d in self.cat.relacionados("  bariloche ")],
            [d.nombre for d in self.cat.relacionados("Bariloche")],
        )

    def test_relacionados_inexistente(self):
        self.assertIsNone(self.cat.relacionados("Atlantis"))

    def test_relacionados_de_destino_aislado(self):
        self.assertEqual(self.cat.relacionados("Isla Perdida"), [])

    def test_catalogo_vacio_da_grafo_vacio(self):
