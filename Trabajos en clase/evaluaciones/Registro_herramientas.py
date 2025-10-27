import csv
import os
#Manejo de csv

# 1. Obtiene la ruta absoluta del directorio donde está ESTE script.
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Une esa ruta con el nombre del archivo.
RUTA_ARCHIVO = os.path.join(script_dir, "herramientas.csv")

def leer_archivo():
    with open (RUTA_ARCHIVO,"r",newline="", encoding="utf-8") as archivo:
        try:
            lector = csv.DictReader(archivo)
            herramientas = list(lector)
            if not herramientas:
                print("No hay herramientas registradas")
                return herramientas
            else:
                return herramientas
        except IOError:
            print("Ocurrio un error a la hora de leer el archivo")
        except FileNotFoundError:
            print("El archivo no existe. Se creara uno nuevo")
            crear_archivo()

def crear_archivo():
    if not os.path.exists(RUTA_ARCHIVO):
        try:
            with open(RUTA_ARCHIVO,"w",newline="") as archivo:
                encabezados = ["nombre","stock","precio"]
                escritor = csv.DictWriter(archivo,fieldnames=encabezados)
                escritor.writeheader()
        except IOError:
            print("Error al crear el archivo")

def main():
    leer_archivo()
    #crear_archivo()
    salir = False
    while not salir:
        opc = input("Ingrese una opción:\n 1) Cargar herramienta\n 2) Mostrar herramientas registradas\n 3) Modificar herramienta(Stock/Precio)\n 4) Elimina herramienta\n 5) Consultar disponibilidad\n 6) Listar productos sin stock\n 7) Salir\n Eliga una opción... ")
        match opc:
            case "1":
                #Cargar herramientas
                continue
            case "2":
                #Mostrar herramientas
                continue
            case "3":
                #Modificar herramientas
                continue
            case "4":
                #Elimina herramienta
                continue
            case "5":
                #Consultar disponibilidad
                continue
            case "6":
                #Listar producto sin stock
                continue
            case "7":
                salir = True
if __name__ == "__main__":
    main()