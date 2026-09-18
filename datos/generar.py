import json
import random
from pathlib import Path

CATEGORIAS = ["playa", "montaña", "ciudad", "naturaleza"]
REGIONES = ["Buenos Aires", "Córdoba", "Uruguay", "Patagonia", "Cuyo", "NOA", "Litoral"]

def generar(n: int) -> None:
    destinos = [
        {
            "nombre": f"Destino {i}",
            "categoria": random.choice(CATEGORIAS),
            "region": random.choice(REGIONES),
            "rating": round(random.uniform(1.0, 10.0), 1),
            "descripcion": f"Destino generado automáticamente {i}" # <- faltaba
        }
        for i in range(n)
    ]
    ruta = Path(f"datos/destinos_{n}.json")
    ruta.parent.mkdir(exist_ok=True) # <- crea carpeta si no existe
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(destinos, archivo, ensure_ascii=False, indent=2)
    print(f"✅ Generado {ruta} con {n} destinos")

if __name__ == "__main__": # <- FIX: solo genera si lo ejecutás
    for n in (100, 1_000, 10_000, 100_000):
        generar(n)