"""
Modelo de dominio: Destino.

Representa un destino turístico dentro del sistema RutaViva.
Los atributos son privados (encapsulamiento) y se accede a ellos
mediante propiedades (getters), evitando modificaciones directas
no controladas desde fuera de la clase.
"""


class Destino:
    def __init__(self, nombre: str, categoria: str, region: str,
                 rating: float, descripcion: str = ""):
        self._nombre = nombre
        self._categoria = categoria      # playa, montaña, ciudad, naturaleza...
        self._region = region            # ej: "Patagonia", "Cuyo", "NOA"
        self._rating = rating            # 0.0 a 10.0
        self._descripcion = descripcion

    # --- Getters (propiedades de solo lectura hacia afuera) ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def region(self) -> str:
        return self._region

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def descripcion(self) -> str:
        return self._descripcion

    # --- Setter controlado: el rating puede actualizarse, pero validado ---
    def actualizar_rating(self, nuevo_rating: float) -> None:
        if not (0 <= nuevo_rating <= 10):
            raise ValueError("El rating debe estar entre 0 y 10.")
        self._rating = nuevo_rating

    def __repr__(self) -> str:
        return f"{self._nombre} ({self._categoria} · {self._region}) ⭐{self._rating}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Destino):
            return False
        return self._nombre.lower() == other._nombre.lower()
