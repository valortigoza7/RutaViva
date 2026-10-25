class HeapBinaria:
    """
    Heap binaria máxima (MaxHeap).

    El elemento con mayor prioridad queda en la raíz.
    En RutaViva, la prioridad es el rating del destino.
    """

    def __init__(self):
        self.heap = []
        self._contador = 0

    def __len__(self):
        """Devuelve la cantidad de elementos."""
        return len(self.heap)

    def esta_vacia(self):
        """Indica si la heap está vacía."""
        return len(self.heap) == 0

    def swapp(self, i, j):
        """Intercambia dos nodos del heap."""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insertar(self, elemento, prioridad):
        """
        Inserta un elemento con su prioridad.

        En RutaViva, la prioridad corresponde al rating.
        """
        nuevo = (prioridad, -self._contador, elemento)
        self._contador += 1

        self.heap.append(nuevo)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, index):
        """Burbujeo hacia arriba para mantener el MaxHeap."""
        parent = (index - 1) // 2

        if index > 0 and self.heap[index][:2] > self.heap[parent][:2]:
            self.swapp(index, parent)
            self.sift_up(parent)

    def sift_down(self, index):
        """Burbujeo hacia abajo para mantener el MaxHeap."""
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if (
            left < len(self.heap)
            and self.heap[left][:2] > self.heap[largest][:2]
        ):
            largest = left

        if (
            right < len(self.heap)
            and self.heap[right][:2] > self.heap[largest][:2]
        ):
            largest = right

        if largest != index:
            self.swapp(index, largest)
            self.sift_down(largest)

    def extraer_maximo(self):
        """
        Extrae el elemento de mayor prioridad.

        Devuelve (prioridad, elemento).
        Si la heap está vacía, devuelve None.
        """
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            prioridad, _, elemento = self.heap.pop()
            return prioridad, elemento

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)

        prioridad, _, elemento = root
        return prioridad, elemento

    def eliminar(self, elemento):
        """Elimina un elemento específico de la heap."""
        index = next(
            (
                i
                for i, nodo in enumerate(self.heap)
                if nodo[2] == elemento
            ),
            -1
        )

        if index == -1:
            return False

        ultimo = self.heap.pop()

        if index < len(self.heap):
            self.heap[index] = ultimo

            parent = (index - 1) // 2

            if (
                index > 0
                and self.heap[index][:2] > self.heap[parent][:2]
            ):
                self.sift_up(index)
            else:
                self.sift_down(index)

        return True