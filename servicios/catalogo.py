"""
Servicio Catalogo.

Se encarga de cargar los destinos desde un archivo JSON y de exponer
las operaciones básicas que va a usar la interfaz de terminal:
Buscar, Listar y Filtrar.

TP2: se agrega una segunda estrategia de búsqueda (buscar_binaria)
para poder comparar su complejidad contra la búsqueda secuencial
del TP1.

TP3: se agrega una tercera estrategia (buscar_en_arbol), basada en
un árbol binario de búsqueda (servicios/arbol_binario.py). Esta es
la estrategia que la interfaz de terminal usa realmente para la
opción "Buscar destino" — no es un árbol aislado de prueba, sino la
implementación de producción de la búsqueda por nombre. Las otras
dos (buscar y buscar_binaria) se conservan porque el TP2 las sigue
necesitando para la comparación de complejidad.
"""

import bisect
import json
from pathlib import Path
from typing import List, Optional

from modelos.destino import Destino
from servicios.arbol_binario import ArbolBinarioBusqueda


class Catalogo:
    def __init__(self):
        self._destinos: List[Destino] = []
        self._nombres_ordenados: List[str] = []  # cache para buscar_binaria (TP2)
        self._arbol = ArbolBinarioBusqueda()      # TP3

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

    # --- Operación 1: Buscar (TP1 — búsqueda secuencial) ---
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
        self._nombres_ordenados = [d.nombre.lower() for d in self._destinos]

    def buscar_binaria(self, nombre: str) -> Optional[Destino]:
        """
        Busca un destino por nombre usando búsqueda binaria (bisect).
        Requiere haber llamado antes a ordenar_por_nombre().
        """
        nombre = nombre.strip().lower()
        indice = bisect.bisect_left(self._nombres_ordenados, nombre)
        if indice < len(self._nombres_ordenados) and self._nombres_ordenados[indice] == nombre:
            return self._destinos[indice]
        return None

    # --- TP3: construcción y búsqueda en árbol binario ---
    def construir_arbol(self) -> None:
        """
        Inserta todos los destinos cargados en el árbol binario de
        búsqueda, usando el nombre (en minúscula) como clave de
        ordenamiento.

        Se llama una sola vez, después de cargar los datos — igual
        que ordenar_por_nombre() en el TP2, insertar es un costo que
        se paga al preparar el catálogo, no en cada búsqueda.
        """
        self._arbol = ArbolBinarioBusqueda()
        for destino in self._destinos:
            self._arbol.insertar(destino.nombre.lower(), destino)

    def buscar_en_arbol(self, nombre: str) -> Optional[Destino]:
        """
        Busca un destino por nombre recorriendo el árbol binario de
        búsqueda. Requiere haber llamado antes a construir_arbol().

        Esta es la estrategia que usa la interfaz de terminal (ver
        ui/terminal.py, opción "Buscar destino"): a diferencia de
        buscar_binaria (TP2), que necesita reordenar toda la lista
        cada vez que se agrega un destino nuevo, el árbol solo
        necesita una inserción O(log n) promedio por destino nuevo.
        """
        return self._arbol.buscar(nombre.strip().lower())

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
