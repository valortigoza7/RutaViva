class NodoGeneral:
    def __init__(self, nombre, elemento=None):
        self.nombre = nombre
        self.elemento = elemento
        self.hijos = []


class ArbolGeneral:
    def __init__(self, nombre_raiz):
        self.raiz = NodoGeneral(nombre_raiz)

    def agregar_hijo(self, nodo_padre, nombre_hijo, elemento=None):
        if not isinstance(nodo_padre, NodoGeneral):
            raise TypeError(
                "El nodo padre debe ser una instancia de NodoGeneral."
            )

        nuevo_nodo = NodoGeneral(nombre_hijo, elemento)
        nodo_padre.hijos.append(nuevo_nodo)

        return nuevo_nodo