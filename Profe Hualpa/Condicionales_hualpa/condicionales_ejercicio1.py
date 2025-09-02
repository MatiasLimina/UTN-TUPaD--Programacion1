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

promedio=float(promedio)

if promedio>= 0 and promedio<=10:
    print("Usted ingreso un promedio valido")
else:
    print("Ingrese un valor valido")

ingreso_familiar = input("Indique el ingreso total de su grupo familiar")
if ingreso_familiar.isdigit() :
    ingreso_familiar=int(ingreso_familiar)
    print("Numero valido")
else:
    print("Ingrese un valor valido")

print(f"{nombre_apellido}, edad: {edad}, con un promedio de {promedio} y un ingreso total de ${ingreso_familiar}")
#Promedio

if promedio<6:
    print("RECHAZADO")
else:
    if ingreso_familiar < 300000:
        print("Usted tiene acceso a la beca completa")
    elif ingreso_familiar>=300000 and ingreso_familiar<=600000:
        print("Usted tiene acceso a una media beca")
    elif ingreso_familiar>600000:
        print("RECHAZADO")


