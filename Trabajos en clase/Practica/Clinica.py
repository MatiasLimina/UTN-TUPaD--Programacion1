import csv, os
ruta_absoluta = os.path.dirname(os.path.abspath(__file__))
RUTA_ARCHIVO = os.path.join(ruta_absoluta,"clinica.csv")
ENCABEZADOS = ["especialidad","turnos"]
def crear_archivo():
    if not os.path.exists(RUTA_ARCHIVO):
        try:
            with open(RUTA_ARCHIVO,"w",newline="",encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
                escritor.writeheader()
        except IOError:
            print("ERROR: No se pudo crear el archivo")

def leer_archivo():
    crear_archivo()
    try:
        with open(RUTA_ARCHIVO,"r",newline="",encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,fieldnames=ENCABEZADOS)
            clinica = []
            #next(lector)
            for linea in lector:
                linea = verificar_linea(linea)
                if linea is False:
                    print("Linea ignorada")
                else:
                    clinica.append(linea)
            if not clinica:
                print("No hay especialidades registradas")
                return clinica
            else:
                return clinica
    except IOError:
        print("ERROR: No se pude acceder al archivo")

def verificar_linea(linea):
    for campo in linea:
        if linea[campo] == "":
            print("ERROR: No pueden haber campos vacios")
            return False
    try:
        linea["turnos"] = int(linea["turnos"])
    except ValueError:
        print("El valor en ¨turnos¨ debe ser un numero entero")
        return False
    return linea

def verificar_duplicados(nombre,clinica):
    if any(n["especialidad"]==nombre for n in clinica):
        return False
    else:
        return nombre

def modificar_archivo(clinica):
    try:
        with open(RUTA_ARCHIVO,"w",newline="",encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
            escritor.writeheader()
            escritor.writerows(clinica)
    except IOError:
        print("ERROR al modificar el archivo")

def ingreso_especialidad(clinica):
    while True:
        try:
            cant_ingresos = int(input("Ingrese la cantidad de especialidades a agregar: "))
            if cant_ingresos < 0:
                print("Debe ingresar un numero positivo")
            else:
                break
        except ValueError:
            print("ERROR: debe ingresar un numero entero")
    especialidad = input("Ingrese el nombre de la especialidad: ").lower().strip()
    especialidad = verificar_duplicados(especialidad,clinica)
    print(especialidad)
    if especialidad is False:
        print("Esa especialidad ya se encuentra registrada")
        print("El ingreso sera ignorado")
    else:
        turnos = 0
        nuevo_ingreso = {"especialidad":especialidad,"turnos":turnos}
        nuevo_ingreso = verificar_linea(nuevo_ingreso)
        if nuevo_ingreso is False:
            print("El ingreso sera ignorado")
        else:
            print("Ingreso exitoso!")
            clinica.append(nuevo_ingreso)
            modificar_archivo(clinica)

def ingresar_turnos(clinica):
    for e in clinica:
        print(f"Actualizara los turnos de {e["especialidad"]} que cuenta con {e["turnos"]}")
        while True:
            try:
                cant_turnos = int(input("Ingrese la cantidad de turnos que quiere agregar: "))
                if cant_turnos < 0:
                    print("ERROR: Debe ingresar un numero positivo")
                else:
                    break
            except ValueError:
                print("ERROR: Ingrese un numero entero")
        e["turnos"] += cant_turnos
        modificar_archivo(clinica)
        print("Turnos actualizados con exito!")

def mostrar_especialidades(clinica):
    print("---------------------")
    for i in clinica:
        print(f"Especialidad: {i["especialidad"]}/ Turnos: {i["turnos"]}")
    print("---------------------")

def consultar_disponibilidad(clinica):
    print("Consulta de disponibilidad")
    consulta = input("Ingrese la especialidad: ").lower().strip()
    encontrado = False
    for i in clinica:
        if consulta == i["especialidad"]:
            encontrado = True
            print(f"Especialidad: {i["especialidad"]}/ Turnos: {i["turnos"]}")
    if encontrado == False:
        print(f"La especialidad {consulta} no se encuentra en el sistema ")

def listar_agotados(clinica):
    agotados = []
    print("Especialidades con turnos agotados")
    for i in clinica:
        if i["turnos"] == 0:
            agotados.append(i)
    mostrar_especialidades(agotados)

def agregar_especialidad (clinica):
    nuevo = input("Ingrese el nombre de la especialidad ").strip().lower()
    nuevo = verificar_duplicados(nuevo)
    if nuevo is False:
        print("Esa especialidad ya se encuentra registrada")
        print("El ingreso sera ignorado")
    else:
        while True:
            try:
                n_turno = int(input("Ingrese la cantidad de turnos "))
                if n_turno < 0:
                    print("Ingrese un numero positivo")
                else:
                    break
            except ValueError:
                print("Debe ingresar un numero entero")
        n_ingreso = {"especialidad":nuevo,"turnos":n_turno}
        n_ingreso = verificar_linea(n_ingreso)
        if n_ingreso is False:
            print("El ingreso sera ignorado")
        else:
            clinica.append(n_ingreso)
            modificar_archivo(clinica)
            print("Ingreso exitoso!")

def main():
    clinica = leer_archivo()
    print(clinica)
    salir = False
    while not salir:
        print("Bienvenido:")
        print("MENU")
        print("1) Ingresar nueva especialidad")
        print("2) Ingresar cantidad turnos")
        print("3) Mostrar info clinica")
        print("4) Consultar disponibilidad")
        print("5) Listar turnos agotados")
        print("6) Agregar una especialidad nueva")
        print("7) Actualizar turnos (reservar/cancelar)")
        print("8) Salir")
        opc = input("Eliga una opcion: ").strip()
        match opc:
            case "1":
                #Ingresar titulo con cantidad 0
                ingreso_especialidad(clinica)
            case "2":
                #Ingresar ejemplares accede al titulo y modificas la cantidad
                ingresar_turnos(clinica)
            case "3":
                #Mostrar catalogo
                mostrar_especialidades(clinica)
            case "4":
                #Consutlar disponibilidad
                consultar_disponibilidad(clinica)
            case "5":
                #Listar agotados
                listar_agotados(clinica)
            case "6":
                #Agregar titulo
                agregar_especialidad(clinica)
            case "7":
                #Actualizar ejemplares venta/devolucion
                continue
            case "8":
                #Salir
                print("Vuelva pronto!")
                salir = True
            case _:
                print("Opcion inválida")

main()