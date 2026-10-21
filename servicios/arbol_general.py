from collections import deque

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
            raise TypeError("El nodo padre debe ser una instancia de NodoGeneral.")

        nuevo_nodo = NodoGeneral(nombre_hijo, elemento)
        nodo_padre.hijos.append(nuevo_nodo)
        return nuevo_nodo

    def buscar(self, nombre, nodo_actual=None):
        if nodo_actual is None:
            nodo_actual = self.raiz

        if nodo_actual.nombre.lower() == nombre.lower():
            return nodo_actual

        for hijo in nodo_actual.hijos:
            hallado = self.buscar(nombre, hijo)
            if hallado:
                return hallado
        return None

    def recorrido_preorden(self, nodo_actual=None, resultado=None):
        if resultado is None:
            resultado = []
        if nodo_actual is None:
            nodo_actual = self.raiz

        resultado.append(nodo_actual.nombre)
        for hijo in nodo_actual.hijos:
            self.recorrido_preorden(hijo, resultado)
        return resultado

    def recorrido_postorden(self, nodo_actual=None, resultado=None):
        if resultado is None:
            resultado = []
        if nodo_actual is None:
            nodo_actual = self.raiz

        for hijo in nodo_actual.hijos:
            self.recorrido_postorden(hijo, resultado)
        resultado.append(nodo_actual.nombre)
        return resultado

    def recorrido_por_niveles(self):
        resultado = []
        if not self.raiz:
            return resultado

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.nombre)
            for hijo in actual.hijos:
                cola.append(hijo)
        return resultado