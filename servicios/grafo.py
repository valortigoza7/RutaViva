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