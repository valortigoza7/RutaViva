import json
from pathlib import Path

from servicios.arbol_avl import ArbolAVL


def calcular_altura(nodo):
    if nodo is None:
        return 0

    altura_izquierda = calcular_altura(nodo.izquierdo)
    altura_derecha = calcular_altura(nodo.derecho)

    return 1 + max(altura_izquierda, altura_derecha)


def verificar_equilibrio(nodo):
    if nodo is None:
        return True

    altura_izquierda = calcular_altura(nodo.izquierdo)
    altura_derecha = calcular_altura(nodo.derecho)

    if abs(altura_izquierda - altura_derecha) > 1:
        return False

    return (
        verificar_equilibrio(nodo.izquierdo)
        and verificar_equilibrio(nodo.derecho)
    )


def main():
    raiz_proyecto = Path(__file__).resolve().parents[2]
    ruta_datos = raiz_proyecto / "datos" / "destinos.json"

    with ruta_datos.open(encoding="utf-8") as archivo:
        destinos = json.load(archivo)

    destinos_ordenados = sorted(
        destinos,
        key=lambda destino: destino["nombre"].lower()
    )

    arbol = ArbolAVL()

    print("VERIFICACIÓN DEL AVL CON DESTINOS DE RUTAVIVA")
    print("=" * 50)

    for destino in destinos_ordenados:
        clave = destino["nombre"].lower()
        arbol.insertar(clave, destino)

    cantidad = len(destinos_ordenados)
    altura = calcular_altura(arbol.raiz)
    equilibrado = verificar_equilibrio(arbol.raiz)

    print(f"Destinos insertados: {cantidad}")
    print(f"Altura del AVL: {altura}")
    print(f"Árbol equilibrado: {equilibrado}")

    # Comprobar que todos los destinos puedan encontrarse.
    encontrados = 0

    for destino in destinos_ordenados:
        clave = destino["nombre"].lower()

        if arbol.buscar(clave) is not None:
            encontrados += 1

    print(f"Destinos encontrados: {encontrados}/{cantidad}")

    # Comprobar que el recorrido inorder esté ordenado.
    recorrido = arbol.inorder()

    nombres = [
        destino["nombre"].lower()
        for destino in recorrido
    ]

    orden_correcto = nombres == sorted(nombres)

    print(f"Recorrido inorder ordenado: {orden_correcto}")

    print("\nRESULTADO FINAL")

    if (
        equilibrado
        and encontrados == cantidad
        and orden_correcto
    ):
        print("VERIFICACIÓN EXITOSA: el AVL funciona correctamente.")
    else:
        print("VERIFICACIÓN FALLIDA: hay que revisar la implementación.")


if __name__ == "__main__":
    main()