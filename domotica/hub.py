
from .base import Dispositivo
from .common import Duplicado, NoEncontrado
from .interfaces import Conmutable, Medible


class Hub:
    def __init__(self):
        self._dispositivos: dict[str, Dispositivo] = {}

    def registrar(self, disp: Dispositivo):
        identificador = disp.get_id()

        if identificador in self._dispositivos:
            raise Duplicado(f"El ID '{identificador}' ya existe")

        self._dispositivos[identificador] = disp

    def listar(self):
        return list(self._dispositivos.values())

    def obtener(self, identificador):
        if identificador not in self._dispositivos:
            raise NoEncontrado(
                f"No existe el dispositivo '{identificador}'"
            )

        return self._dispositivos[identificador]

    def operar_todos(self):
        for dispositivo in self.listar():
            identificador = dispositivo.get_id()

            if isinstance(dispositivo, Medible):
                print(f"- {identificador} → lectura = {dispositivo.leer_valor():.2f} ºC")

            if isinstance(dispositivo, Conmutable):
                es_cerradura = dispositivo.tipo() == "CerraduraInteligente"

                dispositivo.encender()

                if es_cerradura:
                    accion_encender = "encender() (bloquear)"
                else:
                    accion_encender = "encender()"

                dispositivo.apagar()

                if es_cerradura:
                    accion_apagar = "apagar() (desbloquear)"
                else:
                    accion_apagar = "apagar()"

                print(
                    f"- {identificador} → {accion_encender} → OK; "
                    f"{accion_apagar} → OK"
                )

    def estadisticas(self):
        resultado = {}

        for dispositivo in self.listar():
            tipo = dispositivo.tipo()
            resultado[tipo] = resultado.get(tipo, 0) + 1

        return resultado
