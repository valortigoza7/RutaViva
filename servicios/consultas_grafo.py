"""
Consultas de ejemplo sobre el grafo de destinos (TP7, punto 3).

Todas reciben el catálogo y usan solo las operaciones básicas del grafo
(obtener_vecinos y la lista de vértices): no hacen recorridos, que quedan
para los algoritmos de caminos de una etapa posterior.

n = cantidad de vértices, k = cantidad de vecinos de un destino.
"""

from typing import List, Optional, Tuple

from modelos.destino import Destino
from servicios.catalogo import Catalogo


def grado(catalogo: Catalogo, nombre: str) -> Optional[int]:
    """Consulta 1: ¿con cuántos destinos está conectado? O(1) tras buscar el destino."""
    destino = catalogo.buscar(nombre)
    if destino is None:
        return None
    return len(catalogo.grafo.obtener_vecinos(destino.nombre))


def mas_conectados(catalogo: Catalogo, cantidad: int = 3) -> List[Tuple[str, int]]:
    """Consulta 2: los destinos con más conexiones. O(n log n)."""
    grafo = catalogo.grafo
    ranking = [(v, len(vecinos)) for v, vecinos in grafo.adyacencia.items()]
    ranking.sort(key=lambda par: (-par[1], par[0]))
    return ranking[:cantidad]


def estan_conectados(catalogo: Catalogo, a: str, b: str) -> Optional[Tuple[bool, List[str]]]:
    """
    Consulta 3: ¿dos destinos están directamente conectados y por qué?
    Devuelve None si alguno no existe, o (conectados, motivos).
    """
    da, db = catalogo.buscar(a), catalogo.buscar(b)
    if da is None or db is None or da.nombre == db.nombre:
        return None
    conectados = db.nombre in catalogo.grafo.obtener_vecinos(da.nombre)
    return conectados, Catalogo.motivo_relacion(da, db)


def vecinos_en_comun(catalogo: Catalogo, a: str, b: str) -> Optional[List[str]]:
    """Consulta 4: destinos conectados con los dos a la vez. O(k)."""
    da, db = catalogo.buscar(a), catalogo.buscar(b)
    if da is None or db is None:
        return None
    vb = set(catalogo.grafo.obtener_vecinos(db.nombre))
    return sorted(v for v in catalogo.grafo.obtener_vecinos(da.nombre) if v in vb)


def destinos_aislados(catalogo: Catalogo) -> List[str]:
    """Consulta 5: destinos sin ninguna conexión. O(n)."""
    return sorted(v for v, vecinos in catalogo.grafo.adyacencia.items() if not vecinos)
