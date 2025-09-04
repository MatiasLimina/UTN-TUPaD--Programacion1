#Ejercicio 1
for i in range(101):
    print (i)
    break
































































































#Ejercicio 8
#Ejercicio realizado con ayuda del profe Hualpa

def es_par(n):
    return n%2 == 0

def es_impar(n):
    return (n%2 != 0 )
import random
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