#Ejercicio 1 
print("Resolucion ejercicio 1")
print("Hola mundo!")

#Ejercicio 2
print("Resolucion ejercicio 2")
nombre = input("Ingrese su nombre ")
print(f"Hola {nombre}!")

#Ejercicio 3
print("Resolucion ejercicio 3")
apellido = input("Ingrese su apellido ")
edad =int(input("Ingrese su edad "))
lugar_resid = input ("Ingrese su lugar de residencia ")
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_resid}")

#Ejercicio 4
print("Resolucion ejercicio 4")
radio =float(input("Ingrese el radio de un circulo "))
pi = 3.14
area = pi * radio**2
perimetro = 2*pi*radio
print(f"El area del circulo cuyo radio es de {radio} equivale a {area} y su perimetro es de {perimetro}")

#Ejercicio 5
print("Resolucion ejercicio 5")
seg = int(input("Ingrese una cantidad de segundos que desea convertir a horas "))
horas = seg /3600
print (f"La cantidad {seg} segundos equivale a {horas} horas")

#Ejercicio 6
print("Resolucion ejercicio 6")
tabla_num = int(input("Eliga un numero para mostrar su tabla de multiplicar hasta el 10 "))

print(f"A continuacion se mostrara la tabla del numero {tabla_num}")
print(f"1 x {tabla_num} = {tabla_num*1}")
print(f"2 x {tabla_num} = {tabla_num*2}")
print(f"3 x {tabla_num} = {tabla_num*3}")
print(f"4 x {tabla_num} = {tabla_num*4}")
print(f"5 x {tabla_num} = {tabla_num*5}")
print(f"6 x {tabla_num} = {tabla_num*6}")
print(f"7 x {tabla_num} = {tabla_num*7}")
print(f"8 x {tabla_num} = {tabla_num*8}")
print(f"9 x {tabla_num} = {tabla_num*9}")
print(f"10 x {tabla_num} = {tabla_num*10}")

#Ejercicio 7
print("Resolucion ejercicio 7")
print("Ingrese dos numeros distintos de cero")
prim_num = int(input())
seg_num = int(input())

suma = prim_num + seg_num
resta = prim_num - seg_num
multiplicacion = prim_num * seg_num
division = prim_num / seg_num

print (f"{prim_num} + {seg_num} = {suma}")
print (f"{prim_num} - {seg_num} = {resta}")
print (f"{prim_num} x {seg_num} = {multiplicacion}")
print (f"{prim_num} / {seg_num} = {division}")

#Ejercicio 8
print("Resolucion ejercicio 8")
peso=float(input("Ingrese su peso "))
altura=float(input("Ingrese su altura"))
imc = peso/(altura**2)
print("Su indice IMC corresponde a ",imc)

#Ejercicio 9
print("Resolucion ejercicio 9")
temperatura=float(input("Ingrese la temperatura en grados Celcius "))
faren=(9/5)*temperatura + 32
print(f"La temperatura de {temperatura}°C equivale a {faren}°F")

#Ejercicio 10
print("Resolucion ejercicio 10")
num_1=int(input("Ingrese un numero "))
num_2=int(input("Ingrese un numero "))
num_3=int(input("Ingrese un numero "))
promedio = (num_1+num_2+num_3)/3
print (f"EL promedio entre {num_1}, {num_2} y {num_3} equivale a {promedio}")