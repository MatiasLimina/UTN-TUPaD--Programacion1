import csv
productos = [
    {"nombre":"papa","precio":15},
    {"nombre":"tomate","precio":10}
]
def abrir_archivo():
    try:
        with open("Productos.csv","w",newline="") as archivo:
            campos = ["nombre","precio"]
            escritor = csv.DictWriter(archivo,fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(productos)
        with open("Productos.csv","r") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                print(fila)
            
    except FileExistsError:
        print("El archivo ya existe")

# def menu(opc):
#     match opc:
#         case "1":
            
#         case "2":
            
#         case "3":
            

def elegir_menu():
    print("====== MENU =====")
    print("1) Mostrar productos registrados \n 2) Agregar nuevo producto \n 3) Eliminar producto \n 4) Salir ")
    print("================")
    opcion = input("Eliga una opción... ")
    return opcion
