"""
Servicio Catalogo.

Se encarga de cargar los destinos desde un archivo JSON y de exponer
las operaciones básicas que va a usar la interfaz de terminal:
Buscar, Listar y Filtrar.
"""

import json
from pathlib import Path
from typing import List, Optional

from modelos.destino import Destino


class Catalogo:
    def __init__(self):
        self._destinos: List[Destino] = []

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
