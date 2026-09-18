"""
Servicio Catalogo.

Se encarga de cargar los destinos desde un archivo JSON y de exponer
las operaciones básicas que va a usar la interfaz de terminal:
Buscar, Listar y Filtrar.
"""

import json
import bisect
from pathlib import Path
from typing import List, Optional

from modelos.destino import Destino


class Catalogo:
    def __init__(self):
        self._destinos: List[Destino] = []
        self._claves: List[str] = []

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
        self._claves = []

    def buscar(self, nombre: str) -> Optional[Destino]:
        nombre = nombre.strip().lower()
        for destino in self._destinos:
            if destino.nombre.lower() == nombre:
                return destino
        return None

    def listar(self) -> List[Destino]:
        return list(self._destinos)

    def filtrar_por_categoria(self, categoria: str) -> List[Destino]:
        categoria = categoria.strip().lower()
        return [d for d in self._destinos if d.categoria.lower() == categoria]

    def categorias_disponibles(self) -> List[str]:
        return sorted({d.categoria for d in self._destinos})

    def cantidad(self) -> int:
        return len(self._destinos)

    def ordenar_por_nombre(self) -> None:
        """Ordena los destinos alfabéticamente para permitir búsqueda binaria y actualiza cache de claves"""
        self._destinos.sort(key=lambda destino: destino.nombre.lower())
        self._claves = [d.nombre.lower() for d in self._destinos]


    def buscar_binaria(self, nombre: str):
        """Busca un destino por nombre mediante búsqueda binaria."""
        if not self._destinos:
            return None
        if not self._claves or len(self._claves)!= len(self._destinos):
            self._claves = [d.nombre.lower() for d in self._destinos]

        nombre_buscado = nombre.strip().lower()
        indice = bisect.bisect_left(self._claves, nombre_buscado)

        if indice < len(self._claves) and self._claves[indice] == nombre_buscado:
            return self._destinos[indice]
        return None
