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
    while not opc.isnumeric():
        opc = input("Eliga una opción válida: ")
    
    if opc == "1":
        num_nuevas_tarj = int(input("Cuántas tarjetas desea registrar? Máximo de 5 tarjetas a la vez "))
        if num_nuevas_tarj >5:
            print("El número ingresado excede el limite del sistema")
        else:
            for i in range(num_nuevas_tarj):
                nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
                while not nueva_tarjeta.isnumeric() or len(nueva_tarjeta)>16 or len(nueva_tarjeta)<16:
                    print ("Ingreso mal los datos de la nueva tarjeta")
                    nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
                if len(nueva_tarjeta) == 16:
                    tarjetas.append(nueva_tarjeta)
                    saldos.append(0)
        print(tarjetas,saldos)
    elif opc == "8":
        print("Desea salir?")
        aux_salir = input("Si / No ").upper()
        if aux_salir == "SI":
            salir = True

        
