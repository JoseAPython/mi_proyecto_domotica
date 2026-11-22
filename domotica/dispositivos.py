
from .base import Dispositivo
from .common import DatoInvalido, Utils


class SensorTemperatura(Dispositivo):

    def __init__(self, id, nombre, fabricante, celsius):
        super().__init__(id, nombre, fabricante)

        if isinstance(celsius, bool) or not isinstance(celsius, (int, float)):
            raise DatoInvalido("Temperatura inválida")

        self._celsius = float(celsius)

    def leer_valor(self) -> float:
        return self._celsius

    def calibrar(self, offset):
        if isinstance(offset, bool) or not isinstance(offset, (int, float)):
            raise DatoInvalido("Offset inválido")

        self._celsius += offset

    def tipo(self):
        return "SensorTemperatura"


class BombillaInteligente(Dispositivo):

    def __init__(self, id, nombre, fabricante, brillo, encendida=False):
        super().__init__(id, nombre, fabricante)

        self.set_brillo(brillo)

        if not isinstance(encendida, bool):
            raise DatoInvalido("Estado de encendido inválido")

        self._encendida = encendida
        self._version_firmware = None

    def get_brillo(self):
        return self._brillo

    def set_brillo(self, nuevo_brillo):
        if isinstance(nuevo_brillo, bool) or not isinstance(nuevo_brillo, int):
            raise DatoInvalido("El brillo debe ser un entero")

        if not 0 <= nuevo_brillo <= 100:
            raise DatoInvalido("El brillo debe estar entre 0 y 100")

        self._brillo = nuevo_brillo

    def encender(self):
        self._encendida = True

    def apagar(self):
        self._encendida = False

    def actualizar_firmware(self, version: str):
        if not Utils.validar_version(version):
            raise DatoInvalido("Versión inválida. Formato esperado: X.Y.Z")

        self._version_firmware = version

    def tipo(self):
        return "BombillaInteligente"

class CerraduraInteligente(Dispositivo):

    def __init__(self, id, nombre, fabricante, bloqueada=True):
        super().__init__(id, nombre, fabricante)

        if not isinstance(bloqueada, bool):
            raise DatoInvalido("Estado de bloqueo inválido")

        self._bloqueada = bloqueada

    def bloquear(self):
        self._bloqueada = True

    def desbloquear(self):
        self._bloqueada = False

    def get_bloqueada(self):
        return self._bloqueada

    # Adaptación a "Conmutable"
    def encender(self):
        self.bloquear()

    def apagar(self):
        self.desbloquear()

    def tipo(self):
        return "CerraduraInteligente"
