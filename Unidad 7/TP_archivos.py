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
#Ejercicio 2
def leer_archivo():
    with open(RUTA_ARCHIVO,"r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas :
            prod,precio,cant = linea.strip().split(",")
            print(f"Producto: {prod}| Precio: ${precio}| Cantidad: {cant}")
        return lineas

def crear_diccionario(lista:type=list): #Ejercicio 4.1
    lista_productos = []
    for i in range(len(lista)):
        producto, precio, cantidad = lista[i].strip().split(",")
        lista_productos.append({"Productos": producto, "Precio": precio, "Cantidad": cantidad})
    return lista_productos

def validar_nuevo_producto(n_producto,diccionario): #Ejercicio 3.1
    nuevo_aux = n_producto.split(",")
    if len(nuevo_aux) != 3:
        print("ERROR: ingreso los datos en el formato incorrecto")
        return None
    else:
        producto,precio,cantidad = n_producto.split(",")
        if producto in diccionario:
            print("Este producto ya se encuentra en el sistema")
            return None
        else:
            try:
                float(precio)
            except ValueError:
                print("ERROR: debe ingresar un numero")
                return None
            try:
                int(cantidad)
            except ValueError:
                print("ERROR: debe ingresar un numero entero")
                return None
            
            producto = producto.capitalize()
            nuevo_aux[0] = producto
            return ",".join(nuevo_aux)

def agregar_producto(n_producto):
    with open(RUTA_ARCHIVO,"a") as archivo:
        archivo.write(f"{n_producto} \n")

#MAIN
crear_archivo()
aux_productos = leer_archivo()
print (aux_productos)

#Ejercicio 4
lista_diccionarios_productos = crear_diccionario(aux_productos)
print(lista_diccionarios_productos)

#Menu
salir = False
while not salir:
    try:
        opc = int(input("Que desea hacer? \n 1) Agregar un nuevo producto \n 2)Buscar un producto por nombre \n 3) Salir \n Eliga una opcion... " ))
        while opc <= 0 or opc >3:
            opc =int(input("ERROR: Por favor ingrese una opcion válida (Debe ser un número)"))
    except ValueError:
        print ("ERROR: Por favor ingrese una opcion válida (Debe ser un número)")
        continue
    match opc:
        case 1: #Ejercicio 3
            aux_nuevo_producto = input("Coloque la informacion del nuevo producto a agregar: (producto,precio,cantidad)").strip()
            nuevo_producto = validar_nuevo_producto(aux_nuevo_producto,lista_diccionarios_productos)
            if nuevo_producto == None:
                print("Error al ingresar nuevo producto, no será agregado al sistema.")
                continue
            else:
                agregar_producto(nuevo_producto)
                print(f"Producto '{nuevo_producto.split(',')[0]}' agregado con éxito.")
