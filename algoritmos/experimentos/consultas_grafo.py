"""
Ejemplos de consultas sobre el grafo de destinos (TP7, punto 3).

Uso (desde la raíz del proyecto):
    PYTHONPATH=. python algoritmos/experimentos/consultas_grafo.py
En Windows (PowerShell):
    $env:PYTHONPATH="."; python algoritmos/experimentos/consultas_grafo.py
"""

from pathlib import Path

from servicios.catalogo import Catalogo
from servicios import consultas_grafo as q

RUTA = Path(__file__).resolve().parents[2] / "datos" / "destinos.json"


def titulo(texto):
    print("\n" + "=" * 60)
    print(texto)
    print("=" * 60)


def main():
    cat = Catalogo()
    cat.cargar_desde_json(RUTA)
    cat.construir_grafo()

    g = cat.grafo
    aristas = sum(len(v) for v in g.adyacencia.values()) // 2
    print(f"Grafo: {len(g.adyacencia)} vértices, {aristas} aristas")

    titulo("Consulta 1: ¿Qué destinos están relacionados con Bariloche?")
    for d in cat.relacionados("Bariloche") or []:
        motivo = ", ".join(Catalogo.motivo_relacion(cat.buscar("Bariloche"), d))
        print(f"  - {d.nombre} ⭐{d.rating}  ({motivo})")

    titulo("Consulta 2: ¿Con cuántos destinos está conectado cada uno de estos?")
    for nombre in ("Bariloche", "Iguazú", "Cabo Polonio"):
        print(f"  {nombre}: {q.grado(cat, nombre)} conexiones")

    titulo("Consulta 3: Los 3 destinos más conectados")
    for nombre, cantidad in q.mas_conectados(cat, 3):
        print(f"  {nombre}: {cantidad} conexiones")

    titulo("Consulta 4: ¿Están conectados Salta y Salinas Grandes? ¿Y Salta e Iguazú?")
    for a, b in (("Salta", "Salinas Grandes"), ("Salta", "Iguazú"), ("Salta", "Mendoza")):
        resultado = q.estan_conectados(cat, a, b)
        if resultado is None:
            print(f"  {a} - {b}: alguno de los dos no está en el catálogo")
            continue
        conectados, motivos = resultado
        detalle = ", ".join(motivos) if motivos else "no comparten región ni categoría"
        print(f"  {a} - {b}: {'SÍ' if conectados else 'NO'} ({detalle})")

    titulo("Consulta 5: Destinos conectados a la vez con Córdoba y con Mendoza")
    print("  ", q.vecinos_en_comun(cat, "Córdoba", "Mendoza"))

    titulo("Consulta 6: Destinos sin ninguna conexión")
    print("  ", q.destinos_aislados(cat) or "ninguno")

    titulo("Consulta 7: Un destino que no existe")
    print("  relacionados('Atlantis') ->", cat.relacionados("Atlantis"))

    titulo("Consulta 8 (TP8 - BFS): Recomendaciones progresivas desde Bariloche")
    sugerencias = q.recomendaciones_por_cercania_bfs(cat, "Bariloche", limite=6)
    print("  Orden de cercanía (BFS):", " -> ".join(sugerencias or []))

    titulo("Consulta 9 (TP8 - DFS): Itinerario encadenado en profundidad desde Bariloche")
    itinerario = q.itinerario_encadenado_dfs(cat, "Bariloche")
    print("  Ruta profunda (DFS):", " -> ".join(itinerario or []))
if __name__ == "__main__":
    main()
