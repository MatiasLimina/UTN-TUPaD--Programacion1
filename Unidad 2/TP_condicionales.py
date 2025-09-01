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

#Ejercicio 7
frase = input("Ingrese una frase: ")
long_frase = len(frase)
ultima_letra =frase[long_frase-1:long_frase]
print(f"Ultima letra: {ultima_letra}")

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
    print(frase+"!")
else:
    print(frase)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
print ("Eliga entre: ")
print ("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print ("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro")
print ("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro")
opc = int(input("Eliga una opcion: "))

if opc == 1:
    print(nombre.upper())
elif opc == 2:
    print(nombre.lower())
elif opc == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#Ejercicio 9
terremoto = int(input("Ingrese la magnitud de un terremoto: "))

if terremoto<3:
    print("Muy leve (imperceptible)")
elif terremoto>=3 and terremoto<4:
    print("Leve (ligeramente perceptible)")
elif terremoto>=4 and terremoto<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto>=5 and terremoto<6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto>=6 and terremoto<7:
    print("Muy Fuerte (puede causar daños significativos)")
elif terremoto>=7:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra(S para Sur y N para norte) ").upper()
mes = input("Ingrese el mes del año ").lower()
dia = int(input("Ingrese el dia "))

if hemisferio == "S":
    if (mes == "diciembre" and dia >=21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia<=20):
        print("Verano")
    elif (mes == "marzo" and dia>=21) or mes == "abril" or mes == "mayo" or (mes=="junio" and dia<=20):
        print("Otoño")
    elif (mes == "junio" and dia>=21) or mes == "julio" or mes == "agosto" or (mes=="septiembre" and dia<=20):
        print("Invierno")
    elif (mes == "septiembre" and dia>=21) or mes == "octubre" or mes == "noviembre" or (mes=="diciembre" and dia<=20):
        print("Primavera")
elif hemisferio == "N":
    if (mes == "diciembre" and dia >=21) or mes == "enero" or mes == "febrero" or (mes == "marzo" and dia<=20):
        print("Invierno")
    elif (mes == "marzo" and dia>=21) or mes == "abril" or mes == "mayo" or (mes=="junio" and dia<=20):
        print("Primavera")
    elif (mes == "junio" and dia>=21) or mes == "julio" or mes == "agosto" or (mes=="septiembre" and dia<=20):
        print("Verano")
    elif (mes == "septiembre" and dia>=21) or mes == "octubre" or mes == "noviembre" or (mes=="diciembre" and dia<=20):
        print("Otoño")     
