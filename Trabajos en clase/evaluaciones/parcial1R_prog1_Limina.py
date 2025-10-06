herramientas = ["Destornillador","Taladro","Martillo"]
existencias = [0,3,9]
salir = False
while not salir:
    opc = input("Ingrese una opción:\n 1)Ingresar herramientas\n 2)Ingresar existencias de herramientas\n 3)Mostrar existencias\n 4)Consultar disponibilidad\n 5)Listar agotados\n 6)Agregar herramienta y su existencia disponible \n 7)Actualizar existencia(venta/ingreso)\n 8)Salir\n ")
    while not opc.isnumeric():
        print("Opción inválida")
        opc = input("Ingrese una opción:\n 1)Ingresar herramientas\n 2)Ingresar existencias de herramientas\n 3)Mostrar existencias\n 4)Consultar disponibilidad\n 5)Listar agotados\n 6)Agregar herramienta y su existencia disponible \n 7)Actualizar existencia(venta/ingreso)\n 8)Salir\n ")
    if opc == "1":
        cant_nueva_herramienta = int(input("Cuantas herramientas nuevas desea ingresar? "))
        for i in range (cant_nueva_herramienta):
            nueva_herramienta = input("Ingrese la nueva herramienta ").strip().capitalize()
            while nueva_herramienta == "":
                print("Ingreso inválido, no puede dejarlo vacio")
                nueva_herramienta = input("Ingrese la nueva herramienta").strip().capitalize()
            if nueva_herramienta in herramientas:
                print("Esa herramienta ya se encuentra en el sistema")
            elif nueva_herramienta not in herramientas:
                herramientas.append(nueva_herramienta)
                existencias.append(0)
    elif opc == "2":
        if len(herramientas) == 0:
            print("No hay herramientas en el sistema")
        else:
            for i in range(len(herramientas)):
                aux_opc2 = input(f"Desea cambiar la cantidad de existencias de {herramientas[i]}? S/N ").upper()
                if aux_opc2 == "S":
                    print("Ingrese la nueva cantidad de existencias...")
                    existencias[i] = int(input())
                    while existencias[i] < 0:
                        print("Debe ingresar un número mayor o igual a cero")
                        existencias[i] = int(input())
                elif aux_opc2 == "N":
                    continue
    elif opc == "3":
        if len(herramientas) == 0:
            print("No hay herramientas en el sistema")
        else:
            for i in range(len(herramientas)):
                print(f"Herramienta: {herramientas[i]} -Existencias: {existencias[i]}")
    elif opc == "4":
        if len(herramientas) == 0:
            print("No hay herramientas en el sistema")
        else:
            consultar = input("Que herramienta desea consultar su disponibilidad? ").strip().capitalize()
            if consultar not in herramientas:
                print("La herramienta solicitada no se encuentra dentro del sistema ")
            elif consultar in herramientas:
                idx = herramientas.index(consultar)
                print(f"La herramienta {herramientas[idx]} cuenta con {existencias[idx]} existencias")
    elif opc == "5":
        if len(herramientas) == 0:
            print("No hay herramientas en el sistema")
        else:
            agotados = []
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    agotados.append(herramientas[i])
            print("La lista de herramientas sin existencias disponibles es: ")
            for i in range(len(agotados)):
                print(f"-{agotados[i]}")
    elif opc == "6":
        nueva_herramienta = input("Ingrese la nueva herramienta ").strip().capitalize()
        while nueva_herramienta == "":
                print("Ingreso inválido, no puede dejarlo vacio")
                nueva_herramienta = input("Ingrese la nueva herramienta").strip().capitalize()
        if nueva_herramienta in herramientas:
            print("Esa herramienta ya se encuentra en el sistema")
        elif nueva_herramienta not in herramientas:
            herramientas.append(nueva_herramienta)
            aux_6_idx = herramientas.index(nueva_herramienta)
            existencias.append(int(input(f"Ingrese la cantidad de existencias de {nueva_herramienta}")))
            while existencias[aux_6_idx] < 0:
                        print("Debe ingresar un número mayor o igual a cero")
                        existencias[aux_6_idx] = int(input())
    elif opc == "7":
        if len(herramientas) == 0:
            print("No hay herramientas en el sistema")
        else:
            vender_ingresar = input("Que desea hacer?\n 1)Venta de una herramienta 2)Ingreso de nuevas existencias ")
            while not vender_ingresar.isnumeric():
                print("Ingrese una opción válida")
                vender_ingresar = input("Que desea hacer?\n 1)Venta de una herramienta 2)Ingreso de nuevas existencias ")
            if vender_ingresar == "1":#Venta de herramienta
                aux_venta = input("Que herramienta vendio? ").strip().capitalize()
                if aux_venta not in herramientas:
                    print("Esa herramienta no se encuentra en el sistema")
                elif aux_venta in herramientas:
                    idx_venta = herramientas.index(aux_venta)
                    if existencias[idx_venta] == 0:
                        print("No se puede vender mas existencias de esta herramienta")
                    else:
                        existencias[idx_venta] -= 1
            elif vender_ingresar == "2":
                aux_ingresar = input("De que herramienta desea ingresar existencias? ").strip().capitalize()
                if aux_ingresar not in herramientas:
                    print("Esa herramienta no se encuentra en el sistema")
                elif aux_ingresar in herramientas:
                    idx_ingresar = herramientas.index(aux_ingresar)
                    existencias[idx_ingresar] += 1
    elif opc == "8":
        print("Desea salir? S/N ")
        aux_salir = input().upper()
        if aux_salir == "S":
            salir=True
print("Gracias por elegirnos!")