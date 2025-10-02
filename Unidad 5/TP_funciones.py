import math
def hola_mundo():
    return print("Hola Mundo!")

def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

def informacion_personal(nombre,apellido,edad,residencia):
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):
    return PI*(radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2*PI*radio

def segundos_a_horas(segundos):
    print(f"{segundos} segundos convertido a horas equivale a:")
    return print(f"{segundos/3600}")

def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar de {numero}")
    for i in range(1,11):
        print(f"{i} x {numero} = {i*numero}")
#Main
PI = math.pi
nombre = input("Ingrese su nombre ").capitalize()
apellido = input("Ingrese su apellido ").capitalize()
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su lugar de residencia ").capitalize()
radio = float(input("Ingrese el radio de un circulo"))
segundos = int(input("Ingrese una cantidad de segundos: "))
num = int(input("Ingrese un numero del que desea saber su tabla de multiplicar hasta el 10 "))
hola_mundo()
saludar_usuario(nombre)
informacion_personal(nombre,apellido,edad,residencia)
print("Area del circulo: ",calcular_area_circulo(radio))
print("Perimetro del circulo: ",calcular_perimetro_circulo(radio))
segundos_a_horas(segundos)
tabla_multiplicar(num)