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
        if campo == "nombre":
            linea[campo]=linea[campo].strip().capitalize()
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

def modificar_archivo(herramientas):
    try:
        with open(RUTA_ARCHIVO,"w",newline="") as archivo:
            escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
            escritor.writeheader()
            escritor.writerows(herramientas)
    except IOError:
        print("Error al modificar el archivo")

def agregar_linea(linea,herramientas):
    linea = verificar_linea(linea,len(herramientas)+1)
    if linea == False:
        print("Accion abortada, fallo de verificacion")
    else:
        try:
            with open(RUTA_ARCHIVO,"a",newline="") as archivo:
                escritor = csv.DictWriter(archivo,fieldnames=ENCABEZADOS)
                escritor.writerow(linea)
        except IOError:
            print("Error al acceder al archivo")
#Cargar herramientas
def cargar_herramientas(herramientas):
    print("Cuantas herramientas desea agregar?")
    while True:
        try:
            cantidad_agregar = int(input())
            if cantidad_agregar < 0:
                print("ERROR: Debe ingresar un número positivo.")
                continue
            break  # Si el input es válido, salimos del bucle
        except ValueError:
            print("ERROR: Debe ingresar un numero entero.")
    
    for i in range(cantidad_agregar):
        print(f"\n--- Herramienta {i+1} de {cantidad_agregar} ---")
        nombre = input("Nombre: ").strip().capitalize()
        stock = input("Stock: ").strip()
        precio = input("Precio: ").strip()
        aux = {"nombre":nombre,"stock":stock,"precio":precio}
        aux = verificar_linea(aux,len(herramientas)+1)
        #any(e["nombre"] == aux["nombre"] for e in herramientas)
        if aux is False:
            print("Valores ingresados invalidos")
            #print(f"La herramienta {aux['nombre']} ya se encuentra en el sistema")
            continue
        else:
            herramientas.append(aux)
            modificar_archivo(herramientas)
            print(f"Herramienta ´{aux["nombre"]}´ cargada con exito!")
#Mostrar herramientas
def mostrar_herramientas(herramientas):
    for i in herramientas:
        print(f"Herramienta:{i["nombre"]} Stock: {i["stock"]} Precio: ${i["precio"]}")
#Modificar herramienta
def modificar_herramientas(herramientas):
    while True:
        print("\n--- Modificar Herramienta ---")
        if not herramientas:
            print("No hay herramientas para modificar.")
            return herramientas
        print("Herramientas disponibles:")
        mostrar_herramientas(herramientas)
        
        nombre_modificar = input("Ingrese el nombre de la herramienta a modificar (o presione Enter para volver): ").strip().capitalize()
        if not nombre_modificar:
            break

        herramienta_encontrada = None
        indice_herramienta = -1
        for i, h in enumerate(herramientas):
            if h["nombre"] == nombre_modificar:
                herramienta_encontrada = h
                indice_herramienta = i
                break

        if herramienta_encontrada:
            print(f"\nModificando: {herramienta_encontrada['nombre']} (Stock: {herramienta_encontrada['stock']}, Precio: ${herramienta_encontrada['precio']})")
            
            datos_nuevos = herramienta_encontrada.copy()
            datos_nuevos["stock"] = input("Ingrese el nuevo stock: ").strip()
            datos_nuevos["precio"] = input("Ingrese el nuevo precio: ").strip()

            herramienta_validada = verificar_linea(datos_nuevos, indice_herramienta + 1)

            if herramienta_validada is not False:
                herramientas[indice_herramienta] = herramienta_validada
                modificar_archivo(herramientas)
                print("¡Herramienta modificada con éxito!")
            else:
                print("Modificación cancelada debido a valores inválidos.")
        else:
            print(f"ERROR: La herramienta '{nombre_modificar}' no fue encontrada.")
    
    return herramientas

def eliminar_herramienta(herramientas):
    mostrar_herramientas(herramientas)
    h_a_eliminar = input("Ingrese la herramienta que quiere eliminar... ").strip().capitalize()
    for h in herramientas:
        if h["nombre"] == h_a_eliminar:
            herramientas.remove(h)
            modificar_archivo(herramientas)
            print("Herramienta eliminada con exito")
            return herramientas
    print("No se encontro la herramienta en el sistema")
    return herramientas
    
def main():
    herramientas=leer_archivo()
    salir = False
    while not salir:
        opc = input("Ingrese una opción:\n 1) Cargar herramienta\n 2) Mostrar herramientas registradas\n 3) Modificar herramienta(Stock/Precio)\n 4) Elimina herramienta\n 5) Consultar disponibilidad\n 6) Listar productos sin stock\n 7) Salir\n Eliga una opción... ")
        match opc:
            case "1":
                cargar_herramientas(herramientas)
            case "2":
                #Mostrar herramientas
                mostrar_herramientas(herramientas)
            case "3":
                #Modificar herramientas
                herramientas = modificar_herramientas(herramientas)
            case "4":
                #Elimina herramienta
                herramientas = eliminar_herramienta(herramientas)
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