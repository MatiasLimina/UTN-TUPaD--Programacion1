import csv
import os
#Manejo de csv

# 1. Obtiene la ruta absoluta del directorio donde está ESTE script.
script_dir = os.path.dirname(os.path.abspath(__file__))
# 2. Une esa ruta con el nombre del archivo.
RUTA_ARCHIVO = os.path.join(script_dir, "herramientas.csv")
ENCABEZADOS = ["nombre","stock","precio"]
#Manejo del archivo
def leer_archivo():
    crear_archivo()
    try:
        with open(RUTA_ARCHIVO, "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo,fieldnames=ENCABEZADOS)
            herramientas = []
            contador = 0
            for linea in lector:
                contador += 1
                aux = verificar_linea(linea,contador)
                if aux != False:
                    herramientas.append(aux)
            if not herramientas:
                print("No hay herramientas registradas")
            return herramientas
    except IOError:
        print("Ocurrió un error a la hora de leer el archivo")
        return []  # Devolvemos una lista vacía para que el programa pueda continuar

def crear_archivo():
    if not os.path.exists(RUTA_ARCHIVO):
        try:
            with open(RUTA_ARCHIVO,"w",newline="") as archivo:
                
                escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
                escritor.writeheader()
        except IOError:
            print("Error al crear el archivo")

def verificar_linea(linea,num_linea):
    for campo in linea: #Revisa que no haya campos vacios
        if linea[campo] == "":
            print (f"ERROR LINEA {num_linea}: {[campo]} esta vacio")
            return False
    try:#Verifica que el numero sea un entero
        stock_entero=int(linea["stock"])
        if stock_entero >= 0:
            linea["stock"] = stock_entero
        else:
            print(f"ERROR LINEA {num_linea}: El stock debe ser un numero igual o mayor a cero")
            return False
    except ValueError:
        print(f"ERROR LINEA {num_linea}: el Stock debe ser un número entero")
        return False
    try:
        precio_float = float(linea["precio"])
        if precio_float >= 0:
            linea["precio"] = precio_float
        else:
            print(f"ERROR LINEA {num_linea}: El precio debe ser número igual o mayor a cero")
            return False
    except ValueError:
        print(f"ERROR LINEA {num_linea}: el precio debe ser un número")
        return False
    return linea


#Cargar herramientas


def main():
    herramientas=leer_archivo()
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
                #Salir
                salir = True
if __name__ == "__main__":
    main()