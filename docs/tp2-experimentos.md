# TP2 — Análisis de Complejidad y Experimentos

## 1. Operación Crítica Elegida
Se seleccionó la **búsqueda por nombre (título) en el catálogo de destinos**. Esta operación es la más crítica del sistema dado que es la funcionalidad de mayor frecuencia de uso por parte de los usuarios en `RutaViva`. Además, sirve como punto de partida y justificación asintótica para la futura incorporación de estructuras jerárquicas (BST en TP3 y AVL en TP4).

## 2. Estrategias Comparadas

| ID | Estrategia | Implementación / Método | Dónde vive |
|---|---|---|---|
| **A** | **Secuencial** | Recorrido lineal de la lista no ordenada | `Catalogo.buscar` (TP1) |
| **B** | **Binaria** | Búsqueda binaria mediante `bisect` sobre lista ordenada por nombre | `Catalogo.buscar_binaria` (TP2) |

> **Nota:** Para la estrategia B, la lista se ordena una única vez (`ordenar_por_nombre`) al cargar los datos para no distorsionar el tiempo propio de la búsqueda.

## 3. Método de Medición

Se usó `timeit`, con 50 ejecuciones por medición y 5 repeticiones, quedándonos con el **mínimo** por llamada (el promedio se contamina con picos del sistema operativo; el mínimo es el mejor esfuerzo reproducible de la máquina).

En ambos casos se buscó el **mismo nombre**: `Destino {n-1}` (el último elemento generado por `datos/generar.py`), para que la comparación sea justa (misma consulta, mismo dataset, mismas condiciones). El ordenamiento se ejecuta **una sola vez, antes de cronometrar**.

Script de medición: `algoritmos/experimentos/medicion.py`.

## 4. Tabla de Resultados

| N elementos | Secuencial | Binaria | Mejora |
|---|---:|---:|---:|
| **100** | 0.0053 ms | 0.0002 ms | 24.3x |
| **1.000** | 0.0521 ms | 0.0005 ms | 115.3x |
| **10.000** | 0.5648 ms | 0.0003 ms | 1.909,9x |
| **100.000** | 5.7567 ms | 0.0003 ms | 16.724,8x |

![Resultados TP2](capturas/experimento-tp2.png)

La búsqueda secuencial multiplica su tiempo por ~10 cada vez que el dataset crece 10 veces (comportamiento lineal). La binaria se mantiene prácticamente constante en todo el rango medido — la diferencia es tan chica (microsegundos) que queda dentro del ruido de medición, algo coherente con una complejidad logarítmica.

## 5. Expresar la Complejidad

| Estrategia | Peor caso $O()$ | Mejor caso $\Omega()$ | Caso típico $\Theta()$ |
|---|:---:|:---:|:---:|
| **Secuencial (`buscar`)** | $O(n)$ | $\Omega(1)$ *(está primero)* | Proporcional a $n/2$ en promedio |
| **Binaria (`buscar_binaria`)** | $O(\log n)$ | $\Omega(1)$ | $\Theta(\log n)$ |
| **Ordenar antes de la binaria (una vez)** | $O(n \log n)$ | $\Omega(n \log n)$ | Pagado una sola vez, amortizado |

La búsqueda secuencial recorre la lista de destinos hasta encontrar el nombre buscado: en el peor caso recorre los $n$ elementos ($O(n)$). La búsqueda binaria descarta la mitad del espacio de búsqueda en cada comparación ($O(\log n)$). A cambio, requiere que la lista esté ordenada por nombre ($O(n \log n)$) — costo que se paga **una sola vez** al cargar el catálogo.

## 6. Interpretar y Concluir

Se comparó la misma operación sobre los mismos datasets, buscando siempre el mismo elemento para atribuir la diferencia exclusivamente a la estrategia de búsqueda.

