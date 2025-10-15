#Ejercicio 1
productos = [
    "Banana,120.2,2 \n",
    "Manzana,100.0,4 \n",
    "Pera,200.4,7 \n"
    ] 
RUTA_ARCHIVO = "Programacion 1/Universidad/Archivos/Productos.txt"
def crear_archivo():
    try:
        with open(RUTA_ARCHIVO, "x") as archivo:
            archivo.writelines(productos)
            print("Archivo 'Productos.txt' creado por primera vez.")
    except FileExistsError:
        print("El archivo 'Productos.txt' ya existe. No se sobreescribe.")
crear_archivo()
#Ejercicio 2
def leer_archivo():
    with open(RUTA_ARCHIVO,"r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas :
            prod,precio,cant = linea.strip().split(",")
            print(f"Producto: {prod}| Precio: ${precio}| Cantidad: {cant}")
        return lineas

def crear_diccionario(lista:type=list):
    lista_productos = []
    for i in range(len(lista)):
        producto, precio, cantidad = lista[i].strip().split(",")
        lista_productos.append({"Productos": producto, "Precio": precio, "Cantidad": cantidad})
    return lista_productos
#Ejercicio 3
aux_productos = leer_archivo()
print (aux_productos)

#Ejercicio 4
lista_diccionarios_productos = crear_diccionario(aux_productos)
print(lista_diccionarios_productos)