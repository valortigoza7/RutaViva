# TP5 — Árbol general: jerarquía de categorías

## 1. Jerarquía del dominio

RutaViva organiza los destinos en categorías y subcategorías. Un destino pertenece a
una subcategoría (por ejemplo, las Cataratas del Iguazú a "Cataratas y ríos"), y cada
subcategoría cuelga de una categoría principal.

```
RutaViva
├── Naturaleza
│   ├── Bosques y selvas
│   ├── Cataratas y ríos
│   └── Parques naturales
├── Montaña
│   ├── Cordillera
│   └── Sierras
├── Playa
│   ├── Costa atlántica
│   └── Playas de río
└── Ciudad
    ├── Ciudades históricas
    └── Grandes ciudades
```

**Por qué un árbol general y no un BST:** una categoría tiene una cantidad variable de
hijos (Naturaleza tiene 3, Montaña 2), y entre hermanos no hay un orden "menor / mayor".
El BST (máximo 2 hijos, ordenado por clave) sirve para buscar un destino por nombre
(TP3 y TP4); el árbol general sirve para representar la **jerarquía** y navegarla.

## 2. Estructura

- Cada nodo guarda una etiqueta (nombre de la categoría) y una lista de hijos.
- La raíz es "RutaViva"; las hojas son las subcategorías.
- Implementación: `servicios/arbol_general.py`.
- Altura del árbol: 2 (raíz → categoría → subcategoría). Total: 1 + 4 + 9 = 14 nodos.

## 3. Operaciones y complejidad

n = cantidad de nodos del árbol.

| Operación | Descripción | Complejidad |
|---|---|---|
| Recorrido preorden | Visita el nodo y luego sus hijos | O(n) |
| Recorrido postorden | Visita los hijos y luego el nodo | O(n) |
| Recorrido por niveles (BFS) | Visita nivel por nivel con una cola | O(n) |
| Búsqueda jerárquica | Encuentra una categoría por nombre | O(n) en el peor caso |

Todos los recorridos visitan cada nodo una sola vez, por eso son O(n). La búsqueda no
puede ser mejor que O(n) en el peor caso porque el árbol no está ordenado: hay que
mirar nodo por nodo hasta encontrar la etiqueta. Con 14 nodos es instantáneo, y como
la jerarquía de categorías es chica y casi no cambia, no se justifica una estructura
más compleja.

## 4. Integración en la terminal

En el menú, la opción 2 ("Explorar categorías") ahora muestra la jerarquía: el usuario
elige una categoría (Naturaleza, Montaña, Playa, Ciudad) y después una subcategoría
para navegar hacia abajo en el árbol.

## 5. Verificación

Se escribió `tests/test_arbol_general.py` (12 tests con `unittest`) y se corrieron
contra `servicios/arbol_general.py`: **12 de 12 pasan**. Para correrlos:

```
python -m unittest discover -s tests -t . -v
```

| Qué se verifica | Resultado |
|---|---|
| Estructura: raíz "RutaViva", 4 categorías, 14 nodos en total | OK |
| `agregar_hijo` devuelve el nodo nuevo y lo deja colgado del padre | OK |
| `agregar_hijo` con un padre que no es nodo lanza `TypeError` | OK |
| Preorden: cada categoría aparece seguida de sus subcategorías | OK |
| Postorden: cada subcategoría va antes que su categoría; la raíz al final | OK |
| Por niveles: raíz, las 4 categorías y después las subcategorías | OK |
| Los tres recorridos visitan exactamente los mismos 14 nodos | OK |
| Buscar "Playa" encuentra el nodo con sus 2 hijos | OK |
| Buscar "Cordillera" (hoja) lo encuentra, sin hijos | OK |
| La búsqueda ignora mayúsculas ("montaña", "CIUDADES HISTÓRICAS") | OK |
| Buscar una categoría inexistente devuelve `None` | OK |
| Buscar la raíz devuelve la raíz | OK |

> Nota: al armar el primer test se contaron mal los nodos (13 en lugar de 14: son
> 9 subcategorías, no 8). El test lo detectó y se corrigió el conteo en este documento.

## 6. Conclusión

El árbol general modela algo que el BST no puede: una jerarquía de categorías con
cantidad variable de hijos. Los recorridos son O(n) y la búsqueda, al no haber orden
entre hermanos, también. Cada estructura del proyecto responde a un problema distinto:
la lista (TP1–TP2) y el BST/AVL (TP3–TP4) buscan destinos por nombre; el árbol general
(TP5) organiza y navega las categorías.
