"""Tests de Catalogo.top_n (TP6): Top-N con heap binaria."""

import json
import random
import tempfile
import unittest
from pathlib import Path

from servicios.catalogo import Catalogo


def catalogo_con(ratings):
    datos = [
        {"nombre": f"Destino {i}", "categoria": "playa", "region": "Sur", "rating": r}
        for i, r in enumerate(ratings)
    ]
    with tempfile.TemporaryDirectory() as tmp:
        ruta = Path(tmp) / "d.json"
        ruta.write_text(json.dumps(datos), encoding="utf-8")
        cat = Catalogo()
        cat.cargar_desde_json(ruta)
    return cat


class TestTopN(unittest.TestCase):
    def test_devuelve_los_mejores_en_orden(self):
        cat = catalogo_con([5.0, 9.5, 7.0, 8.2, 6.1])
        self.assertEqual([d.rating for d in cat.top_n(3)], [9.5, 8.2, 7.0])

    def test_n_mayor_que_el_catalogo(self):
        cat = catalogo_con([3.0, 9.0])
        self.assertEqual([d.rating for d in cat.top_n(10)], [9.0, 3.0])

    def test_n_cero_o_negativo(self):
        cat = catalogo_con([3.0, 9.0])
        self.assertEqual(cat.top_n(0), [])
        self.assertEqual(cat.top_n(-2), [])

    def test_catalogo_vacio(self):
        self.assertEqual(Catalogo().top_n(5), [])

    def test_empate_sale_primero_el_que_se_cargo_antes(self):
        cat = catalogo_con([8.0, 8.0, 8.0, 9.0])
        nombres = [d.nombre for d in cat.top_n(4)]
        self.assertEqual(nombres, ["Destino 3", "Destino 0", "Destino 1", "Destino 2"])

    def test_no_modifica_el_catalogo(self):
        cat = catalogo_con([5.0, 9.5, 7.0])
        antes = [d.nombre for d in cat.listar()]
        cat.top_n(2)
        self.assertEqual([d.nombre for d in cat.listar()], antes)
        self.assertEqual(cat.cantidad(), 3)

    def test_coincide_con_ordenar_todo(self):
        random.seed(1)
        ratings = [round(random.uniform(0, 10), 1) for _ in range(500)]
        cat = catalogo_con(ratings)
        esperado = sorted(cat.listar(), key=lambda d: -d.rating)[:10]  # sorted es estable
        self.assertEqual([d.nombre for d in cat.top_n(10)], [d.nombre for d in esperado])


if __name__ == "__main__":
    unittest.main()
