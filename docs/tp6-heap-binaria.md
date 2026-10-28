# TP6 — Heap Binaria y Top 10 (Cola de Prioridad)

## Punto 5: Justificación teórica sobre el uso de Max-Heap vs. Ordenamiento Completo

En el desarrollo de **RutaViva**, la funcionalidad **Top-N** tiene como objetivo obtener únicamente los $N$ destinos con mejor calificación (*rating*) dentro de un catálogo que contiene $m$ destinos.

### Comparativa de Algoritmos y Complejidad Temporal

1. **Estrategia A: Ordenamiento Completo (Sort)**
   - **Enfoque:** Ordenar todo el catálogo de destinos con un algoritmo de ordenamiento rápido como Timsort o Mergesort, y luego tomar los primeros $N$ elementos.
   - **Complejidad:** $O(m \log m)$
   - **Desventaja:** Procesa y ordena el $100\%$ de los elementos del catálogo, realizando trabajo innecesario sobre destinos de menor calificación que no formarán parte del ranking final.

2. **Estrategia B: Max-Heap (Cola de Prioridad) — *Implementada***
   - **Enfoque:**
     1. Construir un Max-Heap a partir de los $m$ elementos del catálogo utilizando el algoritmo de Floyd (`heapify`).
     2. Extraer sucesivamente el elemento de mayor prioridad (máximo *rating*) $N$ veces.
   - **Complejidad:**
     - Construcción del Heap (`heapify`): $O(m)$
     - Extracción de $N$ máximos: $N \times O(\log m) = O(N \log m)$
     - **Complejidad Total:** $O(m + N \log m)$

### Conclusión

Dado que en un sistema real el tamaño del catálogo ($m$) es significativamente mayor que la cantidad de recomendaciones solicitadas ($N \ll m$), el enfoque con **Max-Heap** optimiza notablemente el rendimiento del sistema:

$$\text{Si } N \ll m \implies O(m + N \log m) < O(m \log m)$$

Además, esta estructura garantiza **estabilidad en empates de rating** (salen primero los elementos cargados anteriormente) y **no altera el catálogo original**, preservando la integridad de los datos.