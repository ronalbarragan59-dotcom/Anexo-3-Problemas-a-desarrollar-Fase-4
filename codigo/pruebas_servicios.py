
from clientes import Cliente
from reservas import Reserva
from servicios import ReservaSala, AlquilerDeEquipos, AsesoriaPersonalizada
from excepciones import ErrorReserva, ErrorCliente


# --- 1. PRUEBA: Reserva de Sala ---
try:
    print("\n========================================")
    print("=== 1. PRUEBA DE RESERVA DE SALA ===")
    print("========================================")

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 2): "))

    cliente = Cliente("1001", nombre_cliente, "maria@gmail.com", "3104567890")
    sala = ReservaSala("Sala Ejecutiva", 100000, duracion, "Mediana")
    reserva_sala = Reserva(cliente, sala, duracion)

    print("\n--- Métodos del Servicio (Sala) ---")
    print(sala.describir_servicios())
    print("Validación de parámetros:", sala.validar_parametros())

    print("\n--- Métodos de la Reserva (Sala) ---")
    reserva_sala.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_sala.estado)

    reserva_sala.ProcesarReserva()
    print("Estado de la reserva:", reserva_sala.estado)

except (ErrorReserva, ErrorCliente, ValueError) as e:
    print(f"Error controlado en Sala: {e}")


# --- 2. PRUEBA: Alquiler de Equipos ---
try:
    print("\n========================================")
    print("=== 2. PRUEBA DE ALQUILER DE EQUIPOS ===")
    print("========================================")

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nombre_eq = input("Ingrese el nombre del equipo: ")
    duracion = float(input("Ingrese la duración en horas (ej: 3): "))

    cliente = Cliente("1002", nombre_cliente, "maria@gmail.com", "3104567890")
    equipo = AlquilerDeEquipos("Kit Multimedia", 50000, duracion, nombre_eq)
    reserva_equipo = Reserva(cliente, equipo, duracion)

    print("\n--- Métodos del Servicio (Equipo) ---")
    print(equipo.describir_servicios())
    print("Validación de parámetros:", equipo.validar_parametros())

    print("\n--- Métodos de la Reserva (Equipo) ---")
    reserva_equipo.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_equipo.estado)

    reserva_equipo.ProcesarReserva()
    print("Estado de la reserva:", reserva_equipo.estado)

except (ErrorReserva, ErrorCliente, ValueError) as e:
    print(f"Error controlado en Equipos: {e}")


# --- 3. PRUEBA: Asesoría Personalizada (Presencial) ---
try:
    print("\n========================================")
    print("=== 3. PRUEBA DE ASESORÍA (PRESENCIAL) ===")
    print("========================================")

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 1): "))

    cliente = Cliente("1003", nombre_cliente, "maria@gmail.com", "3104567890")
    asesoria_presencial = AsesoriaPersonalizada(
        "Asesoría Software", 130000, duracion, "Presencial", 50000
    )
    reserva_presencial = Reserva(cliente, asesoria_presencial, duracion)

    print("\n--- Métodos del Servicio (Asesoría Presencial) ---")
    print(asesoria_presencial.describir_servicios())
    print("Validación de parámetros:", asesoria_presencial.validar_parametros())

    print("\n--- Métodos de la Reserva (Presencial) ---")
    reserva_presencial.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_presencial.estado)

    reserva_presencial.ProcesarReserva()
    print("Estado de la reserva:", reserva_presencial.estado)

except (ErrorReserva, ErrorCliente, ValueError) as e:
    print(f"Error controlado en Asesoría Presencial: {e}")


# --- 4. PRUEBA: Asesoría Personalizada (Virtual) ---
try:
    print("\n========================================")
    print("=== 4. PRUEBA DE ASESORÍA (VIRTUAL) ===")
    print("========================================")

    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 1): "))

    cliente = Cliente("1004", nombre_cliente, "maria@gmail.com", "3104567890")
    asesoria_virtual = AsesoriaPersonalizada(
        "Asesoría Software", 130000, duracion, "Virtual", 50000
    )
    reserva_virtual = Reserva(cliente, asesoria_virtual, duracion)

    print("\n--- Métodos del Servicio (Virtual) ---")
    print(asesoria_virtual.describir_servicios())
    print("Validación de parámetros:", asesoria_virtual.validar_parametros())

    print("\n--- Métodos de la Reserva (Virtual) ---")
    reserva_virtual.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_virtual.estado)

    reserva_virtual.ProcesarReserva()
    print("Estado de la reserva:", reserva_virtual.estado)

except (ErrorReserva, ErrorCliente, ValueError) as e:
    print(f"Error controlado en Asesoría Virtual: {e}")
