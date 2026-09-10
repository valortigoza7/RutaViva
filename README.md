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

## Cómo ejecutar

Requiere Python 3.10+ (no usa dependencias externas).

```bash
python3 main.py
```

## Estructura del proyecto
