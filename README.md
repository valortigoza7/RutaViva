# RutaViva ✈️

Sistema de recomendación de destinos de viaje — TP Integrador de Estructuras de Datos.

**Estado actual:** TP8 — Recorridos BFS y DFS (Finalizado para entrega y defensa oral)  
**Versión:** 6

RutaViva es una aplicación de terminal desarrollada en Python que permite consultar destinos turísticos, explorar categorías, obtener los destinos mejor valorados y descubrir relaciones entre destinos mediante un grafo.

## Integrantes del Equipo

- **Melina Raso**
- **Ignacio Candido**
- **Valentina Ortigoza**

## Funcionalidades

La aplicación ofrece las siguientes opciones desde el menú de terminal:

1. **Buscar destino:** busca un destino por nombre mediante un árbol binario de búsqueda (BST).
2. **Explorar categorías:** permite recorrer la jerarquía de categorías mediante un árbol general.
3. **Listar todos los destinos:** muestra los destinos cargados en el catálogo.
4. **Ver Top 10:** obtiene los destinos mejor puntuados utilizando una heap binaria máxima.
5. **Ver relacionados:** muestra destinos conectados y los motivos de su relación.
6. **Explorar conexiones:** permite consultar los vecinos de un destino en el grafo.
7. **Encontrar camino:** funcionalidad pendiente de implementación.
8. **Recomendaciones (BFS):** recorre el grafo por niveles y presenta primero los destinos alcanzables con menor cantidad de conexiones.
9. **Explorar destinos en profundidad (DFS):** recorre en profundidad la red de destinos relacionados desde un destino inicial.

## Estructuras de datos y algoritmos

- **Lista de objetos `Destino`:** almacena los destinos cargados desde `datos/destinos.json`.
- **Árbol binario de búsqueda (BST):** organiza los destinos por nombre y permite realizar búsquedas.
- **Árbol AVL:** implementación de un árbol binario de búsqueda balanceado. En la versión actual está implementado de manera independiente y no está integrado al menú principal.
- **Árbol general:** representa la jerarquía de categorías y subcategorías.
- **Heap binaria máxima:** permite obtener los destinos con mayor rating.
- **Grafo no dirigido con listas de adyacencia:** cada vértice representa un destino y las aristas representan relaciones entre destinos que comparten región o categoría.
- **BFS (búsqueda en anchura):** se utiliza para recomendar destinos por cercanía en cantidad de aristas. La implementación utiliza una cola `deque`.
- **DFS (búsqueda en profundidad):** se utiliza para explorar los destinos alcanzables siguiendo las conexiones del grafo.

En el grafo actual, las conexiones no tienen pesos: no representan kilómetros, duración ni costo económico del viaje.

## Estructura del Repositorio

```text
RutaViva/
├── datos/               # Datos de los destinos en formato JSON (destinos.json)
├── modelos/             # Clases que representan los objetos del dominio (Destino)
├── servicios/           # Catálogo, estructuras de datos (BST, AVL, Árbol General, Heap, Grafo) y consultas
├── ui/                  # Interfaz interactiva de terminal
├── tests/               # Pruebas unitarias automatizadas (45 tests)
├── docs/                # Documentación del proyecto, diagramas y entregas
├── main.py              # Punto de entrada principal de la aplicación
└── README.md            # Documentación general del repositorio