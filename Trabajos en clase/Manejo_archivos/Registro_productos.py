import csv

def abrir_archivo(): #Abre el archivo
    try:
        with open("Productos.csv","w",newline="") as archivo:
            campos = ["nombre","precio"]
            escritor = csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos)
    except FileExistsError:
        print("El archivo ya existe")
def mostrar_archivo(): #Muestra productos
    with open("Productos.csv","r") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                print(fila)
def menu(opc): #Elige una opcion
    match opc:
        case "1":
            mostrar_archivo()
        case "2":
            print(2)
        case "3":
            print(3)
        case "4":
            return False

def elegir_menu(): #Muestra menu
    print("====== MENU =====")
    print("1) Mostrar productos registrados \n 2) Agregar nuevo producto \n 3) Eliminar producto \n 4) Salir ")
    print("================")
    opcion = input("Eliga una opción... ")
    return opcion

#main
productos = [
    {"nombre":"papa","precio":15},
    {"nombre":"tomate","precio":10}
]
abrir_archivo()
salir = False
while not salir:
    opcion = elegir_menu()
    aux = menu(opcion)
    if aux == False:
        salir = True