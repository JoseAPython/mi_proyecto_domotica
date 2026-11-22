import re


class DatoInvalido(ValueError):
    """Excepción personalizada para datos inválidos."""

class Duplicado(Exception):
    """Excepción personalizada para elementos duplicados."""

class NoEncontrado(Exception):
    """Excepción personalizada para elementos no encontrados."""


class Utils:

    @staticmethod
    def validar_id(texto: str) -> bool:
        """Valida que el ID introducido cumpla con el formato obligatorio"""

        if not isinstance(texto, str):
            return False

        texto = texto.strip()
        
        if not texto:
            return False

        return bool(re.fullmatch(r"[A-Za-z][A-Za-z0-9-]*", texto))

    @staticmethod
    def fabricar_id(prefijo: str, n: int) -> str:
        """Genera un ID canonizado basado en un prefijo y un número secuencial."""
    
        if not isinstance(prefijo, str) or not prefijo.strip():
            candidato = ""
        else:
            prefijo = prefijo.strip().upper()
            if isinstance(n, int) and not isinstance(n, bool):
                candidato = f"{prefijo}{n:03d}"
            else:
                candidato = f"{prefijo}{n}"

        if not isinstance(n, int) or isinstance(n, bool) or n < 1:
            raise DatoInvalido(f"ID generado inválido: '{candidato}'")
        
        if not Utils.validar_id(candidato):
            raise DatoInvalido(f"ID generado inválido: '{candidato}'")

        return candidato

    @staticmethod
    def validar_version(version: str) -> bool:
        """Valida que la versión introducida cumpla con el formato obligatorio"""

        if not isinstance(version, str):
            return False

        version = version.strip()
        
        if not version:
            return False

        return bool(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version))
    
# print(Utils.validar_version("1.2.3"))  # True
# print(Utils.validar_version("1.2"))    # False