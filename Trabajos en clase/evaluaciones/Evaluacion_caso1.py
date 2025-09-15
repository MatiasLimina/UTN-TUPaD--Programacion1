titulos = ["El señor de los anillos", "Orgullo y prejuicio","La divina comedia","Pepe aventuras"]
ejemplares = [3,5,9,0]
salir = False

while not salir:
    opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo \n  ")
    while not opcion.isnumeric():
        opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo \n  ")
    #Ingreso de nuevos titulos al catalogo general
    if opcion == "1":
        nuevo_titulo = input("Ingrese un nuevo titulo para agregar a la biblioteca ").lower().capitalize()
        titulos.append(nuevo_titulo.title())
        ejemplares.append(0)
        for i in range(len(titulos)):
            print(titulos[i],":",ejemplares[i])
    #Ingrese de numero de copias discponibles a un titulo en especifico
    elif opcion == "2":
        buscar_titulo = input("Ingrese el nombre del titulo al cual quiere actualizar su numero de copias ").capitalize()
        while buscar_titulo not in titulos:
            print("El titulo ingresado no esta en el catálogo...")
            salir_pregunta = input("Si quiere salir ingrese s Si quiere continuar presione cualquier otra tecla ").lower()
            if salir_pregunta == "s":
                break
            buscar_titulo = input("Ingrese el nombre del titulo al cual quiere actualizar su numero de copias ").capitalize()
        if buscar_titulo in titulos:
            indice_tit_buscado = titulos.index(buscar_titulo)
            ejemplares[indice_tit_buscado] = input(f"Ingrese la cantidad de ejemplares del libro {titulos[indice_tit_buscado] }")
    #Catálogo de titulos con copias disponibles
    elif opcion == "3":
        catalogo_con_copias = []
        for i in range (len(titulos)):
            if ejemplares[i] > 0:
                catalogo_con_copias.append(titulos[i])
        print(f"Los titulos con copias disponibles son: {catalogo_con_copias}")
    #Buscar la cantidad de ejemplares de un titulo puntual
    elif opcion == "4":
        disp_titulo = input("Ingrese el titulo del que desea saber la cantidad de copias disponibles ").lower().capitalize()
        while disp_titulo not in titulos:
            print("El titulo ingresado no esta en el catálogo...")
            salir_pregunta = input("Si quiere salir ingrese s Si quiere continuar presione cualquier otra tecla ").lower()
            if salir_pregunta == "s":
                break
            disp_titulo = input("Ingrese el titulo del que desea saber la cantidad de copias disponibles ").lower().capitalize()
        if disp_titulo in titulos:
            indice_tit_buscado = titulos.index(disp_titulo)
            print(f"El titulo {titulos[indice_tit_buscado]} tiene una cantidad de {ejemplares[indice_tit_buscado]} copias")
    #Mostrar ejemplares sin copias
    elif opcion == "5":
        catálogo_sin_copias =[]
        for i in range (len(titulos)):
            if ejemplares[i] == 0:
                catálogo_sin_copias.append(titulos[i])
        print(f"Los titulos sin copias disponibles son: {catálogo_sin_copias}")
    #Agregar nuevo titulo y sus copias disponibles 
    elif opcion == "6":
        nuevo_tit = input("Ingrese un nuevo titulo: ").lower().capitalize()
        copias_nuevo_tit = int(input("Ingrese la cantidad de copias del titulo nuevo "))
        titulos.append(nuevo_tit)
        ejemplares.append(copias_nuevo_tit)
        print(f"El nuevo titulo agregado es {nuevo_tit}, con una cantidad de {copias_nuevo_tit} copias")
    #Actualizar prestamos y devoluciones
    elif opcion == "7":
        actu = input("Desea devolver un libro o pedir prestado un libro? \n 1) Pedir prestado 2) Devolver un ejemplar")
        if actu == "1":
            prestado = input("Que libro desea pedir prestado? ").lower().capitalize()
            while prestado not in titulos:
                print("El titulo ingresado no se encuentra enel catálogo")
                prestado = input("Que libro desea pedir prestado? ").lower().capitalize()
            if prestado in titulos:
                indice_prestado = titulos.index(prestado)
                print(f"Usted va a pedir prestado el libro {titulos[indice_prestado]}")
                if ejemplares[indice_prestado] == 0:
                    print("No quedan copias disponibles de este libro")
                else:
                    print(f"El libro {titulos[indice_prestado]} posee {ejemplares[indice_prestado]} copias")
                    ejemplares[indice_prestado] -= 1
                    print (f"Quedan {ejemplares[indice_prestado]} del libro que usted pidio prestado")

    
    
    break
print("Fuera del ciclo")


