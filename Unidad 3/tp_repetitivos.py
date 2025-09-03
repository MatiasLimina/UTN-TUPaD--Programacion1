#Ejercicio 8
#Ejercicio realizado con ayuda del profe Hualpa

def es_par(n):
    return (n%2 = 0)

def es_impar(n):
    return (n%2 != 0 )

CANT_NUMEROS = 5
lista_numeros = []
def principal():
    for i in range(1,CANT_NUMEROS):
        lista_numeros[i] = input(int("Ingrese el número: ",i))
        
