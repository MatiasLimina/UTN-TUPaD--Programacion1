especialidades = ["Cardiología", "Dermatología", "Pediatría"]
cupos = [5, 3, 10]

salir = False
while not salir:
    opcion = input("Ingrese que desea hacer: 1)Ingresar especialidad \n 2)Ingresar cupos disponibles para una especialidad específica \n 3)Mostrar agenda \n 4)Consultar los cupos disponibles en una especialidad específica \n 5)Mostrar especialidades sin cupos disponibles \n 6) Agregar nueva especialidad y el numero de cupos disponibles para la misma \n 7)Ver las especialidades sin cupos disponibles \n 8)Actualizar cupos (Reservar/Cancelar) \n 9)Ver agenda completa \n 10)Salir \n ")
    while not opcion.isnumeric():
        opcion = input("Ingrese que desea hacer: 1)Ingresar especialidad \n 2)Ingresar cupos disponibles para una especialidad específica \n 3)Mostrar agenda \n 4)Consultar los cupos disponibles en una especialidad específica \n 5)Mostrar especialidades sin cupos disponibles \n 6) Agregar nueva especialidad y el numero de cupos disponibles para la misma \n 7)Ver las especialidades sin cupos disponibles \n 8)Actualizar cupos (Reservar/Cancelar) \n 9)Ver agenda completa \n 10)Salir \n ")
    #Ingreso de nueva especialidad
    if opcion == "1":
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
    
    
    
    if opcion == "10":
        salir_aux = input("Desea salir? \n SI / NO ").upper()
        if salir_aux == "SI":
            salir = True