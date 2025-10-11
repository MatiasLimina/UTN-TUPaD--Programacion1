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
print (solicitar_num)
if solicitar_num == None:
    print("Contacto no encontrado")
else:
    print(f"El numero de telefono de {nombre} es {solicitar_num}")