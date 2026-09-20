"""
Servicio Catalogo.

Se encarga de cargar los destinos desde un archivo JSON y de exponer
las operaciones básicas que va a usar la interfaz de terminal:
Buscar, Listar y Filtrar.

TP2: se agrega una segunda estrategia de búsqueda (buscar_binaria)
para poder comparar su complejidad contra la búsqueda secuencial
del TP1. En TP3 se va a sumar una tercera estrategia basada en un
árbol binario de búsqueda.
"""

import bisect
import json
from pathlib import Path
from typing import List, Optional

from modelos.destino import Destino


class Catalogo:
    def __init__(self):
        self._destinos: List[Destino] = []
        self._nombres_ordenados: List[str] = []  # cache para buscar_binaria

    # --- Carga de datos ---
    def cargar_desde_json(self, ruta: str) -> None:
        path = Path(ruta)
        with path.open(encoding="utf-8") as archivo:
            datos = json.load(archivo)

        self._destinos = [
            Destino(
                nombre=item["nombre"],
                categoria=item["categoria"],
                region=item["region"],
                rating=item["rating"],
                descripcion=item.get("descripcion", ""),
            )
            for item in datos
        ]

    # --- Operación 1: Buscar ---
    def buscar(self, nombre: str) -> Optional[Destino]:
        nombre = nombre.strip().lower()
        for destino in self._destinos:
            if destino.nombre.lower() == nombre:
                return destino
        return None

    # --- TP2: preparación y búsqueda binaria ---
    def ordenar_por_nombre(self) -> None:
        """
        Ordena la lista interna de destinos por nombre.

        Se llama una sola vez (después de cargar los datos), no dentro
        de buscar_binaria: si ordenáramos en cada búsqueda, el costo
        O(n log n) del ordenamiento se sumaría al de cada consulta y
        la medición dejaría de reflejar el costo real de "buscar".
        """
        self._destinos.sort(key=lambda d: d.nombre.lower())
        # Se cachean las claves en minúscula una sola vez acá: si
        # buscar_binaria las reconstruyera en cada llamada, pagaría un
        # recorrido O(n) por consulta y anularía la ventaja de O(log n).
        self._nombres_ordenados = [d.nombre.lower() for d in self._destinos]

    def buscar_binaria(self, nombre: str) -> Optional[Destino]:
        """
        Busca un destino por nombre usando búsqueda binaria (bisect).

        Requiere que la lista ya esté ordenada por nombre
        (llamar antes a ordenar_por_nombre).
        """
        nombre = nombre.strip().lower()
        indice = bisect.bisect_left(self._nombres_ordenados, nombre)
        if indice < len(self._nombres_ordenados) and self._nombres_ordenados[indice] == nombre:
            return self._destinos[indice]
        return None

    # --- Operación 2: Listar ---
    def listar(self) -> List[Destino]:
        return list(self._destinos)

    # --- Operación 3: Filtrar (por categoría) ---
    def filtrar_por_categoria(self, categoria: str) -> List[Destino]:
        categoria = categoria.strip().lower()
        return [d for d in self._destinos if d.categoria.lower() == categoria]

    def categorias_disponibles(self) -> List[str]:
        return sorted({d.categoria for d in self._destinos})

    def cantidad(self) -> int:
        return len(self._destinos)
