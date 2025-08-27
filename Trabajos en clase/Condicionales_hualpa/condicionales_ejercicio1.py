#Ejercicio 1 becas estudiantiles
nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
nombre_apellido = nombre +" "+ apellido
edad = input("Ingrese su edad ")
if edad.isdigit() :
    print("Edad valida")
else:
    print("Ingrese un valor valido")

promedio = input("Ingrese su promedio general")

if promedio.isdigit():
    promedio=float(promedio)
    if promedio>= 0 and promedio<=10:
        print("Usted ingreso un promedio valido")
    else:
        print("Ingrese un valor valido")

else:
    print("Ingrese un valor valido")
