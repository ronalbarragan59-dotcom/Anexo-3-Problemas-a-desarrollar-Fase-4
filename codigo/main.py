
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

# Primera prueba: registrar un cliente correcto
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
    sistema.registro.guardar_error(str(error))


# Segunda prueba: registrar un cliente incorrecto
try:
    cliente2 = Cliente(
        "1020304051",
        "",
        "correo incorrecto",
        "123"
    )

    sistema.registrar_cliente(cliente2)

except (ErrorCliente, ValueError, TypeError) as error:
    print("\nNo se pudo registrar el segundo cliente:")
    print(error)

    sistema.registro.guardar_error(str(error))


# Consultamos los clientes registrados
print("\nCONSULTA DE CLIENTES")
sistema.consultar_clientes()


# Tercera prueba: registrar servicios
print("\nREGISTRO DE SERVICIOS")

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


# Consultamos los servicios registrados
print("\nCONSULTA DE SERVICIOS")
sistema.consultar_servicios()


# Cuarta prueba: registrar una reserva
print("\nREGISTRO DE RESERVA")

try:
    reserva1 = Reserva(cliente1, sala, 2)
    sistema.registrar_reserva(reserva1)

except (ErrorReserva, ErrorCliente, ErrorServicio) as error:
    print("Error al registrar reserva:", error)


# Consultamos las reservas registradas
print("\nCONSULTA DE RESERVAS")
sistema.consultar_reservas()


print("\nFin de las pruebas.")
