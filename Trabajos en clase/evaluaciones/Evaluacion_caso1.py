titulos = ["El señor de los anillos", "Orgullo y prejuicio","La divina comedia"]
ejemplares = [3,5,9]
salir = False

while not salir:
    opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo ")
    while not opcion.isnumeric():
        opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo ")
    if opcion == "1":
        nuevo_titulo = input("Ingrese un nuevo titulo para agregar a la biblioteca ").lower().capitalize()
        titulos.append(nuevo_titulo.title())
        ejemplares.append(0)
        for i in range(len(titulos)):
            print(titulos[i],":",ejemplares[i])
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
    elif opcion == "3":
        catalogo_con_copias = []
        for 
        
    
    
    
    
    
    break
print("Fuera del ciclo")