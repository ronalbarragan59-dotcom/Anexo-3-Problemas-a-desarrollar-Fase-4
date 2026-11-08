
from reservas import Reserva
from servicios import ReservaSala, AlquilerDeEquipos, AsesoriaPersonalizada

# --- 1. PRUEBA: Reserva de Sala ---
try:
    print("\n========================================")
    print("=== 1. PRUEBA DE RESERVA DE SALA ===")
    print("========================================")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 2): "))
    
    sala = ReservaSala("Sala Ejecutiva", 100000, duracion, "Mediana")
    reserva_sala = Reserva(nombre_cliente, sala, duracion)
    
    print("\n--- Métodos del Servicio (Sala) ---")
    print(sala.describir_servicios())
    print("Validación de parámetros:", sala.validar_parametros())
    
    print("\n--- Métodos de la Reserva (Sala) ---")
    reserva_sala.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_sala.estado)
    reserva_sala.CancelacionDeLaReserva()
    print("Estado de la reserva:", reserva_sala.estado)

except Exception as e:
    print(f"Error controlado en Sala: {e}")


# --- 2. PRUEBA: Alquiler de Equipos ---
try:
    print("\n========================================")
    print("=== 2. PRUEBA DE ALQUILER DE EQUIPOS ===")
    print("========================================")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    nombre_eq = input("Ingrese el nombre del equipo: ")
    duracion = float(input("Ingrese la duración en horas (ej: 3): "))
    
    equipo = AlquilerDeEquipos("Kit Multimedia", 50000, duracion, nombre_eq)
    reserva_equipo = Reserva(nombre_cliente, equipo, duracion)
    
    print("\n--- Métodos del Servicio (Equipo) ---")
    print(equipo.describir_servicios())
    print("Validación de parámetros:", equipo.validar_parametros())
    
    print("\n--- Métodos de la Reserva (Equipo) ---")
    reserva_equipo.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_equipo.estado)
    reserva_equipo.CancelacionDeLaReserva()
    print("Estado de la reserva:", reserva_equipo.estado)

except Exception as e:
    print(f"Error controlado en Equipos: {e}")


# --- 3. PRUEBA: Asesoría Personalizada (Presencial) ---
try:
    print("\n========================================")
    print("=== 3. PRUEBA DE ASESORÍA (PRESENCIAL) ===")
    print("========================================")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 1): "))
    
    asesoria_presencial = AsesoriaPersonalizada("Asesoría Software", 130000, duracion, "Presencial", 50000)
    reserva_presencial = Reserva(nombre_cliente, asesoria_presencial, duracion)
    
    print("\n--- Métodos del Servicio (Asesoría Presencial) ---")
    print(asesoria_presencial.describir_servicios())
    print("Validación de parámetros:", asesoria_presencial.validar_parametros())
    
    print("\n--- Métodos de la Reserva (Asesoría Presencial) ---")
    reserva_presencial.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_presencial.estado)
    reserva_presencial.CancelacionDeLaReserva()
    print("Estado de la reserva:", reserva_presencial.estado)

except Exception as e:
    print(f"Error controlado en Asesoría Presencial: {e}")


# --- 4. PRUEBA: Asesoría Personalizada (Virtual) ---
try:
    print("\n========================================")
    print("=== 4. PRUEBA DE ASESORÍA (VIRTUAL) ===")
    print("========================================")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    duracion = float(input("Ingrese la duración en horas (ej: 1): "))
    
    asesoria_virtual = AsesoriaPersonalizada("Asesoría Software", 130000, duracion, "Virtual", 50000)
    reserva_virtual = Reserva(nombre_cliente, asesoria_virtual, duracion)
    
    print("\n--- Métodos del Servicio (Asesoría Virtual) ---")
    print(asesoria_virtual.describir_servicios())
    print("Validación de parámetros:", asesoria_virtual.validar_parametros())
    
    print("\n--- Métodos de la Reserva (Asesoría Virtual) ---")
    reserva_virtual.ConfirmarEstadoDeLaReserva()
    print("Estado de la reserva:", reserva_virtual.estado)
    reserva_virtual.CancelacionDeLaReserva()
    print("Estado de la reserva:", reserva_virtual.estado)

except Exception as e:
    print(f"Error controlado en Asesoría Virtual: {e}")
