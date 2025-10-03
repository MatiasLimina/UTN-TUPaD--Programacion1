import math
def hola_mundo(): #Ejercicio 1
    return print("Hola Mundo!")

def saludar_usuario(nombre): #Ejercicio 2
    return print(f"Hola {nombre}!")

def informacion_personal(nombre,apellido,edad,residencia): #Ejercicio 3
    return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

def calcular_area_circulo(radio):#Ejercicio 4
    return PI*(radio ** 2)

def calcular_perimetro_circulo(radio): #Ejercicio 4.1
    return 2*PI*radio

def segundos_a_horas(segundos): #Ejercicio 5
    print(f"{segundos} segundos convertido a horas equivale a:")
    return print(f"{segundos/3600}")

def tabla_multiplicar(numero):  #Ejercicio 6
    print(f"Tabla de multiplicar de {numero}")
    for i in range(1,11):
        print(f"{i} x {numero} = {i*numero}")

def operaciones_basicas(a,b): #Ejercicio 7
    suma = a+b
    resta = a-b
    multiplicacion = a*b
    division = a/b
    operaciones = (suma,resta,multiplicacion,division)
    return operaciones
#Main
PI = math.pi
nombre = input("Ingrese su nombre ").capitalize()
apellido = input("Ingrese su apellido ").capitalize()
edad = int(input("Ingrese su edad "))
residencia = input("Ingrese su lugar de residencia ").capitalize()
radio = float(input("Ingrese el radio de un circulo"))
segundos = int(input("Ingrese una cantidad de segundos: "))
num_multiplicar = int(input("Ingrese un numero del que desea saber su tabla de multiplicar hasta el 10 "))
num1 = int(input("Ingrese el numero 1 "))
num2 = int(input("Ingresar el num 2 "))
hola_mundo()
saludar_usuario(nombre)
informacion_personal(nombre,apellido,edad,residencia)
print("Area del circulo: ",calcular_area_circulo(radio))
print("Perimetro del circulo: ",calcular_perimetro_circulo(radio))
segundos_a_horas(segundos)
tabla_multiplicar(num_multiplicar)
ope_basicas = operaciones_basicas(num1,num2)
aux_op_basicas = ["Suma: ","Resta: ","Multiplicación: ","División: "]
print(f"Las operacion básicas entre {num1} y {num2} son: ")
for i in range(len(ope_basicas)):
    print(f"{aux_op_basicas[i]}{ope_basicas[i]}")
