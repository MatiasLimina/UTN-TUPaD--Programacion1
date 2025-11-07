import csv
import os
ruta_absoluta = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(ruta_absoluta,"biblioteca.csv")
ENCABEZADOS = ["titulo","cantidad"]
def crear_archivo():
    if not os.path.exists(RUTA_ARCHIVO):
        try:
            with open(RUTA_ARCHIVO,"w",newline="") as archivo:
                escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
                escritor.writeheader()
        except IOError:
            print("ERROR al intentar crear el archivo")

def leer_archivo():
    crear_archivo()
    try:
        with open(RUTA_ARCHIVO,"r",newline="",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,fieldnames=ENCABEZADOS)
            lista = []
            next(lector)
            for linea in lector:
                linea=validar_linea(linea)
                if linea is False:
                    print("La linea sera ignorada")
                else:
                    lista.append(linea)
            return lista
    except IOError:
        print("ERROR al leer el archivo")

def validar_duplicado(nombre,biblioteca):
    if any(t["titulo"] == nombre for t in biblioteca):
        print("Este titulo ya se encuentra en el sistema")
        return False
    else:
        return nombre

def validar_linea(linea):
    for campo in linea:
        if linea[campo] == "":
            print("ERROR: no pueden haber campos vacios")
            return False
    
    try:
        linea["cantidad"] = int(linea["cantidad"])
    except ValueError:
        print("ERROR: la cantidad debe ser un numero entero")
        return False
    return linea

