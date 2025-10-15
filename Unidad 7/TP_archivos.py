#Ejercicio 1
productos = [
    "Banana,120.2,2\n",
    "Manzana,100.0,4\n",
    "Pera,200.4,7\n"
    ] 
RUTA_ARCHIVO = "Programacion 1/Universidad/Archivos/Productos.txt"
def crear_archivo():
    with open(RUTA_ARCHIVO,"w") as archivo:
        archivo.writelines(productos)
archiv_productos = crear_archivo()
#Ejercicio 2

def leer_archivo():
    with open(RUTA_ARCHIVO,"r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas :
            prod,precio,cant = linea.strip().split(",")
            print(f"Producto: {prod}| Precio: ${precio}| Cantidad: {cant}")

leer_archivo()
