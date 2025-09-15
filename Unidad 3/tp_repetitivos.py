import random
#Ejercicio 1

for i in range(101):
    print (i)


#Ejercicio 2
num_digitos = int(input("Ingrese un número entero "))
long_num = len(str(num_digitos))
cant_digitos = 0
for i in range(long_num):
    cant_digitos += 1
print (f"La cantidad de digitos en el número {num_digitos} es de {cant_digitos}")

#Ejercicio 3 
num_entero1 = int(input("Ingrese un número entero "))
num_entero2 = int(input("Ingrese un número entero "))
suma_enteros = 0
for i in range(num_entero1+1,num_entero2):
    suma_enteros += i
print (f"La suma de todos los números comprendidos entre {num_entero1} y {num_entero2} es de {suma_enteros}")

#Ejercicio 4

cancelar = 1
suma_sec= 0
while cancelar != 0:
    num_sec = int(input("Ingrese un número entero, para cancelar ingrese 0: "))
    suma_sec += num_sec
    cancelar = num_sec
    print (f"La suma secuencial de los números ingresados hasta ahora es de: {suma_sec}")
print (f"El resultado final de la suma es de: {suma_sec}")

#Ejercicio 5

intentos = 0
num_azar = random.randint(0,9)
num_jugador = 10
while num_azar != num_jugador:
    num_jugador = int(input("Ingrese un número entre el 0 y el 9 "))
    intentos += 1
    if num_jugador == num_azar:
        print("Felicitaciones, acertaste!")
    else:
        print("Mala suerte, vuelva a intentar")
print (f"Usted requirio {intentos} intentos para acertar el número que era {num_azar}")

#Ejercicio 6

for i in range(100,-1,-2):
    print (i)


#Ejercicio 7
rango_max = int(input("Hasta que entero positivo desea sumar "))
suma_rango = 0
for i in range(0,rango_max+1):
    suma_rango += i
print(f"La suma de todos los enteros comprendidos entre 0 y {rango_max} es de {suma_rango}")

#Ejercicio 8
#Ejercicio realizado con ayuda del profe Hualpa

def es_par(n):
    return n%2 == 0

def es_impar(n):
    return (n%2 != 0 )

CANT_NUMEROS = 100
lista_numeros = []
def principal():
    cont_par = 0
    cont_impar = 0
    cont_positivo = 0
    cont_negativo = 0
    for i in range(0,CANT_NUMEROS):
        lista_numeros.insert(i,(random.randint(-100,100)))
        if es_par(lista_numeros[i]):
            cont_par += 1
        elif es_impar(lista_numeros[i]):
            cont_impar +=1
        
        if lista_numeros[i]>0:
            cont_positivo +=1
        elif lista_numeros[i]<0:
            cont_negativo +=1
    print(f"Números positivos: {cont_positivo} \n Números negativos: {cont_negativo} \n Números pares: {cont_par} \n Números impares: {cont_impar}")

principal()

#Ejercicio 9
suma_media = 0
media_rango = 100


for i in range(media_rango):
    num_media =int(input("Ingrese un número "))
    suma_media += num_media
media = suma_media / media_rango
print (f"La media de los números ingresados por el usuario es de {media}")

#Ejercicio 9
num_original = input("Ingrese un número para invertir ")
num_len = len(num_original)
num_invertido = ""
for i in range(num_len-1,-1,-1):
    num_invertido = num_invertido + num_original[i]
print (f"La version invertida del num {num_original} es {num_invertido}")
