# Sistema de Domótica

Aplicación modular desarrollada en Python que simula un sistema de domótica. Permite gestionar diferentes dispositivos mediante un Hub central, utilizando programación orientada a objetos.

## Funcionalidades

- Registro y gestión de dispositivos desde un Hub central.
- Sensores de temperatura con lectura y calibración.
- Bombillas inteligentes con control de encendido, apagado y brillo.
- Cerraduras inteligentes con funciones de bloqueo y desbloqueo.
- Validación de identificadores y versiones de firmware.
- Detección de capacidades mediante Protocols.
- Operaciones polimórficas sobre diferentes tipos de dispositivos.
- Gestión de excepciones personalizadas y dispositivos duplicados.
- Estadísticas del sistema según el tipo de dispositivo.

## Estructura del proyecto

```text
mi_proyecto_domotica/
│
├── domotica/
│   ├── __init__.py
│   ├── base.py
│   ├── dispositivos.py
│   ├── hub.py
│   ├── interfaces.py
│   └── common.py
│
├── main.py
├── README.md
├── enlace_github.txt
└── .gitignore
```

### Descripción de los módulos

| Archivo | Descripción |
|------------------------------------------------------------------|
| `base.py` | Define la clase abstracta `Dispositivo`. |
| `dispositivos.py` | Implementa sensores, bombillas y cerraduras inteligentes. |
| `hub.py` | Gestiona el registro, listado, operaciones y estadísticas. |
| `interfaces.py` | Define los Protocols `Medible`, `Conmutable` y `Actualizable`. |
| `common.py` | Contiene utilidades de validación y excepciones personalizadas. |
| `__init__.py` | Organiza y expone los elementos principales del paquete. |
| `main.py` | Ejecuta una demostración del sistema. |

## Tecnologías utilizadas

- Python 3.9 o superior.
- Programación Orientada a Objetos (POO).
- Módulos y paquetes de Python.
- Clases abstractas y herencia.
- Polimorfismo y Protocols.
- Manejo de excepciones.

El proyecto utiliza módulos de la biblioteca estándar de Python, sin dependencias externas.

## Ejecución

Desde la carpeta raíz del proyecto, ejecutar:

```bash
python main.py
```

El programa realizará una demostración del sistema, incluyendo la creación y registro de dispositivos, la detección de capacidades, las operaciones polimórficas, las estadísticas y diferentes pruebas de validación y manejo de errores.

---

**UD2: Programación Orientada a Objetos con Python.**