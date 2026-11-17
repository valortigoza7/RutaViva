# Documento de Requerimientos — RutaViva

## 1. Descripción General
**RutaViva** es una aplicación de consola desarrollada en Python para la gestión, consulta y recomendación de destinos turísticos. El sistema permite administrar un catálogo de destinos (con nombre, región, categoría y calificación) y aplicar distintas estructuras de datos (tablas hash, algoritmos de ordenamiento, pilas, colas, árboles y grafos) para resolver búsquedas, historiales de navegación y rutas de recomendación.

---

## 2. Requerimientos Funcionales (RF)

* **RF01 — Carga de catálogo desde archivo:** El sistema debe cargar automáticamente los destinos turísticos desde un archivo estructurado en formato JSON (`datos/destinos.json`) al iniciar la aplicación.
* **RF02 — Búsqueda de destinos por nombre:** El sistema debe permitir buscar un destino específico por su nombre sin distinguir entre mayúsculas, minúsculas o espacios adicionales.
* **RF03 — Filtrado por atributos:** El sistema debe permitir listar y filtrar destinos según su región geográfica o categoría temática.
* **RF04 — Ranking de destinos mejor calificados:** El sistema debe mostrar el listado de destinos ordenados de mayor a menor según su calificación (*rating*), incluyendo el Top N de los mejores puntuados.
* **RF05 — Gestión de historial de navegación (Pila):** El sistema debe registrar los destinos consultados recientemente por el usuario y permitir volver al último destino visitado siguiendo un esquema LIFO.
* **RF06 — Gestión de itinerario pendiente (Cola):** El sistema debe permitir al usuario agregar destinos a una lista de pendientes por visitar y procesarlos en orden de llegada (FIFO).
* **RF07 — Modelado de afinidad mediante grafo:** El sistema debe construir un grafo no dirigido donde cada vértice representa un destino y cada arista conecta destinos que comparten región geográfica o categoría temática.
* **RF08 — Consultas estructurales sobre la red de destinos:** El sistema debe permitir consultar los vecinos directos de un destino (ordenados por rating), el grado de conexión, los destinos más conectados, los vecinos en común entre dos lugares y los destinos aislados.
* **RF09 — Recomendaciones progresivas por cercanía (BFS):** Dado un destino de origen, el sistema debe sugerir destinos relacionados utilizando búsqueda en anchura (BFS), priorizando primero las conexiones directas (primer nivel) y luego las indirectas (segundo nivel en adelante).
* **RF10 — Generación de itinerario encadenado en profundidad (DFS):** Dado un destino de origen, el sistema debe generar una ruta continua de exploración utilizando búsqueda en profundidad (DFS), avanzando por destinos afines conectados antes de retroceder.

---

## 3. Requerimientos No Funcionales (RNF)

* **RNF01 — Eficiencia en búsquedas por clave:** La búsqueda exacta de un destino por nombre normalizado debe resolverse en tiempo promedio constante $O(1)$ mediante indexación por diccionario/tabla hash.
* **RNF02 — Eficiencia en ordenamiento:** El ordenamiento de destinos por calificación o nombre debe ejecutarse en tiempo $O(n \log n)$, evitando algoritmos cuadráticos sobre el catálogo completo.
* **RNF03 — Representación eficiente en memoria del grafo:** La red de destinos debe representarse mediante lista de adyacencia para garantizar un consumo de memoria $O(V + E)$, adecuado para grafos dispersos, y acceso directo a los vecinos de un vértice en $O(1)$.
* **RNF04 — Complejidad de recorridos:** Los recorridos BFS y DFS sobre el grafo deben visitar cada vértice y arista de la componente conexa a lo sumo una vez, manteniendo una complejidad temporal de $O(V + E)$ y evitando ciclos infinitos mediante un conjunto de visitados.
* **RNF05 — Escalabilidad:** El sistema debe soportar al menos 1.000 destinos cargados en el catálogo sin degradar perceptiblemente el tiempo de respuesta en consola.
* **RNF06 — Modularidad y arquitectura por capas:** El código fuente debe mantenerse desacoplado en módulos independientes (`modelos`, `servicios`, `algoritmos`, `ui` y `tests`) para facilitar el mantenimiento y la extensibilidad.
* **RNF07 — Confiabilidad y cobertura de pruebas:** Todas las estructuras de datos, consultas y casos borde (catálogo vacío, destinos inexistentes, nodos aislados) deben estar respaldados por pruebas unitarias automatizadas con `unittest`.

---

## 4. Alcance y Fuera de Alcance

### Dentro del alcance
* Interfaz de usuario interactiva por línea de comandos (CLI / consola).
* Persistencia inicial mediante lectura de archivos JSON locales.
* Implementación y análisis experimental de estructuras de datos lineales, jerárquicas y de grafos aplicadas al dominio turístico.

### Fuera de alcance
* **Autenticación y gestión de usuarios:** No se implementan cuentas personales, inicio de sesión, contraseñas ni perfiles multiusuario.
* **Interfaz gráfica web o móvil:** No se desarrolla frontend web, aplicación móvil ni consumo de mapas interactivos externos.
* **Conexión a APIs externas en tiempo real:** No se consultan precios de vuelos, disponibilidad hotelera, clima ni distancias geográficas por GPS.
* **Base de datos relacional:** No se utiliza motor SQL (PostgreSQL, MySQL, SQLite); los datos residen en archivos JSON locales.
* **Cálculo de caminos mínimos ponderados por kilómetros:** Las aristas representan afinidad temática o regional sin pesos numéricos de distancia física ni tarifas.