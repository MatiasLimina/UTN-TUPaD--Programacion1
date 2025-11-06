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

#Ejercicio 4
def decimal_a_binario_recursivo(n):
    if n == 0:
        return "0"  # Caso base: 0 en decimal es "0" en binario
    elif n == 1:
        return "1"  # Caso base: 1 en decimal es "1" en binario
    else:
        resto = n % 2
        cociente = n // 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

# Ejemplo de uso
print("--- Transformar numero a binario ---")
while True:
    try:
        numero_decimal = int(input("Ingrese un numero entero para saber su binario"))
        if numero_decimal < 0:
            print("Ingrese un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero entero positivo")

binario_resultante = decimal_a_binario_recursivo(numero_decimal)
print(f"El número {numero_decimal} en binario es: {binario_resultante}")

#Ejercicio 5
def es_palindromo(palabra: str) -> bool:
    # Caso base: Una palabra vacía o de un solo carácter es un palíndromo.
    if len(palabra) <= 1:
        return True
    # Caso recursivo: Compara el primer y último carácter.
    # Si son iguales, llama recursivamente a la función con la subcadena
    # que excluye el primer y último carácter.
    else:
        return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])


print("\n--- Verificador de Palíndromos Recursivo ---")
palabra_usuario = input("Ingrese una palabra (sin espacios ni tildes) para verificar si es un palíndromo: ").lower()
if es_palindromo(palabra_usuario):
    print(f"'{palabra_usuario}' ES un palíndromo.")
else:
    print(f"'{palabra_usuario}' NO es un palíndromo.")

#Ejercicio 6
def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    # Caso recursivo: Suma el último dígito (n % 10) con la suma de los dígitos
    # del resto del número (n // 10).
    else:
        return (n % 10) + suma_digitos(n // 10)


print("\n--- Suma de Dígitos Recursiva ---")
numero_a_sumar = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
while True:
    try:
        numero_a_sumar = int(input("Ingrese un número entero positivo para sumar sus dígitos: "))
        if numero_decimal < 0:
            print("Ingrese un numero entero positivo")
        else:
            break
    except ValueError:
        print("Ingrese un numero entero positivo")
resultado_suma_digitos = suma_digitos(numero_a_sumar)
print(f"La suma de los dígitos de {numero_a_sumar} es: {resultado_suma_digitos}")

#Ejercicio 7
def contar_bloques(n: int) -> int:
    # Caso base: Si solo hay un nivel (n=1), se necesita 1 bloque.
    if n == 1:
        return 1
    # Caso recursivo: Suma los bloques del nivel actual (n) con los bloques
    # de la pirámide construida con un nivel menos (n-1).
    else:
        return n + contar_bloques(n - 1)


print("\n--- Calculadora de Bloques de Pirámide Recursiva ---")
while True:
    try:
        nivel_base = int(input("Ingrese el número de bloques en el nivel más bajo de la pirámide (entero positivo): "))
        if nivel_base <= 0:
            print("Error: El número de bloques debe ser un entero positivo.")
        else:
            total_bloques = contar_bloques(nivel_base)
            print(f"Para una pirámide con {nivel_base} bloques en la base, se necesitan un total de {total_bloques} bloques.")
            break
    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número entero.")

#Ejercicio 8
