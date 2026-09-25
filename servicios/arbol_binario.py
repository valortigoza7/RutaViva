class NodoArbol:
    def __init__(self, clave, elemento):
        self.clave = clave
        self.elemento = elemento
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, elemento):
        nuevo_nodo = NodoArbol(clave, elemento)

        if self.raiz is None:
            self.raiz = nuevo_nodo
            return

        actual = self.raiz

        while True:
            if clave < actual.clave:
                if actual.izquierdo is None:
                    actual.izquierdo = nuevo_nodo
                    return
                actual = actual.izquierdo

            elif clave > actual.clave:
                if actual.derecho is None:
                    actual.derecho = nuevo_nodo
                    return
                actual = actual.derecho

            else:
                actual.elemento = elemento
                return

    def buscar(self, clave):
        actual = self.raiz

        while actual is not None:
            if clave == actual.clave:
                return actual.elemento

            if clave < actual.clave:
                actual = actual.izquierdo
            else:
                actual = actual.derecho

        return None

    def inorder(self):
        elementos = []

        def recorrer(nodo):
            if nodo is None:
                return

            recorrer(nodo.izquierdo)
            elementos.append(nodo.elemento)
            recorrer(nodo.derecho)

        recorrer(self.raiz)
        return elementos

    def preorder(self):
        elementos = []

        def recorrer(nodo):
            if nodo is None:
                return

            elementos.append(nodo.elemento)
            recorrer(nodo.izquierdo)
            recorrer(nodo.derecho)

        recorrer(self.raiz)
        return elementos

    def postorder(self):
        elementos = []

        def recorrer(nodo):
            if nodo is None:
                return

            recorrer(nodo.izquierdo)
            recorrer(nodo.derecho)
            elementos.append(nodo.elemento)

        recorrer(self.raiz)
        return elementos