#Ejercicio 8
#Ejercicio realizado con ayuda del profe Hualpa

def es_par(n):
    return n%2 == 0

def es_impar(n):
    return (n%2 != 0 )
import random
CANT_NUMEROS = 5
def principal():
    lista_numeros = []
    for i in range(0,CANT_NUMEROS):
        lista_numeros.insert(i,(random.randint(1,100)))
        print(lista_numeros[i])
        
    

principal()