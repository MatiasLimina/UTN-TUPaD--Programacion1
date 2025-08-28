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