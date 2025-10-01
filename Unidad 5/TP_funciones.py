def hola_mundo():
    return print("Hola Mundo!")

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")



#Main
nombre = input("Ingrese su nombre ").capitalize()
apellido = input("Ingrese su apellido ").capitalize()
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su lugar de residencia ").capitalize()
hola_mundo()
saludar_usuario(nombre)
informacion_personal(nombre,apellido,edad,residencia)