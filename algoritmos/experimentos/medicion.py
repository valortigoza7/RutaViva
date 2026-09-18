import timeit
from servicios.catalogo import Catalogo

def medir(func, number=20, repeat=5) -> float:
    """Devuelve el MEJOR tiempo por llamada en milisegundos (ms)."""
    tiempos = timeit.repeat(func, number=number, repeat=repeat)
    mejor = min(tiempos) / number
    return mejor * 1000  # Convertir a milisegundos

def main() -> None:
    # 1. Definir los tamaños de prueba
    tamaños = (100, 1_000, 10_000, 100_000)
    
    # 2. Imprimir cabecera de la tabla
    print("tamaño\tsecuencial_ms\tbinaria_ms")
    
    for n in tamaños:
        # 3. Preparar el entorno de datos para este tamaño
        catalogo = Catalogo()
        catalogo.cargar_desde_json(f"datos/destinos_{n}.json")
        catalogo.ordenar_por_nombre()  # Requisito indispensable para búsqueda binaria
        
        # 4. Definir el elemento a buscar (Peor caso: el último o casi el último)
        nombre_probe = f"Destino {n - 1}"
        
        # 5. Medir de forma limpia usando lambdas para no ejecutar la función antes de tiempo
        t_sec = medir(lambda: catalogo.buscar(nombre_probe))
        t_bin = medir(lambda: catalogo.buscar_binaria(nombre_probe))
        
        # 6. Mostrar resultados tabulados
        print(f"{n}\t{t_sec:.4f}\t\t{t_bin:.4f}")

if __name__ == "__main__":
    main()