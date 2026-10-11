class NodoAVL:
    def __init__(self, clave, elemento):
        self.clave = clave
        self.elemento = elemento

        self.izquierdo = None
        self.derecho = None

        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0

        return nodo.altura

    def calcular_factor_equilibrio(self, nodo):
        if nodo is None:
            return 0

        altura_izquierda = self.obtener_altura(nodo.izquierdo)
        altura_derecha = self.obtener_altura(nodo.derecho)

        return altura_izquierda - altura_derecha

    def actualizar_altura(self, nodo):
        altura_izquierda = self.obtener_altura(nodo.izquierdo)
        altura_derecha = self.obtener_altura(nodo.derecho)

        nodo.altura = 1 + max(
            altura_izquierda,
            altura_derecha
        )

    def rotacion_derecha(self, y):
        x = y.izquierdo
        subarbol = x.derecho

        x.derecho = y
        y.izquierdo = subarbol

        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotacion_izquierda(self, x):
        y = x.derecho
        subarbol = y.izquierdo

        y.izquierdo = x
        x.derecho = subarbol

        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    def insertar(self, clave, elemento):
        self.raiz = self._insertar(
            self.raiz,
            clave,
            elemento
        )

    def _insertar(self, nodo, clave, elemento):
        if nodo is None:
            return NodoAVL(clave, elemento)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar(
                nodo.izquierdo,
                clave,
                elemento
            )
        elif clave > nodo.clave:
            nodo.derecho = self._insertar(
                nodo.derecho,
                clave,
                elemento
            )
        else:
            nodo.elemento = elemento
            return nodo

        self.actualizar_altura(nodo)

        equilibrio = self.calcular_factor_equilibrio(nodo)

        # Caso izquierda-izquierda (LL)
        if equilibrio > 1 and clave < nodo.izquierdo.clave:
            return self.rotacion_derecha(nodo)

        # Caso derecha-derecha (RR)
        if equilibrio < -1 and clave > nodo.derecho.clave:
            return self.rotacion_izquierda(nodo)

        # Caso izquierda-derecha (LR)
        if equilibrio > 1 and clave > nodo.izquierdo.clave:
            nodo.izquierdo = self.rotacion_izquierda(
                nodo.izquierdo
            )
            return self.rotacion_derecha(nodo)

        # Caso derecha-izquierda (RL)
        if equilibrio < -1 and clave < nodo.derecho.clave:
            nodo.derecho = self.rotacion_derecha(
                nodo.derecho
            )
            return self.rotacion_izquierda(nodo)

        return nodo

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