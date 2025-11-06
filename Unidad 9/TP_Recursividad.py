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

while True:
    try:
        numero_usuario = int(input("Ingrese un número entero positivo: "))
        if numero_usuario < 0:
            print("Ingrese un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero entero positivo")
mostrar_factoriales(numero_usuario)

#Ejercicio 2
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def mostrar_serie_fibonacci(limite):
    print(f"\nSerie de Fibonacci hasta la posición {limite}:")
    for i in range(limite + 1):
        print(f"F({i}) = {fibonacci_recursivo(i)}")

print("\n--- Cálculo de la Serie de Fibonacci ---")
while True:
    try:
        posicion_usuario = int(input("Ingrese la posición máxima para la serie de Fibonacci (un número entero no negativo): "))
        if posicion_usuario < 0:
            print("Ingrese un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero entero positivo")
mostrar_serie_fibonacci(posicion_usuario)

#Ejercicio 3

