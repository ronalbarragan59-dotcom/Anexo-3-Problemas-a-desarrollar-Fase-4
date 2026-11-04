# Importamos las clases necesarias
from clientes import Cliente
from sistema_gestion import SistemaGestion
from excepciones import ErrorCliente

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

print("\nFin de las pruebas.")
