class Grafo:
    """
    Representa un grafo no dirigido mediante una lista de adyacencia.

    Cada vértice representa un destino turístico.
    Las aristas representan relaciones entre destinos que
    comparten región o categoría.
    """

    def __init__(self):
        self.adyacencia = {}

    def agregar_vertice(self, destino):
        """Agrega un destino al grafo si todavía no existe."""
        if destino not in self.adyacencia:
            self.adyacencia[destino] = []

    def conectar(self, destino1, destino2):
        """
        Conecta dos destinos mediante una arista no dirigida.
        """
        self.agregar_vertice(destino1)
        self.agregar_vertice(destino2)

        if destino2 not in self.adyacencia[destino1]:
            self.adyacencia[destino1].append(destino2)

        if destino1 not in self.adyacencia[destino2]:
            self.adyacencia[destino2].append(destino1)

    def obtener_vecinos(self, destino):
        """Devuelve los destinos conectados con el destino indicado."""
        return self.adyacencia.get(destino, [])

    def bfs(self, inicio):
        """
        Recorre el grafo en anchura (BFS).

        Comienza desde un destino y visita primero
        sus vecinos, luego los vecinos de estos.

        Devuelve una lista con el orden de visita.
        """
        if inicio not in self.adyacencia:
            return []

        visitados = []
        cola = [inicio]
        vistos = {inicio}

        while cola:
            actual = cola.pop(0)
            visitados.append(actual)

            for vecino in self.adyacencia[actual]:
                if vecino not in vistos:
                    vistos.add(vecino)
                    cola.append(vecino)

        return visitados

    def dfs(self, inicio):
        """
        Recorre el grafo en profundidad (DFS).

        Explora un camino todo lo posible antes
        de regresar y continuar con otros vecinos.

        Devuelve una lista con el orden de visita.
        """
        if inicio not in self.adyacencia:
            return []

        visitados = []
        pila = [inicio]
        vistos = {inicio}

        while pila:
            actual = pila.pop()
            visitados.append(actual)

            for vecino in reversed(self.adyacencia[actual]):
                if vecino not in vistos:
                    vistos.add(vecino)
                    pila.append(vecino)

        return visitados