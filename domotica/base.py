from abc import ABC, abstractmethod

from .common import DatoInvalido, Utils


class Dispositivo(ABC):

    def __init__(self, id, nombre, fabricante):
        self.set_id(id)
        self.set_nombre(nombre)
        self.set_fabricante(fabricante)

    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_fabricante(self):
        return self._fabricante

    def set_id(self, nuevo_id):
        if not Utils.validar_id(nuevo_id):
            raise DatoInvalido("ID inválido")

        self._id = nuevo_id.strip()

    def set_nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str) or not nuevo_nombre.strip():
            raise DatoInvalido("Nombre inválido")
        
        self._nombre = nuevo_nombre.strip()

    def set_fabricante(self, nuevo_fabricante):
        if not isinstance(nuevo_fabricante, str) or not nuevo_fabricante.strip():
            raise DatoInvalido("Fabricante inválido")
        
        self._fabricante = nuevo_fabricante.strip()

    def __str__(self):
        return f"[{self.tipo()}] {self._nombre} (id={self._id}, fabricante={self._fabricante})"

    @abstractmethod
    def tipo(self):
        pass

