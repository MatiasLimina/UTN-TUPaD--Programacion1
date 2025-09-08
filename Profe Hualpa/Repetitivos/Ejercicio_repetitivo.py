
abc = "abcdefghijklmnopqrstuvwxyz"
patente_valida = False
while patente_valida == False:
    patente = input("Ingrese su patente ").upper()
    print(len(patente))
    if len(patente) == 6:
        letras_patentes = patente[0:2]
        num_patentes =patente[3:5]

        if letras_patentes.isalpha() and num_patentes.isdigit():
            patente_valida = True
    else:
        print("Ingrese una patente válida")
print("Usted ingreso una patente válida")

#Ingresar una patente y sumarle la enesima 

nueva_patente = int(input("Ingrese cuantas patentes mas sumar y buscar en el sistema"))
patente_2 = ""


# Generar nueva patente
# Convert patente ingresada a un número secuencial
def patente_a_num(patente):
    letras = patente[:2]
    numeros = patente[2:]
    num_letras = (abc.index(letras[0]) * 26) + abc.index(letras[1])
    num_total = num_letras * 10000 + int(numeros)
    return num_total

# Convertir número secuencial a patente
def num_a_patente(num):
    num_letras = num // 10000
    numeros = num % 10000
    l1 = abc[num_letras // 26]
    l2 = abc[num_letras % 26]
    return f"{l1}{l2}{numeros:04d}".upper()

patente_num = patente_a_num(patente)
nueva_patente_num = patente_num + nueva_patente
patente_2 = num_a_patente(nueva_patente_num)
print(f"La nueva patente es {patente_2}")