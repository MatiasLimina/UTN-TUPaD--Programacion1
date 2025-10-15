#Ejercicio 1
productos = [
    "Banana,120.2,2\n",
    "Manzana,100.0,4\n",
    "Pera,200.4,7\n"
    ] 
RUTA_ARCHIVO = "Programacion 1/Universidad/Archivos/Productos.txt"

with open(RUTA_ARCHIVO,"a") as archivo:
    archivo.writelines(productos)

#

