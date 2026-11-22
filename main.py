from domotica import (
    Actualizable,
    BombillaInteligente,
    CerraduraInteligente,
    Conmutable,
    DatoInvalido,
    Duplicado,
    Hub,
    Medible,
    NoEncontrado,
    SensorTemperatura,
    Utils,
)


def mostrar_registro(d):
    if isinstance(d, SensorTemperatura):
        categoria = "sensor"
        detalle = f"{d.leer_valor():.1f} ºC"

    elif isinstance(d, BombillaInteligente):
        categoria = "bombilla"
        detalle = f"brillo={d.get_brillo()}"

    else:
        categoria = "cerradura"
        detalle = "bloqueada" if d.get_bloqueada() else "desbloqueada"

    print(
        f"- OK: {d.get_id()} ({categoria}) → "
        f"{d.tipo()} \"{d.get_nombre()}\" "
        f"({d.get_fabricante()}, {detalle})"
    )


if __name__ == "__main__":

    print("=== DEMO DOMÓTICA — INICIO ===\n")

    hub = Hub()

    print("Creando Hub... OK")
    print("Cargando definiciones de dispositivos...")
    print("\nValidando e instanciando:\n")

    definiciones = [
        {"id": "S001", "tipo": "sensor", "nombre": "Sensor Cocina",
         "fabricante": "Acme", "celsius": 22.5},

        {"id": "B001", "tipo": "bombilla", "nombre": "Bombilla Salón",
         "fabricante": "Lumen", "brillo": 80},

        {"id": "C001", "tipo": "cerradura", "nombre": "Puerta Principal",
         "fabricante": "SafeCo", "bloqueada": True},

        {"id": "S002", "tipo": "sensor", "nombre": "Sensor Dormitorio",
         "fabricante": "Acme", "celsius": 19.3},

        {"id": "B002", "tipo": "bombilla", "nombre": "Bombilla Pasillo",
         "fabricante": "Lumen", "brillo": 50},

        {"id": "C002", "tipo": "cerradura", "nombre": "Puerta Trasera",
         "fabricante": "SafeCo", "bloqueada": True},

        {"id": "001", "tipo": "sensor", "nombre": "Sensor Inválido",
         "fabricante": "Acme", "celsius": 20},

        {"id": "B001", "tipo": "bombilla", "nombre": "Duplicada",
         "fabricante": "Lumen", "brillo": 50}
    ]

    for datos in definiciones:

        if not Utils.validar_id(datos["id"]):
            print(f"- ERROR: id \"{datos['id']}\" inválido → se omite")
            continue

        try:
            if datos["tipo"] == "sensor":
                dispositivo = SensorTemperatura(
                    datos["id"], datos["nombre"],
                    datos["fabricante"], datos["celsius"]
                )

            elif datos["tipo"] == "bombilla":
                dispositivo = BombillaInteligente(
                    datos["id"], datos["nombre"],
                    datos["fabricante"], datos["brillo"]
                )

            elif datos["tipo"] == "cerradura":
                dispositivo = CerraduraInteligente(
                    datos["id"], datos["nombre"],
                    datos["fabricante"], datos["bloqueada"]
                )

            else:
                raise DatoInvalido("Tipo de dispositivo desconocido")

            hub.registrar(dispositivo)
            mostrar_registro(dispositivo)

        except Duplicado as e:
            print(f"- ERROR: {e} → se omite")

        except DatoInvalido as e:
            print(f"- ERROR: {e} → se omite")

    dispositivos = hub.listar()

    print(f"\nRegistro en Hub completado: {len(dispositivos)} dispositivos.")

    print("\nListado de dispositivos:\n")

    for d in dispositivos:
        print(f"- {d}")

    print("\nCapacidades detectadas:\n")

    medibles = conmutables = actualizables = 0

    for d in dispositivos:
        capacidades = []

        if isinstance(d, Medible):
            capacidades.append("Medible")
            medibles += 1

        if isinstance(d, Conmutable):
            capacidades.append("Conmutable")
            conmutables += 1

        if isinstance(d, Actualizable):
            capacidades.append("Actualizable")
            actualizables += 1

        print(f"- {d.get_id()} → {', '.join(capacidades)}")

    print("\nOperar todos (polimorfismo):\n")
    hub.operar_todos()

    print("\nAcciones específicas:\n")

    sensor = next(d for d in dispositivos if isinstance(d, SensorTemperatura))

    sensor.calibrar(0.70)
    print(
        f"- Calibrar {sensor.get_id()} con offset +0.70 "
        f"→ nueva lectura = {sensor.leer_valor():.2f} ºC"
    )

    bombillas = [d for d in dispositivos if isinstance(d, BombillaInteligente)]

    bombilla = bombillas[0]
    brillo_anterior = bombilla.get_brillo()
    bombilla.set_brillo(90)

    print(
        f"- {bombilla.get_id()}: brillo previo = {brillo_anterior} "
        f"→ brillo nuevo = {bombilla.get_brillo()}"
    )

    try:
        bombilla.actualizar_firmware("1.2.3")
        print(f"- {bombilla.get_id()}: actualizar_firmware(\"1.2.3\") → OK")
    except DatoInvalido as e:
        print(f"- ERROR: {e}")

    try:
        bombillas[1].actualizar_firmware("1.0")
    except DatoInvalido as e:
        print(f"- {bombillas[1].get_id()}: ERROR: {e}")

    cerradura = next(
        d for d in dispositivos if isinstance(d, CerraduraInteligente)
    )

    estado = "bloqueada" if cerradura.get_bloqueada() else "desbloqueada"
    print(f"- {cerradura.get_id()}: estado → {estado}")

    cerradura.desbloquear()
    print(f"  desbloquear() → OK")

    cerradura.bloquear()
    print(f"  bloquear() → OK")

    print("\nEstadísticas por tipo:\n")

    estadisticas = hub.estadisticas()

    for tipo, cantidad in estadisticas.items():
        print(f"- {tipo}: {cantidad}")

    print(f"Total dispositivos: {len(dispositivos)}")

    print("\nResumen de capacidades:\n")
    print(f"- Medibles: {medibles}")
    print(f"- Conmutables: {conmutables}")
    print(f"- Actualizables: {actualizables}")

    print("\nPruebas de errores controlados:\n")

    try:
        hub.registrar(bombilla)
    except Duplicado as e:
        print(f"- Registrar de nuevo {bombilla.get_id()} → ERROR: {e}")

    print(f"- Validar id \"A_01\" → {Utils.validar_id('A_01')}")

    try:
        bombillas[1].actualizar_firmware("v1.2.3")
    except DatoInvalido as e:
        print(f"- Actualizar firmware B002 a \"v1.2.3\" → ERROR: {e}")

    try:
        hub.obtener("X999")
    except NoEncontrado as e:
        print(f"- Obtener X999 → ERROR: {e}")

    print("\n=== DEMO DOMÓTICA — FIN ===")
