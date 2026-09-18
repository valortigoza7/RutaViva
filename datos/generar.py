import json 
import random 

CATEGORIAS = ["playa", "montaña", "ciudad", "naturaleza"] 
REGIONES = ["Buenos Aires", "Córdoba", "Uruguay", "Patagonia", "Cuyo", "NOA", "Litoral"]

def generar(n: int) -> None: 
    destinos = [ 
        { 
            "nombre": f"Destino {i}", 
            "categoria": random.choice(CATEGORIAS), 
            "region": random.choice(REGIONES),
            "rating": round(random.uniform(1.0, 10.0), 1), 
        } 
        for i in range(n) 
    ] 
    ruta = f"datos/destinos_{n}.json" 
    with open(ruta, "w", encoding="utf-8") as archivo: 
        json.dump(destinos, archivo, ensure_ascii=False, indent=2) 
    print(ruta) 
for n in (100, 1_000, 10_000, 100_000): 
    generar(n)