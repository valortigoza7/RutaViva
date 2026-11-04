# TP7 — Grafos y Modelado de Relaciones en RutaViva

## 1. Decisiones de Diseño y Modelado Teórico

Para modelar la red de conexiones y recomendaciones de destinos turísticos en **RutaViva**, se implementó una estructura de **Grafo No Dirigido y No Pesado**:

* **Vértices (Nodos):** Cada objeto `Destino` dentro del catálogo (por ejemplo, *Bariloche*, *Iguazú*, *Mendoza*) representa un vértice en el grafo.
* **Aristas (Conexiones):** Existe una relación bidireccional entre dos destinos si comparten **región** (ej. Patagonia, Litoral) o **categoría** (ej. Montaña, Naturaleza).
* **Tipo de Grafo (No Dirigido):** La relación es simétrica. Si *Bariloche* está relacionado con *Villa La Angostura*, la conexión aplica en ambas direcciones.
* **Sin Pesos (No Pesado):** El objetivo principal en esta etapa es determinar la existencia del vínculo conceptual y la cercanía temática, sin asignar aún un costo, tiempo o distancia física.
* **Representación en Memoria (Lista de Adyacencia):** Se optó por una representación mediante **lista de adyacencia** (usando diccionarios de conjuntos en Python). Esto resulta altamente eficiente, ya que la matriz de adyacencia reservaría un espacio de memoria $O(V^2)$ con muchas entradas vacías (grafo disperso), mientras que la lista consume $O(V + E)$ facilitando el recorrido rápido de los vecinos directos de cada destino.

---

## 2. Estructura e Integración de Clases

* **`servicios/grafo.py`:** Implementa la estructura genérica del grafo con métodos para agregar vértices, aristas y obtener adyacentes.
* **`servicios/consultas_grafo.py`:** Define consultas avanzadas sobre la red:
  - Destinos más conectados (grados de entrada/salida).
  - Verificación y motivos de conexión entre dos destinos específicos.
  - Vecinos en común y detección de destinos aislados.
* **`servicios/catalogo.py`:** Encargado de instanciar y poblar el grafo automáticamente durante la carga del catálogo, ofreciendo el método `relacionados(nombre)`.
* **`ui/terminal.py`:** Expone la funcionalidad en la **Opción 5 ("Ver relacionados")**, desplegando los destinos conectados y el motivo específico del vínculo (misma región y/o categoría) con pausas de pantalla integradas para una lectura cómoda.

---

## 3. Experimentos y Verificación

Se agregaron los scripts de prueba e integración en `algoritmos/experimentos/consultas_grafo.py` y una suite completa de **14 tests unitarios** en `tests/test_grafo_consultas.py` validando la integridad de las relaciones, simetría del grafo y consistencia en los resultados de búsqueda.