
# Importamos las clases necesarias
from clientes import Cliente
from servicios import ReservaSala, AlquilerDeEquipos, AsesoriaPersonalizada
from reservas import Reserva
from sistema_gestion import SistemaGestion
from excepciones import ErrorCliente, ErrorServicio, ErrorReserva

print("================================")
print("       SISTEMA SOFTWARE FJ")
print("================================")

# Creamos el sistema
sistema = SistemaGestion()


# OPERACION 1: Registrar un cliente correcto
print("\n1. REGISTRO DE CLIENTE")

try:
    cliente1 = Cliente(
        "1020304050",
        "Carlos Ramirez",
        "carlos@gmail.com",
        "3104567890"
    )

    sistema.registrar_cliente(cliente1)

except (ErrorCliente, ValueError, TypeError) as error:
    print("Error al registrar cliente:", error)


# OPERACION 2: Intentar registrar un cliente incorrecto
print("\n2. REGISTRO DE CLIENTE INVALIDO")

try:
    cliente2 = Cliente(
        "1020304051",
        "",
        "correo incorrecto",
        "123"
    )

    sistema.registrar_cliente(cliente2)

except (ErrorCliente, ValueError, TypeError) as error:
    print("No se pudo registrar el cliente:", error)
    sistema.registro.guardar_error(str(error))


# OPERACIONES 3, 4 Y 5: Registrar los tres servicios
print("\n3, 4 Y 5. REGISTRO DE SERVICIOS")

try:
    sala = ReservaSala("Sala Ejecutiva", 100000, 2, "Mediana")
    sistema.registrar_servicio(sala)

    equipo = AlquilerDeEquipos("Kit Multimedia", 50000, 3, "Video Beam")
    sistema.registrar_servicio(equipo)

    asesoria = AsesoriaPersonalizada(
        "Asesoria de Software", 130000, 1, "Virtual", 50000
    )
    sistema.registrar_servicio(asesoria)

except ErrorServicio as error:
    print("Error al registrar servicio:", error)


# OPERACION 6: Intentar registrar un servicio incorrecto
print("\n6. REGISTRO DE SERVICIO INVALIDO")

try:
    servicio_invalido = ReservaSala("", 0, 0, "")
    sistema.registrar_servicio(servicio_invalido)

except (ErrorServicio, ValueError, TypeError) as error:
    print("No se pudo registrar el servicio:", error)
    sistema.registro.guardar_error(str(error))


# OPERACION 7: Registrar una reserva correcta
print("\n7. REGISTRO DE RESERVA CORRECTA")

try:
    reserva1 = Reserva(cliente1, sala, 2)
    sistema.registrar_reserva(reserva1)

    reserva1.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva1.estado)

    reserva1.ProcesarReserva()
    print("Estado de la reserva:", reserva1.estado)

except (ErrorReserva, ErrorCliente, ErrorServicio) as error:
    print("Error al registrar la reserva:", error)


# OPERACION 8: Intentar registrar una reserva con un cliente no registrado
print("\n8. REGISTRO DE RESERVA CON CLIENTE NO REGISTRADO")

try:
    cliente_no_registrado = Cliente(
        "1020304052",
        "Pedro Gomez",
        "pedro@gmail.com",
        "3114567890"
    )

    reserva_invalida = Reserva(cliente_no_registrado, equipo, 1)
    sistema.registrar_reserva(reserva_invalida)

except (ErrorReserva, ErrorCliente, ErrorServicio) as error:
    print("No se pudo registrar la reserva:", error)


# OPERACION 9: Cancelar una reserva pendiente
print("\n9. CANCELACION DE RESERVA")

try:
    reserva2 = Reserva(cliente1, equipo, 1)
    reserva2.CancelacionDeLaReserva()

    print("Estado de la reserva:", reserva2.estado)

except ErrorReserva as error:
    print("Error al cancelar la reserva:", error)


# OPERACION 10: Intentar confirmar una reserva cancelada
print("\n10. CONFIRMACION DE RESERVA CANCELADA")

try:
    reserva2.ConfirmarEstadoDeLaReserva()

except ErrorReserva as error:
    print("No se pudo confirmar la reserva:", error)


# OPERACION 11: Intentar procesar una reserva sin confirmar
print("\n11. PROCESAMIENTO DE RESERVA SIN CONFIRMAR")

try:
    reserva3 = Reserva(cliente1, asesoria, 1)
    reserva3.ProcesarReserva()

except ErrorReserva as error:
    print("No se pudo procesar la reserva:", error)


# CONSULTA FINAL DE LA INFORMACION
print("\n================================")
print("       CONSULTA FINAL")
print("================================")

print("\nCLIENTES REGISTRADOS")
sistema.consultar_clientes()

print("\nSERVICIOS REGISTRADOS")
sistema.consultar_servicios()

print("\nRESERVAS REGISTRADAS")
sistema.consultar_reservas()

print("\nFin de las pruebas del sistema.")
