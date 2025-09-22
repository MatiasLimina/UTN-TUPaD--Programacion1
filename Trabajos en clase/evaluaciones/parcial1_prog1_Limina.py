#Matias Limina
títulos = ["Cualquiera", "Oracion", "Papa", "Pepito", "Argentina", "178"]
ejemplares = [5, 3, 7, 0, 0, 73]
salir = False
cant_titulos = 0
while not salir:
    print("MENU")
    print("1) Ingresar titulos")
    print("2) Ingresar ejemplares")
    print("3) Mostrar catálogo")
    print("4) Consultar disponibiblidad")
    print("5) Listar agotados")
    print("6) Agregar titulos y su cantidad de ejemplares")
    print("7) Actualizar ejemplares (Prestamos/devolución)")
    print("8) Salir")
    opc = input("... ")

    while not opc.isnumeric():
        print("Ingrese una opcion válida")
        opc = input("... ")
    if opc == "1":
        cant_titulos = int(input("Cuantos titulos desea agregar? "))
        for i in range(cant_titulos):
            nuevo_titulo = input("Ingrese un nuevo titulo ").strip().lower().capitalize()
            while nuevo_titulo in títulos:
                print("El titulo ingresado ya se encuentra en el sistema")
                nuevo_titulo = input("Ingrese un nuevo titulo (Para volver a menu no ingrese nada)").strip().lower().capitalize()
                if nuevo_titulo == "":
                    break
            if nuevo_titulo not in títulos and nuevo_titulo != "":
                títulos.append(nuevo_titulo)
    elif opc == "2":
        if cant_titulos == 0:
            print("Usted no ingreso nuevos titulos al sistema")
        else:
            print("Ingrese en orden la cantidad de ejemplares de los libros ingresados")
            for i in range(cant_titulos):
                ejemplares.append(input(f"Ejemplares del libro {i+1}: "))
    elif opc == "3":
        for i in range(len(títulos)):
            print(f"-Libro: {títulos[i]} -Ejemplares: {ejemplares[i]}")
    elif opc == "4":
        disponibilidad = input("De que libro desea consultar disponibilidad? ").strip().lower().capitalize()
        if disponibilidad not in títulos:
            print("Usted ingreso un libro que no se encuentra en nuestro sistema")
        elif disponibilidad in títulos:
            idx = títulos.index(disponibilidad)
            print(f"El libro {títulos[idx]} cuenta con {ejemplares[idx]} copias...")
    elif opc == "5":
        sin_copias = []
        for i in range(len(títulos)):
            if ejemplares[i] == 0:
                sin_copias.append(títulos[i])
        print("Lista de libros sin ejemplares disponibles: ")
        for i in range(len(sin_copias)):
            print(f"Libro: {sin_copias[i]}")
    elif opc == "6":
        nuevo_titulo = input("Ingrese un nuevo título: ").strip().lower().capitalize()
        if nuevo_titulo in títulos:
            print("El libro ingresado ya se encuentra en nuestro catálogo")
        elif nuevo_titulo not  in títulos and nuevo_titulo != "":
            títulos.append(nuevo_titulo)
            ejemplares.append(int(input(f"Cuantas copias tiene de {nuevo_titulo} ")))
    elif opc == "7":
        aux_titulo = input("Que titulo desea devolver o pedir prestado? ").strip().lower().capitalize()
        if aux_titulo not in títulos:
            print("El libro no se encuentra en nuestro sistema")
        elif aux_titulo in títulos:
            prestar_devolver = input("Que desea hacer? 1)Pedir prestado  2) Devolver un ejemplar ")
            while not prestar_devolver.isnumeric():
                print("Ingreso una opcion inválida")
                prestar_devolver = input("Que desea hacer? 1)Pedir prestado  2) Devolver un ejemplar ")
            if prestar_devolver == "1":#Prestado
                idx = títulos.index(aux_titulo)
                print(f"Usted pedira prestado una copia de {aux_titulo}")
                ejemplares[idx] -= 1
            elif prestar_devolver == "2":#Devolver
                idx = títulos.index(aux_titulo)
                print(f"Usted devolvera una copia de {aux_titulo}")
                ejemplares[idx] += 1
    elif opc == "8":
        print("Desea salir?")
        aux_salir=input("Si / No ").lower().strip()
        if aux_salir == "si":
            salir = True
print("Gracias por elegirnos!")