"""
Interfaz de terminal de RutaViva.

TP3: la opción "Buscar destino" pasa a resolverse con el árbol
binario de búsqueda (Catalogo.buscar_en_arbol) en vez de la
búsqueda secuencial del TP1. Esta es la integración real que pide
la consigna: el árbol no es una estructura aislada de prueba, es
la que efectivamente usa el usuario al buscar un destino.
"""

from servicios.catalogo import Catalogo
from servicios.arbol_general import ArbolGeneral

SEPARADOR = "-" * 40


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
    print(f"  Categoría: {destino.categoria} | Región: {destino.region}")
    print(f"  Rating: ⭐{destino.rating}")
    if destino.descripcion:
        print(f"  {destino.descripcion}")


def opcion_buscar(catalogo: Catalogo) -> None:
    nombre = input("Nombre del destino: ").strip()
    resultado = catalogo.buscar_en_arbol(nombre)
    if resultado:
        mostrar_destino(resultado)
    else:
        print(f"\nNo se encontró ningún destino llamado '{nombre}'.")


def opcion_explorar_categorias(catalogo: Catalogo) -> None:
    arbol = construir_jerarquia_rutaviva()
    nodo_actual = arbol.raiz

    while True:
        print(f"\n--- Categoría actual: {nodo_actual.nombre} ---")
        if not nodo_actual.hijos:
            print("  (Categoría final - Sin subcategorías)")
        else:
            for idx, hijo in enumerate(nodo_actual.hijos, start=1):
                print(f"  {idx}. {hijo.nombre}")

        print("  0. Volver al menú principal")
        opcion = input("\nSeleccione una subcategoría: ").strip()

        if opcion == "0":
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(nodo_actual.hijos):
            nodo_actual = nodo_actual.hijos[int(opcion) - 1]
        else:
            print("Opción no válida.")


def opcion_listar(catalogo: Catalogo) -> None:
    print(f"\nCatálogo completo ({catalogo.cantidad()} destinos):")
    for destino in catalogo.listar():
        print(f"  - {destino}")


def menu(catalogo: Catalogo) -> None:
    while True:
        print("\n" + "=" * 40)
        print("        ✈️  RUTAVIVA — TERMINAL")
        print("=" * 40)
        print("1. Buscar destino")
        print("2. Explorar categorías (Árbol General)")
        print("3. Listar todos los destinos")
        print("4. Ver Top 10          (próximamente)")
        print("5. Ver relacionados    (próximamente)")
        print("6. Explorar conexiones (próximamente)")
        print("7. Encontrar camino    (próximamente)")
        print("8. Recomendaciones     (próximamente)")
        print("0. Salir")
        print(SEPARADOR)

        opcion = input("Opción: ").strip()

        if opcion == "1":
            opcion_buscar(catalogo)
        elif opcion == "2":
            opcion_explorar_categorias(catalogo)
        elif opcion == "3":
            opcion_listar(catalogo)
        elif opcion in ("4", "5", "6", "7", "8"):
            print("\nEsta funcionalidad se implementa en una etapa posterior del TP.")
        elif opcion == "0":
            print("\n¡Buen viaje! 👋")
            break
        else:
            print("\nOpción inválida.")