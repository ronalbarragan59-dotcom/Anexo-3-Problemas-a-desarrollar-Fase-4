
# Importamos la clase Cliente
from clientes import Cliente

print("================================")
print(" SISTEMA SOFTWARE FJ")
print("================================")

# Registro de un cliente correcto
try:
    cliente1 = Cliente(
        "1020304050",
        "Carlos Ramirez",
        "carlos@gmail.com",
        "3104567890"
    )

    print("\nCliente registrado correctamente:")
    cliente1.mostrar_informacion()

except ValueError as error:
    print("Error al registrar cliente:", error)


# Intento de registrar un cliente incorrecto
try:
    cliente2 = Cliente(
        "1020304051",
        "",
        "correo incorrecto",
        "123"
    )

    print("\nCliente registrado:")
    cliente2.mostrar_informacion()

except ValueError as error:
    print("\nNo se pudo registrar el segundo cliente:")
    print(error)
