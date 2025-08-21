#Ejercicio 1
numero1 = 25
print (f"La variable numero1: {numero1}")

#Ejercicio 2
numero2 = 30.5
print(f"La variable numero2: {numero2}")

#Ejercicio 3
suma = numero1+numero2
print(f"Suma de numero1 y numero2: {suma}")

#Ejercicio 4
resta = numero1-numero2
multiplicacion = numero1*numero2
division= numero1/numero2
print(f"Resta de numero1 y numero2: {resta}")
print(f"Multiplicacion de numero1 y numero2: {multiplicacion}")
print(f"Division de numero 1 y numero2: {division}")

#Ejercicio 5
nombre="Matias"
print(f"Mi nombre es {nombre}")

#Ejercicio 6
precio = 45.50
print(f"El precio del articulo x es de: ${precio}")

#Ejercicio 7 
descuento = 0.25
print(f"Hay un descuento disponible de %{descuento*100}")

#Ejercicio 8
precio_final = (precio*descuento)
print(f"El precio final del producto x que costaba ${precio}, al aplicarle un descuento de {descuento*100} es de ${precio_final}")

#Ejercicio 9
cadena = "Aguante el rojo"
print(cadena)

#Ejercicio 10
longitud = len(cadena)
print(f"La longitud de la string contenido en la variable cadena es de: {longitud}")

#Ejercicio 11
precio = 12.12
print(precio)
precio = int(precio)
print(precio)

#Ejercicio 12
nombre = "Matias"
apellido = "Limina"
nombre_completo = nombre + " " + apellido
print (f"Mi nombre completo es {nombre_completo}")

#Ejercicio 13
edad = 25
print (f"Mi edad es {edad}")
edad = edad - 5
print (f"Mi edad mas 5 es de {edad}")
edad = edad + 10
print(f"Mi edad luego de restarle 5 y sumarle 10 es de {edad}")

#Ejercicio 14
altura = 1.80
print(f"Mi altura es de {altura} m")
altura= altura*4
print(f"Mi altura multiplicada por 4 es de {altura} m")
altura= altura/3
print(f"Mi altura luego de multiplicarla por 4 y dividirla por 3 equivale a {altura} m")

#Ejercicio 15
nombre_mayus = "MATIAS LIMINA"
nombre_minus = nombre_mayus.lower()
print(f"Mi nombre en mayúsculas: {nombre_mayus}")
print(f"Mi nombre en minúsculas: {nombre_minus}")

#Ejercicio 16
nombre_mayus= nombre_mayus.capitalize()
print(f"Mi nombre con la primera letra en mayúscula: {nombre_mayus}")