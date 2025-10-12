#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300
print(precios_frutas)

#Ejercicio 2
precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800
print(precios_frutas)

#Ejercicio 3
frutas = list(precios_frutas.keys())
print(frutas)

#Ejercicio 4
def almacenar_contactos():
    dic_contacts = dict()
    for i in range(2):
        dic_contacts[input("Coloque el nombre del contacto ").capitalize()] = int(input("Coloque el numero de telefono "))
    return dic_contacts
def buscar_numero(contactos,nombre):
    num_buscado = contactos.get(nombre)
    return num_buscado

contactos = almacenar_contactos()
print(contactos)
nombre = input("Ingrese el nombre de quien desea saber su numero ").capitalize()
solicitar_num = buscar_numero(contactos,nombre)
if solicitar_num == None:
    print("Contacto no encontrado")
else:
    print(f"El numero de telefono de {nombre} es {solicitar_num}")

#Ejercicio 5
frase = input("Ingrese una frase ").capitalize()
frase_aux = tuple(frase.split(" "))
frase_set = set(frase_aux)
print("Las palabras unicas de la frase indicada son: ",frase_set)
frase_palabras_repetidas = dict()
for item in frase_set:
    frase_palabras_repetidas[item] = frase_aux.count(item)
print("A continuacion cada palabra y el numero de veces que se repiten")
for key,value in frase_palabras_repetidas.items():
    print(f"{key}:{value}")

#Ejercicio 6
def ingreso_alumnos():
    alumnos = dict()
    for i in range(3):
        alumnos[input("Ingrese el nombre de un alumno ").capitalize()] = ingreso_notas()
    return alumnos
def ingreso_notas():
    notas = []
    cant_notas = int(input("Cuantas notas desea ingresar? "))
    while cant_notas < 0:
        print("Ingrese un numero superio al 0")
        cant_notas = int(input())
    print(f"Ingrese las {cant_notas} notas de este alumno ")
    for i in range(cant_notas):
        nota_aux = int(input(f"Nota N° {i}: "))
        while nota_aux < 0 or nota_aux > 10:
            print("Ingreso invalido, la nota debe ser mayor o igual a 0 y menor que 10")
            nota_aux = int(input(f"Nota N° {i}: "))
        notas.append(nota_aux)
    notas_final = tuple(notas)
    return notas_final
def promedios(notas):
    promedio = sum(notas)/len(notas)
    return round(promedio,1)

alumnos = ingreso_alumnos()
print (alumnos)
for alumnos,notas in alumnos.items():
    print(f"EL alumno {alumnos} tiene un promedio de {promedios(notas)}")

#Ejercicio 7
set_estudiantes_p1 = {1,4,5,3,7}
set_estudiantes_p2 = {6,7,9,1,2}

print("Parcial 1: ",set_estudiantes_p1)
print("Parcial 2: ",set_estudiantes_p2)

print("Estos son los estudiante que aprobaron ambos parciales: ",set_estudiantes_p1.intersection(set_estudiantes_p2))
print("Estos son los estudiantes que aprobaron solo uno de los parciales: ",set_estudiantes_p1.symmetric_difference(set_estudiantes_p2))
print("Estos son los estudiante que aprobaron al menos uno de los parciales : ",set_estudiantes_p1.union(set_estudiantes_p2))

#Ejercicio 8
def consultar_stock(productos):
    producto = input("De que producto desea consultar stock? ").capitalize()
    if producto in productos:
        stock = productos[producto]
        return f"El stock de {producto} es de {stock}"
    else:
        return "No se encontro el producto en nuestro sistema"

def cambiar_stock(productos,objetivo):
    if objetivo in productos:
        productos[objetivo] = int(input(f"Ingrese el nuevo stock para {objetivo}"))
        return productos
    else:
        return "No se encontro el producto en nuestro sistema"

def agregar_producto(productos,nuevo):
    if nuevo in productos:
        return f"{nuevo} ya se encuentra en el sistema"
    else:
        productos[nuevo] = 0
        return productos

productos = {
    "Madera" : 32,
    "Piedra" : 23,
    "Metal" : 10
}

salir = False
while not salir:
    print("Nuestros productos: ")
    for k,v in productos.items(): # "k" de "keys" y "v" de "values"
        print(f"{k} tiene un stock de {v}")
    opc = input("Que desea hacer: \n 1) Consultar stock de un producto? \n 2) Agragar unidades en un producto \n 3) Agregar un nuevo producto \n 4)Salir \n")
    while not opc.isnumeric() or opc != "1" and opc != "2" and opc != "3" and opc != "4":
        print("Ingreso invalido")
        opc = input("Que desea hacer: \n 1) Consultar stock de un producto? \n 2) Agragar unidades en un producto \n 3) Agregar un nuevo producto \n 4) Salir \n")

    if opc == "1":
        aux_1 = consultar_stock(productos)
        print(aux_1)
    elif opc == "2":
        aux_2 = input("De que producto desea cambiar stock? ").capitalize()
        stock_act = cambiar_stock(productos,aux_2)
        if not type(stock_act) == int:
            print(stock_act)
        else:
            productos = stock_act
            print(f"Stock actualizado: {aux_2} ahora tiene un stock de {productos[aux_2]}")
    elif opc == "3":
        aux_3 = input("Que producto desea agregar? ").capitalize()
        nuevo_prod = agregar_producto(productos,aux_3)
        if not type(nuevo_prod) == dict:
            print(nuevo_prod)
        else:
            productos = nuevo_prod
            print ("Productos actualizados")
            for k,v in productos.items(): # "k" de "keys" y "v" de "values"
                print(f"{k} tiene un stock de {v}")
            
    elif opc == "4":
        salir = True

#Ejercicio 9

agenda = {
    ("lunes","19:00") : "Gym",
    ("martes","10:00"): "Reunion",
    ("miercoles","13:00") : "Almuerzo"
}

consulta = input("Ingrese dia y horario para consultar actividad programada").lower()
aux_consulta = tuple(consulta.split())
for k in agenda.keys():
    if aux_consulta == k:
        print(f"La actividad programada en ese dia a ese horario es: {agenda[k]}")
        sin_concidencias = False
        break
    else:
        sin_concidencias = True
if sin_concidencias == True:
    print("No hay nada agendado en esa fecha y horario")

#Ejercicio 10
pais_capital_og = {
    "Argentina":"Buenos Aires",
    "Brasil":"Brasilia",
    "Chile":"Santiago"
}
pais_capital_invertido = {}

for pais,capital in pais_capital_og.items():
    pais_capital_invertido[capital]=pais
print("Original:")
for pais,capital in pais_capital_og.items():
    print(f"Pais:{pais} Capital:{capital} ")
print("Invertido")
for capital,pais in pais_capital_invertido.items():
    print(f"Capital:{capital} Pais:{pais} ")