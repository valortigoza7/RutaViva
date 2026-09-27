"""
Tests de integración del árbol binario dentro del Catalogo (TP3).

test_arbol_binario.py ya prueba el árbol en aislamiento (inserción,
búsqueda, recorridos). Estos tests prueban que la integración con
Catalogo funcione: que buscar_en_arbol() dé el mismo resultado que
las otras dos estrategias (TP1 y TP2) para el mismo dataset.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from servicios.catalogo import Catalogo

RUTA_DATOS = Path(__file__).parent.parent / "datos" / "destinos.json"


def _catalogo_cargado() -> Catalogo:
    catalogo = Catalogo()
    catalogo.cargar_desde_json(RUTA_DATOS)
    catalogo.ordenar_por_nombre()
    catalogo.construir_arbol()
    return catalogo


def test_buscar_en_arbol_encuentra_destino_existente():
    catalogo = _catalogo_cargado()
    resultado = catalogo.buscar_en_arbol("Bariloche")
    assert resultado is not None
    assert resultado.nombre == "Bariloche"


def test_buscar_en_arbol_no_encuentra_destino_inexistente():
    catalogo = _catalogo_cargado()
    assert catalogo.buscar_en_arbol("Marte") is None


def test_buscar_en_arbol_es_insensible_a_mayusculas_y_espacios():
    catalogo = _catalogo_cargado()
    resultado = catalogo.buscar_en_arbol("  bariloche  ")
    assert resultado is not None
    assert resultado.nombre == "Bariloche"


def test_las_tres_estrategias_coinciden_para_todos_los_destinos():
    """
    Compara buscar (TP1), buscar_binaria (TP2) y buscar_en_arbol (TP3)
    para cada destino del catálogo: las tres tienen que devolver el
    mismo resultado, porque están resolviendo la misma consulta.
    """
    catalogo = _catalogo_cargado()
    for destino in catalogo.listar():
        r_secuencial = catalogo.buscar(destino.nombre)
        r_binaria = catalogo.buscar_binaria(destino.nombre)
        r_arbol = catalogo.buscar_en_arbol(destino.nombre)

        assert r_secuencial is not None
        assert r_binaria is not None
        assert r_arbol is not None
        assert r_secuencial.nombre == r_binaria.nombre == r_arbol.nombre


if __name__ == "__main__":
    test_buscar_en_arbol_encuentra_destino_existente()
    test_buscar_en_arbol_no_encuentra_destino_inexistente()
    test_buscar_en_arbol_es_insensible_a_mayusculas_y_espacios()
    test_las_tres_estrategias_coinciden_para_todos_los_destinos()
    print("Todos los tests de integración pasaron ✅")
