tarjetas = ["1234567890123456", "9876543210987654", "5555666677778888"]
saldos = [150.50, 25.00, -10.00]

salir = False
while not salir:
    print ("MENU")
    print("1) Ingresar nuevas tarjetas al sistema")
    print("2) Asignar saldo para tarjetas recientemente agregadas")
    print("3) Ver tarjetas registradas y sus saldos")
    print("4) Ver salfo de una tarjeta específica")
    print("5) Ver listado de tarjetas con saldo negativo o cero")
    print("6) Registrar una nueva tarjeta y su saldo actual")
    print("7) Aumentar o discminuir el saldo de una tarjeta")
    print("8) Salir")
    opc = input("Eliga una opción: ")
    