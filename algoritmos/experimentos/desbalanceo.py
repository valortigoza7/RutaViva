import json
from pathlib import Path

from servicios.arbol_binario import ArbolBinarioBusqueda


def calcular_altura(nodo):
    """Calcula la altura del árbol en cantidad de nodos."""

    if nodo is None:
        return 0

    altura_izquierda = calcular_altura(nodo.izquierdo)
    altura_derecha = calcular_altura(nodo.derecho)

    return 1 + max(altura_izquierda, altura_derecha)

def main():
    # Localizar el archivo destinos.json del proyecto.
    raiz_proyecto = Path(__file__).resolve().parents[2]
    ruta_datos = raiz_proyecto / "datos" / "destinos.json"

    # Cargar los destinos reales de RutaViva.
    with ruta_datos.open(encoding="utf-8") as archivo:
        destinos = json.load(archivo)

    # Ordenar los destinos alfabéticamente por nombre.
    destinos_ordenados = sorted(
        destinos,
        key=lambda destino: destino["nombre"].lower()
    )

    # Crear el BST original del TP3.
    arbol = ArbolBinarioBusqueda()

    print("EXPERIMENTO: BST DESBALANCEADO")
    print("=" * 40)

    print("\nDestinos insertados en orden alfabético:")

    # Insertar las claves ordenadas en el BST.
    for destino in destinos_ordenados:
        clave = destino["nombre"].lower()

        arbol.insertar(clave, destino)

        print(destino["nombre"])

    # Calcular la altura del árbol resultante.
    cantidad_destinos = len(destinos_ordenados)
    altura = calcular_altura(arbol.raiz)

    print("\nRESULTADOS")
    print("-" * 40)
    print(f"Cantidad de destinos: {cantidad_destinos}")
    print(f"Altura del BST: {altura}")

    if altura == cantidad_destinos:
        print("\nResultado: el BST quedó completamente desbalanceado.")
        print("Todos los nodos forman una cadena hacia la derecha.")
    else:
        print("\nResultado: el árbol no quedó completamente desbalanceado.")

    print("\nConclusión:")
    print(
        "Insertar las claves en orden ascendente puede hacer que "
        "un BST común pierda el equilibrio."
    )


if __name__ == "__main__":
    main()