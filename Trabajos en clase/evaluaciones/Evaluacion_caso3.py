tarjetas = ["1234567890123456", "9876543210987654", "5555666677778888", "2222444422224444", "1234123412341234"]
saldos = [150.50, 25.00, -10.00,0.00,0.00]
num_nuevas_tarj = 0
salir = False
while not salir:
    print ("MENU")
    print("1) Ingresar nuevas tarjetas al sistema")
    print("2) Asignar saldo para tarjetas recientemente agregadas")
    print("3) Ver tarjetas registradas y sus saldos")
    print("4) Ver saldo de una tarjeta específica")
    print("5) Ver listado de tarjetas con saldo negativo o cero")
    print("6) Registrar una nueva tarjeta y su saldo actual")
    print("7) Aumentar o disminuir el saldo de una tarjeta")
    print("8) Salir")
    opc = input("Eliga una opción: ")
    while not opc.isnumeric():
        opc = input("Eliga una opción válida: ")
    if opc == "1": #Ingreso de nuevas tarjetas al sistema
        num_nuevas_tarj = int(input("Cuántas tarjetas desea registrar? Máximo de 5 tarjetas a la vez "))
        if num_nuevas_tarj >5: #Comprueba que el valor ingresado no exceda el limite
            print("El número ingresado excede el limite del sistema")
        else:
            for i in range(num_nuevas_tarj):
                nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
                #El bucle se ejecuta cuando el formato de la tarjeta a registrar no es el correcto o cuando la tarjeta en cuestion ya esta en el sistema
                while not nueva_tarjeta.isnumeric() or len(nueva_tarjeta)>16 or len(nueva_tarjeta)<16 or nueva_tarjeta in tarjetas:
                    print ("Ingreso mal los datos de la nueva tarjeta o ya se encuentra en el sistema")
                    nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
                if len(nueva_tarjeta) == 16 and nueva_tarjeta not in tarjetas: #Si no hay porblemas la tarjeta se agrega al sist
                    tarjetas.append(nueva_tarjeta)
                    saldos.append(0.00)
    
    elif opc == "2":#Asignar saldo para tarjetas recientemente agregadas
        if nueva_tarjeta == 0.00: #Si no se agregaron tarjetas nuevas no permite colocar saldos nuevos
            print("No hay nuevas tarjetas registradas")
        else:
            for i in range(num_nuevas_tarj): #Permite al usuario igresar los saldos en orden
                nuevo_sueldo = float(input("Ingrese el sueldo de las nuevas tarjetas en orden"))
                saldos.append(nuevo_sueldo)
    
    elif opc == "3": # Ver tarjetas registradas y sus saldos
        for i in range(len(tarjetas)):
            print(f"Tarjetas: {tarjetas[i]} -Saldo: {saldos[i]}")
    
    elif opc == "4":#Consultar el saldo de una tarjeta en especifico
        consulta_tarjeta = input("Ingrese el numero de la tarjeta de la cual desea consultar el saldo ")
        #El bucle se ejecuta cuando el formato de la tarjeta a registrar no es el correcto o cuando la tarjeta en cuestion ya esta en el sistema
        while not consulta_tarjeta.isnumeric() or len(consulta_tarjeta)>16 or len(consulta_tarjeta)<16 or consulta_tarjeta not in tarjetas:
            print ("Ingreso mal los datos de la tarjeta")
            nueva_consulta = input("IIngrese el numero de la tarjeta de la cual desea consultar el saldo ")
        if consulta_tarjeta in tarjetas:
            idx = tarjetas.index(consulta_tarjeta)
            print(f"Tarjeta: {tarjetas[idx]}")
            print(f"El saldo es de ${saldos[idx]}")
    elif opc == "5": #Mostrar saldos negativos
        saldo_negativos = []
        for i in range(len(tarjetas)):
            if saldos[i] <= 0.00:
                saldo_negativos.append(tarjetas[i])
        print("A continuacion, las tarjetas con saldo cero o negativo")
        print(saldo_negativos)
    elif opc =="6":
        nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
        #El bucle se ejecuta cuando el formato de la tarjeta a registrar no es el correcto o cuando la tarjeta en cuestion ya esta en el sistema
        while not nueva_tarjeta.isnumeric() or len(nueva_tarjeta)>16 or len(nueva_tarjeta)<16 or nueva_tarjeta in tarjetas:
            print ("Ingreso mal los datos de la nueva tarjeta o ya se encuentra en el sistema")
            nueva_tarjeta = input("Ingrese los datos de la nueva tarjeta: (Debe ser un numero de 16 dígitos)")
        if len(nueva_tarjeta) == 16 and nueva_tarjeta not in tarjetas: #Si no hay porblemas la tarjeta se agrega al sist
            tarjetas.append(nueva_tarjeta)
            saldos.append(float(input("Cuál es el saldo de la tarjeta ingresada?")))
    elif opc == "7":
        valor_min = -500.00
        #Preguntamos a que tarjeta desea acceder el usuario
        consulta_tarjeta = input("Ingrese el numero de la tarjeta a la cual desea debitar o cargar saldo ")
        while not consulta_tarjeta.isnumeric() or len(consulta_tarjeta)>16 or len(consulta_tarjeta)<16 or consulta_tarjeta not in tarjetas:
            print ("Ingreso mal los datos de la tarjeta")
            nueva_consulta = input("Ingrese nuevamente el numero de la tarjeta ")
        if consulta_tarjeta in tarjetas:
            idx = tarjetas.index(consulta_tarjeta)
            #Le preguntamos al usuario que operacion desea realizar
            cargar_debitar = input("Que desea hacer? 1) Debitar saldo 2) Cargar saldo  ")
            while not cargar_debitar.isnumeric():
                cargar_debitar = input("Eliga una opción válida: ")
            if cargar_debitar == "1":#Debitar
                debito = float(input("Ingrese cuanto desea debitar de su saldo: (Su tarjeta puede quedar con un saldo minimo de $ -500.00) "))
                aux_debito = saldos[idx] - debito
                if aux_debito < -500.00:
                    print("El saldo final seria menor que el minimo establecido, la operacion queda cancelada")
                elif aux_debito >= -500.00:
                    saldos[idx] = aux_debito
                    print("El nuevo saldo es de $",saldos[idx])
            elif cargar_debitar == "2":
                carga = float(input("Ingrese cuanto desea cargar a su saldo: "))
                saldos[idx] += carga
                print("Su nuevo saldo es de $",saldos[idx])

                
            

    elif opc == "8":
        print("Desea salir?")
        aux_salir = input("Si / No ").upper()
        if aux_salir == "SI":
            salir = True

        