def modificar_archivo(biblioteca):
    try:
        with open(RUTA_ARCHIVO,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
            escritor.writeheader()
            escritor.writerows(biblioteca)
    except IOError:
        print("ERROR al acceder al archivo")

def ingresar_titulos(biblioteca):
    
    while True:
        try:
            cantidad_agregar = int(input("Ingrese la cantidad de titulos que desea agregar "))
            break
        except ValueError:
            print("Debe ingresar un numero entero")
    for i in range (cantidad_agregar):
        nombre = input("Ingrese el nombre del libro a agregar ").strip().lower()
        nombre=validar_duplicado(nombre,biblioteca)
        if nombre is False:
            print("Este ingreso sera ignorado por que ya se encuentra en el sistema")
        else:
            cantidad = 0
            nueva_linea = {"titulo":nombre,"cantidad":cantidad}
            linea_verificada = validar_linea(nueva_linea)
            if linea_verificada is False:
                print("ERROR DE VERIFICACION: el nuevo ingreso sera ignorado")
            else:
                biblioteca.append(linea_verificada)
                modificar_archivo(biblioteca)
                print(f"Ingreso nuevo correcto")

def ingresar_ejemplares(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        for titulo in biblioteca:
            print(f"Titulo: {titulo["titulo"]} Cantidad: {titulo["cantidad"]}")
            while True:
                try:
                    cantidad_nueva = int(input("Ingrese la cantidad de ejemplares que desea añadir... "))
                    if cantidad_nueva < 0:
                        print("Debe ingresar un numero positivo")
                    else:
                        break
                except ValueError:
                    print("Debe ingresar un numero entero")
            titulo["cantidad"] += cantidad_nueva
            print("Valor actualizado con exito")
        modificar_archivo(biblioteca)

def mostrar_catalogo(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        for i in biblioteca:
            print(f"Titulo: {i["titulo"]} / Cantidad: {i["cantidad"]}")

def consultar_disponibilidad(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        libro_consulta = input("Ingrese el titulo que desea chequear disponibilidad ").strip().lower()
        encontrado = False
        for t in biblioteca:
            if t["titulo"] == libro_consulta:
                print("Libro encontrado!")
                encontrado = True
                print(f"{t["titulo"]} tiene {t["cantidad"]} ejemplares disponibles")
        if encontrado is False:
            print("El titulo no se encontro en el catalogo")

def listar_agotados(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        lista_agotados=[]
        for t in biblioteca:
            if t["cantidad"] == 0:
                lista_agotados.append(t)
        if not lista_agotados:
            print("No hay libros agotados")
        else:
            print("Titulos agotados:")
            mostrar_catalogo(lista_agotados)

def agregar_titulo_nuevo(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        nombre = input("Ingrese el nuevo nombre: ").strip().lower()
        nombre = validar_duplicado(nombre,biblioteca)
        if nombre is False:
            print("Este ingreso sera ignorado por que ya se encuentra en el sistema")
        else:
            cantidad = input("Ingrese la cantidad de ejemplares: ")
            nuevo = {"titulo":nombre,"cantidad":cantidad}
            nuevo = validar_linea(nuevo)
            if nuevo is False:
                print("Ingreso cancelado")
            else:
                biblioteca.append(nuevo)
                modificar_archivo(biblioteca)

def venta_devolucion(biblioteca):
    if not biblioteca:
        print("No hay titulos en el catalogo")
    else:
        salir = False
        while not salir:
            print("Que desea hacer?")
            print("Presione ¨V¨ para Vender")
            print("Presione ¨D¨ para Devolver")
            print("Presione ¨S¨ para Salir")
            opc = input("Elija una opcion... ").strip().lower()
            match opc:
                case "v": #Venta
                    print("Usted va a vender un ejemplar, le mostraremos la lista...")
                    mostrar_catalogo(biblioteca)
                    venta = input("Que libro desea vender?").strip().lower()
                    encontrado = False
                    for t in biblioteca:
                        if t["titulo"] == venta:
                            encontrado = True
                            print("Libro encontrado!")
                            print(f"Titulo: {t["titulo"]} / Cantidad: {t["cantidad"]}")
                            while True:
                                try:#CUantos libros seran vendidos
                                    cantidad_venta=int(input("Ingrese la cantidad que desea vender"))
                                    if cantidad_venta < 0:
                                        print("Debe ingresar un numero positivo")
                                    else:
                                        break
                                except ValueError:
                                    print("Debe ingresar un numero entero")
                            if cantidad_venta > t["cantidad"]:#Si la cantidad q se quieren vender es mayor a la existente
                                print("Operacion cancelada, no hay ejemplares suficientes")
                            elif t["cantidad"] == 0:#Si la cantidad en el sistema es cero
                                print("Operacion cancelada, no hay ejemplares suficientes")
                            elif cantidad_venta <= t["cantidad"]:
                                t["cantidad"]-=cantidad_venta
                                modificar_archivo(biblioteca)
                                print("Valor actualizado:")
                                print(f"Titulo: {t["titulo"]} / Cantidad: {t["cantidad"]}")
                    if encontrado is False:
                        print("Libro no encontrado")
                case "d":
                    print("Usted va a devolver un ejemplar, le mostraremos la lista...")
                    mostrar_catalogo(biblioteca)
                    devolucion = input("Que libro desea devolver?").strip().lower()
                    encontrado=False
                    for t in biblioteca:
                        if t["titulo"] == devolucion:
                            print("Libro encontrado!")
                            print(f"Titulo: {t["titulo"]} / Cantidad: {t["cantidad"]}")
                            encontrado=True
                            while True:
                                try:
                                    cantidad_devolucion=int(input("Ingrese la cantidad que desea devolver"))
                                    if cantidad_devolucion < 0:
                                        print("Debe ingresar un numero positivo")
                                    else:
                                        break
                                except ValueError:
                                    print("Debe ingresar un numero entero")
                            t["cantidad"] += cantidad_devolucion
                            print("Valor actualizado:")
                            print(f"Titulo: {t["titulo"]} / Cantidad: {t["cantidad"]}")
                            modificar_archivo(biblioteca)
                    if encontrado is False:
                        print("Ese libro no esta en el catalogo")
                case "s":
                    salir=True
                case _:
                    print("Opcion invalida")



def main():
    biblioteca = leer_archivo()
    print(biblioteca)
    salir = False
    while not salir:
        print("Bienvenido:")
        print("MENU")
        print("1) Ingresar titulos")
        print("2) Ingresar ejemplares")
        print("3) Mostrar catalogo")
        print("4) Consultar disponibilidad")
        print("5) Listar agotados")
        print("6) Agregar un titulo nuevo")
        print("7) Actualizar ejemplares (prestamo/devolucion)")
        print("8) Salir")
        opc = input("Eliga una opcion: ").strip()
        match opc:
            case "1":
                #Ingresar titulo con cantidad 0
                ingresar_titulos(biblioteca)
            case "2":
                #Ingresar ejemplares accede al titulo y modificas la cantidad
                ingresar_ejemplares(biblioteca)
            case "3":
                #Mostrar catalogo
                mostrar_catalogo(biblioteca)
            case "4":
                #Consutlar disponibilidad
                consultar_disponibilidad(biblioteca)
            case "5":
                #Listar agotados
                listar_agotados(biblioteca)
            case "6":
                #Agregar titulo
                agregar_titulo_nuevo(biblioteca)
            case "7":
                #Actualizar ejemplares venta/devolucion
                venta_devolucion(biblioteca)
            case "8":
                #Salir
                print("Vuelva pronto!")
                salir = True
            case _:
                print("Opcion inválida")

main()