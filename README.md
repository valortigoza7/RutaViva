# RutaViva ✈️

Sistema de recomendación de destinos de viaje — TP Integrador de Estructuras de Datos.

## Estado actual: TP1 — Objetos y clases

En esta etapa el sistema:

- Define la clase de dominio `Destino` con atributos encapsulados (privados) y accesos mediante propiedades.
- Carga los datos desde `datos/destinos.json`.
- Expone tres operaciones sobre el catálogo: **Buscar**, **Listar** y **Filtrar** (por categoría).
- Cuenta con una interfaz de terminal funcional.

Las demás opciones del menú (Top 10, relacionados, conexiones, caminos, recomendaciones)
se van a implementar en etapas posteriores del TP, a medida que se incorporen
árbol binario/AVL, heap, grafo, BFS/DFS y caminos mínimos.

Pruebas automatizadas

Se implementaron pruebas automatizadas para verificar el funcionamiento del catálogo.

Resultado de la ejecución:

.....
----------------------------------------------------------------------
Ran 5 tests in 0.015s

OK

Las pruebas verifican:

- Búsqueda de un destino por nombre.
- Búsqueda sin distinguir mayúsculas y minúsculas.
- Búsqueda de un destino inexistente.
- Listado de destinos.
- Filtrado de destinos por categoría.

Todas las pruebas finalizaron correctamente, sin errores ni fallos.

## Cómo ejecutar

Requiere Python 3.10+ (no usa dependencias externas).

```bash
python3 main.py
```

## Estructura del proyecto