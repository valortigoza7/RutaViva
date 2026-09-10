"""
Interfaz de terminal de RutaViva.
"""

from servicios.catalogo import Catalogo

SEPARADOR = "-" * 40


def mostrar_destino(destino) -> None:
    print(f"\n  {destino.nombre}")
    print(f"  Categoría: {destino.categoria} | Región: {destino.region}")
    print(f"  Rating: ⭐{destino.rating}")
    if destino.descripcion:
        print(f"  {destino.descripcion}")


def opcion_buscar(catalogo: Catalogo) -> None:
    nombre = input("Nombre del destino: ").strip()
    resultado = catalogo.buscar(nombre)
    if resultado:
        mostrar_destino(resultado)
    else:
        print(f"\nNo se encontró ningún destino llamado '{nombre}'.")


def opcion_explorar_categorias(catalogo: Catalogo) -> None:
    categorias = catalogo.categorias_disponibles()
    print("\nCategorías disponibles:")
    for i, cat in enumerate(categorias, start=1):
        print(f"  {i}. {cat}")

    seleccion = input("Elegí una categoría: ").strip().lower()
    resultados = catalogo.filtrar_por_categoria(seleccion)

    if not resultados:
        print(f"\nNo hay destinos en la categoría '{seleccion}'.")
        return

    print(f"\nDestinos en '{seleccion}':")
    for destino in resultados:
        print(f"  - {destino}")


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
        print("2. Explorar categorías")
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
