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
# def almacenar_contactos():
#     dic_contacts = dict()
#     for i in range(2):
#         dic_contacts[input("Coloque el nombre del contacto ").capitalize()] = int(input("Coloque el numero de telefono "))
#     return dic_contacts
# def buscar_numero(contactos,nombre):
#     num_buscado = contactos.get(nombre)
#     return num_buscado

# contactos = almacenar_contactos()
# print(contactos)
# nombre = input("Ingrese el nombre de quien desea saber su numero ").capitalize()
# solicitar_num = buscar_numero(contactos,nombre)
# if solicitar_num == None:
#     print("Contacto no encontrado")
# else:
#     print(f"El numero de telefono de {nombre} es {solicitar_num}")

#Ejercicio 5
frase = input("Ingrese una frase").capitalize()
frase_aux = tuple(frase.split(" "))
frase_set = set(frase_aux)
print("Las palabras unicas de la frase indicada son: ",frase_set)
frase_palabras_repetidas = dict()
for item in frase_set:
    frase_palabras_repetidas[item] = frase_aux.count(item)
print("A continuacion cada palabra y el numero de veces que se repiten")
for key,value in frase_palabras_repetidas.items():
    print(f"{key}:{value}")