#Ejercicio 1
edad = int(input("Por favor ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota>=6 and nota <=10:
    print("Aprobado")
elif nota > 10:
    print("Ingrese una nota valida")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero "))
if numero%2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4
edad_2 = int(input("Ingrese su edad: "))
if edad_2<12:
    print("Niño/a")
elif edad_2 >=12 and edad_2<=18:
    print("Adolescente")
elif edad_2 >=18 and edad_2<=30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#Ejercicio 5
contraseña = input("Ingrese su contraseña(Debe contener entre 8 y 14 caracteres): ")
long_contra = len(contraseña)
if long_contra>=8 and long_contra<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
from statistics import mode, median, mean
import random
i=1
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (f"media: {mean(numeros_aleatorios)} mediana: {median(numeros_aleatorios)} moda: {mode(numeros_aleatorios)}")
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios)>mode(numeros_aleatorios):
    print("Sesgo positivo a la derecha")
elif mean(numeros_aleatorios)<median(numeros_aleatorios) and median(numeros_aleatorios)<mode(numeros_aleatorios):
    print("Sesgo negativo a la izquierda")
elif mean(numeros_aleatorios) == median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")