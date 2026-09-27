"""""
RutaViva — punto de entrada de la aplicación.

TP3: además de cargar los datos, se construye el árbol binario de
búsqueda una sola vez (igual que ordenar_por_nombre en el TP2), para
que la opción "Buscar destino" del menú lo use directamente.
"""

from pathlib import Path

from servicios.catalogo import Catalogo
from ui.terminal import menu

RUTA_DATOS = Path(__file__).parent / "datos" / "destinos.json"


def main() -> None:
    catalogo = Catalogo()
    catalogo.cargar_desde_json(RUTA_DATOS)
    catalogo.construir_arbol()
    print(f"RutaViva cargado con {catalogo.cantidad()} destinos.")
    menu(catalogo)


if __name__ == "__main__":
    main()"
RutaViva — punto de entrada de la aplicación.

TP1: carga los datos desde JSON, arma el catálogo y lanza la
interfaz de terminal.
"""

from pathlib import Path

from servicios.catalogo import Catalogo
from ui.terminal import menu

RUTA_DATOS = Path(__file__).parent / "datos" / "destinos.json"


def main() -> None:
    catalogo = Catalogo()
    catalogo.cargar_desde_json(RUTA_DATOS)
    print(f"RutaViva cargado con {catalogo.cantidad()} destinos.")
    menu(catalogo)


if __name__ == "__main__":
    main()
