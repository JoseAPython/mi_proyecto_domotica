from typing import Protocol, runtime_checkable


@runtime_checkable
class Medible(Protocol):
    def leer_valor(self) -> float: ...

@runtime_checkable
class Conmutable(Protocol):
    """ Adaptar a cada tipo de dispositivo para que se puedan activar/desactivar utilizando polimorfismo llamando al metodo correspondiente si  ya lo integran """
    def encender(self) -> None: ...
    def apagar(self) -> None: ...

@runtime_checkable
class Actualizable(Protocol):
    def actualizar_firmware(self, version: str) -> None: ...