Los resultados muestran que a $N = 100.000$, la búsqueda binaria es más de 16.000 veces más rápida. Para un catálogo de viajes como `RutaViva`, que se consulta constantemente por nombre y no cambia en cada consulta, mantener la lista ordenada y usar búsqueda binaria es la estrategia más conveniente: el costo de ordenar se amortiza en todas las búsquedas posteriores. En TP3 se sumará el árbol binario de búsqueda (BST) como tercera estrategia para evitar reordenar la lista ante nuevos ingresos.

---

## 7. Trampas Típicas de Medición Evitadas

Durante el diseño y ejecución de los experimentos, se contemplaron y mitigaron las siguientes trampas comunes de medición:

| Trampa Común | Por qué altera los resultados | Solución aplicada en nuestro experimento |
|---|---|---|
| **Medir junto con la carga del JSON** | El tiempo de lectura de disco e intérprete JSON es gigantesco comparado con la búsqueda, tapando la diferencia real entre algoritmos. | Se cargaron y ordenaron los datos en memoria **antes** de iniciar el cronómetro. |
| **Incluir la primera llamada (*warm-up*)** | Las importaciones y la asignación inicial de memoria hacen que la primera ejecución sea más lenta de lo normal. | Se realizó una ejecución de prueba (*warm-up*) previa a la toma de tiempos. |
| **Usar un solo `time.time()`** | Una sola medición se ve alterada por procesos del sistema operativo en segundo plano (antivirus, navegador, etc.). | Se utilizó `timeit` con 50 ejecuciones y 5 repeticiones, seleccionando únicamente el tiempo **mínimo**. |
| **Buscar elementos inexistentes** | Si no se aclara, en el peor caso la búsqueda puede comportarse de manera atípica o confundir los resultados. | Se buscó explícitamente el último elemento existente (`Destino {n-1}`) para evaluar el peor caso controlado de la búsqueda secuencial. |
| **Ordenar dentro de la medición** | Incluye el costo $O(n \log n)$ del ordenamiento dentro del tiempo propio de la búsqueda binaria. | Se ordenó la lista una sola vez tras la carga inicial. |

---

## 8. Plantilla y Estructura del Informe Final

El informe final consolidado queda estructurado bajo el siguiente índice estandarizado para la defensa del TP2:

1. **Operación Crítica Elegida:** Justificación del uso de la búsqueda por nombre en `RutaViva`.
2. **Estrategias Comparadas:** Secuencial (`Catalogo.buscar`) vs. Binaria (`Catalogo.buscar_binaria`).
3. **Datos de Prueba:** Datasets sintéticos generados en `datos/generar.py` (100, 1.000, 10.000, 100.000).
4. **Método de Medición:** Script `algoritmos/experimentos/medicion.py` utilizando `timeit` con 50 ejecuciones x 5 repeticiones (tomando el mínimo).
5. **Resultados Obtenidos:** Tabla comparativa y gráfico en `docs/capturas/experimento-tp2.png`.
6. **Análisis de Complejidad:** Cuadro comparativo $O()$, $\Omega()$ y $\Theta()$.
7. **Interpretación y Conclusión:** Justificación de la amortización del costo de ordenamiento y preparación para el BST del TP3.

---

## 9. Checklist del TP2

Verificación final de los requerimientos antes de la entrega:

- [x] **Operación crítica definida y justificada** (Búsqueda por nombre/título).
- [x] **Dos estrategias implementadas** (Secuencial y Binaria con `bisect`).
- [x] **Script de generación de datos commiteado** (`datos/generar.py`).
- [x] **Script de medición reproducible commiteado** (`algoritmos/experimentos/medicion.py`).
- [x] **Mediciones confiables** (Mapeo con `timeit`, toma de tiempos mínimos, warm-up ejecutado).
- [x] **Condiciones de prueba idénticas** (Mismo dataset y mismo elemento de prueba en ambas estrategias).
- [x] **Tabla de resultados formateada en Markdown** para los 4 tamaños de dataset.
- [x] **Análisis explícito de complejidad** ($O$, $\Omega$ y $\Theta$).
- [x] **Conclusión justificada** con explicación de costo/beneficio y amortización.
- [x] **Gráfico visual de rendimiento** embebido (`docs/capturas/experimento-tp2.png`).