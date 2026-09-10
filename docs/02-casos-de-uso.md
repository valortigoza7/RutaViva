# Casos de uso — RutaViva

## Caso de uso: Buscar destino

- Actor: Usuario
- Precondición: el catálogo está cargado.
- Flujo principal:
  1. El usuario selecciona "Buscar destino".
  2. El sistema pide el nombre del destino.
  3. El usuario ingresa el nombre.
  4. El sistema lo busca sin distinguir mayúsculas y minúsculas y muestra el resultado.
- Flujo alternativo: si no se encuentra el destino, el sistema informa que no existe.

## Caso de uso: Listar todos los destinos

- Actor: Usuario
- Precondición: el catálogo está cargado.
- Flujo principal:
  1. El usuario selecciona "Listar destinos".
  2. El sistema obtiene los destinos del catálogo.
  3. El sistema muestra todos los destinos disponibles.
- Flujo alternativo: si no hay destinos cargados, el sistema informa que no hay destinos disponibles.

## Caso de uso: Filtrar por categoría

- Actor: Usuario
- Precondición: el catálogo está cargado.
- Flujo principal:
  1. El usuario selecciona "Filtrar por categoría".
  2. El sistema pide la categoría.
  3. El usuario ingresa una categoría.
  4. El sistema busca los destinos que pertenecen a esa categoría.
  5. El sistema muestra los destinos encontrados.
- Flujo alternativo: si no existen destinos para la categoría indicada, el sistema informa que no se encontraron destinos.