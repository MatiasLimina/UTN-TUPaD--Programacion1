#Ejercicio 1
def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n-1)

def mostrar_factoriales(limite):
    
    for i in range(1, limite + 1):
        factorial = factorial_recursivo(i)
        print(f"El factorial de {i} es: {factorial}")


numero_usuario = int(input("Ingrese un número entero positivo: "))
mostrar_factoriales(numero_usuario)

#Ejercicio 2
