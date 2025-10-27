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

def verificar_linea(linea):
    for campo in linea: #Revisa que no haya campos vacios
        if linea[campo] == "":
            print (f"ERROR: {[campo]} esta vacio")
            return False
    try:#Verifica que el numero sea un entero
        stock_entero=int(linea["stock"])
        if stock_entero >= 0:
            linea["stock"] = stock_entero
        else:
            print("ERROR: El stock debe ser un numero igual o mayor a cero")
            return False
    except ValueError:
        print(f"ERROR: el Stock debe ser un número entero")
        return False
    try:
        precio_float = float(linea["precio"])
        if precio_float >= 0:
            linea["precio"] = precio_float
        else:
            print("ERROR: El precio debe ser número igual o mayor a cero")
            return False
    except ValueError:
        print("ERROR: el precio debe ser un número")
        return False
    return linea
#Cargar herramientas
def cargar_herramientas(herramientas):
    nueva_herramienta = herramienta_nueva()

    pass
def herramienta_nueva():
    print("Ingrese los datos de la nueva herramienta")
    nombre = input("Ingrese el nombre de la nueva herramienta: ")
    stock = input("Ingrese el stock de la nueva herramienta: ")
    precio = input("Ingrese el precio de la nueva herramienta: ")
    herramienta_nueva = {"nombre":nombre, "stock":stock, "precio":precio}
    print (herramienta_nueva)

def main():
    herramientas=leer_archivo()
    print(herramientas)
    for i in herramientas:
        print(f"Herramienta:{i["nombre"]} Stock: {i["stock"]} Precio: ${i["precio"]}")
    
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