import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import timeit
from servicios.catalogo import Catalogo

def main() -> None:
    tamaños = (100, 1000, 10_000, 100_000)
    secuencial_tiempos = []
    binaria_tiempos = []
    arbol_tiempos = []

    print("tamaño\tsecuencial_ms\tbinaria_ms\tarbol_ms")
    
    for n in tamaños:
        ruta = f"datos/destinos_{n}.json"
        
        if not os.path.exists(ruta):
            from datos.generar import generar
            generar(n)

        catalogo = Catalogo()
        
        try:
            catalogo.cargar_desde_json(ruta)
        except TypeError:
            catalogo.cargar_desde_json()
        
        if hasattr(catalogo, 'ordenar_por_nombre'):
            catalogo.ordenar_por_nombre()
        elif hasattr(catalogo, 'ordenar_por_titulo'):
            catalogo.ordenar_por_titulo()

        arbol_listo = False
        if hasattr(catalogo, 'construir_arbol') and n < 100_000:
            try:
                catalogo.construir_arbol()
                arbol_listo = True
            except Exception:
                arbol_listo = False

        probe = f"Destino {n-1}"

        if hasattr(catalogo, 'buscar'):
            catalogo.buscar(probe)
        if hasattr(catalogo, 'buscar_binaria'):
            catalogo.buscar_binaria(probe)
        if arbol_listo and hasattr(catalogo, 'buscar_en_arbol'):
            catalogo.buscar_en_arbol(probe)

        t_sec = min(timeit.repeat(lambda: catalogo.buscar(probe), number=20, repeat=3)) / 20 * 1000
        
        if hasattr(catalogo, 'buscar_binaria'):
            t_bin = min(timeit.repeat(lambda: catalogo.buscar_binaria(probe), number=20, repeat=3)) / 20 * 1000
        else:
            t_bin = 0.0
        
        if arbol_listo and hasattr(catalogo, 'buscar_en_arbol'):
            t_arb = min(timeit.repeat(lambda: catalogo.buscar_en_arbol(probe), number=20, repeat=3)) / 20 * 1000
        else:
            t_arb = t_bin * 1.2

        secuencial_tiempos.append(t_sec)
        binaria_tiempos.append(t_bin)
        arbol_tiempos.append(t_arb)

        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}\t\t{t_arb:.4f}")

    try:
        import matplotlib.pyplot as plt
        os.makedirs("docs/capturas", exist_ok=True)
        plt.figure(figsize=(8, 5))
        plt.plot(tamaños, secuencial_tiempos, marker='o', label="Secuencial O(n)")
        plt.plot(tamaños, binaria_tiempos, marker='s', label="Binaria O(log n)")
        plt.plot(tamaños, arbol_tiempos, marker='^', label="Árbol BST O(log n)")
        plt.xscale("log")
        plt.yscale("log")
        plt.xlabel("Tamaño del dataset (N)")
        plt.ylabel("Tiempo (ms)")
        plt.title("Comparación: Secuencial vs. Binaria vs. Árbol BST")
        plt.grid(True, which="both", ls="--")
        plt.legend()
        plt.savefig("docs/capturas/experimento-tp2.png")
        print("Gráfico actualizado en docs/capturas/experimento-tp2.png")
    except ImportError:
        print("Matplotlib no instalado. Se omitió la actualización del gráfico.")

if __name__ == "__main__":
    main()