especialidades = ["Cardiología", "Dermatología", "Pediatría","Psicología"]
cupos = [5, 3, 10,0]

salir = False
while not salir:
    opcion = input("Ingrese que desea hacer:\n 1)Ingresar especialidad \n 2)Ingresar cupos disponibles para una especialidad específica \n 3)Mostrar agenda \n 4)Consultar los cupos disponibles en una especialidad específica \n 5)Mostrar especialidades sin cupos disponibles \n 6) Agregar nueva especialidad y el numero de cupos disponibles para la misma  \n 7)Actualizar cupos (Reservar/Cancelar) \n 8)Ver agenda completa \n 9)Salir \n ")
    while not opcion.isnumeric():
        opcion = input("Ingrese que desea hacer:\n 1)Ingresar especialidad \n 2)Ingresar cupos disponibles para una especialidad específica \n 3)Mostrar agenda \n 4)Consultar los cupos disponibles en una especialidad específica \n 5)Mostrar especialidades sin cupos disponibles \n 6) Agregar nueva especialidad y el numero de cupos disponibles para la misma  \n 7)Actualizar cupos (Reservar/Cancelar) \n 8)Ver agenda completa \n 9)Salir \n ")
    #Ingreso de nueva especialidad
    if opcion == "1":
        cant_nuevas_espe = int(input("Cuantas especialidades desea agregar? "))
        for j in range(cant_nuevas_espe):
            nueva_espe = input("Ingrese una nueva especialidad ").lower().capitalize()
            while nueva_espe in especialidades:
                print("La especialidad ingreada ya esta dentro del sistema")
                nueva_espe = input("Ingrese una nueva especialidad ").lower().capitalize()
            if nueva_espe not in especialidades:
                especialidades.append(nueva_espe)
                cupos.append(0)
            for i in range(len(cupos)):
                print (f"Especialidad: {especialidades[i]} Cupos: {cupos[i]} ")
    #Ingresar cupos disponibles por especialidad
    if opcion == "2":
        for i in range(len(especialidades)):
            print(f"Especialidad: {especialidades[i]} Cupos: {cupos[i]}")
            if cupos[i] != 0:
                print("Esta especialidad ya cuenta con una cantidad de cupos especificada")
            elif cupos[i] == 0:
                cupos[i] = int(input(f"Ingrese la cantidad de cupos disponibles para la especialidad {especialidades[i]}: "))    
    #Mostrar agenda
    if opcion == "3":
        print("Le mostraremos nuestra agenda")
        for i in range(len(especialidades)):
            print(f"Especialidad: {especialidades[i]} Cupos: {cupos[i]}")
    #Consultar cupos especialidad especifica
    if opcion == "4":
        cupos_espe = input("De que especialidad desea chequear disponibilidad ").lower().capitalize()
        while cupos_espe not in especialidades:
            print("No contamos con esa especialidad en este establecimiento")
            print("Le mostraremos nuestras especialidades a continuacion")
            for i in range(len(especialidades)):
                print(especialidades[i])
            cupos_espe = input("Ingrese una de las especialidades mostradas anteriormente ").lower().capitalize()
        if cupos_espe in especialidades:
            index = especialidades.index(cupos_espe)
            print(f"La cantidad de cupos disponibles para {cupos_espe} es de {cupos[index]}")
    #Mostrar todas las especialidades sin cupos disponibles
    if opcion == "5":
        espe_sin_cupos=[]
        for i in range(len(especialidades)):
            if cupos[i] == 0:
                espe_sin_cupos.append(especialidades[i])
        print("Las especialidades sin cupo disponibles son: ")
        for i in espe_sin_cupos:
            print(i)
    #Agregar nueva especialidad y sus cupos
    if opcion == "6":
        nueva_espe = input("Ingrese una nueva especialidad ").lower().capitalize()
        while nueva_espe in especialidades:
                print("La especialidad ingreada ya esta dentro del sistema")
                nueva_espe = input("Ingrese una nueva especialidad ").lower().capitalize()
        if nueva_espe not in especialidades:
            especialidades.append(nueva_espe)
            nueva_cupos = int(input("Cuantos cupos tiene esta especialdad? "))
            cupos.append(nueva_cupos)
            for i in range(len(especialidades)):
                print (f"{especialidades[i]} Cupos: {cupos[i]}")
    #
    #Salir del menu
    if opcion == "10":
        salir_aux = input("Desea salir? \n SI / NO ").upper()
        if salir_aux == "SI":
            salir = True