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

TP6: se agrega top_n, que usa la heap binaria (servicios/heap_binaria.py)
para obtener los N destinos mejor puntuados sin ordenar todo el catálogo.

TP7: se agrega el grafo de destinos (servicios/grafo.py). Dos destinos
quedan conectados si comparten región o categoría. Los vértices son los
nombres de los destinos (no los objetos Destino, porque Destino define
__eq__ sin __hash__ y por eso no se puede usar como clave de un dict).
"""

import bisect
import json
from pathlib import Path
from typing import List, Optional

from modelos.destino import Destino
from servicios.arbol_binario import ArbolBinarioBusqueda
from servicios.grafo import Grafo
from servicios.heap_binaria import HeapBinaria


class Catalogo:
    def __init__(self):
        self._destinos: List[Destino] = []
        self._nombres_ordenados: List[str] = []  # cache para buscar_binaria (TP2)
        self._arbol = ArbolBinarioBusqueda()      # TP3
        self._grafo = Grafo()                     # TP7

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

    # --- TP6: Top-N con heap binaria ---
    def top_n(self, n: int) -> List[Destino]:
        """
        Devuelve los n destinos con mayor rating, de mejor a peor.
        Si hay empate de rating, sale primero el que se cargó antes.

        Complejidad: O(m + n log m), con m = cantidad de destinos.
        - Armar la heap con la construcción de Floyd (sift_down desde
          la mitad hacia atrás) cuesta O(m), en vez de O(m log m) que
          costaría insertar de a uno.
        - Cada extraer_maximo cuesta O(log m) y se hace solo n veces.
        Ordenar todo el catálogo costaría O(m log m) aunque se pidan
        solo 10 destinos.
        """
        if n <= 0:
            return []

        heap = HeapBinaria()
        # Misma tupla que arma HeapBinaria.insertar: (prioridad, -orden, elemento)
        heap.heap = [
            (destino.rating, -i, destino)
            for i, destino in enumerate(self._destinos)
        ]
        heap._contador = len(heap.heap)
        for i in range(len(heap.heap) // 2 - 1, -1, -1):
            heap.sift_down(i)

        resultado = []
        while len(resultado) < n and not heap.esta_vacia():
            _, destino = heap.extraer_maximo()
            resultado.append(destino)
        return resultado

    # --- TP7: grafo de destinos relacionados ---
    def construir_grafo(self) -> None:
        """
        Arma el grafo no dirigido de destinos: cada destino es un vértice
        (identificado por su nombre) y dos destinos se conectan si
        comparten región o categoría.

        Se llama una sola vez después de cargar los datos. Comparar todos
        los pares cuesta O(m^2); es un costo de preparación, no de consulta.
        """
        self._grafo = Grafo()
        for destino in self._destinos:
            self._grafo.agregar_vertice(destino.nombre)
        for i, a in enumerate(self._destinos):
            for b in self._destinos[i + 1:]:
                if self.motivo_relacion(a, b):
                    self._grafo.conectar(a.nombre, b.nombre)

    @staticmethod
    def motivo_relacion(a: Destino, b: Destino) -> List[str]:
        """Devuelve por qué dos destinos están relacionados (lista vacía si no lo están)."""
        motivos = []
        if a.region.lower() == b.region.lower():
            motivos.append(f"misma región ({a.region})")
        if a.categoria.lower() == b.categoria.lower():
            motivos.append(f"misma categoría ({a.categoria})")
        return motivos

    @property
    def grafo(self) -> Grafo:
        """Grafo de destinos; se construye la primera vez que se pide."""
        if not self._grafo.adyacencia:
            self.construir_grafo()
        return self._grafo

    def relacionados(self, nombre: str) -> Optional[List[Destino]]:
        """
        Devuelve los destinos conectados con el indicado, del mejor al peor
        rating (con empate, por nombre). Devuelve None si el destino no existe.
        Costo: O(k log k), con k = cantidad de vecinos.
        """
        destino = self.buscar(nombre)
        if destino is None:
            return None
        vecinos = [self.buscar(n) for n in self.grafo.obtener_vecinos(destino.nombre)]
        return sorted(vecinos, key=lambda d: (-d.rating, d.nombre))

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
