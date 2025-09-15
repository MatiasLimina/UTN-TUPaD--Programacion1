titulos = ["El señor de los anillos", "Orgullo y prejuicio","La divina comedia"]
ejemplares = [3,5,9]
salir = False

while not salir:
    opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo ")
    while not opcion.isnumeric():
        opcion = input("Que desea hacer: 1) Ingresar nuevos titulos al caralogo \n 2) Ingresar el numero de copias disponibles de un titulo \n 3) Mostrar el catálogo con copias disponibles \n 4) Buscar la disponibilidad de un titulo especifico \n 5) Mostrar ejemplares que sin copias disponibles \n 6) Agregar un titulo nuevo y sus copias disponibles \n 7) Actualizar ejemplares (prestamo/devolución) \n 8) Ver catálogo ")
    if opcion == "1":
        nuevo_titulo = input("Ingrese un nuevo titulo para agregar a la biblioteca ").title()
        while not nuevo_titulo.isalpha():
            nuevo_titulo = input("Ingrese un nuevo titulo para agregar a la biblioteca ").title()
        titulos.append(nuevo_titulo.title())
        ejemplares.append(0)
        for i in range(len(titulos)):
            print(titulos[i],":",ejemplares[i])
    
    
    
    
    break
print("Fuera del ciclo")