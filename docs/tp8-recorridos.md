TP8 — Recorridos de grafos: BFS y DFS

1. Introducción

En RutaViva se implementaron dos algoritmos de recorrido de grafos: BFS (búsqueda en anchura) y DFS (búsqueda en profundidad).

Ambos algoritmos permiten recorrer los destinos turísticos relacionados dentro del grafo del sistema. Sin embargo, utilizan estrategias diferentes y resuelven necesidades distintas.

El grafo es no dirigido y utiliza listas de adyacencia. Cada vértice representa un destino turístico y dos destinos se conectan cuando comparten la misma región o categoría.

2. BFS — Búsqueda en anchura

BFS (Breadth-First Search) recorre el grafo por niveles. Primero visita los vecinos directos del destino inicial y después continúa con los destinos que se encuentran a mayor distancia en cantidad de aristas.

Funcionamiento

- Comienza desde un destino elegido por el usuario.
- Utiliza una cola FIFO (primero en entrar, primero en salir).
- Visita primero los destinos conectados directamente.
- Continúa con los siguientes niveles de conexiones.
- Utiliza un conjunto de visitados para evitar recorrer un destino más de una vez.

En RutaViva se utiliza "deque" para implementar la cola y "popleft()" para retirar eficientemente el primer elemento.

Caso de uso en RutaViva

La opción 8 del menú, «Recomendaciones», utiliza BFS para mostrar destinos relacionados con el elegido.

Por ejemplo, si el usuario selecciona Bariloche, el sistema muestra primero los destinos conectados directamente y después los que se encuentran a dos o más conexiones.

La función responsable de esta consulta es:

"recomendaciones_por_cercania_bfs()"

Se encuentra en "servicios/consultas_grafo.py".

El destino inicial no se incluye en la lista de recomendaciones.

3. DFS — Búsqueda en profundidad

DFS (Depth-First Search) recorre el grafo profundizando por un camino todo lo posible antes de retroceder y continuar con otros vecinos.

Funcionamiento

- Comienza desde un destino elegido por el usuario.
- Utiliza una pila (LIFO: último en entrar, primero en salir).
- Avanza hacia destinos relacionados que todavía no fueron visitados.
- Cuando no encuentra más destinos para continuar, retrocede y explora otras conexiones.
- Utiliza un conjunto de visitados para evitar repetir destinos.

Caso de uso en RutaViva

La opción 9 del menú, «Explorar destinos en profundidad (DFS)», permite al usuario explorar la red de destinos relacionados desde un punto de partida.

Por ejemplo, al seleccionar Bariloche, el sistema recorre los destinos alcanzables siguiendo las conexiones del grafo y muestra el orden de visita.

La función responsable de esta consulta es:

"itinerario_encadenado_dfs()"

Se encuentra en "servicios/consultas_grafo.py".

DFS permite explorar la red, pero no ordena los destinos por rating, distancia geográfica ni tiempo de viaje.

4. Comparación entre BFS y DFS

Característica| BFS| DFS
Estrategia| Recorre por niveles| Profundiza por caminos
Estructura auxiliar| Cola| Pila
Orden de exploración| Primero los más cercanos en aristas| Primero un camino en profundidad
Uso en RutaViva| Recomendaciones por cercanía| Exploración de conexiones
Complejidad temporal| O(V + E)| O(V + E)

Ambos algoritmos recorren los vértices alcanzables desde el destino inicial y evitan visitar repetidamente los mismos vértices.

5. Análisis de complejidad

Para analizar los algoritmos se utilizan las siguientes variables:

- V: cantidad de vértices del grafo (destinos turísticos).
- E: cantidad de aristas del grafo (conexiones entre destinos).

Complejidad temporal

Tanto BFS como DFS tienen una complejidad temporal de:

O(V + E)

Esto se debe a que cada vértice se visita como máximo una vez y las conexiones se examinan durante el recorrido.

En BFS, el uso de "deque" permite retirar elementos del comienzo de la cola sin desplazar los restantes.

Complejidad espacial

Ambos algoritmos requieren espacio adicional O(V) en el peor caso.

Esto se debe a que pueden almacenar hasta V vértices en las estructuras auxiliares y en el conjunto de visitados.

- BFS utiliza una cola y un conjunto de visitados.
- DFS utiliza una pila y un conjunto de visitados.

6. Justificación de los algoritmos

Se implementaron ambos recorridos porque permiten resolver consultas diferentes dentro de RutaViva.

BFS resulta adecuado para las recomendaciones porque permite priorizar los destinos que se encuentran a menor cantidad de conexiones del destino seleccionado.

DFS resulta adecuado para explorar la red porque permite recorrer los destinos alcanzables profundizando por las conexiones antes de retroceder.

Es importante aclarar que la cercanía calculada por BFS corresponde a la cantidad de aristas del grafo. No representa kilómetros, duración del viaje ni distancia geográfica.

Tampoco se trata de un sistema de caminos mínimos ponderados: esa funcionalidad permanece fuera del alcance de estos recorridos.

7. Integración en el menú

Los algoritmos están conectados a la interfaz de terminal de RutaViva:

Opción| Funcionalidad| Algoritmo
8| Recomendaciones| BFS
9| Explorar destinos en profundidad| DFS

De esta manera, ambos recorridos pueden utilizarse directamente desde el programa.

8. Conclusión

La implementación de BFS y DFS amplía las funcionalidades del grafo de RutaViva.

BFS permite generar recomendaciones ordenadas según la cantidad de conexiones desde el destino inicial, mientras que DFS permite explorar en profundidad la red de destinos relacionados.

Ambos algoritmos tienen una complejidad temporal O(V + E) y utilizan estructuras auxiliares diferentes para controlar el recorrido.

Con estas implementaciones, RutaViva cumple con los recorridos solicitados en el TP8 y permite utilizarlos desde su interfaz de terminal.