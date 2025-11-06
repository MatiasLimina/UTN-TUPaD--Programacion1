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
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        print("Advertencia: La fórmula dada es más adecuada para exponentes no negativos.")
        return 1 / potencia_recursiva(base, -exponente)
    else:
        return base * potencia_recursiva(base, exponente - 1)


print("\n--- Cálculo de Potencia Recursiva ---")
while True:
    try:
        base_usuario = float(input("Ingrese la base (un número): "))
        exponente_usuario = int(input("Ingrese el exponente (un entero no negativo): "))
        if exponente_usuario < 0:
            print("Error: El exponente debe ser un entero no negativo para esta implementación directa de la fórmula.")
        else:
            resultado = potencia_recursiva(base_usuario, exponente_usuario)
            print(f"El resultado de {base_usuario} elevado a la {exponente_usuario} es: {resultado}")
            break
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar números válidos.")


