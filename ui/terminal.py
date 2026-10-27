"""
Interfaz de terminal de RutaViva.

TP3: la opción "Buscar destino" pasa a resolverse con el árbol
binario de búsqueda (Catalogo.buscar_en_arbol) en vez de la
búsqueda secuencial del TP1. Esta es la integración real que pide
la consigna: el árbol no es una estructura aislada de prueba, es
la que efectivamente usa el usuario al buscar un destino.

TP6: la opción "Ver Top 10" se resuelve con la heap binaria
(Catalogo.top_n), que devuelve los destinos mejor puntuados sin
ordenar todo el catálogo.
"""

from servicios.catalogo import Catalogo
from servicios.arbol_general import ArbolGeneral

SEPARADOR = "-" * 40
CANTIDAD_TOP = 10


def construir_jerarquia_rutaviva() -> ArbolGeneral:
    arbol = ArbolGeneral("RutaViva")

    nat = arbol.agregar_hijo(arbol.raiz, "Naturaleza")
    mon = arbol.agregar_hijo(arbol.raiz, "Montaña")
    pla = arbol.agregar_hijo(arbol.raiz, "Playa")
    ciu = arbol.agregar_hijo(arbol.raiz, "Ciudad")

    arbol.agregar_hijo(nat, "Bosques y selvas")
    arbol.agregar_hijo(nat, "Cataratas y ríos")
    arbol.agregar_hijo(nat, "Parques naturales")

    arbol.agregar_hijo(mon, "Cordillera")
    arbol.agregar_hijo(mon, "Sierras")

    arbol.agregar_hijo(pla, "Costa atlántica")
    arbol.agregar_hijo(pla, "Playas de río")

    arbol.agregar_hijo(ciu, "Ciudades históricas")
    arbol.agregar_hijo(ciu, "Grandes ciudades")

    return arbol


def mostrar_destino(destino) -> None:
    print(f"\n  {destino.nombre}")
    print(f"  Categoría:
